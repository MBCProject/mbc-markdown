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
<td><b>Disk Wipe (<a href="https://attack.mitre.org/techniques/T1561/">T1561</a>)</b></td>
</tr>
<tr>
<td><b>Impact Type</b></td>
<td><b>Availability</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>3.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>15 April 2021</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>21 November 2022</b></td>
</tr>
</table>

# Disk Wipe

Malware may erase the content of storage devices. This behavior is different than **Data Destruction ([E1485](../impact/data-destruction.md))** because sections of the disk are erased rather than individual files.

This description refines the ATT&CK **Disk Wipe ([T1203](https://attack.mitre.org/techniques/T1561/)**) sub-technique.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|--|An overwrite component will overwrite the MBR so that the compromised computer can no longer start. [[1]](#1)|

## References

<a name="1">[1]</a> https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=281521ea-2d18-4bf9-9e88-8b1dc41cfdb6&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments

