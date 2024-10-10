#### problemstellung
Traditional RCA methods, which rely on manual investigations of data sources such as logs and traces,
are often laborious, error-prone, and challenging for on-call
engineers  
https://arxiv.org/pdf/2305.15778 (Abstract)

#### methodik
 The first step is to collect
system logs from various systems with various formats. The second step is to
process, convert, and standardize all collected logs from unstructured to structured
form. In addition, it also performs data abstraction by taking the similarity and
relevance of information in log data into account. The third step is to analyze the
log to make it more readable and understandable before continuing to analyze
system behavior. Finally, there are two approaches: reactive or proactive. In the
reactive approach, it focuses on anomaly detection, root cause analysis and system
recovery. Meanwhile, in a proactive approach, it focuses on preventing future
incident by predicting it
(https://www.aasmr.org/jsms/Vol13/No.1/Vol.13.No.1.19.pdf, S. 347)