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

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[office_postscript](https://github.com/CAPESandbox/community/tree/master/modules/signatures/office_postscript.py)|Create File (C0016)|NtWriteFile|
|[spreading_autoruninf](https://github.com/CAPESandbox/community/tree/master/modules/signatures/spreading_autoruninf.py)|Create File (C0016)|--|
|[arkei_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/arkei_files.py)|Create File (C0016)|--|
|[xpertrat_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/xpertrat_files.py)|Create File (C0016)|--|
|[nemty_note](https://github.com/CAPESandbox/community/tree/master/modules/signatures/nemty_note.py)|Create File (C0016)|NtWriteFile|
|[warzonerat_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/warzonerat_files.py)|Create File (C0016)|--|
|[masslogger_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/masslogger_files.py)|Create File (C0016)|--|
|[ransomware_message](https://github.com/CAPESandbox/community/tree/master/modules/signatures/ransomware_message.py)|Create File (C0016)|NtWriteFile|
|[stack_pivot_file_created](https://github.com/CAPESandbox/community/tree/master/modules/signatures/stack_pivot_file_created.py)|Create File (C0016)|NtCreateFile|
|[neshta_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/neshta_files.py)|Create File (C0016)|NtCreateFile|
|[copies_self](https://github.com/CAPESandbox/community/tree/master/modules/signatures/copies_self.py)|Create File (C0016)|--|
|[office_write_exe](https://github.com/CAPESandbox/community/tree/master/modules/signatures/office_write_exe.py)|Create File (C0016)|NtWriteFile|
|[stealth_file](https://github.com/CAPESandbox/community/tree/master/modules/signatures/stealth_file.py)|Create File (C0016)|NtSetInformationFile, NtClose, NtCreateFile, NtDuplicateObject, NtOpenFile|
|[obliquerat_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/obliquerat_files.py)|Create File (C0016)|--|
|[ransomware_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/ransomware_files.py)|Create File (C0016)|--|
|[ransomware_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/ransomware_files.py)|Create File::Create Ransomware File (C0016.002)|--|
|[dcrat_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/dcrat_files.py)|Create File (C0016)|--|
|[karagany_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/karagany_files.py)|Create File (C0016)|--|
|[rtf_embedded_office_file](https://github.com/CAPESandbox/community/tree/master/modules/signatures/rtf_embedded_office_file.py)|Create File (C0016)|--|
|[rtf_embedded_office_file](https://github.com/CAPESandbox/community/tree/master/modules/signatures/rtf_embedded_office_file.py)|Create File::Create Office Document (C0016.001)|--|
|[qulab_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/qulab_files.py)|Create File (C0016)|--|
|[remcos_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/remcos_files.py)|Create File (C0016)|--|
