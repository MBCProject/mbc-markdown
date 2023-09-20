<table>
<tr>
<td><b>ID</b></td>
<td><b>C0016</b></td>
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
<td><b>14 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>13 September 2023</b></td>
</tr>
</table>


# Create File

Malware creates a file. 

## Methods

|Name|ID|Description|
|---|---|---|
|**Create Office Document**|C0016.001|An Office document is created.|
|**Create Ransomware File**|C0016.002|Create a file used by ransomware.|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[create or open file](https://github.com/mandiant/capa-rules/blob/master/lib/create-or-open-file.yml)|Create File (C0016)|CreateFile, CreateFileEx, IoCreateFile, IoCreateFileEx, ZwOpenFile, ZwCreateFile, NtOpenFile, NtCreateFile, LZCreateFile, LZOpenFile, fopen, fopen64, fdopen, freopen, open, openat|
