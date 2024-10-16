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



