|||
|---|---|
|**ID**|**B0009**|
|**Objective(s)**|[Anti-Behavioral Analysis](../anti-behavioral-analysis)|
|**Related ATT&CK Technique**|Virtualization/Sandbox Evasion ([T1497](https://attack.mitre.org/techniques/T1497/), [T1633](https://attack.mitre.org/techniques/T1633/))|


Virtual Machine Detection
=========================
Detects whether the malware instance is being executed in a virtual machine (VM), such as VMWare. If so, conditional execution selects a benign execution path. [[1]](#1)

The related Virtualization/Sandbox Evasion ([T1497](https://attack.mitre.org/techniques/T1497/), [T1633](https://attack.mitre.org/techniques/T1633/)) ATT&CK technique was defined subsequent to this MBC behavior.

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Check File and Directory Artifacts**|B0009.001|Virtual machines create files on the file system (e.g., VMware creates files in the installation directory C:\Program Files\VMware\VMware Tools). Malware can check the different folders to find virtual machine artifacts (e.g., Virtualbox has the artifact VBoxMouse.sys). [[2]](#2)|
|**Check Memory Artifacts**|B0009.002|VMware leaves many artifacts in memory. Some are critical processor structures, which, because they are either moved or changed on a virtual machine, leave recognizable footprints. Malware can search through physical memory for the strings VMware, commonly used to detect memory artifacts. [[2]](#2)|
|**Check Named System Objects**|B0009.003|Virtual machines often include specific named system objects by default, such as Windows device drivers, which can be detected by testing for specific strings, whether found in the Windows registry or other places.|
|**Check Processes**|B0009.004|The VMware Tools use processes like VMwareServices.exe or VMwareTray.exe, to perform actions on the virtual environment. Malware can list the process and searches for the VMware string. Process related to Virtualbox can be detected by malware by query the process list. [[2]](#2)|
|**Check Registry Keys**|B0009.005|Virtual machines register artifacts in the registry, which can be detected by malware. For example, a search for "VMware" or "VBOX" in the registry might reveal keys that include information about a virtual hard drive, adapters, running services, or virtual mouse. [[2]](#2) Example registry key value artifacts include "HARDWARE\Description\System (SystemBiosVersion) (VBOX)" and "SYSTEM\ControlSet001\Control\SystemInformation (SystemManufacturer) (VMWARE)"; example registry key artifacts include "SOFTWARE\VMware, Inc.\VMware Tools (VMWARE)" and "SOFTWARE\Oracle\VirtualBox Guest Additions (VBOX)". [[5]](#5)|
|**Check Running Services**|B0009.006|VMwareService.exe runs the VMware Tools Service as a child of services.exe. It can be identified by listing services. [[2]](#2)|
|**Check Software**|B0009.007|Malware may check software version; for example, to determine whether the software is relatively current.|
|**Check Virtual Devices**|B0009.008|The presence of virtual devices can indicate a virtualized environment (e.g., "\\.\VBoxTrayIPC"). [[5]](#5)|
|**Check Windows**|B0009.009|Malware may check windows for VM-related characteristics.|
|**Check Windows - Title bars**|B0009.022|Malware may check windows for VM-related characteristics. May inject malicious code to svchost.exe to check all open window title bar text to a list of strings indicating virtualized environment.|
|**Check Windows - Unique windows**|B0009.021|Malware may check windows for VM-related characteristics. May check for the presence of known windows from analysis tools running in a VM.|
|**Check Windows - Window size**|B0009.020|Malware may check windows for VM-related characteristics. Tiny window size may indicate a VM.|
|**Guest Process Testing**|B0009.010|Virtual machines offer guest additions that can be installed to add functionality such as clipboard sharing. Detecting the process responsible for these tasks, via its name or other methods, is a technique employed by malware for detecting whether it is being executed in a virtual machine.|
|**HTML5 Performance Object Check**|B0009.011|In three browser families, it is possible to extract the frequency of the Windows performance counter frequency, using standard HTML and Javascript. This value can then be used to detect whether the code is being executed in a virtual machine, by detecting two specific frequencies commonly used in virtual but not physical machines.|
|**Human User Check**|B0009.012|Detects whether there is any "user" activity on the machine, such as the movement of the mouse cursor, non-default wallpaper, or recently opened Office files. Directories or file might be counted. If there is no human activity, the machine is suspected to be a virtualized machine and/or sandbox. Other items used to detect a user: mouse clicks (single/double), DialogBox, scrolling, color of background pixel, change in foreground window [[5]](#5). This method is very similar to ATT&CK's [Virtualization/Sandbox Evasion: User Activity Based Checks](https://attack.mitre.org/techniques/T1497/002/) sub-technique.|
|**Instruction Testing**|B0009.029|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2)|
|**Instruction Testing - CPUID**|B0009.034|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2) Checking the CPU ID found within the registry can provide information to system type.|
|**Instruction Testing - IN**|B0009.035|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2)|
|**Instruction Testing - RDTSC**|B0009.036|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2)|
|**Instruction Testing - SGDT/SLDT (no pill)**|B0009.031|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2) The No Pill technique relies on the fact that the LDT structure is assigned to a processor not an Operating System. The LDT location on a host machine will be zero and on a virtual machine will be non-zero.|
|**Instruction Testing - SIDT (red pill)**|B0009.030|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2) Red Pill is an anti-VM technique that executes the SIDT instruction to grab the value of the IDTR register. The virtual machine monitor must relocate the guest's IDTR to avoid conflict with the host's IDTR. Since the virtual machine monitor is not notified when the virtual machine runs the SIDT instruction, the IDTR for the virtual machine is returned.|
|**Instruction Testing - SMSW**|B0009.032|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2)|
|**Instruction Testing - STR**|B0009.033|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2)|
|**Instruction Testing - VMCPUID**|B0009.037|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2)|
|**Instruction Testing - VPCEXT**|B0009.038|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2)|
|**Modern Specs Check**|B0009.013|Different aspects of the hardware are inspected to determine whether the machine has modern characteristics. A machine with substandard specifications indicates a virtual environment.|
|**Modern Specs Check - Drive size**|B0009.015|Different aspects of the hardware are inspected to determine whether the machine has modern characteristics. A machine with substandard specifications indicates a virtual environment. Most modern machines have at least 80 GB disks. May use DeviceloControl (IOCTL_DISK_GET_LENGTH_INFO) or GetDiskFreeSpaceEx (TotalNumberOfBytes) [[5]](#5).|
|**Modern Specs Check - Keyboard layout**|B0009.019|Different aspects of the hardware are inspected to determine whether the machine has modern characteristics. A machine with substandard specifications indicates a virtual environment. Check keyboard layout.|
|**Modern Specs Check - Printer**|B0009.017|Different aspects of the hardware are inspected to determine whether the machine has modern characteristics. A machine with substandard specifications indicates a virtual environment. Checks whether there is a potential connected printer or default Windows printers; if not a virtual environment is suspected.|
|**Modern Specs Check - Processor count**|B0009.018|Different aspects of the hardware are inspected to determine whether the machine has modern characteristics. A machine with substandard specifications indicates a virtual environment. Checks number of processors; single CPU machines are suspect.|
|**Modern Specs Check - Total physical memory**|B0009.014|Different aspects of the hardware are inspected to determine whether the machine has modern characteristics. A machine with substandard specifications indicates a virtual environment. Most modern machines have at leave 4 GB of memory. (GlobalMemoryStatusEx) [[5]](#5).|
|**Modern Specs Check - USB drive**|B0009.016|Different aspects of the hardware are inspected to determine whether the machine has modern characteristics. A machine with substandard specifications indicates a virtual environment. Checks whether there is a potential USB drive; if not a virtual environment is suspected.|
|**Unique Hardware/Firmware Check**|B0009.023|Malware may check for hardware characteristics unique to being virtualized, allowing the malware to detect the virtual environment.|
|**Unique Hardware/Firmware Check - BIOS**|B0009.024|Malware may check for hardware characteristics unique to being virtualized, allowing the malware to detect the virtual environment. Characteristics of the BIOS, such as version, can indicate virtualization.|
|**Unique Hardware/Firmware Check - CPU Location**|B0009.027|Malware may check for hardware characteristics unique to being virtualized, allowing the malware to detect the virtual environment. When an Operating System is virtualized, the CPU is relocated. [[2]](#2)|
|**Unique Hardware/Firmware Check - CPU Name**|B0009.026|Malware may check for hardware characteristics unique to being virtualized, allowing the malware to detect the virtual environment. Checks the CPU name to determine virtualization.|
|**Unique Hardware/Firmware Check - I/O Communication Port**|B0009.025|Malware may check for hardware characteristics unique to being virtualized, allowing the malware to detect the virtual environment. VMware uses virtual I/O ports for communication between the virtual machine and the host operating system to support functionality like copy and paste between the two systems. The port can be queried and compared with a magic number VMXh to identify the use of VMware.|
|**Unique Hardware/Firmware Check - MAC Address**|B0009.028|Malware may check for hardware characteristics unique to being virtualized, allowing the malware to detect the virtual environment. VMware uses specific virtual MAC address that can be detected. The usual MAC address used started with the following numbers: "00:0C:29", "00:1C:14", "00:50:56", "00:05:69". Virtualbox uses specific virtual MAC address that can be detected by Malware. The usual MAC address used started with the following numbers: 08:00:27. [[2]](#2)|

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**GravityRAT**](../xample-malware/gravity-rat.md)|May 2018|GravityRAT checks system temperature by recording thermal readings for detecting VMs. Heat levels indicate whether the system is a VM. [[3]](#3)|
|[**WebCobra**](../xample-malware/webcobra.md)|2018|WebCobra injects malicious code to svchost.exe and uses an infinite loop to check all open windows and to compare each window’s title bar text with a set of strings to determine whether it is running in an isolated, malware analysis environment [[4]](#4)|
|[**Redhip**](../xample-malware/redhip.md)|2011|Redhip detects VMWare, Virtual PC and Virtual Box. It also detects VM environments in general by considering timing lapses. [[6]](#6)|

Code Snippets
-------------
**Virtual Machine Detection::Instruction Testing** (B0009.029)
 <br/>MD5: 0e058126f26b54b3a4a950313ec5dbce
```asm
; ___unwind { // __except handler4
push ebp
mov ebp, esp
push 0FFFFFFFEh
push offset stru_413980
push offset __except handler4
mov eax, large fs:0
push eax
sub esp, 14h
push ebx
push esi
push edi
mov eax, ___security_cookie
xor [epb+ms_exc.registration.ScopeTable], eax
xor eax, ebp
push eax
lea eax, [ebp+ms_exc.registration]
mov large fs:0 eax
mov [ebp+var_19], al
;  __try { // __except at loc_401CB8
mov [ebp+ms_exc.registration.TryLevel], eax
push ebx
mov ebx, 0
mov eax, 1
vpcext 7, 08h
test ebx, ebx
setz [ebp+var_19]
pop ebx
jmp short loc_401CBB
```



References
----------
<a name="1">[1]</a> https://www.fireeye.com/blog/threat-research/2011/01/the-dead-giveaways-of-vm-aware-malware.html

<a name="2">[2]</a> https://search.unprotect.it/map/sandbox-evasion/

<a name="3">[3]</a> https://www.hackread.com/gravityrat-malware-evades-detection-targets-india/

<a name="4">[4]</a> https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/

<a name="5">[5]</a> https://github.com/LordNoteworthy/al-khaser

<a name="6">[6]</a> https://www.fireeye.com/blog/threat-research/2011/01/the-dead-giveaways-of-vm-aware-malware.html
