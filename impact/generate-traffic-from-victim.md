<table>
<tr>
<td><b>ID</b></td>
<td><b>E1643</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../impact">Impact</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Generate Traffic from Victim (<a href="https://attack.mitre.org/techniques/T1643/">T1643</a>)</b></td>
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
<td><b>12 June 2023</b></td>
</tr>
</table>


# Generate Traffic from Victim

Malware may generate network traffic from a victim's system to achieve various malicious objectives. This could include disguising its own traffic, overwhelming a network with high traffic volume (Denial of Service attacks), exhausting the victim's system resources, or simulate clicks of advertising links that generate fraudulent ad revenue. The generated traffic can also be used to trigger network-based rules, alerts, or other types of indicators. This technique can make it difficult for defenders to identify malicious activity and can potentially lead to false positives. The ATT&CK technique, **Generate Traffic from Victim ([T1643](https://attack.mitre.org/techniques/T1643/))**, is only associated with the mobile platform, but the behavior is applicable to other platforms as well.

## Methods

|Name|ID|Description|
|---|---|---|
|**Advertisement Replacement Fraud**|E1643.m02|Malware injects ad windows onto websites the user views. [[2]](#2)|
|**Click Hijacking**|E1643.m01|Malware alters DNS server settings to route to a rogue DNS server: when the user clicks on a search result link displayed through a search engine query, malware re-routes the user to different website. Instead of going to the requested site, the user is taken to an alternate website such that the click triggers payment to the threat actor. [[1]](#1) This method is related to Unprotect technique U0904.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**DNSChanger**](../xample-malware/dnschanger.md)|2011|E1643.m02|Malware alters DNS server settings to route to a rogue DNS server for the purpose of click hijacking. [[1]](#1)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|Kovter performs click-fraud. [[4]](#4)|
|[**YiSpecter**](../xample-malware/yispecter.md)|2015|E1643.m02|The malware displays brief advertisements whenever the user opens applications on their phone. [[5]](#5)|

## References

<a name="1">[1]</a> https://www.huffingtonpost.com/2011/11/09/click-hijack-hackers-online-ad-scam_n_1084497.html

<a name="2">[2]</a> https://www.fipp.com/news/insightnews/what-are-the-nine-types-of-digital-ad-fraud

<a name="3">[3]</a> https://www.bleepingcomputer.com/virus-removal/remove-kovter-trojan

<a name="4">[4]</a> https://unit42.paloaltonetworks.com/yispecter-first-ios-malware-attacks-non-jailbroken-ios-devices-by-abusing-private-apis/

<a name="5">[5]</a> https://blog.malwarebytes.com/threat-analysis/2016/07/untangling-kovter/
