<table>
<tr>
<td><b>ID</b></td>
<td><b>C0049</b></td>
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


# Get File Attributes

Malware gets file attributes.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|--|Dark Comet gets file attributes. [[1]](#1)|
|[**DNSChanger**](../xample-malware/dnschanger.md)|2011|--|DNSChanger gets file attributes. [[1]](#1)|
|[**Gamut**](../xample-malware/gamut.md)|2014|--|Gamut gets file attributes. [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Hupigon gets file attributes. [[1]](#1)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|--|Redhip gets file attributes. [[1]](#1)|
|[**UP007**](../xample-malware/up007.md)|2016|--|UP007 gets file attributes. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[get file attributes](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/meta/get-file-attributes.yml)|Get File Attributes (C0049)|kernel32.GetFileAttributes, ZwQueryDirectoryFile, ZwQueryInformationFile, NtQueryDirectoryFile, NtQueryInformationFile, System.IO.File::GetAttributes, System.IO.File::GetCreationTime, System.IO.File::GetCreationTimeUtc, System.IO.File::GetLastAccessTime, System.IO.File::GetLastAccessTimeUtc, System.IO.File::GetLastWriteTime, System.IO.File::GetLastWriteTimeUtc|

### C0049 Snippet
<details>
<summary> File System::Get File Attributes </summary>
SHA256: 465d3aac3ca4daa9ad4de04fcb999f358396efd7abceed9701c9c28c23c126db
Location: 0x4094B0
<pre>
push    ebx     ; Name of file to get attributes for
mov     ebx, param_1
mov     param_1, ebx
call    FUN_00404DFC
push    param_1 ; Return value for function call
call    KERNEL32.DLL::GetFileAttributesA        ; Call Windows API for file deletion
cmp     param_1, -0x1   ; Test if the return value indicates an error
jz      LAB_004094C9    ; If the function returned an error, go to this address to continue execution
test    param_1, 0x10   ; Test to see if the file queried is a directory
jnz     LAB_004094CD    ; If the file is not a directory, continue execution from this address
</pre>
</details>

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

