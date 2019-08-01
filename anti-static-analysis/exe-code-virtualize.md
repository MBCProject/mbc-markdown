|||
|---------|------------------------|
|**ID**|**M0008**|
|**Objective(s)**| [Anti-Behavioral Analysis](https://github.com/MAECProject/malware-behaviors/tree/master/anti-behavioral-analysis), [Anti-Static Analysis](https://github.com/MAECProject/malware-behaviors/tree/master/anti-static-analysis)|
|**Related ATT&CK Technique(s)**|None|


Executable Code Virtualization
==============================
Original executable code is virtualized by translating the code into a special format that only a special virtual machine (VM) can run; the VM uses a customized virtual instruction set. A "stub" function calls the VM when the code is run. Virtualized code makes static analysis and reverse engineering more difficult; dumped code won’t run without the VM.

Virtualized code is a software protection technique. Themida is a commercial tool; WPProtect is an open source tool. [[1]](#1) 

Methods
-------
* **Multiple VMs**: multiple virtual machines with different architectures (CISC, RISC, etc.) can be used inside of a single executable in order to make reverse engineering even more difficult.

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|
| Locky Bart | January 2017 | Code virtualization is added to the Locky Bart binary using WPProtect. [[2]](#2)

References
----------
<a name="1">[1]</a> https://github.com/xiaoweime/WProtect

<a name="2">[2]</a> https://blog.malwarebytes.com/threat-analysis/2017/01/locky-bart-ransomware-and-backend-server-analysis/
