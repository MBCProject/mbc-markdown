<table>
<tr>
<td><b>ID</b></td>
<td><b>C0050</b></td>
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
<td><b>30 April 2024</b></td>
</tr>
</table>


# Set File Attributes

Malware sets file attributes.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**DNSChanger**](../../xample-malware/dnschanger.md)|2011|--|DNSChanger sets file attributes. [[1]](#1)|
|[**Gamut**](../../xample-malware/gamut.md)|2014|--|Gamut sets file attributes. [[1]](#1)|
|[**Hupigon**](../../xample-malware/hupigon.md)|2013|--|Hupigon sets file attributes. [[1]](#1)|
|[**Kovter**](../../xample-malware/kovter.md)|2016|--|Kovter sets file attributes. [[1]](#1)|
|[**Redhip**](../../xample-malware/redhip.md)|2011|--|Redhip sets file attributes. [[1]](#1)|
|[**UP007**](../../xample-malware/up007.md)|2016|--|UP007 sets file attributes. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[change file permission on Linux](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/change-file-permission-on-linux.yml)|Set File Attributes (C0050)|chown, fchown, lchown, fchownat, chmod, fchmod, fchmodat|
|[set file attributes](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/meta/set-file-attributes.yml)|Set File Attributes (C0050)|kernel32.SetFileAttributes, ZwSetInformationFile, NtSetInformationFile, System.IO.File::SetAttributes, System.IO.File::SetCreationTime, System.IO.File::SetCreationTimeUtc, System.IO.File::SetLastAccessTime, System.IO.File::SetLastAccessTimeUtc, System.IO.File::SetLastWriteTime, System.IO.File::SetLastWriteTimeUtc|

### C0050 Snippet
<details>
<summary> File System::Set File Attributes </summary>
SHA256: 27253651170386863b148afb2a0fdda7780ae65cbc31405acbd99fa06b44b79f
Location: 0x140006a6d
<pre>
mov     edx, 0x2        ; pass the value indicating for the 'hidden' attribute to be set on the file
lea     rcx, [rsp + 0x40]       ; name of the file for which attributes should be changed
call    qword ptr [->KERNEL32.DLL::SetFileAttributesA]  ; call Windows API for changing file attributes
</pre>
</details>

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

