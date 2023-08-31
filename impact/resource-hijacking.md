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
<td><b>8 May 2023</b></td>
</tr>
</table>


# Resource Hijacking

Malware uses system resources for other than intended purposes, negatively impacting availability as well as performance, whether user endpoint or cloud-based. Digital currency mining, e.g., bitcoin, exemplifies this behavior: malicious actors infect systems with malware, taking control of system resources for purposes of verifying new transactions to the blockchain and earning new currency/coins. Cloud-based systems, e.g., Kubernetes clusters, are not immune to infection and are attractive targets for resource hijacking, given their substantial computing power [[1]](#1),[[2]](#2).

The related **Resource Hijacking ([T1496](https://attack.mitre.org/techniques/T1496/))** ATT&CK technique was defined subsequent to this MBC behavior.

## Methods

|Name|ID|Description|
|---|---|---|
|**Cryptojacking**|B0018.002|Consume system resources to mine for cryptocurrency (e.g., Bitcoin, Litecoin, etc.).|
|**Password Cracking**|B0018.001|Consume system resources for the purpose of password cracking.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**WebCobra**](../xample-malware/webcobra.md)|2018|B0018.002|The malware drops software that mines for cryptocurrency, depending on the system architecture. If the system has x86 architecture, the malware drops Cryptonight miner. If the system has x64 architecture, the malware drops Claymore's Zcash miner. [[3]](#3)|
|[**Adylkuzz**]|2017|--|Malware consumes system resources to mine for cryptocurrency. [[4]](#4)|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|--|GoBotKR can use the compromised computer’s network bandwidth to seed torrents or execute DDoS. [[5]](#5)|
|[**Clipminer**](../xample-malware/clipminer.md)|2011|--|Clipminer uses sytem resources to mine for cryptocurrency. [[6]](#6)|


## References
<a name="1">[1]</a> B. G. a. M. Ahuje,"CrowdStrike Discovers First-Ever Dero Cryptojacking Campaign Targeting Kubernetes," CrowdStrike, blog, 15 Mar. 2023. [Online]. Available: https://www.crowdstrike.com/blog/crowdstrike-discovers-first-ever-dero-cryptojacking-campaign-targeting-kubernetes/.

<a name="2">[2]</a> D. Ramel,"Hackers Turn Kubernetes Machine Learning to Crypto Mining in Azure Cloud," Virtualization and Cloud Review, 24 June 2020. [Online]. Available: https://virtualizationreview.com/articles/2020/06/24/azure-cloud-exploit.aspx.

<a name="3">[3]</a> https://www.mcafee.com/blogs/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/

<a name="4">[4]</a> https://blog.trendmicro.com/trendlabs-security-intelligence/wannacry-uiwix-ransomware-monero-mining-malware-follow-suit/

<a name="5">[5]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="6">[6]</a> https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/clipminer-bitcoin-mining-hijacking

