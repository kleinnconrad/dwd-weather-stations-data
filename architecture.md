# DWD Historical Climate Data Ingestion Architecture

## 1. Context for Antigravity IDE
**Target Context:** June 2026 build environment.
**Agent Instructions:** Generate the following repository exactly as specified. This application is a strictly modular Extract, Transform, Load (ETL) pipeline. It is designed to run locally on a standard laptop to ingest the full historical daily climate timeseries of all German weather stations from the Deutscher Wetterdienst (DWD). The pipeline performs concurrent, memory-efficient in-flight parsing and persists the output locally as a Hive-partitioned Parquet data lake. There is no visualization or dashboard layer included. Ensure no emojis are used in the codebase or terminal output.

## 2. Directory Tree
Scaffold the following folder structure relative to the project root:

```text
dwd-ingestion-app/
├── requirements.txt
├── .gitignore
└── src/
    ├── __init__.py
    ├── main.py
    ├── config/
    │   ├── __init__.py
    │   └── settings.py
    ├── extract/
    │   ├── __init__.py
    │   ├── metadata.py
    │   └── scraper.py
    ├── transform/
    │   ├── __init__.py
    │   └── cleaner.py
    └── load/
        ├── __init__.py
        └── writer.py
```

---

## 3. Implementation Modules

### `requirements.txt`
```text
pandas>=2.2.0
requests>=2.31.0
pyarrow>=15.0.0
```

### `.gitignore`
```text
__pycache__/
.venv/
data/
.DS_Store
```

### `src/config/settings.py`
```python
import os
from pathlib import Path

# Data Source URLs
BASE_URL = "[https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/historical/](https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/historical/)"
STATION_LIST_URL = f"{BASE_URL}KL_Tageswerte_Beschreibung_Stationen.txt"

# Storage Configuration
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent.parent
OUTPUT_DIR = os.path.join(WORKSPACE_ROOT, "data", "dwd_historical_lake")

# Execution Configuration
MAX_WORKERS = 6 
HTTP_TIMEOUT = 30
```

### `src/extract/metadata.py`
```python
import io
import requests
import pandas as pd
from src.config.settings import STATION_LIST_URL, HTTP_TIMEOUT

def fetch_station_metadata() -> dict:
    print("Resolving station metadata and regional mapping from DWD...")
    response = requests.get(STATION_LIST_URL, timeout=HTTP_TIMEOUT)
    response.encoding = 'latin-1'
    
    col_specs = [(0, 5), (6, 14), (15, 23), (24, 38), (39, 50), (51, 60), (61, 102), (102, 140)]
    col_names = ["Station_ID", "Start_Date", "End_Date", "Altitude", "Latitude", "Longitude", "Station_Name", "Bundesland"]
    
    df_meta = pd.read_fwf(
        io.StringIO(response.text), 
        skiprows=2, 
        names=col_names, 
        colspecs=col_specs, 
        dtype={"Station_ID": str}
    )
    df_meta['Station_ID'] = df_meta['Station_ID'].str.zfill(5)
    df_meta['Bundesland'] = df_meta['Bundesland'].str.strip()
    
    return df_meta.set_index("Station_ID")[["Bundesland", "Latitude", "Longitude", "Altitude"]].to_dict('index')
```

### `src/extract/scraper.py`
```python
import re
import requests
from src.config.settings import BASE_URL, HTTP_TIMEOUT

def get_payload_manifest() -> dict:
    print("Scraping DWD directory for historical datasets...")
    response = requests.get(BASE_URL, timeout=HTTP_TIMEOUT)
    response.raise_for_status()
    
    pattern = r'href="(tageswerte_KL_(\d{5})_.*?_hist\.zip)"'
    matches = re.findall(pattern, response.text)
    
    manifest = {station_id: filename for filename, station_id in matches}
    print(f"Manifest built: Found {len(manifest)} datasets.")
    return manifest
```

### `src/transform/cleaner.py`
```python
import io
import zipfile
import pandas as pd
import pyarrow as pa

def transform_and_enrich(file_content: bytes, station_id: str, metadata: dict) -> pa.Table:
    with zipfile.ZipFile(io.BytesIO(file_content)) as z:
        data_filename = [name for name in z.namelist() if name.startswith('produkt_klima_tag_')][0]
        with z.open(data_filename) as f:
            df = pd.read_csv(f, sep=';', skipinitialspace=True, na_values=[-999, "-999"])
            
    df.columns = df.columns.str.strip()
    columns_to_keep = {
        'STATIONS_ID': 'Station_ID', 
        'MESS_DATUM': 'Date', 
        'TMK': 'Mean_Temp_C', 
        'TXK': 'Max_Temp_C', 
        'TNK': 'Min_Temp_C'
    }
    
    # Safe renaming mapping
    existing_cols = [col for col in columns_to_keep.keys() if col in df.columns]
    df = df[existing_cols].rename(columns={k: columns_to_keep[k] for k in existing_cols})
    
    # Fill missing columns to preserve strict Parquet schema
    for expected_col in columns_to_keep.values():
        if expected_col not in df.columns:
            df[expected_col] = None
            
    df['Station_ID'] = df['Station_ID'].astype(str).str.zfill(5)
    df['Date'] = pd.to_datetime(df['Date'].astype(str), format='%Y%m%d')
    
    meta = metadata.get(station_id, {"Bundesland": "Unknown", "Latitude": None, "Longitude": None, "Altitude": None})
    df['Bundesland'] = meta['Bundesland']
    df['Latitude'] = meta['Latitude']
    df['Longitude'] = meta['Longitude']
    df['Altitude'] = meta['Altitude']
    
    # Enforce float typing to prevent PyArrow inference conflicts
    df['Latitude'] = df['Latitude'].astype(float)
    df['Longitude'] = df['Longitude'].astype(float)
    df['Altitude'] = df['Altitude'].astype(float)
    df['Mean_Temp_C'] = df['Mean_Temp_C'].astype(float)
    df['Max_Temp_C'] = df['Max_Temp_C'].astype(float)
    df['Min_Temp_C'] = df['Min_Temp_C'].astype(float)
    
    return pa.Table.from_pandas(df, preserve_index=False)
```

### `src/load/writer.py`
```python
import pyarrow as pa
import pyarrow.dataset as ds
from src.config.settings import OUTPUT_DIR

def get_target_schema() -> pa.Schema:
    return pa.schema([
        ('Station_ID', pa.string()),
        ('Date', pa.timestamp('ns')),
        ('Mean_Temp_C', pa.float64()),
        ('Max_Temp_C', pa.float64()),
        ('Min_Temp_C', pa.float64()),
        ('Bundesland', pa.string()),
        ('Latitude', pa.float64()),
        ('Longitude', pa.float64()),
        ('Altitude', pa.float64())
    ])

def write_partitioned_dataset(arrow_table: pa.Table):
    ds.write_dataset(
        arrow_table, 
        base_dir=OUTPUT_DIR, 
        format="parquet",
        partitioning=ds.partitioning(pa.schema([('Bundesland', pa.string())]), flavor="hive"),
        schema=get_target_schema(), 
        existing_data_behavior="overwrite_or_ignore"
    )
```

### `src/main.py`
```python
import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from src.config.settings import OUTPUT_DIR, MAX_WORKERS, BASE_URL, HTTP_TIMEOUT
from src.extract.metadata import fetch_station_metadata
from src.extract.scraper import get_payload_manifest
from src.transform.cleaner import transform_and_enrich
from src.load.writer import write_partitioned_dataset

def run_pipeline():
    print("--- Starting DWD Data Ingestion Pipeline ---")
    
    metadata = fetch_station_metadata()
    manifest = get_payload_manifest()
    
    print(f"Targeting local data lake destination: {OUTPUT_DIR}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    processed_count = 0
    total_stations = len(manifest)
    
    print(f"Beginning concurrent processing with {MAX_WORKERS} workers...")
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(requests.get, BASE_URL + filename, timeout=HTTP_TIMEOUT): (station_id, filename) 
            for station_id, filename in manifest.items()
        }
        
        for future in as_completed(futures):
            station_id, filename = futures[future]
            try:
                response = future.result()
                if response.status_code == 200:
                    arrow_table = transform_and_enrich(response.content, station_id, metadata)
                    write_partitioned_dataset(arrow_table)
                    
                    processed_count += 1
                    if processed_count % 25 == 0 or processed_count == total_stations:
                        print(f"Progress: Storage sync complete for {processed_count}/{total_stations} stations.")
                else:
                    print(f"Network error {response.status_code} for station {station_id}.")
            except Exception as e:
                print(f"Skipping station {station_id} due to pipeline error: {e}")

    print("--- DWD Data Ingestion Complete ---")

if __name__ == "__main__":
    run_pipeline()
```

## 4. Execution Protocol
Execute the ETL pipeline via the terminal:

```bash
pip install -r requirements.txt
python -m src.main
```