<table>
<tr>
<td><b>ID</b></td>
<td><b>C0063</b></td>
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
<td><b>30 August 2021</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>6 February 2024</b></td>
</tr>
</table>


# Move File

Malware moves a file.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Gamut**](../xample-malware/gamut.md)|2014|--|Gamut moves files. [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Hupigon moves files. [[1]](#1)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|Kovter moves files. [[1]](#1)|
|[**Mebromi**](../xample-malware/mebromi.md)|2011|--|Mebromi moves files. [[1]](#1)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|--|Shamoon moves files. [[1]](#1)|
|[**UP007**](../xample-malware/up007.md)|2016|--|UP007 moves files. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[move file](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/move/move-file.yml)|Move File (C0063)|kernel32.MoveFile, kernel32.MoveFileEx, MoveFileWithProgress, MoveFileTransacted, rename, _wrename, System.IO.FileInfo::MoveTo, System.IO.File::Move, kernel32.SHFileOperation|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[move_file_on_reboot](https://github.com/CAPESandbox/community/tree/master/modules/signatures/move_file_on_reboot.py)|Move File (C0063)|MoveFileWithProgressTransactedA, MoveFileWithProgressTransactedW|

### C0063 Snippet
<details>
<summary> File System::Move File </summary>
SHA256: bb8c0e477512adab1db26eb77fe10dadbc5dcbf8e94569061c7199ca4626a420
Location: 0x41a61d
<pre>
push    0x4     ; option to delay move until the next reboot
push    edi     ; new name for the moved file
lea     eax, [ebp + 0xffffefc4]
push    eax     ; name of the file to be moved
call    dword ptr [->KERNEL32.DLL::MoveFileExW] ; Windows API function to move the file from one name to another
</pre>
</details>

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

