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
        ('Altitude', pa.float64()),
        ('Sensor_Typ', pa.string()),
        ('Strahlungsschutz', pa.string()),
        ('Berechnungs_Methode', pa.string()),
        ('Historische_Breite', pa.float64()),
        ('Historische_Laenge', pa.float64()),
        ('Historische_Hoehe', pa.float64())
    ])

def write_partitioned_dataset(arrow_table: pa.Table, station_id: str):
    ds.write_dataset(
        arrow_table, 
        base_dir=OUTPUT_DIR, 
        format="parquet",
        partitioning=ds.partitioning(pa.schema([('Bundesland', pa.string())]), flavor="hive"),
        schema=get_target_schema(), 
        existing_data_behavior="overwrite_or_ignore",
        basename_template=f"{station_id}-part-{{i}}.parquet"
    )
