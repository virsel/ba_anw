# lemma rca
- real-world data from two domains: IT operations and OT operations.
- IT domain includes sub-datasets from Product Review and Cloud Computing microservice systems, while the OT domain includes SWaT and WADI sub-datasets from water treatment and distribution systems.
(https://arxiv.org/html/2406.05375v1 Kap. 3)

#### cloud logs von lemma rca
- in logs sind errors  
- error verursacht durch gelabelten root cause sind vermutlich mit "with root cause" gekennzeichnet (carts-b59845878-zhk8s_messages_structured 2023_12_07)

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

### Cloud Computing
- six different types of faults (such as cryptojacking, mistakes made by GitOps, configuration change failure, etc.)

#### system status information
- Latency, error rate, and utilization rate were tracked using JMeter tool, serving as Key performance indicators (KPIs)

#### metriks
- were directly extracted from CloudWatch Metrics on EC2 instances, and the time granularity of these system metrics is 1 second

#### logs
- acquired from CloudWatch Logs, 
- consisting of three data types (i.e., log messages, api debug log, and mysql log). 
- Log message describes general log message about all system entities; 
- api debug log contains debug information of the AP layer when the API was executed; 
- mysql logs contain log information from database layer, including connection logs to mysql, which user connected from which host, and what queries were executed.