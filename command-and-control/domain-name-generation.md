<table>
<tr>
<td><b>ID</b></td>
<td><b>B0031</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../command-and-control">Command and Control</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Dynamic Resolution: Domain Generation Algorithms (<a href="https://attack.mitre.org/techniques/T1568/002/">T1568.002</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>21 November 2022</b></td>
</tr>
</table>


# Domain Name Generation

Malware generates the domain name of the controller to which it connects. Access to on the fly domains enables C2 to operate as domains and IP addresses are blocked. The algorithm can be complicated in more advanced implants; understanding the details so that names can be predicted can be useful in mitigation and response. [[1]](#1)

The related **Dynamic Resolution: Domain Generation Algorithms ([T1568.002](https://attack.mitre.org/techniques/T1568/002/))** ATT&CK sub-technique (oriented toward an adversary perspective with examples that include malware) was defined subsequent to this MBC behavior.

This behavior is related to Unprotect technique U0906.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Kraken**](../xample-malware/kraken.md)|2008|--|Kraken uses a domain generating algorithm to provide new domains. [[2]](#2)|
|[**Conficker**](../xample-malware/conficker.md)|2008|--|Conficker uses a domain name generator seeded by the current date to ensure that every copy of the virus generates the same names on their respective days. [[3]](#3)|
|[**CryptoLocker**](../xample-malware/cryptolocker.md)|2013|--|The malware uses an internal domain generation algorithm. [[4]](#4)|
|[**Ursnif**](../xample-malware/ursnif.md)|2016|--|Previous interations of Ursnif have used a Domain Name Generation algorithm. [[5]](#5)|


## References

<a name="1">[1]</a> https://blog.malwarebytes.com/security-world/2016/12/explained-domain-generating-algorithm/

<a name="2">[2]</a> http://blog.threatexpert.com/2008/04/kraken-changes-tactics.html

<a name="3">[3]</a> https://en.wikipedia.org/wiki/Conficker

<a name="4">[4]</a> https://www.secureworks.com/research/cryptolocker-ransomware

<a name="5">[5]</a> https://www.proofpoint.com/us/threat-insight/post/ursnif-variant-dreambot-adds-tor-functionality

