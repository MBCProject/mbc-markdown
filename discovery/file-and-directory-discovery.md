<table>
<tr>
<td><b>ID</b></td>
<td><b>E1083</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../discovery">Discovery</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>File and Directory Discovery (<a href="https://attack.mitre.org/techniques/T1083/">T1083</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.2</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>2 August 2022</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>5 December 2023</b></td>
</tr>
</table>


# File and Directory Discovery

Malware may enumerate files and directories or may search for specific files or in specific locations.

## Methods

|Name|ID|Description|
|---|---|---|
|**Log File**|E1083.m01|Malware may look for system log files.|
|**Filter by Extension**|E1083.m02|Malware may filter by extension (common in ransomware).|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**CryptoWall**](../xample-malware/cryptowall.md)|2014|--|The malware searches for user files before encrypting them. [[1]](#1)|
|[**CryptoLocker**](../xample-malware/cryptolocker.md)|2013|--|The malware searches for user files before encrypting them. [[2]](#2)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|--|The malware collects machine information and local files with specified file extensions. [[3]](#3)|
|[**Matanbuchus**](../xample-malware/matanbuchus.md)|2021|--|Malware verifies that the folder from the first stage loader exists on the system. The malware also checks for the path for the Opera web browser. If it exists, the malware exits. [[4]](#4) [[5]](#5)|
|[**GravityRAT**](../xample-malware/gravity-rat.md)|2018|--|GravityRAT enumerates files on Windows. [[6]](#6)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Hupigon enumerates files recursively. [[6]](#6)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|E1083.m01|Hupigon accesses the Windows event log. [[6]](#6)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|Kovter gets file version info. [[6]](#6)|
|[**Kovter**](../xample-malware/kovter.md)|2016|E1083.m01|Kovter accesses the Windows event log. [[6]](#6)|
|[**SamSam**](../xample-malware/samsam.md)|2015|--|SamSam enumerates files on Windows. [[6]](#6)|
|[**UP007**](../xample-malware/up007.md)|2016|--|The malware enumerates files on Windows. [[6]](#6)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|--|The malware gets the common file path. [[6]](#6)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|--|The malware gets file version info. [[6]](#6)|
|[**Gamut**](../xample-malware/gamut.md)|2014|--|Gamut gets the common file path. [[6]](#6)|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|--|GoBotKR checks if a file exists. [[6]](#6)|
|[**Locky Bart**](../xample-malware/locky-bart.md)|2017|--|The malware gets a file size. [[6]](#6)|
|[**Mebromi**](../xample-malware/mebromi.md)|2011|--|Mebromi gets a file size. [[6]](#6)|
|[**Redhip**](../xample-malware/redhip.md)|2011|--|Redhip gets a file size. [[6]](#6)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|--|The malware gets the file version info. [[6]](#6)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|--|Shamoon gets a common file path. [[6]](#6)|
|[**ElectroRAT**](../xample-malware/electrorat.md)|2020|--|ElectroRat looks for wallets to steal cryptocurrency. [[7]](#7)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[get common file path](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/get-common-file-path.yml)|File and Directory Discovery (E1083)|kernel32.GetTempPath, kernel32.GetTempFileName, kernel32.GetSystemDirectory, kernel32.GetWindowsDirectory, kernel32.GetSystemWow64Directory, GetAllUsersProfileDirectory, GetAppContainerFolderPath, GetCurrentDirectory, GetDefaultUserProfileDirectory, GetProfilesDirectory, GetUserProfileDirectory, SHGetFolderPathAndSubDir, shell32.SHGetFolderPath, shell32.SHGetFolderLocation, shell32.SHGetKnownFolderPath, shell32.SHGetSpecialFolderPath, shell32.SHGetSpecialFolderLocation, System.IO.Directory::GetCurrentDirectory, System.Environment::GetFolderPath|
|[get file version info](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/meta/get-file-version-info.yml)|File and Directory Discovery (E1083)|version.GetFileVersionInfo, version.GetFileVersionInfoEx, System.Diagnostics.FileVersionInfo::GetVersionInfo, version.VerQueryValue, version.GetFileVersionInfoSize, version.GetFileVersionInfoSizeEx|
|[get file size](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/meta/get-file-size.yml)|File and Directory Discovery (E1083)|kernel32.GetFileSize, kernel32.GetFileSizeEx|
|[check if file exists](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/exists/check-if-file-exists.yml)|File and Directory Discovery (E1083)|kernel32.GetFileAttributes, kernel32.GetLastError, shlwapi.PathFileExists, System.IO.File::Exists|
|[enumerate files on Linux](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/files/list/enumerate-files-on-linux.yml)|File and Directory Discovery (E1083)|getdents, getdents64, opendir, readdir|
|[enumerate files on Windows](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/files/list/enumerate-files-on-windows.yml)|File and Directory Discovery (E1083)|kernel32.FindFirstFile, kernel32.FindFirstFileEx, kernel32.FindFirstFileTransacted, kernel32.FindFirstFileName, kernel32.FindFirstFileNameTransacted, kernel32.FindNextFile, kernel32.FindNextFileName, kernel32.FindClose, ntdll.NtOpenDirectoryObject, ntdll.NtQueryDirectoryObject, RtlAllocateHeap, System.IO.DirectoryInfo::GetFiles, System.IO.DirectoryInfo::EnumerateFiles, System.IO.Directory::GetFiles, System.IO.Directory::EnumerateFiles, System.IO.Directory::EnumerateFileSystemEntries, System.IO.DirectoryInfo::GetDirectories, System.IO.DirectoryInfo::EnumerateDirectories, System.IO.Directory::GetDirectories, System.IO.Directory::EnumerateDirectories|
|[enumerate files recursively](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/files/list/enumerate-files-recursively.yml)|File and Directory Discovery (E1083)|--|
|[read data from CLFS log container](https://github.com/mandiant/capa-rules/blob/master/host-interaction/log/clfs/read-data-from-clfs-log-container.yml)|File and Directory Discovery::Log File (E1083.m01)|clfsw32.CreateLogFile, clfsw32.CreateLogMarshallingArea, clfsw32.ReadLogRecord, clfsw32.ReadNextLogRecord|
|[access the Windows event log](https://github.com/mandiant/capa-rules/blob/master/host-interaction/log/winevt/access/access-the-windows-event-log.yml)|File and Directory Discovery::Log File (E1083.m01)|OpenEventLog, ClearEventLog, OpenBackupEventLog, ReportEvent|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[antisandbox_cuckoo_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_cuckoo_files.py)|File and Directory Discovery (E1083)|--|
|[antisandbox_threattrack_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_threattrack_files.py)|File and Directory Discovery (E1083)|--|
|[antivm_directory_objects](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_directory_objects.py)|File and Directory Discovery (E1083)|NtQueryDirectoryObject, NtOpenDirectoryObject|
|[antivm_vmware_events](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_vmware_events.py)|File and Directory Discovery (E1083)|NtOpenEvent, NtCreateEvent|
|[antivm_vmware_events](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_vmware_events.py)|File and Directory Discovery::Log File (E1083.m01)|NtOpenEvent, NtCreateEvent|
|[antivm_vbox_devices](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_vbox_devices.py)|File and Directory Discovery (E1083)|--|
|[antivm_vmware_devices](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_vmware_devices.py)|File and Directory Discovery (E1083)|--|
|[antivm_vbox_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_vbox_files.py)|File and Directory Discovery (E1083)|--|
|[antivm_vmware_libs](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_vmware_libs.py)|File and Directory Discovery (E1083)|LdrLoadDll|
|[antiav_detectfile](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antiav_detectfile.py)|File and Directory Discovery (E1083)|--|
|[antivm_vpc_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_vpc_files.py)|File and Directory Discovery (E1083)|--|
|[antivm_vbox_libs](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_vbox_libs.py)|File and Directory Discovery (E1083)|LdrLoadDll|
|[driver_filtermanager](https://github.com/CAPESandbox/community/tree/master/modules/signatures/driver_filtermanager.py)|File and Directory Discovery (E1083)|--|
|[antisandbox_joe_anubis_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_joe_anubis_files.py)|File and Directory Discovery (E1083)|--|
|[antivm_vmware_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_vmware_files.py)|File and Directory Discovery (E1083)|--|
|[antisandbox_fortinet_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_fortinet_files.py)|File and Directory Discovery (E1083)|--|
|[antisandbox_sunbelt_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_sunbelt_files.py)|File and Directory Discovery (E1083)|--|
|[antianalysis_detectfile](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antianalysis_detectfile.py)|File and Directory Discovery (E1083)|--|

## References

<a name="1">[1]</a> https://news.sophos.com/en-us/2015/12/17/the-current-state-of-ransomware-cryptowall/

<a name="2">[2]</a> https://www.secureworks.com/research/cryptolocker-ransomware

<a name="3">[3]</a> https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf

<a name="4">[4]</a> https://www.0ffset.net/reverse-engineering/matanbuchus-loader-analysis/

<a name="5">[5]</a> https://www.cyberark.com/resources/threat-research-blog/inside-matanbuchus-a-quirky-loader

<a name="6">[6]</a> capa v4.0, analyzed at MITRE on 10/12/2022

<a name="7">[7]</a> https://www.intezer.com/blog/research/operation-electrorat-attacker-creates-fake-companies-to-drain-your-crypto-wallets/