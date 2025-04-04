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
<td><b>2.3</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>4 December 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>30 April 2024</b></td>
</tr>
</table>


# Delete File

Malware deletes a file.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Dark Comet**](../../xample-malware/dark-comet.md)|2008|--|Dark Comet deletes files. [[1]](#1)|
|[**Gamut**](../../xample-malware/gamut.md)|2014|--|Gamut deletes files. [[1]](#1)|
|[**GoBotKR**](../../xample-malware/gobotkr.md)|2019|--|GoBotKR deletes files. [[1]](#1)|
|[**GravityRAT**](../../xample-malware/gravity-rat.md)|2018|--|GravityRAT deletes files. [[1]](#1)|
|[**Hupigon**](../../xample-malware/hupigon.md)|2013|--|Hupigon deletes files. [[1]](#1)|
|[**Kovter**](../../xample-malware/kovter.md)|2016|--|Kovter deletes files. [[1]](#1)|
|[**Mebromi**](../../xample-malware/mebromi.md)|2011|--|Mebromi deletes files. [[1]](#1)|
|[**Redhip**](../../xample-malware/redhip.md)|2011|--|Redhip deletes files. [[1]](#1)|
|[**Rombertik**](../../xample-malware/rombertik.md)|2015|--|Rombertik deletes files. [[1]](#1)|
|[**SamSam**](../../xample-malware/samsam.md)|2015|--|SamSam deletes files. [[1]](#1)|
|[**Shamoon**](../../xample-malware/shamoon.md)|2012|--|Shamoon deletes files. [[1]](#1)|
|[**Stuxnet**](../../xample-malware/stuxnet.md)|2010|--|Stuxnet deletes files. [[1]](#1)|
|[**UP007**](../../xample-malware/up007.md)|2016|--|UP007 deletes files. [[1]](#1)|
|[**Snake**](../../xample-malware/snake.md)|2004|--|Snake deletes files. [[2]](#2)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[delete file](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/delete/delete-file.yml)|Delete File (C0047)|kernel32.DeleteFile, DeleteFileTransacted, NtDeleteFile, ZwDeleteFile, remove, _wremove, System.IO.File::Delete, System.IO.FileSystemInfo::Delete, kernel32.SHFileOperation, MoveFileEx|

|Tool: CAPE|Class|Mapping|APIs|
|---|---|---|---|
|[clears_logs](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/clears_logs.py)|ClearsLogs|Delete File (C0047)|--|
|[trickbot_task_delete](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/trickbot_files.py)|TrickBotTaskDelete|Delete File (C0047)|DeleteFileW|
|[upatre_behavior](https://github.com/CAPESandbox/community/blob/master/modules/signatures/deprecated/upatre_apis.py)|Upatre_APIs|Delete File (C0047)|DeleteFileA|
|[ransomware_file_modifications](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/ransomware_filemodifications.py)|RansomwareFileModifications|Delete File (C0047)|MoveFileWithProgressW, MoveFileWithProgressTransactedW, NtCreateFile, NtWriteFile|
|[anomalous_deletefile](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/anomalous_deletefile.py)|anomalous_deletefile|Delete File (C0047)|NtDeleteFile, DeleteFileW, DeleteFileA|
|[deletes_self](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/deletes_self.py)|DeletesSelf|Delete File (C0047)|NtDeleteFile, DeleteFileW, DeleteFileA, MoveFileWithProgressW, MoveFileWithProgressTransactedW|
|[deletes_files](https://github.com/CAPESandbox/community/blob/master/modules/signatures/linux/deletes_files.py)|LinuxDeletesFile|Delete File (C0047)|--|
|[ransomware_recyclebin](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_recyclebin.py)|RansomwareRecyclebin|Delete File (C0047)|--|
|[removes_zoneid_ads](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/removes_zoneid_ads.py)|RemovesZoneIdADS|Delete File (C0047)|DeleteFileW, DeleteFileA|

### C0047 Snippet
<details>
<summary> File System::Delete File </summary>
SHA256: 000b535ab2a4fec86e2d8254f8ed65c6ebd37309ed68692c929f8f93a99233f6
Location: 0x409BB1
<pre>
call    FUN_00404E80    ; generate file name to delete and store in eax
push    eax     ; use the name generated by the previous function as an argument to the next function call
call    KERNEL32.DLL::DeleteFileA       ; delete the file
cmp     eax, 0x1        ; if the file was successfully deleted, the previous function call will return a 1 into eax
sbb     eax, eax        ; isolate the carry flag from the previous comparison.  This will only be 1 if the previous command failed, otherwise it will be 0.
</pre>
</details>

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

<a name="2">[2]</a> https://www.cybereason.com/blog/research/threat-analysis-report-snake-infostealer-malware


