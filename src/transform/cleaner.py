import io
import zipfile
import pandas as pd
import pyarrow as pa

def transform_and_enrich(file_content: bytes, station_id: str, metadata: dict) -> pa.Table:
    with zipfile.ZipFile(io.BytesIO(file_content)) as z:
        data_filename = [name for name in z.namelist() if name.startswith('produkt_klima_tag_')][0]
        with z.open(data_filename) as f:
            df = pd.read_csv(f, sep=';', skipinitialspace=True, na_values=[-999, "-999"])
            
        hw_filenames = [n for n in z.namelist() if n.startswith('Metadaten_Geraete_Lufttemperatur_') and n.endswith('.txt')]
        hw_df = pd.read_csv(z.open(hw_filenames[0]), sep=';', skipinitialspace=True, encoding='latin-1') if hw_filenames else None
        
        param_filenames = [n for n in z.namelist() if n.startswith('Metadaten_Parameter_klima_tag_') and n.endswith('.txt')]
        param_df = pd.read_csv(z.open(param_filenames[0]), sep=';', skipinitialspace=True, encoding='latin-1') if param_filenames else None
        
        geo_filenames = [n for n in z.namelist() if n.startswith('Metadaten_Geographie_') and n.endswith('.txt')]
        geo_df = pd.read_csv(z.open(geo_filenames[0]), sep=';', skipinitialspace=True, encoding='latin-1') if geo_filenames else None
            
    df.columns = df.columns.str.strip()
    columns_to_keep = {
        'STATIONS_ID': 'Station_ID', 
        'MESS_DATUM': 'Date', 
        'TMK': 'Mean_Temp_C', 
        'TXK': 'Max_Temp_C', 
        'TNK': 'Min_Temp_C'
    }
    
    existing_cols = [col for col in columns_to_keep.keys() if col in df.columns]
    df = df[existing_cols].rename(columns={k: columns_to_keep[k] for k in existing_cols})
    
    for expected_col in columns_to_keep.values():
        if expected_col not in df.columns:
            df[expected_col] = None
            
    df['Station_ID'] = df['Station_ID'].astype(str).str.zfill(5)
    df['Date'] = pd.to_datetime(df['Date'].astype(str), format='%Y%m%d')
    df = df.sort_values('Date')
    
    def merge_interval_meta(main_df, meta_df, rename_cols, filter_col=None, filter_val=None):
        if meta_df is None or meta_df.empty:
            for col in rename_cols.values():
                main_df[col] = None
            return main_df
            
        meta_df = meta_df.copy()
        meta_df.columns = meta_df.columns.str.strip()
        if filter_col and filter_val and filter_col in meta_df.columns:
            meta_df = meta_df[meta_df[filter_col] == filter_val].copy()
            
        von_col = next((c for c in meta_df.columns if c.lower() == 'von_datum'), None)
        bis_col = next((c for c in meta_df.columns if c.lower() == 'bis_datum'), None)
        
        if not von_col or not bis_col:
            for col in rename_cols.values():
                main_df[col] = None
            return main_df
            
        meta_df['Von_Datum_dt'] = pd.to_datetime(meta_df[von_col].astype(str).str.split('.').str[0], format='%Y%m%d', errors='coerce')
        meta_df['Bis_Datum_dt'] = pd.to_datetime(meta_df[bis_col].astype(str).str.split('.').str[0], format='%Y%m%d', errors='coerce').fillna(pd.Timestamp('2099-12-31'))
        meta_df = meta_df.dropna(subset=['Von_Datum_dt']).sort_values('Von_Datum_dt')
        
        cols_to_keep = ['Von_Datum_dt', 'Bis_Datum_dt']
        actual_renames = {}
        for src, dst in rename_cols.items():
            src_match = next((c for c in meta_df.columns if c.lower() == src.lower()), None)
            if src_match:
                cols_to_keep.append(src_match)
                actual_renames[src_match] = dst
                
        meta_df = meta_df[cols_to_keep].rename(columns=actual_renames)
        merged = pd.merge_asof(main_df, meta_df, left_on='Date', right_on='Von_Datum_dt', direction='backward')
        
        out_of_bounds = merged['Date'] > merged['Bis_Datum_dt']
        for dst in actual_renames.values():
            merged.loc[out_of_bounds, dst] = None
            
        for dst in rename_cols.values():
            if dst not in merged.columns:
                merged[dst] = None
                
        return merged.drop(columns=['Von_Datum_dt', 'Bis_Datum_dt'])

    df = merge_interval_meta(df, hw_df, {'Geraetetyp Name': 'Sensor_Typ', 'Messverfahren': 'Strahlungsschutz'})
    df = merge_interval_meta(df, param_df, {'Datenquelle (Strukturversion=SV)': 'Berechnungs_Methode'}, 'Parameter', 'TMK')
    df = merge_interval_meta(df, geo_df, {'Geogr.Breite': 'Historische_Breite', 'Geogr.Laenge': 'Historische_Laenge', 'Stationshoehe': 'Historische_Hoehe'})
    
    meta = metadata.get(station_id, {"Bundesland": "Unknown", "Latitude": None, "Longitude": None, "Altitude": None})
    df['Bundesland'] = meta['Bundesland']
    df['Latitude'] = meta['Latitude']
    df['Longitude'] = meta['Longitude']
    df['Altitude'] = meta['Altitude']
    
    # Enforce types
    df['Latitude'] = df['Latitude'].astype(float)
    df['Longitude'] = df['Longitude'].astype(float)
    df['Altitude'] = df['Altitude'].astype(float)
    df['Mean_Temp_C'] = df['Mean_Temp_C'].astype(float)
    df['Max_Temp_C'] = df['Max_Temp_C'].astype(float)
    df['Min_Temp_C'] = df['Min_Temp_C'].astype(float)
    
    df['Sensor_Typ'] = df['Sensor_Typ'].astype(str).replace('nan', None)
    df['Strahlungsschutz'] = df['Strahlungsschutz'].astype(str).replace('nan', None)
    df['Berechnungs_Methode'] = df['Berechnungs_Methode'].astype(str).replace('nan', None)
    
    # Also handle None values properly for PyArrow compat
    df.loc[df['Sensor_Typ'].isna(), 'Sensor_Typ'] = None
    df.loc[df['Strahlungsschutz'].isna(), 'Strahlungsschutz'] = None
    df.loc[df['Berechnungs_Methode'].isna(), 'Berechnungs_Methode'] = None
    
    df['Historische_Breite'] = df['Historische_Breite'].astype(float)
    df['Historische_Laenge'] = df['Historische_Laenge'].astype(float)
    df['Historische_Hoehe'] = df['Historische_Hoehe'].astype(float)
    
    from src.load.writer import get_target_schema
    schema = get_target_schema()
    
    # Ensure columns match schema order
    df = df[[f.name for f in schema]]
    
    return pa.Table.from_pandas(df, preserve_index=False, schema=schema)
