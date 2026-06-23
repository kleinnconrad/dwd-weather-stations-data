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
                    write_partitioned_dataset(arrow_table, station_id)
                    
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
