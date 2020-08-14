|||
|---------|------------------------|
|**ID**|**B0019**|
|**Objective(s)**| [Impact](https://github.com/MBCProject/mbc-beta/tree/master/impact)|
|**Related ATT&CK Sub-Technique**|[Data Manipulation: Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1565/002/)|


Manipulate Network Traffic
==========================
Malware intercepts and manipulates network traffic, typically accessing or modifying data, going to or originating from the system on which the malware instance is executing. Also known as a Man-in-the-Middle attack.

The subsequently defined ATT&CK sub-technique [Data Manipulation: Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1565/002/) is related to this MBC behavior.

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|
|[**SearchAwesome**](https://github.com/MBCProject/mbc-beta/blob/master/xample-malware/searchawesome.md)| 2018| Intercepts encrypted web traffic to inject adds. [[1]](#1)|
|[**MazarBot**](https://github.com/MBCProject/mbc-beta/blob/master/xample-malware/mazarbot.md)|2016|Intercepts data coming into and going out of device.|

References
----------
<a name="1">[1]</a> https://blog.malwarebytes.com/threat-analysis/2018/10/mac-malware-intercepts-encrypted-web-traffic-for-ad-injection/