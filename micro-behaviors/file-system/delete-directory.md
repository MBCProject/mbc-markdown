<table>
<tr>
<td><b>ID</b></td>
<td><b>C0048</b></td>
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
<td><b>2.1</b></td>
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


# Delete Directory

Malware deletes a directory.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Gamut**](../xample-malware/gamut.md)|2014|--|Gamut deletes directories. [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Delete directory (This capa rule had 1 match) [[1]](#1)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|Delete directory (This capa rule had 4 matches) [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[delete directory](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/delete/delete-directory.yml)|Delete Directory (C0048)|RemoveDirectory, RemoveDirectoryTransacted, _rmdir, _wrmdir, System.IO.DirectoryInfo::Delete, System.IO.Directory::Delete|

### C0048 Snippet
<details>
<summary> File System::Delete Directory </summary>
SHA256: 27253651170386863b148afb2a0fdda7780ae65cbc31405acbd99fa06b44b79f
Location: 0x140002204
<pre>
mov     param_1, rdi    ; store name of directory to remove
call    qword ptr [->KERNEL32.DLL::RemoveDirectoryA]   ; call Windows API function to remove directory
</pre>
</details>

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

