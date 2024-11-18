<table>
<tr>
<td><b>ID</b></td>
<td><b>C0015</b></td>
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
<td><b>14 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>5 December 2023</b></td>
</tr>
</table>


# Alter File Extension

Malware alters a file extension. This could be done for many reasons, including to hide the file or as part of a ransomware's encryption process. 

## Methods

|Name|ID|Description|
|---|---|---|
|**Append Extension**|C0015.001|A new extension is appended.|

## Detection

|Tool: CAPE|Class|Mapping|APIs|
|---|---|---|---|
|[mimics_extension](https://github.com/CAPESandbox/community/blob/master/modules/signatures/all/mimics_filename.py)|MimicsExtension|Alter File Extension (C0015)|--|
|[ransomware_file_modifications](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/ransomware_filemodifications.py)|RansomwareFileModifications|Alter File Extension (C0015)|MoveFileWithProgressW, MoveFileWithProgressTransactedW, NtCreateFile, NtWriteFile|
|[ransomware_extensions](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/ransomware_fileextensions.py)|RansomwareExtensions|Alter File Extension (C0015)|--|
