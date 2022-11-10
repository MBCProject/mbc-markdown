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
<td><b>31 October 2022</b></td>
</tr>
</table>


Supply Chain Compromise
=======================
The supply chain may be compromised to enable initial malware infection. MBC objectives don't encompass initial infection, but the malware-related methods are listed below supplement the information available defined in ATT&CK and allow for lateral movement: **Supply Chain Compromise ([T1195](https://attack.mitre.org/techniques/T1195/), [T1474](https://attack.mitre.org/techniques/T1474/))**.  

## Methods

|Name|ID|Description|
|---|---|---|
|**Abuse Enterprise Certificates**|E1195.m01|Abusing enterprise certificates enables malware to exploit private APIs and infect a wide range of users (see *Exploit Private APIs* below).|
|**Exploit Private APIs**|E1195.m02|Malware can exploit private APIs to infect jailbroken and non-jailbroken iOS devices. Research shows that over 100 apps in the App Store have abused private APIs and bypassed Apple’s strict code review.|

## Use in Malware

|Name|Date|Description|
|---|---|---|
|[**YiSpecter**](../xample-malware/yispecter.md)|October 2015|Attacks both jailbroken and non-jailbroken iOS devices by exploiting private APIs. [[1]](#1)|

## References

<a name="1">[1]</a> http://researchcenter.paloaltonetworks.com/2015/10/yispecter-first-ios-malware-attacks-non-jailbroken-ios-devices-by-abusing-private-apis/
