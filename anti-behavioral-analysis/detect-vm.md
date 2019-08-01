|||
|---------|------------------------|
|**ID**|**M0009**|
|**Objective(s)**|[Anti-Behavioral Analysis](https://github.com/MAECProject/malware-behaviors/tree/master/anti-behavioral-analysis)|
|**Related ATT&CK Technique(s)**|[Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497/)|


Virtual Machine Detection
=========================
Detects whether the malware instance is being executed in a virtual machine (VM), such as VMWare. If so, conditional execution selects a benign execution path. [[1]](#1)

The Virtual Machine Detection behavior relates to anti-analysis, whereas a related ATT&CK technique relates to [Defense Evasion](https://github.com/MAECProject/malware-behaviors/tree/master/defense-evasion): for details, see the ATT&CK: [**Virtualization/Sandbox Evasion**](https://attack.mitre.org/techniques/T1497/).

Methods
-------
* **Guest Process Testing**: Virtual machines offer guest additions that can be installed to add functionality such as clipboard sharing. Detecting the process responsible for these tasks, via its name or other methods, is a technique employed by malware for detecting whether it is being executed in a virtual machine.
* **HTML5 Performance Object**: In three browser families, it is possible to extract the frequency of the Windows performance counter frequency, using standard HTML and Javascript. This value can then be used to detect whether the code is being executed in a virtual machine, by detecting two specific frequencies commonly used in virtual but not physical machines.
* **Named System Object Checks**: Virtual machines often include specific named system objects by default, such as Windows device drivers, which can be detected by testing for specific strings, whether found in the Windows registry or other places.
* **Machine Specs**: Different aspects of the hardware are inspected to determine whether the machine has standard, modern characteristics. Machines with substandard specs indicate a virtual environment: 
   * Memory size: most modern machines have at leave 4 GB of memory. 
   * Drive size: most modern machines have at least 80 GB disks.
   * USB drive: checks whether there is a potential USB drive; if not a virtual environment is suspected.
   * Printer: checks whether there is a potential connected printer or default Windows printers; if not a virtual environment is suspected.
   * CPU: checks number of processors; single CPU machines are suspect.
* **x86 Instructions**: The execution of certain x86 instructions will result in different values when executed inside of a VM instead of on bare metal. Accordingly, these can be used to detect the execution of the malware in a VM. [[2]](#2)
   * SIDT (red pill): Red Pill is an anti-VM technique that executes the SIDT instruction to grab the value of the IDTR register. The virtual machine monitor must relocate the guest's IDTR to avoid conflict with the host's IDTR. Since the virtual machine monitor is not notified when the virtual machine runs the SIDT instruction, the IDTR for the virtual machine is returned.
   * SGDT/SLDT (no pill): The No Pill technique relies on the fact that the LDT structure is assigned to a processor not an Operating System. The LDT location on a host machine will be zero and on a virtual machine will be non-zero.
   * SMSW
   * STR
   * CPUID: Checking the CPU ID found within the registry can provide information to system type.
   * IN
   * RDTSC
   * VMCPUID
   * VPCEXT
* **Check CPU Location**: When an Operating System is virtualized, the CPU is relocated. That allows a malware to detect the virtual environment. [[2]](#2)
* **Check for Memory Artifacts**: VMware leaves many artifacts in memory. Some are critical processor structures, which, because they are either moved or changed on a virtual machine, leave recognizable footprints. Malware can search through physical memory for the strings VMware, commonly used to detect memory artifacts. [[2]](#2)
* **Mac Address Detection**: VMware uses specific virtual Mac address that can be detected. The usual mac address used started with the following numbers: "00:0C:29", "00:1C:14", "00:50:56", "00:05:69". Virtualbox uses specific virtual Mac address that can be detected by Malware. The usual mac address used started with the following numbers: 08:00:27. [[2]](#2)
* **Registry Keys**: Virtual machines and emulators register artifacts in the registry, which can be detected by malware. For example, a search for "VMware" or "VBOX" in the registry might reveal keys that include information about the virtual hard drive, adapters, and virtual mouse. [[2]](#2)
* **Check Processes**: The VMware Tools use processes like VMwareServices.exe or VMwareTray.exe, to perform actions on the virtual environment. A malware can list the process and searches for the VMware string. Process related to Virtualbox can be detected by malware by query the process list. [[2]](#2)
* **Check Files**: Virtual machines create files on the file system (e.g., VMware creates files in the installation directory C:\Program Files\VMware\VMware Tools). Malware can check the different folders to find virtual machine artifacts (e.g., Virtualbox has the artifact VBoxMouse.sys). [[2]](#2)
* **Check Window Title Bars**: Injects malicious code to svchost.exe to check all open window title bar text to a list of strings indicating analysis environment.
* **Check Running Services**: VMwareService.exe runs the VMware Tools Service as a child of services.exe. It can be identified by listing services. [[2]](#2)
* **Query I/O Communication Port**: VMware uses virtual I/O ports for communication between the virtual machine and the host operating system to support functionality like copy and paste between the two systems. The port can be queried and compared with a magic number VMXh to identify the use of VMware.

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|-----------|-----------------------------|
|**GravityRAT** | May 2018 | GravityRAT checks system temperature by recording thermal readings for detecting VMs. Heat levels indicate whether the system is a VM. [[3]](#3)| 
|**WebCobra** | 2018 | WebCobra injects malicious code to svchost.exe and uses an infinite loop to check all open windows and to compare each window’s title bar text with a set of strings to determine whether it is running in an isolated, malware analysis environment [[4]](#4)|

References
----------
<a name="1">[1]</a> https://www.fireeye.com/blog/threat-research/2011/01/the-dead-giveaways-of-vm-aware-malware.html 

<a name="2">[2]</a> http://unprotect.tdgt.org/index.php/Sandbox_Evasion

<a name="3">[3]>/a> https://www.hackread.com/gravityrat-malware-evades-detection-targets-india/
 
<a name="4">[4]</a> https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/
