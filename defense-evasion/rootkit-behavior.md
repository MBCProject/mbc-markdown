|||
|---------|------------------------|
|**ID**|**E1014**|
|**Objective(s)**| [Defense Evasion](https://github.com/MAECProject/malware-behaviors/tree/master/defense-evasion)|
|**Related ATT&CK Technique(s)**|[Rootkit](https://attack.mitre.org/techniques/T1014)|


Rootkit Behavior
================
Behaviors of a rootkit: "A rootkit is a collection of computer software, typically malicious, designed to enable access to a computer or areas of its software that is not otherwise allowed and often masks its existence or the existence of other software." [[1]](#1)

See ATT&CK: [**Rootkit**](https://attack.mitre.org/techniques/T1014).

Methods
------- 
* **Hide Kernel Modules**: Hides the usage of any kernel modules by the malware instance.
* **Hide Services**: Hides any system services that the malware instance creates or injects itself into.
* **Hide Threads**: Hides one or more threads that belong to the malware instance. 
* **Hide Userspace Libraries**: Hides the usage of userspace libraries by the malware instance.
* **Prevent API Unhooking**: Prevents the API hooks installed by the malware instance from being removed.
* **Prevent Registry Access**: Prevents access to the Windows registry, including to the entire registry and/or to particular registry keys/values.
* **Prevent Registry Deletion**: Prevent Windows registry keys and/or values associated with the malware instance from being deleted from a system. 
* **Prevent File Access**: Prevents access to the file system, including to specific files and/or directories associated with the malware instance. 
* **Prevent File Deletion**: Prevents files and/or directories associated with the malware instance from being deleted from a system.
* **Prevent Memory Access**: Prevents access to system memory where the malware instance may be storing code or data.
* **Prevent Native API Hooking**: Prevents other software from hooking native system APIs.

References
----------
<a name="1">[1]</a> https://en.wikipedia.org/wiki/Rootkit