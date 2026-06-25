import os
from pathlib import Path

# Data Source URLs
BASE_URL = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/historical/"
STATION_LIST_URL = f"{BASE_URL}KL_Tageswerte_Beschreibung_Stationen.txt"
PHENOLOGY_URL = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/phenology/annual_reporters/fruit/historical/PH_Jahresmelder_Obst_Sauerkirsche_1925_2024_hist.txt"

# Storage Configuration
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent.parent
OUTPUT_DIR = os.path.join(WORKSPACE_ROOT, "data", "dwd_historical_lake")
PHENOLOGY_OUTPUT_DIR = os.path.join(WORKSPACE_ROOT, "data", "processed")

# Execution Configuration
MAX_WORKERS = 6 
HTTP_TIMEOUT = 30
