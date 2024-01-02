<table>
<tr>
<td><b>ID</b></td>
<td><b>F0005</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../defense-evasion">Defense Evasion</a>, <a href="../persistence">Persistence</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Hide Artifacts: Hidden Files and Directories (<a href="https://attack.mitre.org/techniques/T1564/001/">T1564.001</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.2</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>5 December 2023</b></td>
</tr>
</table>


# Hidden Files and Directories

Malware may hide files and folders to avoid detection and/or to persist on the system. See potential methods below. 

This behavior is related to Unprotect technique U1230.

See ATT&CK: **Hide Artifacts: Hidden Files and Directories ([T1564.001](https://attack.mitre.org/techniques/T1564/001/))**.

## Methods

|Name|ID|Description|
|---|---|---|
|**Attribute**|F0005.003|Malware may change or choose an attribute to hide a file or directory.|
|**Extension**|F0005.001|Malware may change or use a particular file extension to hide a file.|
|**Location**|F0005.002|Malware may change or choose the location of itself, another file, or a directory to prevent detection.|
|**Timestamp**|F0005.004|Malware may change the timestamp on a file to prevent detection.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|--| GoBotKR stores itself in a file with Hidden and System attributes. [[1]](#1)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|F0005.004|Malware modifies target files' time to August 2012 as an antiforensic trick. [[2]](#2)|
|[**CHOPSTICK**](../xample-malware/chopstick.md)|2015|--|CHOPSTICK creates a hidden file for temporary storage. [[3]](#3)|
|[**Vobfus**](../xample-malware/vobfus.md)|2016|F0005.002|Vobfus is located on external drives or network shares and attaches itself to ZIP and RAR files, other removable drives, and network shares. Vobfus hides folders on the external drive and drops an executable with the same name and a disguised folder icon. [[4]](#4)|
|[**Matanbuchus**](../xample-malware/matanbuchus.md)|2021|F0005.002|Malware looks for a specific folder on the victim. If the folder doesn't exist, the malware creates the folder on the victim by calling CreateDirectoryA and downloads the remote file into the new folder. [[5]](#5) [[6]](#6)|
|[**Matanbuchus**](../xample-malware/matanbuchus.md)|2021|F0005.001|The malware also appends the filename and extension .ocx to the ProgramData folder path. [[5]](#5) [[6]](#6)|
|[**WannaCry**](../xample-malware/wannacry.md)|2017|F0005.003|WannaCry uses the +h attribute to hide its files. [[7]](#7)|

## Detection

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[spoofs_procname](https://github.com/CAPESandbox/community/tree/master/modules/signatures/spoofs_procname.py)|Hidden Files and Directories (F0005)|--|
|[spoofs_procname](https://github.com/CAPESandbox/community/tree/master/modules/signatures/spoofs_procname.py)|Hidden Files and Directories::Location (F0005.002)|--|
|[pe_compile_timestomping](https://github.com/CAPESandbox/community/tree/master/modules/signatures/pe_compile_timestomping.py)|Hidden Files and Directories (F0005)|--|
|[pe_compile_timestomping](https://github.com/CAPESandbox/community/tree/master/modules/signatures/pe_compile_timestomping.py)|Hidden Files and Directories::Timestamp (F0005.004)|--|
|[stealth_hidden_extension](https://github.com/CAPESandbox/community/tree/master/modules/signatures/stealth_hidden_extension.py)|Hidden Files and Directories (F0005)|--|
|[stealth_hiddenreg](https://github.com/CAPESandbox/community/tree/master/modules/signatures/stealth_hiddenreg.py)|Hidden Files and Directories (F0005)|--|
|[stealth_file](https://github.com/CAPESandbox/community/tree/master/modules/signatures/stealth_file.py)|Hidden Files and Directories (F0005)|NtSetInformationFile, NtClose, NtCreateFile, NtDuplicateObject, NtOpenFile|

## References

<a name="1">[1]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="2">[2]</a> https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-returns-to-wipe-systems-in-middle-east-europe/

<a name="3">[3]</a> https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf

<a name="4">[4]</a> https://securitynews.sonicwall.com/xmlpost/revisiting-vobfus-worm-mar-8-2013/

<a name="5">[5]</a> https://www.0ffset.net/reverse-engineering/matanbuchus-loader-analysis/

<a name="6">[6]</a> https://www.cyberark.com/resources/threat-research-blog/inside-matanbuchus-a-quirky-loader

<a name="7">[7]</a> https://www.mandiant.com/resources/blog/wannacry-malware-profile