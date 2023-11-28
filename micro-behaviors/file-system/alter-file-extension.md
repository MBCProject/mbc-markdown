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
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>14 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>10 November 2022</b></td>
</tr>
</table>


# Alter File Extension

Malware alters a file extension. This could be done for many reasons, including to hide the file or as part of a ransomware's encryption process. 

## Methods

|Name|ID|Description|
|---|---|---|
|**Append Extension**|C0015.001|A new extension is appended.|

## Detection

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[ransomware_extensions](https://github.com/CAPESandbox/community/tree/master/modules/signatures/ransomware_extensions.py)|Alter File Extension (C0015)|--|

|[mimics_extension](https://github.com/CAPESandbox/community/tree/master/modules/signatures/mimics_extension.py)|Alter File Extension (C0015)|--|
