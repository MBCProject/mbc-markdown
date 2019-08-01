|||
|---------|------------------------|
|**ID**|**T1038**|
|**Objective(s)**|[Defense Evasion](https://github.com/MAECProject/malware-behaviors/tree/master/defense-evasion), [Persistence](https://github.com/MAECProject/malware-behaviors/tree/master/persistence), [Privilege Escalation](https://github.com/MAECProject/malware-behaviors/tree/master/privilege-escalation)|
|**Related ATT&CK Technique(s)**|[DLL Search Order Hijacking](https://attack.mitre.org/techniques/T1038)|

DLL Search Order Hijacking
==========================
Malware may place a malicious DLL with the same name as a legitimate, but ambiguously specified, DLL in a location that Windows searches before the legitimate DLL (called a binary planting attack).

**See ATT&CK Technique:** [**DLL Search Order Hijacking**](https://attack.mitre.org/techniques/T1038).