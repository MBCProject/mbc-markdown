|||
|---------|------------------------|
|**ID**|**M0028**|
|**Objective(s)**|[Defense Evasion](https://github.com/MAECProject/malware-behaviors/tree/master/defense-evasion), [Persistence](https://github.com/MAECProject/malware-behaviors/tree/master/persistence)|
|**Related ATT&CK Technique(s)**|[Bootkit](https://attack.mitre.org/techniques/T1067/)|

Boot Sector Modification
========================
The boot sectors of a hard drive are modified (e.g., Master Boot Record (MBR)). ATT&CK associates bootkits with the Persistence. See ATT&CK: [**Bootkit**](https://attack.mitre.org/techniques/T1067/).

The MBC also associates the Bootkit behavior with Defense Evasion because the malware may execute before or external to the system's kernel or hypervisor (e.g., through the BIOS), making it more difficult to detect. 

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|-----------|-----------------------------|
|Mebromi|2011|An MBR bootkit and a BIOS bootkit targeting Award BIOS. [[1]](#1)|

References
----------
<a name="1">[1]</a> https://www.webroot.com/blog/2011/09/13/mebromi-the-first-bios-rootkit-in-the-wild/
 