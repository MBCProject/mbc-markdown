|||
|---------|------------------------|
|**ID**|**M0007**|
|**Objective(s)**|[Anti-Behavioral Analysis](https://github.com/MBCProject/mbc-markdown/tree/master/anti-behavioral-analysis)|
|**Related ATT&CK Technique**|None|


Sandbox Detection
=================
Detects whether the malware instance is being executed inside an instrumented sandbox environment (e.g., Cuckoo Sandbox). If so, conditional execution selects a benign execution path.

The Sandbox Detection behavior relates to anti-analysis, whereas a related ATT&CK technique relates to [Defense Evasion](https://github.com/MBCProject/mbc-markdown/tree/master/defense-evasion): for details, see the ATT&CK: [**Virtualization/Sandbox Evasion**](https://attack.mitre.org/techniques/T1497/).

Methods
-------
* **Check Clipboard Data**: Checks clipboard data which can be used to detect whether execution is inside a sandbox.
* **Check Files**: Sandboxes create files on the file system. Malware can check the different folders to find sandbox artifacts.
* **Human User Check**: Detects whether there is any "user" activity on the machine, such as the movement of the mouse cursor, non-default wallpaper, or recently opened Office files. If there is no human activity, the machine is suspected to be a virtualized machine and/or sandbox. Other items used to detect a user: mouse clicks (single/double), DialogBox, scrolling, color of background pixel [[3]](#3).
* **Injected DLL Testing**: Testing for the name of a particular DLL that is known to be injected by a sandbox for API hooking is a common way of detecting sandbox environments. This can be achieved through the kernel32!GetModuleHandle API call and other means.
* **Machine Specs**: Different aspects of the hardware are inspected to determine whether the machine has standard, modern characteristics. Machines with substandard specs indicate a sandbox or virtual environment: 
   * Total physical memory: most modern machines have at leave 4 GB of memory. (GlobalMemoryStatusEx) [[3]](#3).
   * Drive size: most modern machines have at least 80 GB disks. May use DeviceloControl (IOCTL_DISK_GET_LENGTH_INFO) or GetDiskFreeSpaceEx (TotalNumberOfBytes) [[3]](#3).
   * USB drive: checks whether there is a potential USB drive; if not a virtual environment is suspected.
   * Printer: checks whether there is a potential connected printer or default Windows printers; if not a virtual environment is suspected.
   * Processor count: checks number of processors; single CPU machines are suspect.
   * Keyboard layout
* **Software Check**: Malware may check software to determine whether its running in a sandbox. For example malicious Office documents might check Microsoft Office version, window size, or VB project name.
* **Product Key/ID Testing**: Checking for a particular product key/ID associated with a sandbox environment (commonly associated with the Windows host OS used in the environment) can be used to detect whether a malware instance is being executed in a particular sandbox. This can be achieved through several means, including testing for the Key/ID in the Windows registry. 
* **Screen Resolution Testing**: Sandboxes aren't used in the same manner as a typical user environment, so most of the time the screen resolution stays at the minimum 800x600 or lower. No one is actually working on a such small screen. Malware could potentially detect the screen resolution to determine if it's a user machine or a sandbox.

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|
|[**Redhip**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/redhip.md)|January 2011|Redhip detects publicly available automated analysis workbenches (e.g., Joe Box) by considering OS product keys and special DLLs. [[1]](#1)|
|**Rombertik**|May 2015|[[2]](#2)|

References
----------
<a name="1">[1]</a> https://www.fireeye.com/blog/threat-research/2011/01/the-dead-giveaways-of-vm-aware-malware.html 
 
<a name="2">[2]</a> http://labs.lastline.com/exposing-rombertik-turning-the-tables-on-evasive-malware

<a name="3">[3]</a> https://github.com/LordNoteworthy/al-khaser