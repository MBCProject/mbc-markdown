<table>
<tr>
<td><b>ID</b></td>
<td><b>B0009</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../anti-behavioral-analysis">Anti-Behavioral Analysis</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Virtualization/Sandbox Evasion (<a href="https://attack.mitre.org/techniques/T1497/">T1497</a>, <a href="https://attack.mitre.org/techniques/T1633/">T1633</a>)</b></td>
</tr>
<tr>
<td><b>Anti-Analysis Type</b></td>
<td><b>Detection</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>13 September 2023</b></td>
</tr>
</table>


# Virtual Machine Detection

Malware checks whether it is being executed inside a virtual environment. In performing reconnaissance of its environment, the malware will check on a variety of user or system based artifacts. Examples include: 

- monitoring for user action as reflected by scrolling
- verifying system characteristics through Windows Management Interface (WMI) queries, e.g., for MAC address
- observing whether tool artifacts represented by strings or processes exist, e.g., VirtualBox.exe or joeboxserver.exe  
- checking specific registry keys or values [[1]](#1)

Upon detection of the virtual machine, conditional execution will change the malware’s behavior. For example, execution may terminate, or activity may appear benign, e.g., connecting to a benign domain.

The related **Virtualization/Sandbox Evasion ([T1497](https://attack.mitre.org/techniques/T1497/), [T1633](https://attack.mitre.org/techniques/T1633/))** ATT&CK techniques were defined subsequent to this MBC behavior.

## Methods

|Name|ID|Description|
|---|---|---|
|**Check File and Directory Artifacts**|B0009.001|Virtual machines create files on the file system (e.g., VMware creates files in the installation directory C:\Program Files\VMware\VMware Tools). Malware can check the different folders to find virtual machine artifacts (e.g., Virtualbox has the artifact VBoxMouse.sys). [[2]](#2)|
|**Check Memory Artifacts**|B0009.002|VMware leaves many artifacts in memory. Some are critical processor structures, which, because they are either moved or changed on a virtual machine, leave recognizable footprints. Malware can search through physical memory for the strings VMware, commonly used to detect memory artifacts. [[2]](#2)|
|**Check Named System Objects**|B0009.003|Virtual machines often include specific named system objects by default, such as Windows device drivers, which can be detected by testing for specific strings, whether found in the Windows registry or other places.|
|**Check Processes**|B0009.004|The VMware Tools use processes like VMwareServices.exe or VMwareTray.exe, to perform actions on the virtual environment. Malware can list the processes and searches for the VMware string. Processes related to Virtualbox can be detected by the malware by querying the process list. [[2]](#2) This method is related to Unprotect technique U1334.|
|**Check Registry Keys**|B0009.005|Virtual machines register artifacts in the registry, which can be detected by malware. For example, a search for "VMware" or "VBOX" in the registry might reveal keys that include information about a virtual hard drive, adapters, running services, or a virtual mouse. [[2]](#2) Example registry key value artifacts include "HARDWARE\Description\System (SystemBiosVersion) (VBOX)" and "SYSTEM\ControlSet001\Control\SystemInformation (SystemManufacturer) (VMWARE)"; example registry key artifacts include "SOFTWARE\VMware, Inc.\VMware Tools (VMWARE)" and "SOFTWARE\Oracle\VirtualBox Guest Additions (VBOX)". [[5]](#5)|
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
|**Instruction Testing**|[B0009.029](#b0009029-snippet)|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2)|
|**Instruction Testing - CPUID**|B0009.034|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2) Checking the CPU ID found within the registry can provide information to system type. This method is related to Unprotect technqiue U1324.|
|**Instruction Testing - IN**|B0009.035|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2) This method is related to Unprotect technique U1323.|
|**Instruction Testing - RDTSC**|B0009.036|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2)|
|**Instruction Testing - SGDT/SLDT (no pill)**|B0009.031|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2) The No Pill technique relies on the fact that the LDT structure is assigned to a processor not an Operating System. The LDT location on a host machine will be zero and on a virtual machine will be non-zero. This method is related to Unprotect technique U1327.|
|**Instruction Testing - SIDT (red pill)**|B0009.030|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2) Red Pill is an anti-VM technique that executes the SIDT instruction to grab the value of the IDTR register. The virtual machine monitor must relocate the guest's IDTR to avoid conflict with the host's IDTR. Since the virtual machine monitor is not notified when the virtual machine runs the SIDT instruction, the IDTR for the virtual machine is returned. This method is related to Unprotect technique U1328.|
|**Instruction Testing - SMSW**|B0009.032|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2) This method is related to Unprotect technique U1326.|
|**Instruction Testing - STR**|B0009.033|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2) This method is related to Unprotect technique U1325.|
|**Instruction Testing - VMCPUID**|B0009.037|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2) This method is related to Unprotect technique U1322.|
|**Instruction Testing - VPCEXT**|B0009.038|The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2) This method is related to Unprotect technique U1321.|
|**Modern Specs Check**|B0009.013|Different aspects of the hardware are inspected to determine whether the machine has modern characteristics. A machine with substandard specifications indicates a virtual environment.|
|**Modern Specs Check - Drive size**|B0009.015|Different aspects of the hardware are inspected to determine whether the machine has modern characteristics. A machine with substandard specifications indicates a virtual environment. Most modern machines have at least 80 GB disks. May use DeviceloControl (IOCTL_DISK_GET_LENGTH_INFO) or GetDiskFreeSpaceEx (TotalNumberOfBytes) [[5]](#5). This method is related to Unprotect technique U1312.|
|**Modern Specs Check - Keyboard layout**|B0009.019|Different aspects of the hardware are inspected to determine whether the machine has modern characteristics. A machine with substandard specifications indicates a virtual environment. Check keyboard layout.|
|**Modern Specs Check - Printer**|B0009.017|Different aspects of the hardware are inspected to determine whether the machine has modern characteristics. A machine with substandard specifications indicates a virtual environment. Checks whether there is a potential connected printer or default Windows printers; if not a virtual environment is suspected. This method is related to Unprotect technique U1309.|
|**Modern Specs Check - Processor count**|B0009.018|Different aspects of the hardware are inspected to determine whether the machine has modern characteristics. A machine with substandard specifications indicates a virtual environment. Checks number of processors; single CPU machines are suspect. This method is related to Unprotect technique U1340.|
|**Modern Specs Check - Total physical memory**|B0009.014|Different aspects of the hardware are inspected to determine whether the machine has modern characteristics. A machine with substandard specifications indicates a virtual environment. Most modern machines have at leave 4 GB of memory. (GlobalMemoryStatusEx) [[5]](#5). This method is related to Unprotect technique U1313.|
|**Modern Specs Check - USB drive**|B0009.016|Different aspects of the hardware are inspected to determine whether the machine has modern characteristics. A machine with substandard specifications indicates a virtual environment. Checks whether there is a potential USB drive; if not a virtual environment is suspected. This method is related to Unprotect technique U1310.|
|**Unique Hardware/Firmware Check**|B0009.023|Malware may check for hardware characteristics unique to being virtualized, allowing the malware to detect the virtual environment.|
|**Unique Hardware/Firmware Check - BIOS**|B0009.024|Malware may check for hardware characteristics unique to being virtualized, allowing the malware to detect the virtual environment. Characteristics of the BIOS, such as version, can indicate virtualization.|
|**Unique Hardware/Firmware Check - CPU Location**|B0009.027|Malware may check for hardware characteristics unique to being virtualized, allowing the malware to detect the virtual environment. When an Operating System is virtualized, the CPU is relocated. [[2]](#2)|
|**Unique Hardware/Firmware Check - CPU Name**|B0009.026|Malware may check for hardware characteristics unique to being virtualized, allowing the malware to detect the virtual environment. Checks the CPU name to determine virtualization.|
|**Unique Hardware/Firmware Check - I/O Communication Port**|B0009.025|Malware may check for hardware characteristics unique to being virtualized, allowing the malware to detect the virtual environment. VMware uses virtual I/O ports for communication between the virtual machine and the host operating system to support functionality like copy and paste between the two systems. The port can be queried and compared with a magic number VMXh to identify the use of VMware. This method is related to Unprotect technique U1336.|
|**Unique Hardware/Firmware Check - MAC Address**|B0009.028|Malware may check for hardware characteristics unique to being virtualized, allowing the malware to detect the virtual environment. VMware uses specific virtual MAC address that can be detected. The usual MAC address used started with the following numbers: "00:0C:29", "00:1C:14", "00:50:56", "00:05:69". Virtualbox uses specific virtual MAC address that can be detected by Malware. The usual MAC address used started with the following numbers: 08:00:27. [[2]](#2) This method is related to Unprotect technique U1335.|


## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**GravityRAT**](../xample-malware/gravity-rat.md)|2018|--|GravityRAT checks system temperature by recording thermal readings for detecting VMs. Heat levels indicate whether the system is a VM. [[3]](#3)|
|[**GravityRAT**](../xample-malware/gravity-rat.md)|2018|B0009.018|GravityRAT determines the machine is a VM if the core count is 1. [[3]](#3)|
|[**GravityRAT**](../xample-malware/gravity-rat.md)|2018|B0009.023|GravityRAT checks if the manufacturer field in the Win32_Computer entry (in WMI) contains "Virtual," "Vmware," or "Virtualbox." [[3]](#3)|
|[**GravityRAT**](../xample-malware/gravity-rat.md)|2018|B0009.024|GravityRAT creates a WMI request to identify the BIOS version. [[13]](#13)|
|[**GravityRAT**](../xample-malware/gravity-rat.md)|2018|B0009.028|GravityRAT checks if the MAC address starts with a well-known hexadecimal number used by various VM developers. [[3]](#3)|
|[**WebCobra**](../xample-malware/webcobra.md)|2018|B0009.022|WebCobra injects malicious code in to svchost.exe and uses an infinite loop to check all open windows and to compare each window’s title bar text with a set of strings to determine whether it is running in a VM. [[4]](#4)|
|[**Redhip**](../xample-malware/redhip.md)|2011|--|Redhip detects VMWare, Virtual PC, and Virtual Box. It also detects VM environments in general by considering time lapses. [[6]](#6)|
|[**Emotet**](../xample-malware/emotet.md)|2018|B0009.010|Emotet checks for various processes that are associated with various virtual machines by comparing hash values of the process names with the hash values of the list of running process names. [[7]](#7)|
|[**Vobfus**](../xample-malware/vobfus.md)|2016|--|Vobfus checks for the presence of virtualization software by querying the system registry. [[8]](#8)|
|[**Matanbuchus**](../xample-malware/matanbuchus.md)|2021|B0009.003|Malware checks if it is running in a sandbox. If it is, the malware exits. [[9]](#9) [[10]](#10)|
|[**Ursnif**](../xample-malware/ursnif.md)|2016|B0009.004|The malware checks if there are virtual machine processes running (Vbox, vmware, etc). [[11]](#11)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|B0009.012|The malware checks for an unmoving mouse cursor. [[12]](#12)|


## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[check for sandbox and av modules](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-av/check-for-sandbox-and-av-modules.yml)|Virtual Machine Detection (B0009)|GetModuleHandle|
|[check for Windows sandbox via genuine state](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-vm/vm-detection/check-for-windows-sandbox-via-genuine-state.yml)|Virtual Machine Detection (B0009)|SLIsGenuineLocal, UuidFromString|
|[reference anti-VM strings targeting Parallels](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-vm/vm-detection/reference-anti-vm-strings-targeting-parallels.yml)|Virtual Machine Detection (B0009)| |
|[check for unmoving mouse cursor](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-vm/vm-detection/check-for-unmoving-mouse-cursor.yml)|Virtual Machine Detection::Human User Check (B0009.012)| |
|[reference anti-VM strings targeting VirtualPC](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-vm/vm-detection/reference-anti-vm-strings-targeting-virtualpc.yml)|Virtual Machine Detection (B0009)| |
|[reference anti-VM strings targeting VMWare](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-vm/vm-detection/reference-anti-vm-strings-targeting-vmware.yml)|Virtual Machine Detection (B0009)| |
|[check for foreground window switch](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-vm/vm-detection/check-for-foreground-window-switch.yml)|Virtual Machine Detection::Human User Check (B0009.012)|Sleep|
|[detect VM via disk hardware WMI queries](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-vm/vm-detection/detect-vm-via-disk-hardware-wmi-queries.yml)|Virtual Machine Detection::Unique Hardware/Firmware Check (B0009.023)| |
|[reference anti-VM strings targeting Qemu](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-vm/vm-detection/reference-anti-vm-strings-targeting-qemu.yml)|Virtual Machine Detection (B0009)| |
|[reference anti-VM strings targeting Xen](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-vm/vm-detection/reference-anti-vm-strings-targeting-xen.yml)|Virtual Machine Detection (B0009)| |
|[check for sandbox username or hostname](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-vm/vm-detection/check-for-sandbox-username-or-hostname.yml)|Virtual Machine Detection (B0009)| |
|[check for Windows sandbox via process name](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-vm/vm-detection/check-for-windows-sandbox-via-process-name.yml)|Virtual Machine Detection (B0009)| |
|[check for Windows sandbox via dns suffix](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-vm/vm-detection/check-for-windows-sandbox-via-dns-suffix.yml)|Virtual Machine Detection (B0009)|GetAdaptersAddresses|
|[check for Windows sandbox via device](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-vm/vm-detection/check-for-windows-sandbox-via-device.yml)|Virtual Machine Detection (B0009)| |
|[reference anti-VM strings targeting VirtualBox](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-vm/vm-detection/reference-anti-vm-strings-targeting-virtualbox.yml)|Virtual Machine Detection (B0009)| |
|[check for Windows sandbox via registry](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-vm/vm-detection/check-for-windows-sandbox-via-registry.yml)|Virtual Machine Detection (B0009)|RegOpenKeyEx, RegEnumValue|
|[reference anti-VM strings](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-vm/vm-detection/reference-anti-vm-strings.yml)|Virtual Machine Detection (B0009)| |

## Code Snippets

### B0009.029 Snippet
<details>
<summary> Virtual Machine Detection::Instruction Testing </summary>
SHA256: cfaf863181e49906df33f9104795678f2fb41a007a8fd066a84fd99f613d7ef3
<pre>
asm
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
</pre>
</details>


## References

<a name="1">[1]</a> Check Point Research,"CP<r>: Evasion Techniques," evasions.checkpoint.com, [Online]. Available: https://evasions.checkpoint.com.

<a name="2">[2]</a> https://search.unprotect.it/category/sandbox-evasion/

<a name="3">[3]</a> https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html

<a name="4">[4]</a> https://www.mcafee.com/blogs/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/

<a name="5">[5]</a> https://github.com/LordNoteworthy/al-khaser

<a name="6">[6]</a> https://web.archive.org/web/20161025013916/https://www.fireeye.com/blog/threat-research/2011/01/the-dead-giveaways-of-vm-aware-malware.html

<a name="7">[7]</a> https://securelist.com/the-banking-trojan-emotet-detailed-analysis/69560/

<a name="8">[8]</a> https://securitynews.sonicwall.com/xmlpost/revisiting-vobfus-worm-mar-8-2013/

<a name="9">[9]</a> https://www.0ffset.net/reverse-engineering/matanbuchus-loader-analysis/

<a name="10">[10]</a> https://www.cyberark.com/resources/threat-research-blog/inside-matanbuchus-a-quirky-loader

<a name="11">[11]</a> https://www.proofpoint.com/us/threat-insight/post/ursnif-banking-trojan-campaign-sandbox-evasion-techniques

<a name="12">[12]</a> capa v4.0, analyzed at MITRE on 10/12/2022

<a name="12">[12]</a> https://www.hackread.com/gravityrat-malware-evades-detection-targets-india/
