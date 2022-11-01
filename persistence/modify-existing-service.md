<table>
<tr>
<td><b>ID</b></td>
<td><b>F0011</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../persistence">Persistence</a>, <a href="../privilege-escalation">Privilege Escalation</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Create or Modify System Process::Windows Service (<a href="https://attack.mitre.org/techniques/T1543/003/">T1543.003</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>2 August 2022</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>31 October 2022</b></td>
</tr>
</table>


Modify Existing Service
=======================
Malware may modify an existing service to gain persistence. Modification may include disabling a service.

See ATT&CK: **Create or Modify System Process::Windows Service ([T1543.003](https://attack.mitre.org/techniques/T1543/003/))**.

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**Poison-Ivy**](../xample-malware/poison-ivy.md)|2005|After the Poison-Ivy server is running on the target machine, the attacker can use a Windows GUI client to control the target computer. [[1]](#1)|
|[**YiSpecter**](../xample-malware/yispecter.md)|2015|Hijacks other installed applications' launch routines to use "ADPage" (an installed malicious app) to display advertisements  [[2]](#2)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|Locates an inactive driver service to Hijack and set it to start automatically [[3]](#3)|
|[**Conficker**](../xample-malware/conficker.md)|2008|Copies itself into the $systemroot%\system32 directory and registers as a service  [[4]](#4)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|Shamoon enables the RemoteRegistry service to allow remote registry modification [[5]](#5)|

References
----------
<a name="1">[1]</a> https://www.cyber.nj.gov/threat-profiles/trojan-variants/poison-ivy

<a name="2">[2]</a> http://researchcenter.paloaltonetworks.com/2015/10/yispecter-first-ios-malware-attacks-non-jailbroken-ios-devices-by-abusing-private-apis/

<a name="3">[3]</a> https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf

<a name="4">[4]</a> https://en.wikipedia.org/wiki/Conficker

<a name="5">[5]</a> https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-returns-to-wipe-systems-in-middle-east-europe/
