|||
|---|---|
|**ID**|**B0007**|
|**Objective(s)**|[Anti-Behavioral Analysis](../anti-behavioral-analysis)|
|**Related ATT&CK Sub-techniques**|[Virtualization/Sandbox Evasion: System Checks](https://attack.mitre.org/techniques/T1497/001/), [Virtualization/Sandbox Evasion: User Activity Based Checks](https://attack.mitre.org/techniques/T1497/002/)|


Sandbox Detection
=================
Detects whether the malware instance is being executed inside an instrumented sandbox environment (e.g., Cuckoo Sandbox). If so, conditional execution selects a benign execution path.

The Sandbox Detection behavior relates to anti-analysis, whereas a related ATT&CK technique relates to [Defense Evasion](../defense-evasion): for details, see the ATT&CK [**Virtualization/Sandbox Evasion**](https://attack.mitre.org/techniques/T1497/) technique and its sub-techniques.

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Check Clipboard Data**|B0007.001|Checks clipboard data which can be used to detect whether execution is inside a sandbox.|
|**Check Files**|B0007.002|Sandboxes create files on the file system. Malware can check the different folders to find sandbox artifacts.|
|**Human User Check**|B0007.003|Detects whether there is any "user" activity on the machine, such as the movement of the mouse cursor, non-default wallpaper, or recently opened Office files. Directories or file might be counted. If there is no human activity, the machine is suspected to be a virtualized machine and/or sandbox. Other items used to detect a user: mouse clicks (single/double), DialogBox, scrolling, color of background pixel [[3]](#3). This method is very similar to ATT&CK's [Virtualization/Sandbox Evasion: User Activity Based Checks](https://attack.mitre.org/techniques/T1497/002/) sub-technique.|
|**Injected DLL Testing**|B0007.004|Testing for the name of a particular DLL that is known to be injected by a sandbox for API hooking is a common way of detecting sandbox environments. This can be achieved through the kernel32!GetModuleHandle API call and other means.|
|**Product Key/ID Testing**|B0007.005|Checking for a particular product key/ID associated with a sandbox environment (commonly associated with the Windows host OS used in the environment) can be used to detect whether a malware instance is being executed in a particular sandbox. This can be achieved through several means, including testing for the Key/ID in the Windows registry.|
|**Screen Resolution Testing**|B0007.006|Sandboxes aren't used in the same manner as a typical user environment, so most of the time the screen resolution stays at the minimum 800x600 or lower. No one is actually working on a such small screen. Malware could potentially detect the screen resolution to determine if it's a user machine or a sandbox.|
|**Self Check**|B0007.007|Malware may check its own characteristics to determine whether it's running in a sandbox. For example, a malicious Office document might check its file name or VB project name.|
|**Timing/Date Check**|B0007.008|Calling GetSystemTime or equiv and only executing code if the current date/hour/minute/second passes some check. Often this is for running only after or only until a specific date. This behavior can be mitigated in non-automated analysis environments.|
|**Timing/Uptime Check**|B0007.009|Comparing single GetTickCount with some value to see if system has been started at least *X* amount ago. This behavior can be mitigated in non-automated analysis environments.|
|**Test API Routines**|B0007.010|Calls Windows API routines with invalid arguments to identify error supression.|


Code Snippets
-------------
**Sandbox Detection::Product Key/ID Testing** (B0007.005) - the value 55274-640-2673064-23950 corresponds to Joe Sandbox.
```asm
push    ebx
add     esp, 0FFFFFEF4h
xor     ebx, ebx
push    esp             ; phkResult
push    1               ; samDesired
push    0               ; ulOptions
push    offset SubKey   ; "Software\Microsoft\Windows\CurrentVersi"...
push    80000002h       ; hKey
call    RegOpenKeyExA
test    eax, eax
jnz     short loc_405387
mov     [esp+110h+cbData], 101h
lea     eax, [esp+110h+cbData]
push    eax             ; lpcbData
lea     eax, [esp+114h+Data]
push    eax             ; lpData
push    0               ; lpType 
push    0               ; lpReserved
push    offset ValueName ; "ProductId"
mov     eax, [esp+124h+hKey]
push    eax             ; hKey
call    RegQueryValueExA
lea     eax, [esp+110h+Data]
cmp     eax, offset a55274640267306 ; "55274-640-2673064-23950"
jnz     short loc_405387
mov     bl, 1
```

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**Redhip**](../xample-malware/redhip.md)|January 2011|Redhip detects publicly available automated analysis workbenches (e.g., Joe Box) by considering OS product keys and special DLLs. [[1]](#1)|
|[**Rombertik**](../xample-malware/rombertik.md)|May 2015|[[2]](#2)|
|[**Terminator**](../xample-malware/terminator.md)|May 2013|The Terminator rat evades a sandbox by not executing until after a reboot. Most sandboxes don't reboot during an analysis. [[4]](#4)|
|[**Ursnif**](../xample-malware/ursnif.md)|2016|Ursnif uses malware macros to evade sandbox detection.|
|[**GotBotKR**](../anti-behavioral-analysis/detect-sandbox.md)|2019|GoBotKR performs several checks on the compromised machine to avoid being emulated or executed in a sandbox. [[5]](#5)|
|[**Rombertik**](../anti-behavioral-analysis/detect-vm.md)|2015|The malware check for sandboxes that suppress errors returned from API routine calls the using ZwGetWriteWatch routine. [[6]](#6)|
References
----------
<a name="1">[1]</a> https://www.fireeye.com/blog/threat-research/2011/01/the-dead-giveaways-of-vm-aware-malware.html 
 
<a name="2">[2]</a> https://blogs.cisco.com/security/talos/rombertik

<a name="3">[3]</a> https://github.com/LordNoteworthy/al-khaser

<a name="4">[4]</a> https://www.fireeye.com/content/dam/fireeye-www/current-threats/pdfs/pf/file/fireeye-hot-knives-through-butter.pdf

<a name="5">[5]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="6">[6]</a> https://blogs.cisco.com/security/talos/rombertik
