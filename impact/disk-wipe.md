|||
|---|---|
|**ID**|**F0014**|
|**Objective(s)**|[Impact](../impact)|
|**Related ATT&CK Sub-Technique**|[Disk Wipe](https://attack.mitre.org/techniques/T1561/)|

Disk Wipe
=========
Malware may erase the content of storage devices. This behavior is different than [Data Destruction](../impact/data-destruction.md) because sections of the disk are erased rather than individual files.

This description refines the ATT&CK [**Disk Wipe**](https://attack.mitre.org/techniques/T1561/) sub-technique.

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|An overwrite component will overwrite the MBR so that the compromised computer can no longer start  [[1]](#1)|


References
----------
<a name="1">[1]</a> https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=281521ea-2d18-4bf9-9e88-8b1dc41cfdb6&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments
