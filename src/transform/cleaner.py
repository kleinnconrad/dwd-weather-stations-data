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
