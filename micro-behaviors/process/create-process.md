|||
|---|---|
|**ID**|**C0017**|
|**Objective(s)**|[Process](../process)|
|**Related ATT&CK Technique**|None|


Create Process
==============
Malware creates a process. 

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Create Process via Shellcode**|C0017.001|Malware uses shellcode to create a process.|
|**Create Process via WMI**|C0017.002|Malware uses WMI to create a process.|
|**Create Suspended Process**|C0017.003|Malware created a suspended process.|


Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|Stuxnet will use WMI operations with the explorere.exe token in order to copy itself and exscute on the remote share  [[1]](#1)|


References
----------
<a name="1">[1]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en
