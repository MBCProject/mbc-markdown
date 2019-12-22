|||
|---------|------------------------|
|**ID**|**E1055**|
|**Objective(s)**| [Defense Evasion](https://github.com/MBCProject/mbc-markdown/tree/master/defense-evasion), [Privilege Escalation](https://github.com/MBCProject/mbc-markdown/tree/master/privilege-escalation)|
|**Related ATT&CK Technique**|[Process Injection](https://attack.mitre.org/techniques/T1055)|


Process Injection
=================
Malware may execute code in the address space of a separate process. 

See ATT&CK: [**Process Injection**](https://attack.mitre.org/techniques/T1055).

Methods
------- 
* **Shell_TrayWnd**: Injects code using the Shell_TRyaWnd technique.
* **CreateRemoteThread**: Malware creates a thread using CreateRemoteThread (or NtCreateThreadEx, RtlCreateUserThread) and LoadLibrary. The path to the malware's malicious dynamic-link library (DLL) is written in the virtual address space of another process; the malware ensures the remote process loads it by creating a remote thread in the target process. This is one of the most common process injection methods. [[4]](#4)
* **PE Injection**: Malware copies its malicious code into an existing open process and causes it to execute via shellcode or by calling CreateRemoteThread (instead of passing the address of the LoadLibrary) [[4]](#4)
* **Thread Execution Hijacking**: Malware targets an existing thread of a process, avoiding noisy process or thread creations operations. [[4]](#4)
* **SetWindowsHooksEx**: Malware can leverage hooking functionality to have its malicious DLL loaded upon an event getting triggered in a specific thread, which is usually done by calling SetWindowsHookEx to install a hook routine into the hook chain. [[4]](#4)
* **APC Injection**: Malware may leverage Asynchronous Procedure Calls (APC) to force another thread to execute its code by attaching it to the APC Queue of the target thread (using QueueUserAPC / NtQueueApcThread); also called AtomBombing [[3]](#3), [[4]](#4).
* **RunPE**: GetThreadContext / SetThreadContext [[3]](#3).
* **Registry Modification**: Malware may insert the location of its malicious library under a registry key (e.g., Appinit_DLL, AppCertDlls, IFEO) to have another process load its library. [[4]](#4)
* **Extra Window Memory Injection (EWMI)**: Malware may inject into Explorer tray window’s extra window memory [[4]](#4).
* **Shims**: Malware may use shims to target an executable (shims are a way of hooking into APIs and targeting specific executables and are provided by Microsoft for backward compatibility, allowing developers to apply program fixes without rewriting code) [[4]](#4). 


Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|
|[**UP007**](https://github.com/MBCProject/mbc-markdown/tree/master/xample-malware/up007.md)|April 2016|The UP007 malware family... [[1]](#1)|
|[**TrickBot**](https://github.com/MBCProject/mbc-markdown/tree/master/xample-malware/trickbot.md)|2016|Trojan spyware program that has mainly been used for targeting banking sites.|
|[**Poison-Ivy**](https://github.com/MBCProject/mbc-markdown/tree/master/xample-malware/poison-ivy.md)|2005|After the Poison-Ivy server is running on the target machine, the attacker can use a Windows GUI client to control the target computer. [[2]](#2)|

References
----------
<a name="1">[1]</a> https://citizenlab.ca/2016/04/between-hong-kong-and-burma/

<a name="2">[2]</a> https://www.cyber.nj.gov/threat-profiles/trojan-variants/poison-ivy

<a name="3">[3]</a> https://github.com/LordNoteworthy/al-khaser 

<a name="4">[4]</a> https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process 