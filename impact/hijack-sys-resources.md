|||
|---------|------------------------|
|**ID**|**B0018**|
|**Objective(s)**| [Impact](https://github.com/MBCProject/mbc-beta/tree/master/impact)|
|**Related ATT&CK Technique**|[Resource Hijacking](https://attack.mitre.org/techniques/T1496/)|


Resource Hijacking
==================
Uses system resources for other purposes; as a result, the system may not be available for intended uses.

The subsequently defined ATT&CK technique [Resource Hijacking](https://attack.mitre.org/techniques/T1496/) is related to this MBC behavior.

Methods
-------
|ID|Name|Description|
|-----------------------------|--------|-----------------------------|
|B0018.001|**Password Cracking**|Consume system resources for the purpose of password cracking.|
|B0018.002|**Cryptojacking**|Consume system resources to mine for cryptocurrency (e.g., Bitcoin, Litecoin, etc.).|

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|
|[**WebCobra**](https://github.com/MBCProject/mbc-beta/blob/master/xample-malware/webcobra.md)|2018|Drops software to mine for cryptocurrency. [[1]](#1)|
| Adylkuzz| May 2017| Consumes system resources to mine for cryptocurrency. [[2]](#2)| 

References
----------
<a name="1">[1]</a> https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/

<a name="2">[2]</a> https://blog.trendmicro.com/trendlabs-security-intelligence/wannacry-uiwix-ransomware-monero-mining-malware-follow-suit/
