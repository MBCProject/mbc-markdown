<table>
<tr>
<td><b>ID</b></td>
<td><b>F0014</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../impact">Impact</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Disk Wipe (<a href="https://attack.mitre.org/techniques/T1561/001">T1561.001</a>)</b></td>
</tr>
<tr>
<td><b>Impact Type</b></td>
<td><b>Availability</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>3.2</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>15 April 2021</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>30 April 2024</b></td>
</tr>
</table>

# Disk Wipe

Malware may erase the content of storage devices. This behavior is different than **Data Destruction ([E1485](../impact/data-destruction.md))** because sections of the disk are erased rather than individual files.

This description refines the ATT&CK **Disk Wipe: Disk Content Wipe ([T1561.001](https://attack.mitre.org/techniques/T1561/001/)**) sub-technique.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|--|An overwrite component will overwrite the MBR so that the compromised computer can no longer start. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[overwrite Master Boot Record (MBR)](https://github.com/mandiant/capa-rules/blob/master/impact/wipe-disk/wipe-mbr/overwrite-master-boot-record-mbr.yml)|Disk Wipe (F0014)|kernel32.WriteFile|
|[delete drive layout via IOCTL](https://github.com/mandiant/capa-rules/blob/v7.1.0/impact/wipe-disk/delete-drive-layout-via-ioctl.yml)|Disk Wipe (F0014)|--|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[deletes_shadow_copies](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/deletes_shadowcopies.py)|Disk Wipe (F0014)|ShellExecuteExW, NtCreateUserProcess, CreateProcessInternalW|
|[deletes_system_state_backup](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/deletes_system_backup.py)|Disk Wipe (F0014)|ShellExecuteExW, NtCreateUserProcess, CreateProcessInternalW|
|[wiper_zeroedbytes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/wiper.py)|Disk Wipe (F0014)|NtWriteFile|

## References

<a name="1">[1]</a> https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=281521ea-2d18-4bf9-9e88-8b1dc41cfdb6&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments

