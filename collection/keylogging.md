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
<td><b>21 November 2022</b></td>
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

|Name|Date|Method|Description|
|---|---|---|---|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|F0002, F0002.002|Please see the Hupigon malware page for details. [[1]](#1)|
|[**UP007**](../xample-malware/up007.md)|2016|--|The malware logs keystrokes to a file  [[2]](#2)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|F0002|Keylogger plugin allows for collection of keystrokes [[3]](#3)|
|[**Poison-Ivy**](../xample-malware/poison-ivy.md)|2005|F0002|Can capture keystrokes  [[5]](#5)|
|[**CHOPSTICK**](../xample-malware/chopstick.md)|2015|F0002|CHOPSTICK collects user keystrokes [[6]](#6)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|F0002, F0002.002|Please see the Dark Comet malware page for details. [[4]](#4)|
|[**Kovter**](../xample-malware/kovter.md)|2016|F0002.002|Log keystrokes via polling (This capa rule had 1 match) [[7]](#7)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|F0002.001, F0002.002|Please see the Redhip malware page for details. [[7]](#7)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|F0002.002|Log keystrokes via polling (This capa rule had 7 matches) [[7]](#7)|
|[**UP007 Malware Family**](../xample-malware/up007.md)|2016|F0002|The malware logs keystrokes to a file  [[2]](#2)|
|[**Ursnif**](../xample-malware/ursnif.md)|2016|F0002.002|Log keystrokes via polling (This capa rule had 1 match) [[7]](#7)|

## References

<a name="1">[1]</a> https://www.f-secure.com/v-descs/backdoor_w32_hupigon.shtml

<a name="2">[2]</a> https://citizenlab.ca/2016/04/between-hong-kong-and-burma/

<a name="3">[3]</a> https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/

<a name="4">[4]</a> https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/

<a name="5">[5]</a> https://www.cyber.nj.gov/threat-center/threat-profiles/trojan-variants/poison-ivy

<a name="6">[6]</a> https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf

<a name="7">[7]</a> capa v4.0, analyzed at MITRE on 10/12/2022

