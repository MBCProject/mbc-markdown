<table>
<tr>
<td><b>ID</b></td>
<td><b>E1204</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../execution">Execution</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>User Execution (<a href="https://attack.mitre.org/techniques/T1204">T1204</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>28 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>17 August 2023</b></td>
</tr>
</table>


# User Execution

Malware may include code that relies on specific actions by a user to execute. Note that this MBC behavior differs from [User Execution](https://attack.mitre.org/techniques/T1204) in that it does do not include direct code execution (user action for *initial* execution) - MBC does not encompass ATT&CK's Initial Access Tactic.  

This behavior is related to Unprotect technique U1339.

See ATT&CK Technique: **User Execution ([T1204](https://attack.mitre.org/techniques/T1204/))**.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|--| GoBotKR makes their malware look like the torrent content that the user intended to download, in order to entice a user to click on it. [[1]](#1)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|--|The malware relies on a victim to execute itself. [[2]](#2)|
|[**Terminator**](../xample-malware/terminator.md)|2013|--|The malware relies on user interaction to execute. [[3]](#3)|
|[**Vobfus**](../xample-malware/vobfus.md)|2016|--|The malware relies on user interaction to run the executable. [[4]](#4)|
|[**CryptoLocker**](../xample-malware/vobfus.md)|2013|--|The malware relies on victims to execute. [[4]](#4)|
|[**SearchAwesome**](../xample-malware/searchawesome.md)|2018|--|The user opens a disk image file which invisibly installs its components. [[6]](#6)|

## References

<a name="1">[1]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="2">[2]</a> https://blogs.cisco.com/security/talos/rombertik

<a name="3">[3]</a> https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2013/FireEye-Terminator_RAT.pdf

<a name="4">[4]</a> https://securitynews.sonicwall.com/xmlpost/revisiting-vobfus-worm-mar-8-2013/

<a name="5">[5]</a> https://www.secureworks.com/research/cryptolocker-ransomware

<a name="6">[6]</a> https://www.malwarebytes.com/blog/news/2018/10/mac-malware-intercepts-encrypted-web-traffic-for-ad-injection
