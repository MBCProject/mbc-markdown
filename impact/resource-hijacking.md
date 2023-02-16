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
<td><b>Resource Hijacking (<a href="https://attack.mitre.org/techniques/T1496/">T1496</a>)</b></td>
</tr>
<tr>
<td><b>Impact Type</b></td>
<td><b>Breach</b></td>
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


# Resource Hijacking

Malware uses system resources for other purposes; as a result, the system may not be available for intended uses.

The related **Resource Hijacking ([T1496](https://attack.mitre.org/techniques/T1496/))** ATT&CK technique was defined subsequent to this MBC behavior.

## Methods

|Name|ID|Description|
|---|---|---|
|**Cryptojacking**|B0018.002|Consume system resources to mine for cryptocurrency (e.g., Bitcoin, Litecoin, etc.).|
|**Password Cracking**|B0018.001|Consume system resources for the purpose of password cracking.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**WebCobra**](../xample-malware/webcobra.md)|2018|B0018.002|The malware drops software that mines for cryptocurrency, depending on the system architecture. If the system has x86 architecture, the malware drops Cryptonight miner. If the system has x64 architecture, the malware drops Claymore's Zcash miner. [[1]](#1)|
|[**Adylkuzz**]|2017|--|Malware consumes system resources to mine for cryptocurrency. [[2]](#2)|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|--|GoBotKR can use the compromised computer’s network bandwidth to seed torrents or execute DDoS. [[3]](#3)|
|[**Clipminer**](../xample-malware/clipminer.md)|2011|--|Clipminer uses sytem resources to mine for cryptocurrency. [[4]](#4)|


## References

<a name="1">[1]</a> https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/

<a name="2">[2]</a> https://blog.trendmicro.com/trendlabs-security-intelligence/wannacry-uiwix-ransomware-monero-mining-malware-follow-suit/

<a name="3">[3]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="4">[4]</a> https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/clipminer-bitcoin-mining-hijacking

