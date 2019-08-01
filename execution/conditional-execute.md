|||
|---------|------------------------|
|**ID**|**M0025**|
|**Objective(s)**|[Execution](https://github.com/MAECProject/malware-behaviors/tree/master/execution)|
|**Related ATT&CK Technique(s)**|None|

Conditional Execution
=====================
Malware checks system environment conditions or characteristics to determine execution path. For example, malware may not run or be dormant unless system conditions are right, or file that is dropped may vary according to execution environment. Conditional execution happens autonomously, not because of an attacker's command.

Methods
-------
* **Suicide Exit**: Malware terminates its execution based on a trigger condition or value (or because it has completed). 

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|
|[WebCobra](https://github.com/MAECProject/malware-behaviors/blob/master/xample-malware/webcobra.md)| Drops either Cryptonight or Claymore's Zcash miner, depending on system architecture. [[1]](#1)|

References
----------
<a name="1">[1]</a> https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/
