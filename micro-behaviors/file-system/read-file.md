<table>
<tr>
<td><b>ID</b></td>
<td><b>C0051</b></td>
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
<td><b>6 February 2024</b></td>
</tr>
</table>


# Read File

Malware reads a file.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|--|Dark Comet reads files on Windows. [[1]](#1)|
|[**DNSChanger**](../xample-malware/dnschanger.md)|2011|--|DNSChanger reads files on Windows. [[1]](#1)|
|[**Gamut**](../xample-malware/gamut.md)|2014|--|Gamut reads files on Windows. [[1]](#1)|
|[**GravityRAT**](../xample-malware/gravity-rat.md)|2018|--|GravityRAT reads files on Windows. [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Hupigon reads files on Windows. [[1]](#1)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|Kovter reads files on Windows. [[1]](#1)|
|[**Locky Bart**](../xample-malware/locky-bart.md)|2017|--|Locky Bart reads files on Windows. [[1]](#1)|
|[**Mebromi**](../xample-malware/mebromi.md)|2011|--|Mebromi reads files on Windows. [[1]](#1)|
|[**Poison Ivy**](../xample-malware/poison-ivy.md)|2005|--|Poison Ivy reads files on Windows. [[1]](#1)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|--|Redhip reads files on Windows. [[1]](#1)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|--|Rombertik reads files on Windows. [[1]](#1)|
|[**SamSam**](../xample-malware/samsam.md)|2015|--|SamSam reads files on Windows. [[1]](#1)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|--|Shamoon reads files on Windows. [[1]](#1)|
|[**UP007**](../xample-malware/up007.md)|2016|--|UP007 reads files on Windows. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[read file on Windows](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/read/read-file-on-windows.yml)|Read File (C0051)|kernel32.ReadFile, ReadFileEx, NtReadFile, ZwReadFile, LZRead, _read, fread, System.IO.File::ReadAllBytes, System.IO.File::ReadAllBytesAsync, System.IO.File::ReadAllLines, System.IO.File::ReadAllLinesAsync, System.IO.File::ReadAllText, System.IO.File::ReadAllTextAsync, System.IO.File::ReadLines|
|[read file via mapping](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/read/read-file-via-mapping.yml)|Read File (C0051)|kernel32.MapViewOfFile, kernel32.UnmapViewOfFile, kernel32.CreateFileMapping|
|[read file on Linux](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/read/read-file-on-linux.yml)|Read File (C0051)|fgetc, fgets, getc, getchar, read, getline, getdelim, fgetwc, getwc, fscanf, vfscanf, fread|
|[read .ini file](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/read/read-ini-file.yml)|Read File (C0051)|GetPrivateProfileInt, GetPrivateProfileString, GetPrivateProfileStruct, GetPrivateProfileSection, GetPrivateProfileSectionNames, GetFullPathName|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[reads_self](https://github.com/CAPESandbox/community/tree/master/modules/signatures/reads_self.py)|Read File (C0051)|NtReadFile, NtSetInformationFile, NtClose, NtCreateFile, NtOpenFile|
|[accesses_sysvol](https://github.com/CAPESandbox/community/tree/master/modules/signatures/accesses_sysvol.py)|Read File (C0051)|--|
|[antidebug_devices](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antidebug_devices.py)|Read File (C0051)|--|
|[antiav_detectfile](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antiav_detectfile.py)|Read File (C0051)|--|
|[infostealer_browser](https://github.com/CAPESandbox/community/tree/master/modules/signatures/infostealer_browser.py)|Read File (C0051)|NtReadFile, CopyFileA, CopyFileExW, CopyFileW|
|[antianalysis_detectfile](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antianalysis_detectfile.py)|Read File (C0051)|--|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

