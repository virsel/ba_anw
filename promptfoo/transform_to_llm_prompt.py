import pandas as pd
import ast

# CSV-Datei einlesen (Pfad anpassen)
df = pd.read_csv('features_labeled_4llm_step3.csv')

# Konvertiere String-Listen zu echten Listen
df['result_list_inhealthy_lessoften'] = df['result_list_inhealthy_lessoften'].apply(ast.literal_eval)
df['result_list_inhealthy_moreoften'] = df['result_list_inhealthy_moreoften'].apply(ast.literal_eval)

# Gruppiere nach 'inject_time' und aggregiere die Daten
grouped_df = df.groupby('inject_time').agg({
    'abnormal_time': 'first',      # Nimm das erste Datum
    'inject_pod': 'first',         # Nimm das erste Pod
    'inject_type': 'first',        # Nimm den ersten Typ
    'result_list_inhealthy_lessoften': 'sum',  # Füge Listen zusammen
    'result_list_inhealthy_moreoften': 'sum',  # Füge Listen zusammen
    'root_cause': 'first',         # Nimm das erste Root Cause
    'inject_comp_tdiff': 'mean',   # Durchschnittliche Differenz
    'nezha_rank_050': 'mean'       # Durchschnittliche Rank
}).reset_index()

# Entferne unerwünschte Spalten
grouped_df = grouped_df.drop(columns=['inject_time', 'abnormal_time', 'inject_pod', 'inject_comp_tdiff', 'nezha_rank_050'])

# Spalten umbenennen
grouped_df.rename(columns={
    'inject_type': '__expected',
    'result_list_inhealthy_lessoften': 'lessoften',
    'result_list_inhealthy_moreoften': 'moreoften',
    'root_cause': 'rootcause_bynezha'
}, inplace=True)

# Ersetze Kommas durch Semikolons in den Spalten 'lessoften' und 'moreoften'
grouped_df['lessoften'] = grouped_df['lessoften'].astype(str).apply(lambda x: x.replace(',', ';'))
grouped_df['moreoften'] = grouped_df['moreoften'].astype(str).apply(lambda x: x.replace(',', ';'))

# Ersetze hin zu den injecttypes (als wirkliche rootcauses)
grouped_df['__expected'] = grouped_df['__expected'].replace(
    {'cpu_contention': 'CPU', 'cpu_consumed': 'CPU','exception': 'CODEBUG', 'return': "CODEBUG", 'network_delay': 'Network'}
)


# Verschiebe '__expected' nach hinten
columns = list(grouped_df.columns)
columns.append(columns.pop(columns.index('__expected')))
grouped_df = grouped_df[columns]

# Speichern der aggregierten Datei
grouped_df.to_csv('features_labeled_4llm_step4.csv', index=False)

# Erfolgsmeldung
print("Die Datei wurde erfolgreich unter 'features_labeled_4llm_step4.csv' gespeichert.")
