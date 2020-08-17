|||
|---------|------------------------|
|**ID**|**F0013**|
|**Objective(s)**|[Defense Evasion](https://github.com/MBCProject/mbc-markdown/tree/master/defense-evasion), [Persistence](https://github.com/MBCProject/mbc-markdown/tree/master/persistence)|
|**Related ATT&CK Sub-Technique**|[Pre-OS Boot: Bootkit](https://attack.mitre.org/techniques/T1542/003)|

Bootkit
=======
The boot sectors of a hard drive are modified (e.g., Master Boot Record (MBR)). ATT&CK associates bootkits with the Persistence. See ATT&CK: [**Pre-OS Boot: Bootkit**](https://attack.mitre.org/techniques/T1067/).

The MBC also associates the Bootkit behavior with Defense Evasion because the malware may execute before or external to the system's kernel or hypervisor (e.g., through the BIOS), making it more difficult to detect. (As of 2020, ATT&CK also associates the technique with Persistence.) 

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|-----------|-----------------------------|
|[**Mebromi**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/mebromi.md)|2011|An MBR bootkit and a BIOS bootkit targeting Award BIOS. [[1]](#1)|

References
----------
<a name="1">[1]</a> https://www.webroot.com/blog/2011/09/13/mebromi-the-first-bios-rootkit-in-the-wild/
 