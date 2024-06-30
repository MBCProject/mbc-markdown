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

|Tool: CAPE|Class|Mapping|APIs|
|---|---|---|---|
|[spreading_autoruninf](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/spreading_autoruninf.py)|CreatesAutorunInf|Create File (C0016)|--|
|[ransomware_message](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_message.py)|RansomwareMessage|Create File (C0016)|NtWriteFile|
|[copies_self](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/copies_self.py)|CopiesSelf|Create File (C0016)|--|
|[office_write_exe](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/office_write_exe.py)|OfficeWriteEXE|Create File (C0016)|NtWriteFile|
|[stealth_file](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/stealth_file.py)|StealthFile|Create File (C0016)|NtSetInformationFile, NtClose, NtCreateFile, NtDuplicateObject, NtOpenFile|
|[ransomware_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_files.py)|RansomwareFiles|Create File (C0016), Create File::Create Ransomware File (C0016.002)|--|
|[copies_self](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/copies_self.py)|CopiesSelf|Create File (C0016)|--|
|[rat_pcclient](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/rat_pcclient.py)|PcClientMutexes|Create File (C0016)|--|
|[ransomware_radamant](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/ransomware_radamant.py)|RansomwareRadamant|Create File (C0016)|--|
|[remcos](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/remcos.py)|RemcosFiles|Create File (C0016)|--|
|[rat_karagany](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/rat_karagany.py)|KaraganyFiles|Create File (C0016)|--|
|[rat_oblique](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/rat_oblique.py)|ObliquekRATFiles|Create File (C0016)|--|
|[ransomware_message](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/ransomware_message.py)|RansomwareMessage|Create File (C0016)|NtWriteFile|
|[rat_luminosity](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/rat_luminosity.py)|LuminosityRAT|Create File (C0016)|NtCreateFile, CryptHashData|
|[rat_xpert](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/rat_xpert.py)|XpertRATFiles|Create File (C0016)|--|
|[ransomware_nemty](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/ransomware_nemty.py)|NemtyNote|Create File (C0016)|NtWriteFile|
|[office_write_exe](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/office_write_exe.py)|OfficeWriteEXE|Create File (C0016)|NtWriteFile|
|[rat_warzone](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/rat_warzone.py)|WarzoneRATFiles|Create File (C0016)|--|
|[spreading_autoruninf](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/spreading_autoruninf.py)|CreatesAutorunInf|Create File (C0016)|--|
|[virus_neshta](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/virus_neshta.py)|NeshtaFiles|Create File (C0016)|NtCreateFile|
|[infostealer_arkei](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/infostealer_arkei.py)|ArkeiFiles|Create File (C0016)|--|
|[office_exploit](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/office_exploit.py)|OfficePostScript|Create File (C0016)|NtWriteFile|
|[rat_nanocore](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/rat_nanocore.py)|NanocoreRAT|Create File (C0016)|CryptHashData|
|[infostealer_qulab](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/infostealer_qulab.py)|QulabFiles|Create File (C0016)|--|
|[ransomware_files](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/ransomware_files.py)|RansomwareFiles|Create File (C0016), Create File::Create Ransomware File (C0016.002)|--|
|[rat_dcrat](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/rat_dcrat.py)|DCRatFiles|Create File (C0016)|--|
|[office_rtf](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/office_rtf.py)|RTFEmbeddedOfficeFile|Create File (C0016), Create File::Create Office Document (C0016.001)|--|
|[stack_pivot](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/stack_pivot.py)|StackPivotFileCreated|Create File (C0016)|NtCreateFile|
|[infostealer_masslogger](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/infostealer_masslogger.py)|MassLoggerFiles|Create File (C0016)|--|
|[stealth_file](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/stealth_file.py)|StealthFile|Create File (C0016)|NtCreateFile, NtDuplicateObject, NtOpenFile, NtClose, NtSetInformationFile|