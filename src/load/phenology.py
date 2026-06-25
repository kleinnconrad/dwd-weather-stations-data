import os
import pyarrow as pa
import pyarrow.parquet as pq
from src.config.settings import PHENOLOGY_OUTPUT_DIR

def write_phenology_dataset(arrow_table: pa.Table):
    os.makedirs(PHENOLOGY_OUTPUT_DIR, exist_ok=True)
    parquet_ziel_pfad = os.path.join(PHENOLOGY_OUTPUT_DIR, "kirschbluete_doy.parquet")
    
    pq.write_table(arrow_table, parquet_ziel_pfad, compression='snappy')
    
    print(f"Successfully saved phenology data to: {parquet_ziel_pfad}")
    print(f"Number of extracted data points: {arrow_table.num_rows}")
    
    df_bluete = arrow_table.to_pandas()
    print("\n--- Analytischer Schnell-Check (Median Jultag) ---")
    median_historisch = df_bluete[df_bluete['Referenzjahr'] < 1990]['Jultag'].median()
    median_modern = df_bluete[df_bluete['Referenzjahr'] >= 2000]['Jultag'].median()
    print(f"Durchschnittlicher Blütebeginn VOR 1990 (Tag im Jahr): {median_historisch}")
    print(f"Durchschnittlicher Blütebeginn AB 2000 (Tag im Jahr): {median_modern}")
    differenz = median_historisch - median_modern
    print(f"Verschiebung: Die Natur ist heute im Schnitt {differenz} Tage früher dran.")
