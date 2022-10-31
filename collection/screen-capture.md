<table>
<tr>
<td><b>ID</b></td>
<td><b>E1113</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../collection">Collection</a>, <a href="../credential-access">Credential Access</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Screen Capture (<a href="https://attack.mitre.org/techniques/T1113/">T1113</a>)</b></td>
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


Screen Capture
=============
Malware takes screen captures of the desktop.

See ATT&CK: **Screen Capture ([T1113](https://attack.mitre.org/techniques/T1113/))**.

Methods
-------
|Name|ID|Description|
|---|---|---|
|**WinAPI**|E1113.m01|Screen is captured using WinAPI functions (e.g., user32.GetDesktopWindow).|


Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**GotBotKR**](../xample-malware/gobotkr.md)|2019| GoBotKR is capable of capturing screenshots. [[1]](#1)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|Screenshot plugin allows for collection of screenshots  [[2]](#2)|
|[**DarkComet**](../xample-malware/dark-comet.md)|2008|Can take screenshots of victim's computer [[3]](#3)|

References
----------
<a name="1">[1]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="2">[2]</a> https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/

<a name="3">[3]</a> https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/
