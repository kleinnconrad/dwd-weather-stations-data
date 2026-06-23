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
    df_meta['Bundesland'] = df_meta['Bundesland'].replace(
        {'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'Ä': 'Ae', 'Ö': 'Oe', 'Ü': 'Ue', 'ß': 'ss'}, 
        regex=True
    )
    
    return df_meta.set_index("Station_ID")[["Bundesland", "Latitude", "Longitude", "Altitude"]].to_dict('index')
