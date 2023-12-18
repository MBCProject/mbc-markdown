<table>
<tr>
<td><b>ID</b></td>
<td><b>E1510</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../impact">Impact</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Clipboard Data (<a href="https://attack.mitre.org/techniques/T1115/">T1115</a>), Data Manipulation: Transmitted Data Manipulation (<a href="https://attack.mitre.org/techniques/T1641/001/">T1641.001</a>)</b></td>
</tr>
<tr>
<td><b>Impact Type</b></td>
<td><b>Integrity</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.1</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>4 December 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>5 December 2023</b></td>
</tr>
</table>


# Clipboard Modification

ATT&CK defines Clipboard Modification as a Mobile technique (Android platform). MBC extends it to the Windows platform.

After E1510 was defined, T1510 was replaced by T1610.001, and Clipboard Data (<a href="https://attack.mitre.org/techniques/T1115/">T1115</a>) was updated to include content modification.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Clipminer**](../xample-malware/clipminer.md)|2011|--|Clipminer monitors the clipboard for cryptocurrency addresses and replaces them with ones controlled by the adversary. [[1]](#1)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|--|The malware writes clipboard data.  [[2]](#2)|
|[**Emotet**](../xample-malware/emotet.md)|2018|--|Emotet writes clipboard data. [[2]](#2)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Hupigon replaces clipboard data. [[2]](#2)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|--|The malware replaces clipboard data. [[2]](#2)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[write clipboard data](https://github.com/mandiant/capa-rules/blob/master/host-interaction/clipboard/write-clipboard-data.yml)|Clipboard Modification (E1510)|user32.EmptyClipboard, System.Windows.Forms.Clipboard::Clear, user32.SetClipboardData, System.Windows.Forms.Clipboard::SetAudio, System.Windows.Forms.Clipboard::SetData, System.Windows.Forms.Clipboard::SetDataObject, System.Windows.Forms.Clipboard::SetFileDropList, System.Windows.Forms.Clipboard::SetImage, System.Windows.Forms.Clipboard::SetText|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[set_clipboard_data](https://github.com/CAPESandbox/community/tree/master/modules/signatures/set_clipboard_data.py)|Clipboard Modification (E1510)|SetClipboardData|

## References

<a name="1">[1]</a> https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/clipminer-bitcoin-mining-hijacking

<a name="2">[2]</a> capa v4.0, analyzed at MITRE on 10/12/2022

