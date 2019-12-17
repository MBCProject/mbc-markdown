|||
|---------|------------------------|
|**ID**|**T1165**|
|**Objective(s)**| [Persistence](https://github.com/MBCProject/mbc-markdown/tree/master/persistence), [Privilege Escalation](https://github.com/MBCProject/mbc-markdown/tree/master/privilege-escalation)|
|**Related ATT&CK Technique**|[Startup Items](https://attack.mitre.org/techniques/T1165)|


Startup Items
=============
Malware may add an entry to the macOS StartupItems directory to enable persistence. Because StartupItems run during the bootup phase of macOS, they will run as root, enabling privilege escalation. [[1]](#1)

See ATT&CK: [**Startup Items**](https://attack.mitre.org/techniques/T1165) . 

References
----------
