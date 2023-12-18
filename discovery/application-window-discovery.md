<table>
<tr>
<td><b>ID</b></td>
<td><b>E1010</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../discovery">Discovery</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Application Window Discovery (<a href="https://attack.mitre.org/techniques/T1010/">T1010</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>4 December 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>18 December 2023</b></td>
</tr>
</table>


# Application Window Discovery

Malware may attempt to gain information about the operating system and applications running on a system by enumerating open application windows.

## Methods

|Name|ID|Description|
|---|---|---|
|**Window Text**|E1010.m01|After finding an open application window, malware gets graphical window text.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|E1010.m01|DarkComet gets graphical window texts. [[1]](#1)|
|[**Gamut**](../xample-malware/gamut.md)|2014|E1010.m01|Gamut gets graphical window texts. [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|E1010.m01|Hupigon gets graphical window texts. [[1]](#1)|
|[**Kovter**](../xample-malware/kovter.md)|2016|E1010.m01|Kovter gets graphical window texts. [[1]](#1)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|E1010.m01|Rombertik gets graphical window texts. [[1]](#1)|
|[**UP007**](../xample-malware/up007.md)|2016|E1010.m01|UP007 gets graphical window text. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[get graphical window text](https://github.com/mandiant/capa-rules/blob/master/host-interaction/gui/window/get-text/get-graphical-window-text.yml)|Application Window Discovery (E1010)|user32.IsWindowVisible, user32.SendMessage, user32.GetForegroundWindow, user32.GetWindowText|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[browser_needed](https://github.com/CAPESandbox/community/tree/master/modules/signatures/browser_needed.py)|Application Window Discovery (E1010)|FindWindowW, FindWindowExA, FindWindowExW, FindWindowA|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

