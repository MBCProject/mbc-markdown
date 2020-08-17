|||
|---------|------------------------|
|**ID**|**B0007**|
|**Objective(s)**|[Anti-Behavioral Analysis](https://github.com/MBCProject/mbc-markdown/tree/master/anti-behavioral-analysis)|
|**Related ATT&CK Sub-techniques**|[Virtualization/Sandbox Evasion: System Checks](https://attack.mitre.org/techniques/T1497/001/), [Virtualization/Sandbox Evasion: User Activity Based Checks](https://attack.mitre.org/techniques/T1497/002/)|


Sandbox Detection
=================
Detects whether the malware instance is being executed inside an instrumented sandbox environment (e.g., Cuckoo Sandbox). If so, conditional execution selects a benign execution path.

The Sandbox Detection behavior relates to anti-analysis, whereas a related ATT&CK technique relates to [Defense Evasion](https://github.com/MBCProject/mbc-markdown/tree/master/defense-evasion): for details, see the ATT&CK [**Virtualization/Sandbox Evasion**](https://attack.mitre.org/techniques/T1497/) technique and its sub-techniques.

Methods
-------
|ID|Name|Description|
|-----------------------------|--------|-----------------------------|
|B0007.001|**Check Clipboard Data**|Checks clipboard data which can be used to detect whether execution is inside a sandbox.|
|B0007.002|**Check Files**|Sandboxes create files on the file system. Malware can check the different folders to find sandbox artifacts.|
|B0007.003|**Human User Check**|Detects whether there is any "user" activity on the machine, such as the movement of the mouse cursor, non-default wallpaper, or recently opened Office files. Directories or file might be counted. If there is no human activity, the machine is suspected to be a virtualized machine and/or sandbox. Other items used to detect a user: mouse clicks (single/double), DialogBox, scrolling, color of background pixel [[3]](#3). This method is very similar to ATT&CK's [Virtualization/Sandbox Evasion: User Activity Based Checks](https://attack.mitre.org/techniques/T1497/002/) sub-technique.|
|B0007.004|**Injected DLL Testing**|Testing for the name of a particular DLL that is known to be injected by a sandbox for API hooking is a common way of detecting sandbox environments. This can be achieved through the kernel32!GetModuleHandle API call and other means.|
|B0007.005|**Product Key/ID Testing**|Checking for a particular product key/ID associated with a sandbox environment (commonly associated with the Windows host OS used in the environment) can be used to detect whether a malware instance is being executed in a particular sandbox. This can be achieved through several means, including testing for the Key/ID in the Windows registry.|
|B0007.006|**Screen Resolution Testing**|Sandboxes aren't used in the same manner as a typical user environment, so most of the time the screen resolution stays at the minimum 800x600 or lower. No one is actually working on a such small screen. Malware could potentially detect the screen resolution to determine if it's a user machine or a sandbox.|
|B0007.007|**Self Check**|Malware may check its own characteristics to determine whether it's running in a sandbox. For example, a malicious Office document might check its file name or VB project name.|
|B0007.008|**Timing/Date Check**|Calling GetSystemTime or equiv and only executing code if the current date/hour/minute/second passes some check. Often this is for running only after or only until a specific date. This behavior can be mitigated in non-automated analysis environments.|
|B0007.009|**Timing/Uptime Check**|Comparing single GetTickCount with some value to see if system has been started at least *X* amount ago. This behavior can be mitigated in non-automated analysis environments.|

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|
|[**Redhip**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/redhip.md)|January 2011|Redhip detects publicly available automated analysis workbenches (e.g., Joe Box) by considering OS product keys and special DLLs. [[1]](#1)|
|[**Rombertik**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/rombertik.md)|May 2015|[[2]](#2)|
|[**Terminator**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/terminator.md)|May 2013|The Terminator rat evades a sandbox by not executing until after a reboot. Most sandboxes don't reboot during an analysis. [[4]](#4) |
|[**Ursnif**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/ursnif.md)|2016|Ursnif uses malware macros to evade sandbox detection.|

References
----------
<a name="1">[1]</a> https://www.fireeye.com/blog/threat-research/2011/01/the-dead-giveaways-of-vm-aware-malware.html 
 
<a name="2">[2]</a> http://labs.lastline.com/exposing-rombertik-turning-the-tables-on-evasive-malware

<a name="3">[3]</a> https://github.com/LordNoteworthy/al-khaser

<a name="4">[4]</a> https://www.fireeye.com/content/dam/fireeye-www/current-threats/pdfs/pf/file/fireeye-hot-knives-through-butter.pdf 