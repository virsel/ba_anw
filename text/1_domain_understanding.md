## Bedeutung von RCA
- RCA (Root Cause Analysis) kann in verschiedenen Bereichen eingesetzt werden:  
    - Produktion   
    - Gesundheitswesen  
    - Informationstechnologie  
    - Regierung  
    - Kundenzufriedenheit (z.b. bei Cloudanbietern https://www.youtube.com/watch?v=GKiU7cI3fHs)

- Ziel von RCA ist die Identifizierung der Grundursache eines Problems, nicht nur der Symptome
- Nach Identifizierung der Grundursache können Korrekturmaßnahmen ergriffen werden, um ein erneutes Auftreten des Problems zu verhindern
- RCA kann zeitaufwändig sein, ist aber eine lohnende Investition zur Verbesserung von Qualität und Zuverlässigkeit

## Offline RCA
- Training mit großem historischen Datensatz
- Periodische komplette Neutrainings
- Keine Anpassung zwischen Trainings
- Beispiel: Wöchentliches/monatliches Neutraining
- Wichtige Methoden:
  * PC: Kausale Graphenerstellung mittels Unabhängigkeitstest
  * Dynotears: Konstruiert dynamische Bayessche Netzwerke
  * C-LSTM: Modelliert zeitliche Abhängigkeiten
  * GOLEM: Verwendet relaxierte DAG-Beschränkungen
  * REASON: Lernt intra- und inter-level kausale Beziehungen
  * Nezha: Multi-modales Verfahren für Anomalie-Erkennung
  * MULAN: Multi-modales Verfahren mit Korrelationslernen
- Vorteile:
  * Gründlichere Analyse möglich
  * Kann komplexere Algorithmen verwenden
  * Nutzt vollständige historische Daten
  (https://arxiv.org/html/2406.05375v1 Kap. 4)

## Online RCA
- Initiales Training mit historischen Daten
- Kontinuierliche Aktualisierung durch Mini-Batches
- Behält gelerntes Wissen bei (inkrementelles Lernen)
- Schnelle Anpassung an neue Systemzustände
- Beispiel: 5-Minuten-Fenster für Updates
- Wichtige Methoden:
  * CORAL: Inkrementelles kausales Graphenlernen
  * NOTEARS*: Online-Adaption von NOTEARS
  * GOLEM*: Online-Version von GOLEM
- Eigenschaften:
  * Verwendet initiale normale Daten (z.B. 8 Stunden) für ersten Graph
  * Kontinuierliche Aktualisierung bei neuen Datenbatches
  * Schnellere Anpassung an sich ändernde Muster
  (https://arxiv.org/html/2406.05375v1 Kap. 4)

## Unterschied Online/Offline

1. Update-Häufigkeit:
   - Online: Häufige kleine Updates (Mini-Batches)
   - Offline: Seltene große Updates (kompletter Datensatz)

2. Lernmethode:
   - Online: Inkrementelles Lernen (baut auf bestehendem Wissen auf)
   - Offline: Komplettes Neutraining von Grund auf

3. Ressourcennutzung:
   - Online: Kontinuierliche kleine Berechnungen
   - Offline: Periodische intensive Berechnungen

4. Anpassungsfähigkeit:
   - Online: Schnelle Reaktion auf neue Systemmuster
   - Offline: Verzögerte Anpassung bis zum nächsten Training

5. Praktischer Einsatz:
   - Online: Gut für sich schnell ändernde Systeme
   - Offline: Gut für stabile, vorhersehbare Systeme

## manuelles RCA:
 The manual RCA
investigation consists of 5 steps: 1) Incident Detection, which typically relies on
Analysis of Key Performance Indices. 2) Symptom Detection, which detect the
primary effect of the service disruption on performance factor. 3) Investigation,
which requires intensive communication between teams of Site Reliability Engineer
in order to understand the nature of the incident and decide a target team who can
undertake the RCA Investigation. 4) Immediate Resolution, based on the
conclusion of investigation, action taken is workaround to mitigate problem
temporarily. 5) Root Cause Investigation, the RCA target team can finally find the
true root cause.
(https://www.aasmr.org/jsms/Vol13/No.1/Vol.13.No.1.19.pdf, S. 346)

## mögliche Datenquellen:
Root Cause Analysis (RCA) for IT incidents will involve data from various
domains. For example, when there is a delay in access to a database application, the
domain that must be investigated is not limited to the application area (system) but
also infrastructure aspects such as servers, disk storage, network, and security.
System logs provide the information about each component's status and record the
system operational changes such as starting or stopping services, software
configuration modifications, software execution errors and hardware faults, and so
on. Therefore, telemetry data generated from various application systems and
infrastructure devices such as log files, server metrics, SNMP, Syslog, usage stats
events, IT service tickets, and Known Error Database (KEDB) can be optimized as
strategic assets in predicting the root cause of an IT incident. 
(https://www.aasmr.org/jsms/Vol13/No.1/Vol.13.No.1.19.pdf, S. 346)



