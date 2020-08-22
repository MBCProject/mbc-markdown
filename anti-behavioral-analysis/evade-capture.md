|||
|---|---|
|**ID**|**B0036**|
|**Objective(s)**|[Anti-Behavioral Analysis](../anti-behavioral-analysis)|
|**Related ATT&CK Technique**|None|


Capture Evasion
===============
Malware has characteristics enabling it to evade capture from the infected system.

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Encrypted Payloads**|B0036.002|Decryption key is stored external to the executable or never touches the disk.|
|**Memory-only Payload**|B0036.001|Malware is never written to disk (e.g., RAT plugins received from the controller are never written to disk).|
|**Multiple Stages of Loaders**|B0036.003|Multiple stages of loaders are used with an encoded payload.|
