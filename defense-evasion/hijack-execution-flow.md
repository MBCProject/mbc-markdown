|||
|---|---|
|**ID**|**F0015**|
|**Objective(s)**|[Defense Evasion](../defense-evasion), [Persistence](../persistence), [Privilege Escalation](../privilege-escalation)|
|**Related ATT&CK Technique**|[Hijack Execution Flow](https://attack.mitre.org/techniques/T1574/)|


Hijack Execution Flow
=====================
Malware may execute by hijacking the way operating systems run programs. Malware (e.g. rootkit) alters API behavior or redirects execution to a malicious API version for a variety of purposes. Malware may use hooking to load and execute code within the context of another process, hiding execution and gaining elevated privileges and access to the process's memory. Different types of hooking are defined as methods below.

See ATT&CK: [**Hijack Execution Flow**](https://attack.mitre.org/techniques/T1574/).

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Abuse Windows Function Calls**|F0015.006|Malware abuses native Windows function calls to transfer execution to shellcode that it loads into memory. A pointer to the callback function is used to supply the memory address of the shellcode. Functions that can be abused include EnumResourceTypesA and EnumUILanguagesW. [[4]](#4)|
|**Export Address Table (EAT) Hooking**|F0015.001|Malware (e.g. rootkit) hooks the export address table (EAT).|
|**Import Address Table (IAT) Hooking**|F0015.003|Malware (e.g. rootkit) modifies a process's import address table (IAT), which stores pointers to imported API functions.[[1]](#1)|
|**Inline Patching**|F0015.002|Inline patching (inline hooking) is done by modifying the beginning of a function in order to redirect the execution flow to custom code (i.e. redirecting code flow) before jumping back to the original function.[[2]](#2)|
|**Shadow System Service Dispatch Table Hooking**|F0015.004|The Shadow System Service Dispatch Table (SSDT) can be hooked similarly to how the SSDT and IAT are hooked. The target of the hooking with the Shadow SSDT is the Windows subsystem (win32k.sys).[[3]](#3)|
|**System Service Dispatch Table Hooking**|F0015.005|Malware (e.g. rootkit, malicious drivers) may hook the system service dispatch table (SSDT), also called the system service descriptor table. The SSDT contains information about the service tables used by the operating system for dispatching system calls. Hooking the SSDT enables malware to hide files, registry keys, and network connections.[[3]](#3)|

References
----------
<a name="1">[1]</a> https://www.sans.org/media/score/checklists/rootkits-investigation-procedures.pdf

<a name="2">[2]</a> https://www.oreilly.com/library/view/learning-malware-analysis/9781788392501/a0a506d6-d062-48c1-a0a8-57d6acb77785.xhtml

<a name="3">[3]</a> https://www.mdpi.com/1999-5903/4/4/971/html

<a name="4">[4]</a> http://ropgadget.com/posts/abusing_win_functions.html

