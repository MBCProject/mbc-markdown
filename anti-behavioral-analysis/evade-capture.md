|||
|---------|------------------------|
|**ID**|**B0036**|
|**Objective(s)**|[Anti-Behavioral Analysis](https://github.com/MBCProject/mbc-markdown/tree/master/anti-behavioral-analysis)|
|**Related ATT&CK Technique**|None|

Capture Evasion
===============
Malware has characteristics enabling it to evade capture from the infected system.

Methods
-------
|ID|Name|Description|
|-----------------------------|--------|-----------------------------|
|B0036.001|**Memory-only Payload**|Malware is never written to disk (e.g., RAT plugins received from the controller are never written to disk).|
|B0036.002|**Encrypted Payloads**|Decryption key is stored external to the executable or never touches the disk.|
|B0036.003|**Multiple Stages of Loaders**: Multiple stages of loaders are used with an encoded payload.|

 
 
