<table>
<tr>
<td><b>ID</b></td>
<td><b>C0045</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../file-system">File System</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.2</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>4 December 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>6 February 2024</b></td>
</tr>
</table>


# Copy File

Malware copies a file.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|--|GoBotKR copies files. [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Hupigon copies files. [[1]](#1)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|Kovter copies files. [[1]](#1)|
|[**Mebromi**](../xample-malware/mebromi.md)|2011|--|Mebromi copies files. [[1]](#1)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|--|Redhip copies files. [[1]](#1)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|--|Shamoon copies files. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[copy file](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/copy/copy-file.yml)|Copy File (C0045)|kernel32.CopyFile, kernel32.CopyFileEx, CopyFile2, CopyFileTransacted, LZCopy, System.IO.FileInfo::CopyTo, System.IO.File::Copy, kernel32.SHFileOperation|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[injection_needextension](https://github.com/CAPESandbox/community/tree/master/modules/signatures/injection_needextension.py)|Copy File (C0045)|NtCreateUserProcess, CreateProcessInternalW|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

