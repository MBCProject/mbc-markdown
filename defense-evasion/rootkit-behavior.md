|||
|---------|------------------------|
|**ID**|**E1014**|
|**Objective(s)**| [Defense Evasion](https://github.com/MBCProject/mbc-beta/tree/master/defense-evasion)|
|**Related ATT&CK Technique**|[Rootkit](https://attack.mitre.org/techniques/T1014)|


Rootkit
=======
Behaviors of a rootkit: "A rootkit is a collection of computer software, typically malicious, designed to enable access to a computer or areas of its software that is not otherwise allowed and often masks its existence or the existence of other software." [[1]](#1)

See ATT&CK: [**Rootkit**](https://attack.mitre.org/techniques/T1014).

Methods
------- 
|ID|Name|Description|
|-----------------------------|--------|-----------------------------|
|E1014.m01|**Hide Kernel Modules**|Hides the usage of any kernel modules by the malware instance.|
|E1014.m02|**Hide Services**|Hides any system services that the malware instance creates or injects itself into.|
|E1014.m04|**Hide Threads**|Hides one or more threads that belong to the malware instance.|
|E1014.m05|**Hide Userspace Libraries**|Hides the usage of userspace libraries by the malware instance.|
|E1014.m06|**Prevent API Unhooking**|Prevents the API hooks installed by the malware instance from being removed.|
|E1014.m07|**Prevent Registry Access**|Prevents access to the Windows registry, including to the entire registry and/or to particular registry keys/values.|
|E1014.m08|**Prevent Registry Deletion**|Prevent Windows registry keys and/or values associated with the malware instance from being deleted from a system.|
|E1014.m09|**Prevent File Access**|Prevents access to the file system, including to specific files and/or directories associated with the malware instance.|
|E1014.m10|**Prevent File Deletion**|Prevents files and/or directories associated with the malware instance from being deleted from a system.|
|E1014.m11|**Prevent Memory Access**|Prevents access to system memory where the malware instance may be storing code or data.|
|E1014.m12|**Prevent Native API Hooking**|Prevents other software from hooking native system APIs.|

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|
|[**Poison-Ivy**](https://github.com/MBCProject/mbc-beta/tree/master/xample-malware/poison-ivy.md)|2005|After the Poison-Ivy server is running on the target machine, the attacker can use a Windows GUI client to control the target computer. [[2]](#2)|

References
----------
<a name="1">[1]</a> https://en.wikipedia.org/wiki/Rootkit

<a name="2">[2]</a> https://www.cyber.nj.gov/threat-profiles/trojan-variants/poison-ivy
