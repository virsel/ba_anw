import pandas as pd
import ast

# CSV-Datei einlesen (passen Sie den Pfad zu Ihrer CSV-Datei an)
df = pd.read_csv('features_labeled_4llm_step3.csv')

# Konvertiere result_list_inhealthy_lessoften und result_list_inhealthy_moreoften von String-Listen zu echten Listen
df['result_list_inhealthy_lessoften'] = df['result_list_inhealthy_lessoften'].apply(ast.literal_eval)
df['result_list_inhealthy_moreoften'] = df['result_list_inhealthy_moreoften'].apply(ast.literal_eval)

# Gruppiere nach 'inject_time' und fasse die Werte zusammen
grouped_df = df.groupby('inject_time').agg({
    'abnormal_time': 'first',  # Nimm das erste Datum
    'inject_pod': 'first',  # Nimm das erste Pod (kann angepasst werden, je nach Logik)
    'inject_type': 'first',  # Nimm den ersten Typ
    'normal_time': 'first',  # Nimm das erste Normal Time
    'result_list_inhealthy_lessoften': 'sum',  # Füge Listen zusammen
    'result_list_inhealthy_moreoften': 'sum',  # Füge Listen zusammen
    'root_cause': 'first',  # Nimm das erste Root Cause
    'inject_comp_tdiff': 'mean',  # Durchschnittliche Differenz
    'nezha_rank_050': 'mean'  # Durchschnittliche Rank
}).reset_index()

# Speichern der Datei unter dem angegebenen Namen im aktuellen Arbeitsverzeichnis
grouped_df.to_csv('features_labeled_4llm_step4.csv', index=False)

# Erfolgsmeldung
print("Die Datei wurde erfolgreich unter 'features_labeled_4llm_step4.csv' gespeichert.")
