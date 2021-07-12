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

For hooking related to memory dump evasion, see [Memory Dump Evasion](../anti-behavioral-analysis/evade-memory-dump.md).

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Procedure Hooking**|F0003.003|Intercepts and executes designated code in response to events such as messages, keystrokes, and mouse inputs. [[1]](#1)|
|**Inline Patching**|F0003.002|Overwrites the first bytes in an API function to redirect code flow.|
|**Export Address Table (EAT) Hooking**|F0003.006|Hooks the export address table (EAT).|
|**Import Address Table (IAT) Hooking**|F0003.001|Modifies a process's import address table (IAT), which stores pointers to imported API functions.|
|**System Service Dispatch Table Hooking**|F0003.004|Hooks the system service dispatch table (SSDT), also called the system service descriptor table. The SSDT contains information about the service tables used by the operating system for dispatching system calls. Hooking the SSDT enables malware to hide files, registry keys, and network connections.|
|**Shadow SDT Hooking**|F0003.005|Hooks the Shadow SSDT similarly to how the SSDT and IAT are hooked. The target of the hooking with the Shadow SSDT is the Windows subsystem (win32k.sys).|

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|**Kronos**|June 2014|Kronos hooks the API of processes to prevent detection. [[2]](#2)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|Trojan spyware program that has mainly been used for targeting banking sites.|

References
----------
<a name="1">[1]</a> https://docs.microsoft.com/en-us/windows/win32/winmsg/about-hooks?redirectedfrom=MSDN#hook-procedures

<a name="2">[2]</a> https://blog.malwarebytes.com/cybercrime/2017/08/inside-kronos-malware/


