|||
|---------|------------------------|
|**ID**|**B0024**|
|**Objective(s)**|[Execution](https://github.com/MBCProject/mbc-markdown/tree/master/execution)|
|**Related ATT&CK Technique**|None|

Prevent Concurrent Execution
============================
To avoid running multiple instances of itself, malware may check a system to see if it is already running.

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|
|[**Bagle**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/bagle.md)|2004|Some variants look for an unnamed mutex to ensure only one copy of itself is running on a system. [1](#1)|

References
----------
<a name="1">[1]</a> https://www.trendmicro.com/vinfo/us/threat-encyclopedia/archive/malware/worm_bagle.u