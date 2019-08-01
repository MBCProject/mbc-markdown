|||
|------------------|------------------------|
|**ID**|**E1179**|
|**Objective(s)**|[Anti-Behavioral Analysis](https://github.com/MAECProject/malware-behaviors/tree/master/anti-behavioral-analysis), [Credential Access](https://github.com/MAECProject/malware-behaviors/tree/master/credential-access), [Defense Evasion](https://github.com/MAECProject/malware-behaviors/tree/master/defense-evasion), [Persistence](https://github.com/MAECProject/malware-behaviors/tree/master/persistence), [Privilege Escalation](https://github.com/MAECProject/malware-behaviors/tree/master/privilege-escalation)|
|**Related ATT&CK Technique**|[Hooking](https://attack.mitre.org/techniques/T1179/)|


Hooking
=======
Malware alters API behavior or redirects execution to a malicious API version for a variety of purposes. Malware may use hooking to load and execute code within the context of another process, hiding execution and gaining elevated privileges and access to the process's memory. Methods related to anti-behavioral analysis are below. For example, hooking can be used to prevent memory dumps - see also [Memory Dump Obstruction](https://github.com/MAECProject/malware-behaviors/blob/master/anti-behavioral-analysis/memory-dump-obstruct.md).

For discussion related to the Credential Access, Persistence, and Privilege Escalation objectives, see ATT&CK: [**Hooking**](https://attack.mitre.org/techniques/T1179/). 

Note that in MBC, but not in ATT&CK, Hooking is also associated with the [Defense Evasion](https://github.com/MAECProject/malware-behaviors/tree/master/defense-evasion) and [Anti-Behavioral Analysis](https://github.com/MAECProject/malware-behaviors/tree/master/anti-behavioral-analysis) objectives.

Methods
-------
* **Patch MmGetPhysicalMemoryRanges**: Patching this function to always return NULL prevents drivers from getting information about the physical address space layout, preventing memory dumps. [[1]](#1)
* **Hook memory mapping APIs**: Prevents memory dumps by preventing mapping of memory into the kernel's virtual address space. [[1]](#1)

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|-----------|-----------------------------|
|**Kronos** | June 2014 | Kronos hooks the API of processes to prevent detection. [[2]](#2)| 

References
----------
<a name="1">[1]</a> J. Stuttgen, M. Cohen, Anti-forensic resilient memory acquisition, www.dfrws.org/sites/default/files/session-files/paper-anti-forensic_resilient_memory_acquisition.pdf

<a name="2">[2]</a> https://blog.malwarebytes.com/cybercrime/2017/08/inside-kronos-malware/ 


 