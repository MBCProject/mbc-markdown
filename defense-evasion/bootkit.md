<table>
<tr>
<td><b>ID</b></td>
<td><b>F0013</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../defense-evasion">Defense Evasion</a>, <a href="../persistence">Persistence</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Pre-OS Boot: Bootkit (<a href="https://attack.mitre.org/techniques/T1542/003">T1542.003</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.1</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>28 April 2024</b></td>
</tr>
</table>


# Bootkit

The boot sectors of a hard drive are modified (e.g., Master Boot Record (MBR)). ATT&CK associates bootkits with the Persistence. See ATT&CK: **Pre-OS Boot: Bootkit ([T1542.003](https://attack.mitre.org/techniques/T1542/003/))**.

The MBC also associates the Bootkit behavior with Defense Evasion because the malware may execute before or external to the system's kernel or hypervisor (e.g., through the BIOS), making it more difficult to detect. (As of 2020, ATT&CK also associates the technique with Persistence.) 

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Mebromi**](../xample-malware/mebromi.md)|2011|--|The malware is an MBR bootkit and a BIOS bootkit targeting Award BIOS. [[1]](#1)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|--|The malware can implement malicious code into firmware, allowing read, write, and/or erasure of the UEFI/BIOS firmware. [[2]](#24)|

## Detection

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[accesses_primary_patition](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/accesses_primary_patition.py)|Bootkit (F0013)|--|
|[bootkit](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/bootkit.py)|Bootkit (F0013)|NtSetInformationFile, NtClose, DeviceIoControl, NtCreateFile, NtDuplicateObject, NtOpenFile, NtWriteFile, NtDeviceIoControlFile|
|[direct_hdd_access](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/direct_hdd_access.py)|Bootkit (F0013)|--|
|[enumerates_physical_drives](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/enumerates_physical_drives.py)|Bootkit (F0013)|--|
|[physical_drive_access](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/physical_drive_access.py)|Bootkit (F0013)|--|
|[suspicious_ioctl_scsipassthough](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/suspicious_ioctl_scsipassthough.py)|Bootkit (F0013)|DeviceIoControl, NtDeviceIoControlFile|

## References

<a name="1">[1]</a> https://www.webroot.com/blog/2011/09/13/mebromi-the-first-bios-rootkit-in-the-wild/

<a name="2">[2]</a> https://eclypsium.com/wp-content/uploads/TrickBot-Now-Offers-TrickBoot-Persist-Brick-Profit.pdf

