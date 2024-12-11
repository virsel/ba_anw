def get_unique_root_causes():
    return (
        "['CpuUsageRate(%)'], "
        "['NetworkP90(ms)'], "
        "['Placing order started', 'Order placed complete'], "
        "['Query product with name', 'Query product successfully'], "
        "['Received ad request', 'No context provided'], "
        "['Serving product page started', 'GetProduct start'], "
        "['Start charge card', 'Charge successfully']"
    )

# Funktionsaufruf und Ausgabe der Ergebnisse
print(get_unique_root_causes())
