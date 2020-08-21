|||
|---|---|
|**ID**|**B0025**|
|**Objective(s)**|[Execution](https://github.com/MBCProject/mbc-markdown/tree/master/execution)|
|**Related ATT&CK Technique**|None|


Conditional Execution
=====================
Malware checks system environment conditions or characteristics to determine execution path. For example, malware may not run or be dormant unless system conditions are right, or file that is dropped may vary according to execution environment. Conditional execution happens autonomously, not because of an attacker's command.

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Suicide Exit**|B0025.001|Malware terminates its execution based on a trigger condition or value (or because it has completed).|

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**WebCobra**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/webcobra.md)|2018|Drops either Cryptonight or Claymore's Zcash miner, depending on system architecture. [[1]](#1)|
|[**Conficker**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/conficker.md)|2008|A routine causes the process to suicide exit if the keyboard language is set to Ukranian.|

References
----------
<a name="1">[1]</a> https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/
