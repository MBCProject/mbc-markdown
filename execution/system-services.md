|||
|---|---|
|**ID**|**E1569**|
|**Objective(s)**|[Execution](../execution)|
|**Related ATT&CK Technique**|[System Services](https://attack.mitre.org/techniques/T1569/)|


System Services
===============
Malware may abuse system services or daemons to execute. 

**See ATT&CK:** [**System Services**](https://attack.mitre.org/techniques/T1569/).

Methods
-------
|Name|ID|Description|
|---|---|---|
|**MSDTC**|E1569.m01|The Distributed Transaction Coordinator (MSDTC) coordinates transaction across multiple resource managers (databases, message queues and file systems). This legitimate Microsoft service is part of Windows 2000 and later and can be used to import and load DLLs. Malware may abuse MSDTC to import and load DLLs.[[1]](#1)|


References
----------
<a name="1">[1]</a> https://support.resolver.com/hc/en-ca/articles/207161116-Configure-Microsoft-Distributed-Transaction-Coordinator-MSDTC-