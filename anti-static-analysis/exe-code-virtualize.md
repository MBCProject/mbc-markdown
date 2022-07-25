|||
|---|---|
|**ID**|**B0008**|
|**Objective(s)**|[Anti-Behavioral Analysis](../anti-behavioral-analysis), [Anti-Static Analysis](../anti-static-analysis)|
|**Related ATT&CK Technique**|None|


Executable Code Virtualization
==============================
Original executable code is virtualized by translating the code into a special format that only a special virtual machine (VM) can run; the VM uses a customized virtual instruction set. A "stub" function calls the VM when the code is run. Virtualized code makes static analysis and reverse engineering more difficult; dumped code won’t run without the VM.

Virtualized code is a software protection technique. Themida is a commercial tool; VMProtect is an open source tool. [[1]](#1) 

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Multiple VMs**|B0008.001|Multiple virtual machines with different architectures (CISC, RISC, etc.) can be used inside of a single executable in order to make reverse engineering even more difficult.|

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**Locky Bart**](../xample-malware/locky-bart.md)|January 2017|Code virtualization is added to the Locky Bart binary using WPProtect. [[2]](#2)|

References
----------
<a name="1">[1]</a> https://github.com/xiaoweime/WProtect

<a name="2">[2]</a> https://blog.malwarebytes.com/threat-analysis/2017/01/locky-bart-ransomware-and-backend-server-analysis/
