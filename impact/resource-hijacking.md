
<table>
<tr>
<td><b>ID</b></td>
<td><b>B0018</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../impact">Impact</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b><a href="https://attack.mitre.org/techniques/T1496/">Resource Hijacking (T1496)</a></b></td>
</tr>
</table>


Resource Hijacking
==================
Uses system resources for other purposes; as a result, the system may not be available for intended uses.

The related [Resource Hijacking (T1496)](https://attack.mitre.org/techniques/T1496/) ATT&CK technique was defined subsequent to this MBC behavior.

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Cryptojacking**|B0018.002|Consume system resources to mine for cryptocurrency (e.g., Bitcoin, Litecoin, etc.).|
|**Password Cracking**|B0018.001|Consume system resources for the purpose of password cracking.|

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**WebCobra**](../xample-malware/webcobra.md)|2018|Drops software to mine for cryptocurrency. [[1]](#1)|
|Adylkuzz|May 2017|Consumes system resources to mine for cryptocurrency. [[2]](#2)|
|[**GotBotKR**](../xample-malware/gotbotkr.md)|2019|GoBotKR can use the compromised computer’s network bandwidth to seed torrents or execute DDoS. [[3]](#3)|

References
----------
<a name="1">[1]</a> https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/

<a name="2">[2]</a> https://blog.trendmicro.com/trendlabs-security-intelligence/wannacry-uiwix-ransomware-monero-mining-malware-follow-suit/

<a name="3">[3]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/
