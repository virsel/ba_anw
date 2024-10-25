# lemma rca
- real-world data from two domains: IT operations and OT operations.
- IT domain includes sub-datasets from Product Review and Cloud Computing microservice systems, while the OT domain includes SWaT and WADI sub-datasets from water treatment and distribution systems.
(https://arxiv.org/html/2406.05375v1 Kap. 3)

## Vorteile LEMMA Dataset
* Reale Systemfehler statt künstlicher Injektionen
* Domänenübergreifende Fehlerszenarien
* Praxisnahe Fehlerfälle

## Nachteile anderer Datasets
* Oft nur künstlich injizierte Fehler
* Meist auf einzelne Domänen beschränkt
* Limitierte Verfügbarkeit durch Vertraulichkeit
 (https://arxiv.org/html/2406.05375v1 Kap. 1)

##  IT domain

two microservice platforms: the Product Review Platform and the Cloud Computing Platform.
(https://arxiv.org/html/2406.05375v1 Kap. 3.1)

### Product Review
- simulated four distinct system faults, including out-of-memory, high-CPU-usage, external-storage-full, and DDoS attack, on four different dates

#### system status information
- The JMeter [21] was employed to collect the system status information, such as elapsed time, latency, connect time, thread name, throughput, etc. The latency is considered as system KPI as the system failure would result in the latency significantly increasing.

#### metriks
- recorded by Prometheus

#### logs
- Log data collected by ElasticSearch [20] and stored in JSON files with detailed timestamps and retrieval periods
- contents of system logs include timestamp, pod name, log message, etc.