|||
|---------|------------------------|
|**ID**|**M0031:T1483**|
|**Objective(s)**|[Command and Control](https://github.com/MAECProject/malware-behaviors/tree/master/command-and-control)|
|**Related ATT&CK Technique(s)**|[Domain Generation Algorithms](https://attack.mitre.org/techniques/T1483/)|

Domain Name Generation
======================
Malware generates the domain name of the command and control server to which it connects. Access to on the fly domains enables C2 to operate as domains and IP addresses are blocked. The algorithm can be complicated in more advanced bots; understanding the details so that names can be predicted can be useful in mitigation and response. [[1]](#1)

The newly defined ATT&CK Technique ([Domain Generation Algorithms](https://attack.mitre.org/techniques/T1483/)) is oriented toward an adversary perspective, but the examples include malware.

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|
|[**Kraken**](https://github.com/MAECProject/malware-behaviors/blob/master/xample-malware/kraken.md) | April 2008 | Kraken uses a domain generating algorithm to provide new domains. [[2]](#2)|
|[**Conficker**](https://github.com/MAECProject/malware-behaviors/blob/master/xample-malware/conficker.md)| November 2008| Conficker uses a domain name generator. [[3]](#3)

References
----------
<a name="1">[1]</a> https://blog.malwarebytes.com/security-world/2016/12/explained-domain-generating-algorithm/

<a name="2">[2]</a> http://blog.threatexpert.com/2008/04/kraken-changes-tactics.html

<a name="3">[3]</a> https://en.wikipedia.org/wiki/Conficker