|||
|---|---|
|**ID**|**C0042**|
|**Objective(s)**|[Process](../process)|
|**Related ATT&CK Technique**|None|


Create Mutex
============
Malware creates a mutex. 

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**Poison-Ivy**](../xample-malware/poison-ivy.md)|2005|Poison Ivy has a default process mutex, but can be altered at build time [2] [[1]](#1)|

|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|Creates global mutexes signal that rootkit installation has occurred successfully  [[2]](#2)|

References
----------
<a name="1">[1]</a> https://www.mandiant.com/sites/default/files/2021-09/rpt-poison-ivy.pdf

<a name="2">[2]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en
