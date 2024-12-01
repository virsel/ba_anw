import pandas as pd

# Den Dateipfad der CSV-Datei angeben (im selben Ordner wie das Python-Skript)
file_path = 'features_labeled_4llm_step3.csv'

# CSV-Datei mit pandas einlesen
df = pd.read_csv(file_path)

# Alle eindeutigen Werte der Spalte 'root_cause' abrufen
unique_root_causes = df['root_cause'].unique()

# Die eindeutigen Werte ausgeben
print(unique_root_causes)
