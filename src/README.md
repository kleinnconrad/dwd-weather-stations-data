# Source Code Architecture

## Table of Contents
1. [Folder Structure](#folder-structure)
2. [Module Overview](#module-overview)
3. [Script Interactions](#script-interactions)

## Folder Structure
```text
src
|   main.py
|   __init__.py
|   
+---config
|       settings.py
|       __init__.py
|       
+---extract
|       metadata.py
|       scraper.py
|       __init__.py
|       
+---load
|       writer.py
|       __init__.py
|       
\---transform
        cleaner.py
        __init__.py
```

## Module Overview

### `main.py`
The application entry point. It orchestrates the pipeline execution by sequentially calling extraction modules and managing a thread pool for concurrent data processing. It delegates transformations and storage operations to specialized modules.

### `config/settings.py`
The configuration module. It centrally defines system parameters such as endpoints, directory paths, worker counts, and network timeouts. All other modules import these constants to ensure central configuration management.

### `extract/metadata.py`
Fetches and parses the station metadata manifest. It extracts structural information such as geographic coordinates, station names, and regions, returning a structured dictionary utilized for data enrichment.

### `extract/scraper.py`
Responsible for analyzing the data directory structure. It retrieves the index page of the data source and uses regular expressions to build a manifest mapping station identifiers to historical archive filenames.

### `transform/cleaner.py`
Processes the raw binary archives. It decompresses the payload in memory, normalizes column names, enforces strict typing, handles missing data, and enriches the dataset with metadata. It outputs an Apache Arrow table.

### `load/writer.py`
Manages data persistence. It takes the Apache Arrow table and writes the records to the file system as Parquet files, applying a Hive-style partition strategy based on geographic regions.

## Script Interactions

```mermaid
graph TD
    A["main.py"] -->|"1. Fetch Metadata"| B["extract/metadata.py"]
    A -->|"2. Get Manifest"| C["extract/scraper.py"]
    
    A -->|"3. Concurrent Download"| D["HTTP Request"]
    D -->|"4. Raw Bytes"| E["transform/cleaner.py"]
    B -->|"Metadata Dictionary"| E
    
    E -->|"5. Arrow Table"| F["load/writer.py"]
    
    G["config/settings.py"] -.-> A
    G -.-> B
    G -.-> C
    G -.-> F
```
