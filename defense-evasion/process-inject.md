|||
|---------|------------------------|
|**ID**|**E1055**|
|**Objective(s)**| [Defense Evasion](https://github.com/MBCProject/mbc-markdown/tree/master/defense-evasion), [Privilege Escalation](https://github.com/MBCProject/mbc-markdown/tree/master/privilege-escalation)|
|**Related ATT&CK Technique(s)**|[Process Injection](https://attack.mitre.org/techniques/T1055)|


Process Injection
=================
Malware may execute code in the address space of a separate process. 

See ATT&CK: [**Process Injection**](https://attack.mitre.org/techniques/T1055).

Methods
------- 
* **Shell_TrayWnd**: Injects code using the Shell_TRyaWnd technique.
* **CreateRemoteThread**: Create a thread using CreateRemoteThread.
* **SetWindowsHooksEx**
* **NtCreateThreadEx**
* **RtlCreateUserThread**
* **APC**: QueueUserAPC / NtQueueApcThread [[3]](#3).
* **RunPE**: GetThreadContext / SetThreadContext [[3]](#3).


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