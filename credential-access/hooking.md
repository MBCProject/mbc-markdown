|||
|---|---|
|**ID**|**F0003**|
|**Objective(s)**|[Anti-Behavioral Analysis](../anti-behavioral-analysis), [Collection](../collection), [Credential Access](../credential-access), [Defense Evasion](../defense-evasion), [Persistence](../persistence), [Privilege Escalation](../privilege-escalation)|
|**Related ATT&CK Sub-Technique**|[Input Capture: Credential API Hooking](https://attack.mitre.org/techniques/T1056/004/)|


Hooking
=======
Malware alters API behavior or redirects execution to a malicious API version for a variety of purposes. Malware may use hooking to load and execute code within the context of another process, hiding execution and gaining elevated privileges and access to the process's memory. Methods related to anti-behavioral analysis are below. For example, hooking can be used to prevent memory dumps - see also [Memory Dump Evasion](../anti-behavioral-analysis/evade-memory-dump.md).

For discussion related to the Credential Access and Collection objectives, see ATT&CK: [**Input Capture: Credential API Hooking**](https://attack.mitre.org/techniques/T1056/004/). 

Note that in MBC, Hooking is also associated with the [Defense Evasion](../defense-evasion), [Persistence](../persistence), [Privilege Escalation](../privilege-escalation), and [Anti-Behavioral Analysis](../anti-behavioral-analysis) objectives.

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Hook memory mapping APIs**|F0003.002|Prevents memory dumps by preventing mapping of memory into the kernel's virtual address space. [[1]](#1)|
|**Hook procedures**|F0003.003|Intercepts and executes designated code in response to events such as messages, keystrokes, and mouse inputs. [[3]](#3)|
|**Import Address Table (IAT) Hooking**|F0003.004|Uses modifications to a process's IAT where pointers to imported API functions are stored.|
|**Inline Hooking**|F0003.005|Overwrites the first bytes in an API function to redirect code flow.|
|**Patch MmGetPhysicalMemoryRanges**|F0003.001|Patching this function to always return NULL prevents drivers from getting information about the physical address space layout, preventing memory dumps. [[1]](#1)|

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|**Kronos**|June 2014|Kronos hooks the API of processes to prevent detection. [[2]](#2)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|Trojan spyware program that has mainly been used for targeting banking sites.|

References
----------
<a name="1">[1]</a> J. Stuttgen, M. Cohen, Anti-forensic resilient memory acquisition, https://www.dfrws.org/sites/default/files/session-files/paper-anti-forensic_resilient_memory_acquisition.pdf

<a name="2">[2]</a> https://blog.malwarebytes.com/cybercrime/2017/08/inside-kronos-malware/

<a name="3">[3]</a> https://docs.microsoft.com/en-us/windows/win32/winmsg/about-hooks?redirectedfrom=MSDN#hook-procedures
