<table>
<tr>
<td><b>ID</b></td>
<td><b>F0002</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../collection">Collection</a>, <a href="../credential-access">Credential Access</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Input Capture: Keylogging (<a href="https://attack.mitre.org/techniques/T1056/001">T1056.001</a>, <a href="https://attack.mitre.org/techniques/T1417/001/">T1417.001</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>14 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>31 October 2022</b></td>
</tr>
</table>


# Keylogging

Malware captures user keyboard input.

See ATT&CK: **Input Capture: Keylogging ([T1056.001](https://attack.mitre.org/techniques/T1056/001), [T1417.001](https://attack.mitre.org/techniques/T1417/001/))**

## Methods

|Name|ID|Description|
|---|---|---|
|**Application Hook**|F0002.001|Keystrokes are captured with an application hook.|
|**Polling**|F0002.002|Keystrokes are captured via polling (e.g., user32.GetAsyncKeyState, user32.GetKeyState).|


## Use in Malware

|Name|Date|Description|
|---|---|---|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|Certain variants of the malware may have keylogging functionality [[1]](#1)|
|[**UP007**](../xample-malware/up007.md)|2016|The malware logs keystrokes to a file  [[2]](#2)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|Keylogger plugin allows for collection of keystrokes [[3]](#3)|
|[**DarkComet**](../xample-malware/dark-comet.md)|2008|DarkComet can capture keystrokes [[4]](#4)|
|[**Poison-Ivy**](../xample-malware/poison-ivy.md)|2005|Can capture keystrokes  [[5]](#5)|

## References

<a name="1">[1]</a> https://www.f-secure.com/v-descs/backdoor_w32_hupigon.shtml

<a name="2">[2]</a> https://citizenlab.ca/2016/04/between-hong-kong-and-burma/

<a name="3">[3]</a> https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/

<a name="4">[4]</a> https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/

<a name="5">[5]</a> https://www.cyber.nj.gov/threat-center/threat-profiles/trojan-variants/poison-ivy
