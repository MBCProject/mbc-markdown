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


# Set File Attributes

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**DNSChanger**](../xample-malware/dnschanger.md)|2011|--|DNSChanger sets file attributes. [[1]](#1)|
|[**Gamut**](../xample-malware/gamut.md)|2014|--|Gamut sets file attributes. [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Hupigon sets file attributes. [[1]](#1)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|Kovter sets file attributes. [[1]](#1)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|--|Redhip sets file attributes. [[1]](#1)|
|[**UP007**](../xample-malware/up007.md)|2016|--|UP007 sets file attributes. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[change file permission on Linux](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/change-file-permission-on-linux.yml)|Set File Attributes (C0050)|chown, fchown, lchown, fchownat|
|[set file attributes](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/meta/set-file-attributes.yml)|Set File Attributes (C0050)|kernel32.SetFileAttributes, ZwSetInformationFile, NtSetInformationFile, System.IO.File::SetAttributes, System.IO.File::SetCreationTime, System.IO.File::SetCreationTimeUtc, System.IO.File::SetLastAccessTime, System.IO.File::SetLastAccessTimeUtc, System.IO.File::SetLastWriteTime, System.IO.File::SetLastWriteTimeUtc|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

