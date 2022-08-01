|||
|---|---|
|**ID**|**E1564**|
|**Objective(s)**|[Defense Evasion](../defense-evasion), [Persistence](../persistence)|
|**Related ATT&CK Technique**|Hide Artifacts ([T1564](https://attack.mitre.org/techniques/T1564/), [T1628](https://attack.mitre.org/techniques/T1628/))|


Hide Artifacts
==============
Malware may hide artifacts to evade detection and/or to persist on the system. See potential methods related to malware below. 

See ATT&CK: **Hide Artifacts ([T1564](https://attack.mitre.org/techniques/T1564/), [T1628](https://attack.mitre.org/techniques/T1628/))**.

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Hidden Userspace Libraries**|E1564.m01|Hides userspace libraries used by the malware instance. Technique refers to hiding libraries loaded in memory (not disk). For example, a userspace library may be injected into a system process such that memory scanning tools may be prevented from finding them. This technique is different than DLL injection, in which the DLL will continue to show up in process metadata that tracks what is stored in memory. This technique involves clearing that metadata or making it inaccessible to security and inspection tools.|
|**Direct Kernel Object Manipulation**|E1564.m02|Direct Kernel Object Manipulation (DKOM) can be used instead of loading a new driver. It leverages an undocumented function exported by ntdll.dll (NtSystemDebugControl()) that provides debugging functionalities at the kernel level.|
|**Hidden Kernel Modules**|E1564.m05|Hides the use of kernel modules by the malware instance (e.g. rootkit). Techniques include kernel module list unlinking.|
|**Hidden Processes**|E1564.m03|Hides processes used by the adversary or malware instance. This can involve techniques such as process list unlinking.|
|**Hidden Services**|E1564.m04|Hides any system services that the malware instance creates or injects itself into. Services can be hidden by hiding associated registry keys.|

