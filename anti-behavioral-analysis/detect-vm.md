|||
|---|---|
|**ID**|**B0009**|
|**Objective(s)**|[Anti-Behavioral Analysis](https://github.com/MBCProject/mbc-markdown/tree/master/anti-behavioral-analysis)|
|**Related ATT&CK Technique**|[Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497/)|


Virtual Machine Detection
=========================
Detects whether the malware instance is being executed in a virtual machine (VM), such as VMWare. If so, conditional execution selects a benign execution path. [[1]](#1)

The Virtual Machine Detection behavior relates to anti-analysis, whereas a related ATT&CK technique relates to [Defense Evasion](https://github.com/MBCProject/mbc-markdown/tree/master/defense-evasion): for details, see the ATT&CK [**Virtualization/Sandbox Evasion**](https://attack.mitre.org/techniques/T1497/) technique and its sub-techniques.

Methods
-------
|ID|Name|Description|
|---|---|---|
|B0009.001|**Check File and Directory Artifacts**|Virtual machines create files on the file system (e.g., VMware creates files in the installation directory C:\Program Files\VMware\VMware Tools). Malware can check the different folders to find virtual machine artifacts (e.g., Virtualbox has the artifact VBoxMouse.sys). [[2]](#2)|
|B0009.002|**Check Memory Artifacts**|VMware leaves many artifacts in memory. Some are critical processor structures, which, because they are either moved or changed on a virtual machine, leave recognizable footprints. Malware can search through physical memory for the strings VMware, commonly used to detect memory artifacts. [[2]](#2)|
|B0009.003|**Check Named System Objects**|Virtual machines often include specific named system objects by default, such as Windows device drivers, which can be detected by testing for specific strings, whether found in the Windows registry or other places.|
|B0009.004|**Check Processes**|The VMware Tools use processes like VMwareServices.exe or VMwareTray.exe, to perform actions on the virtual environment. Malware can list the process and searches for the VMware string. Process related to Virtualbox can be detected by malware by query the process list. [[2]](#2)|
|B0009.005|**Check Registry Keys**|Virtual machines register artifacts in the registry, which can be detected by malware. For example, a search for "VMware" or "VBOX" in the registry might reveal keys that include information about a virtual hard drive, adapters, running services, or virtual mouse. [[2]](#2) Example registry key value artifacts include "HARDWARE\Description\System (SystemBiosVersion) (VBOX)" and "SYSTEM\ControlSet001\Control\SystemInformation (SystemManufacturer) (VMWARE)"; example registry key artifacts include "SOFTWARE\VMware, Inc.\VMware Tools (VMWARE)" and "SOFTWARE\Oracle\VirtualBox Guest Additions (VBOX)". [[5]](#5)|
|B0009.006|**Check Running Services**|VMwareService.exe runs the VMware Tools Service as a child of services.exe. It can be identified by listing services. [[2]](#2)|
|B0009.007|**Check Software**|Malware may check software version; for example, to determine whether the software is relatively current.|
|B0009.008|**Check Virtual Devices**|The presence of virtual devices can indicate a virtualized environment (e.g., "\\.\VBoxTrayIPC"). [[5]](#5)|
|B0009.009|**Check Windows**|Malware may check windows for VM-related characteristics.|
|B0009.010|**Guest Process Testing**|Virtual machines offer guest additions that can be installed to add functionality such as clipboard sharing. Detecting the process responsible for these tasks, via its name or other methods, is a technique employed by malware for detecting whether it is being executed in a virtual machine.|
|B0009.011|**HTML5 Performance Object Check**|In three browser families, it is possible to extract the frequency of the Windows performance counter frequency, using standard HTML and Javascript. This value can then be used to detect whether the code is being executed in a virtual machine, by detecting two specific frequencies commonly used in virtual but not physical machines.|
|B0009.012|**Human User Check**|Detects whether there is any "user" activity on the machine, such as the movement of the mouse cursor, non-default wallpaper, or recently opened Office files. Directories or file might be counted. If there is no human activity, the machine is suspected to be a virtualized machine and/or sandbox. Other items used to detect a user: mouse clicks (single/double), DialogBox, scrolling, color of background pixel, change in foreground window [[5]](#5). This method is very similar to ATT&CK's [Virtualization/Sandbox Evasion: User Activity Based Checks](https://attack.mitre.org/techniques/T1497/002/) sub-technique.|
|B0009.013|**Modern Specs Check**|Different aspects of the hardware are inspected to determine whether the machine has modern characteristics. A machine with substandard specifications indicates a virtual environment.|
|B0009.014|**Modern Specs Check - Total physical memory**|Different aspects of the hardware are inspected to determine whether the machine has modern characteristics. A machine with substandard specifications indicates a virtual environment. Most modern machines have at leave 4 GB of memory. (GlobalMemoryStatusEx) [[5]](#5).|
|B0009.015|**Modern Specs Check - Drive size**|Different aspects of the hardware are inspected to determine whether the machine has modern characteristics. A machine with substandard specifications indicates a virtual environment. Most modern machines have at least 80 GB disks. May use DeviceloControl (IOCTL_DISK_GET_LENGTH_INFO) or GetDiskFreeSpaceEx (TotalNumberOfBytes) [[5]](#5).|
|B0009.016|**Modern Specs Check - USB drive**|Different aspects of the hardware are inspected to determine whether the machine has modern characteristics. A machine with substandard specifications indicates a virtual environment. Checks whether there is a potential USB drive; if not a virtual environment is suspected.|
|B0009.017|**Modern Specs Check - Printer**|Different aspects of the hardware are inspected to determine whether the machine has modern characteristics. A machine with substandard specifications indicates a virtual environment. Checks whether there is a potential connected printer or default Windows printers; if not a virtual environment is suspected.|
|B0009.018|**Modern Specs Check - Processor count**|Different aspects of the hardware are inspected to determine whether the machine has modern characteristics. A machine with substandard specifications indicates a virtual environment. Checks number of processors; single CPU machines are suspect.|
|B0009.019|**Modern Specs Check - Keyboard layout**|Different aspects of the hardware are inspected to determine whether the machine has modern characteristics. A machine with substandard specifications indicates a virtual environment. Check keyboard layout.|
|B0009.020|**Check Windows - Window size**|Malware may check windows for VM-related characteristics. Tiny window size may indicate a VM.|
|B0009.021|**Check Windows - Unique windows**|Malware may check windows for VM-related characteristics. May check for the presence of known windows from analysis tools running in a VM.|
|B0009.022|**Check Windows - Title bars**|Malware may check windows for VM-related characteristics. May inject malicious code to svchost.exe to check all open window title bar text to a list of strings indicating virtualized environment.|
|B0009.023|**Unique Hardware/Firmware Check**|Malware may check for hardware characteristics unique to being virtualized, allowing the malware to detect the virtual environment.|
|B0009.024|**Unique Hardware/Firmware Check - BIOS**|Malware may check for hardware characteristics unique to being virtualized, allowing the malware to detect the virtual environment. Characteristics of the BIOS, such as version, can indicate virtualization.|
|B0009.025|**Unique Hardware/Firmware Check - I/O Communication Port**|Malware may check for hardware characteristics unique to being virtualized, allowing the malware to detect the virtual environment. VMware uses virtual I/O ports for communication between the virtual machine and the host operating system to support functionality like copy and paste between the two systems. The port can be queried and compared with a magic number VMXh to identify the use of VMware.|
|B0009.026|**Unique Hardware/Firmware Check - CPU Name**|Malware may check for hardware characteristics unique to being virtualized, allowing the malware to detect the virtual environment. Checks the CPU name to determine virtualization.|
|B0009.027|**Unique Hardware/Firmware Check - CPU Location**|Malware may check for hardware characteristics unique to being virtualized, allowing the malware to detect the virtual environment. When an Operating System is virtualized, the CPU is relocated. [[2]](#2)|
|B0009.028|**Unique Hardware/Firmware Check - MAC Address**|Malware may check for hardware characteristics unique to being virtualized, allowing the malware to detect the virtual environment. VMware uses specific virtual MAC address that can be detected. The usual MAC address used started with the following numbers: "00:0C:29", "00:1C:14", "00:50:56", "00:05:69". Virtualbox uses specific virtual MAC address that can be detected by Malware. The usual MAC address used started with the following numbers: 08:00:27. [[2]](#2)|
|B0009.029|**Instruction Testing**|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2)|
|B0009.030|**Instruction Testing - SIDT (red pill)**|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2) Red Pill is an anti-VM technique that executes the SIDT instruction to grab the value of the IDTR register. The virtual machine monitor must relocate the guest's IDTR to avoid conflict with the host's IDTR. Since the virtual machine monitor is not notified when the virtual machine runs the SIDT instruction, the IDTR for the virtual machine is returned.|
|B0009.031|**Instruction Testing - SGDT/SLDT (no pill)**|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2) The No Pill technique relies on the fact that the LDT structure is assigned to a processor not an Operating System. The LDT location on a host machine will be zero and on a virtual machine will be non-zero.|
|B0009.032|**Instruction Testing - SMSW**|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2)|
|B0009.033|**Instruction Testing - STR**|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2)|
|B0009.034|**Instruction Testing - CPUID**|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2) Checking the CPU ID found within the registry can provide information to system type.|
|B0009.035|**Instruction Testing - IN**|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2)|
|B0009.036|**Instruction Testing - RDTSC**|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2)|
|B0009.037|**Instruction Testing - VMCPUID**|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2)|
|B0009.038|**Instruction Testing - VPCEXT**|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2)|

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**GravityRAT**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/gravity-rat.md)|May 2018|GravityRAT checks system temperature by recording thermal readings for detecting VMs. Heat levels indicate whether the system is a VM. [[3]](#3)|
|[**WebCobra**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/webcobra.md)|2018|WebCobra injects malicious code to svchost.exe and uses an infinite loop to check all open windows and to compare each window’s title bar text with a set of strings to determine whether it is running in an isolated, malware analysis environment [[4]](#4)|
|[**Redhip**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/redhip.md)|2011|Redhip detects VMWare, Virtual PC and Virtual Box. It also detects VM environments in general by considering timing lapses. [[6]](#6)|

References
----------
<a name="1">[1]</a> https://www.fireeye.com/blog/threat-research/2011/01/the-dead-giveaways-of-vm-aware-malware.html

<a name="2">[2]</a> http://unprotect.tdgt.org/index.php/Sandbox_Evasion

<a name="3">[3]</a> https://www.hackread.com/gravityrat-malware-evades-detection-targets-india/

<a name="4">[4]</a> https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/

<a name="5">[5]</a> https://github.com/LordNoteworthy/al-khaser

<a name="6">[6]</a> https://www.fireeye.com/blog/threat-research/2011/01/the-dead-giveaways-of-vm-aware-malware.html
