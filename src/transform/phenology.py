import io
import pandas as pd
import pyarrow as pa

def transform_phenology_data(raw_content: bytes) -> pa.Table:
    print("Processing phenology data...")
    # DWD-Daten nutzen oft Latin-1 Encoding und Semikolons als Trennzeichen
    roh_text = raw_content.decode('latin1')
    df = pd.read_csv(io.StringIO(roh_text), sep=';')
    
    # Spaltennamen bereinigen (Leerzeichen entfernen)
    df.columns = df.columns.str.strip()
    
    # Filtern auf Phase_ID 5: "Beginn der Blüte" (Sauerkirsche spezifisch)
    if 'Phase_id' not in df.columns:
        raise ValueError("Die Spalte 'Phase_id' fehlt in den geladenen Daten.")
        
    df_bluete = df[df['Phase_id'] == 5].copy()
    
    # Wir behalten die analytisch wichtigen Spalten
    df_bluete = df_bluete[['Stations_id', 'Referenzjahr', 'Jultag']]
    
    # Fehleinträge (oft als -999 markiert) bereinigen
    df_bluete = df_bluete[df_bluete['Jultag'] > 0]
    
    # Datentypen für Parquet erzwingen
    df_bluete['Stations_id'] = df_bluete['Stations_id'].astype(int)
    df_bluete['Referenzjahr'] = df_bluete['Referenzjahr'].astype(int)
    df_bluete['Jultag'] = df_bluete['Jultag'].astype(int) # Tag des Jahres (1-365)

    schema = pa.schema([
        ('Stations_id', pa.int32()),
        ('Referenzjahr', pa.int32()),
        ('Jultag', pa.int32())
    ])
    
    return pa.Table.from_pandas(df_bluete, schema=schema)
