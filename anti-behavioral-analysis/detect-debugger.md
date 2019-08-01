|||
|---------|------------------------|
|**ID**|**M0001**|
|**Objective(s)**|[Anti-Behavioral Analysis](https://github.com/MAECProject/malware-behaviors/tree/master/anti-behavioral-analysis)|
|**Related ATT&CK Technique(s)**|None|


Debugger Detection
==================
Detects whether the malware instance is being executed inside of a debugger. If so, conditional execution selects a benign execution path. [[1]](#1), [[2]](#2)

A thorough reference for anti-debugging, both detection and evasion, is given in [[3]](#3).

Methods
-------
* **Debugger Artifacts**: Detects a debugger by its artifact (window title, device driver, exports, etc.).
* **Monitoring Thread**: Spawn a monitoring thread to detect tampering, breakpoints, etc.
* **Process Environment Block**: The Process Environment Block (PEB) is a Windows data structure associated with each process that contains several fields, one of which is "BeingDebugged". Testing the value of this PEB field of a particular process can indicate whether the process is being debugged; this is equivalent to using the kernel32!IsDebuggerPresent API call (see next method).
* **API Call: IsDebuggerPresent**: The IsDebuggerPresent API call checks the PEB to see if the calling process is being debugged. This is one of the most basic and common ways of detecting debugging.
* **Timing/Delay Checks**: Comparing time between two points to detect unusual execution, such as the (relative) massive delays introduced by debugging. 
* **Stack Canary**: Similar to the anti-exploitation method of the same name, malware may try to detect mucking with values on the stack.
* **TIB Aware**: Accessing thread information (e.g., fs:[20h]) for debug detection or process obfuscation.
* **RtlAdjustPrivilege**: Calling RtlAdjustPrivilege to either prevent a debugger from attaching or to detect if a debugger is attached.
* **Interrupt 2D**: If int 0x2d is mishandled by the debugger, it can cause a single-byte instrustion to be inadvertently skipped, which can be detected by the malware.

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|
|[**Redhip**](https://github.com/MAECProject/malware-behaviors/tree/master/xample-malware/redhip.md) | January 2011 |Redhip uses general approaches to detecting user level debuggers (e.g., Process Environment Block 'Being Debugged' field), as well as specific checks for kernel level debuggers like SOFICE. [[4]](#4)|

References
----------
<a name="1">[1]</a> http://antukh.com/blog/2015/01/19/malware-techniques-cheat-sheet/ 

<a name="2">[2]</a> https://blog.malwarebytes.com/threat-analysis/2014/09/five-anti-debugging-tricks-that-sometimes-fool-analysts/

<a name="3">[3]</a> https://anti-reversing.com/Downloads/Anti-Reversing/The_Ultimate_Anti-Reversing_Reference.pdf

<a name="4">[4]</a> https://www.fireeye.com/blog/threat-research/2011/01/the-dead-giveaways-of-vm-aware-malware.html 
 
