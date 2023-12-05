<table>
<tr>
<td><b>ID</b></td>
<td><b>C0047</b></td>
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
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>4 December 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>13 September 2023</b></td>
</tr>
</table>


# Delete File

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|--|Dark Comet deletes files. [[1]](#1)|
|[**Gamut**](../xample-malware/gamut.md)|2014|--|Gamut deletes files. [[1]](#1)|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|--|GoBotKR deletes files. [[1]](#1)|
|[**GravityRAT**](../xample-malware/gravity-rat.md)|2018|--|GravityRAT deletes files. [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Hupigon deletes files. [[1]](#1)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|Kovter deletes files. [[1]](#1)|
|[**Mebromi**](../xample-malware/mebromi.md)|2011|--|Mebromi deletes files. [[1]](#1)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|--|Redhip deletes files. [[1]](#1)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|--|Rombertik deletes files. [[1]](#1)|
|[**SamSam**](../xample-malware/samsam.md)|2015|--|SamSam deletes files. [[1]](#1)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|--|Shamoon deletes files. [[1]](#1)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|--|Stuxnet deletes files. [[1]](#1)|
|[**UP007**](../xample-malware/up007.md)|2016|--|UP007 deletes files. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[delete file](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/delete/delete-file.yml)|Delete File (C0047)|kernel32.DeleteFile, DeleteFileTransacted, NtDeleteFile, ZwDeleteFile, remove, _wremove, System.IO.File::Delete, System.IO.FileSystemInfo::Delete, kernel32.SHFileOperation, MoveFileEx|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[clears_logs](https://github.com/CAPESandbox/community/tree/master/modules/signatures/clears_logs.py)|Delete File (C0047)|--|
|[removes_zoneid_ads](https://github.com/CAPESandbox/community/tree/master/modules/signatures/removes_zoneid_ads.py)|Delete File (C0047)|DeleteFileW, DeleteFileA|
|[ransomware_recyclebin](https://github.com/CAPESandbox/community/tree/master/modules/signatures/ransomware_recyclebin.py)|Delete File (C0047)|--|
|[trickbot_task_delete](https://github.com/CAPESandbox/community/tree/master/modules/signatures/trickbot_task_delete.py)|Delete File (C0047)|DeleteFileW|
|[anomalous_deletefile](https://github.com/CAPESandbox/community/tree/master/modules/signatures/anomalous_deletefile.py)|Delete File (C0047)|NtDeleteFile, DeleteFileW, DeleteFileA|
|[deletes_self](https://github.com/CAPESandbox/community/tree/master/modules/signatures/deletes_self.py)|Delete File (C0047)|NtDeleteFile, DeleteFileW, DeleteFileA, MoveFileWithProgressW, MoveFileWithProgressTransactedW|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

