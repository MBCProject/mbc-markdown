|||
|---------|------------------------|
|**ID**|**M0018:T1496**|
|**Objective(s)**| [Impact](https://github.com/MAECProject/malware-behaviors/tree/master/impact)|
|**Related ATT&CK Technique(s)**|[Resource Hijacking](https://attack.mitre.org/techniques/T1496/)|


Hijack System Resources
=======================
Uses system resources for other purposes; as a result, the system may not be available for intended uses.

Methods
-------
* **Password Cracking**: Consume system resources for the purpose of password cracking.
* **Cryptojacking**: Consume system resources to mine for cryptocurrency (e.g., Bitcoin, Litecoin, etc.).

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|
| WebCobra| November 2018| Drops software to mine for cryptocurrency. [[1]](#1)|
| Adylkuzz| May 2017| Consumes system resources to mine for cryptocurrency. [[2]](#2)| 

References
----------
<a name="1">[1]</a> https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/

<a name="2">[2]</a> https://blog.trendmicro.com/trendlabs-security-intelligence/wannacry-uiwix-ransomware-monero-mining-malware-follow-suit/
