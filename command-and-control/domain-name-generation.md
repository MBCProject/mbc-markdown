|||
|---|---|
|**ID**|**B0031**|
|**Objective(s)**|[Command and Control](../command-and-control)|
|**Related ATT&CK Sub-Technique**|[Dynamic Resolution: Domain Generation Algorithms](https://attack.mitre.org/techniques/T1568/002/)|


Domain Name Generation
======================
Malware generates the domain name of the controller to which it connects. Access to on the fly domains enables C2 to operate as domains and IP addresses are blocked. The algorithm can be complicated in more advanced implants; understanding the details so that names can be predicted can be useful in mitigation and response. [[1]](#1)

The subsequently defined ATT&CK sub-technique [Dynamic Resolution: Domain Generation Algorithms](https://attack.mitre.org/techniques/T1568/002/), which is oriented toward an adversary perspective (although its examples include malware), is related to this MBC behavior.

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**Kraken**](../xample-malware/kraken.md)|April 2008|Kraken uses a domain generating algorithm to provide new domains. [[2]](#2)|
|[**Conficker**](../xample-malware/conficker.md)|November 2008|Conficker uses a domain name generator. [[3]](#3)|
|[**CryptoLocker**](../xample-malware/cryptolocker.md)|2013|The malware sends a hash value generated from system information [[4]](#4|
|[**Ursnif**](../xample-malware/ursnif.md)|2016|Ursnif has used a Domain name generation algorithm in the past [[5]](#5)|

References
----------
<a name="1">[1]</a> https://blog.malwarebytes.com/security-world/2016/12/explained-domain-generating-algorithm/

<a name="2">[2]</a> http://blog.threatexpert.com/2008/04/kraken-changes-tactics.html

<a name="3">[3]</a> https://en.wikipedia.org/wiki/Conficker

<a name="4">[4]</a> https://www.secureworks.com/research/cryptolocker-ransomware

<a name="5">[5]</a> https://www.proofpoint.com/us/threat-insight/post/ursnif-variant-dreambot-adds-tor-functionality
