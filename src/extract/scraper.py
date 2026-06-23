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
