|||
|---|---|
|**ID**|**F0011**|
|**Objective(s)**|[Persistence](https://github.com/MBCProject/mbc-markdown/tree/master/persistence), [Privilege Escalation](https://github.com/MBCProject/mbc-markdown/tree/master/privilege-escalation)|
|**Related ATT&CK Sub-Technique**|[Create or Modify System Process: Windows Service](https://attack.mitre.org/techniques/T1543/003/)|


Modify Existing Service
=======================
Malware may modify an existing service to gain persistence. Modification may include disabling a service.

See ATT&CK: [**Create or Modify System Process: Windows Service**](https://attack.mitre.org/techniques/T1543/003/).

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**Poison-Ivy**](https://github.com/MBCProject/mbc-markdown/tree/master/xample-malware/poison-ivy.md)|2005|After the Poison-Ivy server is running on the target machine, the attacker can use a Windows GUI client to control the target computer. [[1]](#1)|

References
----------
<a name="1">[1]</a> https://www.cyber.nj.gov/threat-profiles/trojan-variants/poison-ivy
