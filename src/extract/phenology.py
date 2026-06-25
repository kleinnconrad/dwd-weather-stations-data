import requests
from src.config.settings import PHENOLOGY_URL, HTTP_TIMEOUT

def fetch_phenology_data() -> bytes:
    print(f"Downloading phenology data from: {PHENOLOGY_URL} ...")
    response = requests.get(PHENOLOGY_URL, timeout=HTTP_TIMEOUT)
    response.raise_for_status()
    print("Download completed.")
    return response.content
