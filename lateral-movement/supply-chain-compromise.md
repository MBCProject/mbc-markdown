<table>
<tr>
<td><b>ID</b></td>
<td><b>E1195</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../lateral-movement">Lateral Movement</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Supply Chain Compromise (<a href="https://attack.mitre.org/techniques/T1195/">T1195</a>, <a href="https://attack.mitre.org/techniques/T1474/">T1474</a>)</b></td>
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
<td><b>17 August 2023</b></td>
</tr>
</table>


# Supply Chain Compromise

The supply chain may be compromised to enable initial malware infection. MBC objectives don't encompass initial infection, but the malware-related methods listed below supplement the information available and defined in ATT&CK and allow for lateral movement: **Supply Chain Compromise ([T1195](https://attack.mitre.org/techniques/T1195/), [T1474](https://attack.mitre.org/techniques/T1474/))**.  

## Methods

|Name|ID|Description|
|---|---|---|
|**Abuse Enterprise Certificates**|E1195.m01|Abusing enterprise certificates enables malware to exploit private APIs and infect a wide range of users (see *Exploit Private APIs* below).|
|**Exploit Private APIs**|E1195.m02|Malware can exploit private APIs to infect jailbroken and non-jailbroken iOS devices. Research shows that over 100 apps in the App Store have abused private APIs and bypassed Apple’s strict code review.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|--|TrickBot comes with a signed downloader component. [[2]](#2)|
|[**YiSpecter**](../xample-malware/yispecter.md)|2015|E1195.m01|YiSpecter's malicious apps were signed with three iOS enterprise certificates issued by Apple so they can be installed as enterprise apps on non-jailbroken iOS devices via in-house distribution. [[1]](#1)|
|[**YiSpecter**](../xample-malware/yispecter.md)|2015|E1195.m02|Within the malware, use of the private API allows installation of malicious apps and uninstallation of legitimate apps without user notification. [[1]](#1)|


## References

<a name="1">[1]</a> https://unit42.paloaltonetworks.com/yispecter-first-ios-malware-attacks-non-jailbroken-ios-devices-by-abusing-private-apis/

<a name="2">[2]</a> https://eclypsium.com/wp-content/uploads/TrickBot-Now-Offers-TrickBoot-Persist-Brick-Profit.pdf

