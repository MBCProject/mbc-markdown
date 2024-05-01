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
<td><b>2.2</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>2 August 2022</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>30 April 2024</b></td>
</tr>
</table>


# Modify Existing Service

Malware may modify an existing service to gain persistence. Modification may include disabling a service.

See ATT&CK: **Create or Modify System Process::Windows Service ([T1543.003](https://attack.mitre.org/techniques/T1543/003/))**.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**YiSpecter**](../xample-malware/yispecter.md)|2015|--|The malware hijacks other installed applications' launch routines to use "ADPage" (an installed malicious app) to display advertisements. [[2]](#2)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|--|Malware locates an inactive driver service to hijack and set it to start automatically. [[3]](#3)|
|[**Conficker**](../xample-malware/conficker.md)|2008|--|Malware copies itself into the $systemroot%\system32 directory and registers as a service. [[4]](#4)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|--|Shamoon enables the RemoteRegistry service to allow remote registry modification. [[5]](#5)|
|[**Vobfus**](../xample-malware/vobfus.md)|2016|--|Vobfus disables Windows AutoUpdate and patches the first byte of TerminateProcess and TerminateThread API with C3 (RET Instruction) to prevent external processes from terminating the running instance of malware. [[6]](#6)|

## Detection

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[volatility_svcscan_1](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/volatility_sig.py)|Modify Existing Service (F0011)|--|
|[volatility_svcscan_2](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/volatility_sig.py)|Modify Existing Service (F0011)|--|
|[volatility_svcscan_3](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/volatility_sig.py)|Modify Existing Service (F0011)|--|
|[antiav_servicestop](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antiav_servicestop.py)|Modify Existing Service (F0011)|OpenServiceA, ControlService, OpenServiceW|
|[persistence_service](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/persistence_service.py)|Modify Existing Service (F0011)|--|
|[modify_security_center_warnings](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/modifies_seccenter.py)|Modify Existing Service (F0011)|--|

## References

<a name="1">[1]</a> https://www.cyber.nj.gov/threat-center/threat-profiles/trojan-variants/poison-ivy

<a name="2">[2]</a> https://unit42.paloaltonetworks.com/yispecter-first-ios-malware-attacks-non-jailbroken-ios-devices-by-abusing-private-apis/

<a name="3">[3]</a> https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf

<a name="4">[4]</a> https://en.wikipedia.org/wiki/Conficker

<a name="5">[5]</a> https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-returns-to-wipe-systems-in-middle-east-europe/

<a name="6">[6]</a> https://securitynews.sonicwall.com/xmlpost/revisiting-vobfus-worm-mar-8-2013/