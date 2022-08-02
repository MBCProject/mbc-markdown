|||
|---|---|
|**ID**|**F0013**|
|**Objective(s)**|[Defense Evasion](../defense-evasion), [Persistence](../persistence)|
|**Related ATT&CK Sub-Technique**|[Pre-OS Boot: Bootkit](https://attack.mitre.org/techniques/T1542/003)|


Bootkit
=======
The boot sectors of a hard drive are modified (e.g., Master Boot Record (MBR)). ATT&CK associates bootkits with the Persistence. See ATT&CK: [**Pre-OS Boot: Bootkit**](https://attack.mitre.org/techniques/T1067/).

The MBC also associates the Bootkit behavior with Defense Evasion because the malware may execute before or external to the system's kernel or hypervisor (e.g., through the BIOS), making it more difficult to detect. (As of 2020, ATT&CK also associates the technique with Persistence.) 

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**Mebromi**](../xample-malware/mebromi.md)|2011|An MBR bootkit and a BIOS bootkit targeting Award BIOS. [[1]](#1)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|Can implement malicious code into firmware, allowing read, write, and/or erasure of the UEFI/BIOS firmware  [[2]](#24)|

References
----------
<a name="1">[1]</a> https://www.webroot.com/blog/2011/09/13/mebromi-the-first-bios-rootkit-in-the-wild/

<a name="2">[2]</a> https://eclypsium.com/wp-content/uploads/2020/12/TrickBot-Now-Offers-TrickBoot-Persist-Brick-Profit.pdf
