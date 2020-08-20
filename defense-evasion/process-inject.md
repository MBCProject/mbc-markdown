|||
|---|---|
|**ID**|**E1055**|
|**Objective(s)**|[Defense Evasion](https://github.com/MBCProject/mbc-markdown/tree/master/defense-evasion), [Privilege Escalation](https://github.com/MBCProject/mbc-markdown/tree/master/privilege-escalation)|
|**Related ATT&CK Technique**|[Process Injection](https://attack.mitre.org/techniques/T1055)|


Process Injection
=================
Malware may execute code in the address space of a separate process. 

See ATT&CK: [**Process Injection**](https://attack.mitre.org/techniques/T1055). Notes on sub-techniques in the context of [[1]](#1) are in as follows:

|ID|ATT&CK Sub-Technique|Notes|
|---|---|---|
|T1055.001|Dynamic-link Library Injection|Malware creates a thread using CreateRemoteThread (or NtCreateThreadEx, RtlCreateUserThread) and LoadLibrary. The path to the malware's malicious dynamic-link library (DLL) is written in the virtual address space of another process; the malware ensures the remote process loads it by creating a remote thread in the target process. This is one of the most common process injection methods. Called *Classic DLL Injection via CreateRemoteThread and LoadLibrary* in [[1]](#1).|
|T1055.002|Portable Executable Injection|Malware copies its malicious code into an existing open process and causes it to execute via shellcode or by calling CreateRemoteThread (instead of passing the address of the LoadLibrary). Called *Portable Executable Injection* in [[1]](#1).|
|T1055.003|Thread Execution Hijacking|Malware targets an existing thread of a process, avoiding noisy process or thread creations operations. Called *Thread Execution Hijacking* in [[1]](#1).|
|T1055.004|Asynchronous Procedure Call|Malware may leverage Asynchronous Procedure Calls (APC) to force another thread to execute its code by attaching it to the APC Queue of the target thread (using QueueUserAPC / NtQueueApcThread); also called AtomBombing [[3]](#3). Called *APC Injection and AtomBombing* in [[1]](#1).|
|T1055.011|Extra Window Memory Injection|Malware may inject into Explorer tray window’s extra window memory. Called *Extra Window Memory Injection* in [[1]](#1).|
|T1055.012|Process Hollowing|Instead of injecting code into a program, malware can upmap (hollow out) legitimate code from memory of a target process, overwriting it with a malicious executable. Called *Process Hollowing* in [[1]](#1).|

Methods not captured by ATT&CK Process Injection sub-techniques are listed below. Note that IAT hooking and inline hooking (aka userland rootkits) are defined as methods under the [Hooking](https://github.com/MBCProject/mbc-markdown/blob/master/credential-access/hooking.md) behavior.

Methods
------- 
|ID|Name|Description|
|---|---|---|
|E1055.m01|**Hook Injection via SetWindowsHooksEx**|Malware can leverage hooking functionality to have its malicious DLL loaded upon an event getting triggered in a specific thread, which is usually done by calling SetWindowsHookEx to install a hook routine into the hook chain. [[1]](#1)|
|E1055.m02|**Injection and Persistence via Registry Modification**|Malware may insert the location of its malicious library under a registry key (e.g., Appinit_DLL, AppCertDlls, IFEO) to have another process load its library. [[1]](#1)|
|E1055.m03|**Injection using Shims**|Malware may use shims to target an executable (shims are a way of hooking into APIs and targeting specific executables and are provided by Microsoft for backward compatibility, allowing developers to apply program fixes without rewriting code). [[1]](#1)|

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**UP007**](https://github.com/MBCProject/mbc-markdown/tree/master/xample-malware/up007.md)|April 2016|Injects secondary payload into memory. [[4]](#4)|
|[**TrickBot**](https://github.com/MBCProject/mbc-markdown/tree/master/xample-malware/trickbot.md)|2016|Trojan spyware program that has mainly been used for targeting banking sites.|
|[**Poison-Ivy**](https://github.com/MBCProject/mbc-markdown/tree/master/xample-malware/poison-ivy.md)|2005|After the Poison-Ivy server is running on the target machine, the attacker can use a Windows GUI client to control the target computer. [[2]](#2)|
|[**WebCobra**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/webcobra.md)|2018|Injects minor code into a running process.|

References
----------
<a name="1">[1]</a> Ashkan Hosseini, *Ten Process Injection Techniques: A Technical Survey of Common and Trending Process Injection Techniques*, July 2017. https://www.elastic.co/blog/ten-process-injection-techniques-technical-survey-common-and-trending-process

<a name="2">[2]</a> https://www.cyber.nj.gov/threat-profiles/trojan-variants/poison-ivy

<a name="3">[3]</a> https://github.com/LordNoteworthy/al-khaser

<a name="4">[4]</a> https://citizenlab.ca/2016/04/between-hong-kong-and-burma/
