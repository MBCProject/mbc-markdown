|||
|---------|------------------------|
|**ID**|**B0002**|
|**Objective(s)**|[Anti-Behavioral Analysis](https://github.com/MBCProject/mbc-markdown/tree/master/anti-behavioral-analysis)|
|**Related ATT&CK Technique**|None|


Debugger Evasion
================
Behaviors that make debugging difficult.

A thorough reference for anti-debugging, both detection and evasion, is given in [[1]](#1).

Methods
-------
|ID|Name|Description|
|-----------------------------|--------|-----------------------------|
|B0002.001|**Block Interrupts**|Block interrupt (via hooking) 1 and/or 3 to prevent debuggers from working.|
|B0002.002|**Break Point Clearing**|Intentionally clearing software or hardware breakpoints.|
|B0002.003|**Byte Stealing**|Move or copy the first bytes / instructions of the original code elsewhere. AKA stolen bytes or code splicing. For example, a packer may incorporate the first few instructions of the original EntryPoint (EP) into its unpacking stub before the tail transition in order to confuse automated unpackers and novice analysts. This can make it harder for rebuilding and may bypass breakpoints if set prematurely.|
|B0002.004|**Change SizeOfImage**|Changinging this value during run time can prevent some debuggers from attaching. Also confuses some unpackers and dumpers.|
|B0002.005|**Code Integrity Check**|Check that the unpacking code is unmodified. Variation exists where unpacking code is part of the "key" used to unpack, therefore any Software Breakpoints during debugging causes unpacking to completely fail or result in malformed unpacked code.|
|B0002.006|**Exception Misdirection**|Using exception handling (SEH) to cause flow of program to non-obvious paths.|
|B0002.007|**Get Base Indirectly**|CALL to a POP; finds base of code or data, often the packed version of the code; also used often in obfuscated/packed shellcode.|
|B0002.008|**Guard Pages**|Encrypt blocks of code individually and decrypt temporarily only upon execution.|
|B0002.009|**Hook Interrupt**|Modification of interrupt vector or descriptor tables.|
|B0002.010|**Import Obfuscation**: Add obfuscation between imports calls and APIs.|
|B0002.011|**Inlining**|Variation of static linking where full API code inserted everywhere it would have been called.|
|B0002.012|**Loop Escapes**|Use SEH or other methods to break out of a loop instead of a conditional jump.|
|B0002.013|**Malloc Use**|Instead of unpacking into a pre-defined section/segment (ex: .text) of the binary, use malloc() / VirtualAlloc() to create a new segment. This makes keeping track of memory locations across different runs more difficult, as there is no guarantee that malloc/VirtualAlloc will assign the same address range each time.|
|B0002.014|**Modify PE Header**|Any part of the header is changed or erased.|
|B0002.015|**Nanomites**|int3 with code replacement table; debugs itself.|
|B0002.016|**Obfuscate Library Use**|LoadLibrary API calls or direct access of kernel32 via PEB (fs[0]) pointers, used to rebuild IAT or just obfuscate library use.|
|B0002.017|**Parallel Threads**|Use several parallel threads to make analysis harder.|
|B0002.018|**Pipeline Misdirection**|Take advantage of pipelining in modern processors to misdirect debugging, emulation, or static analysis tools. An unpacker can assume a certain number of opcodes will be cached and then proceed to overwrite them in memory, causing a debugger/emulator/analyzer to follow different code than is normally executed.|
|B0002.019|**Pre-Debug**|Prevents debugger from attaching to process or to break until after the code of interest has been executed.|
|B0002.020|**Relocate API Code**|Relocate API code in separate buffer (calls don’t lead to imported DLLs).|
|B0002.021|**Return Obfuscation**|Overwrite the RET address on the stack or the code at the RET address. Variation seen that writes to the start-up code or main module that called the malware's WinMain or DllMain.|
|B0002.022|**RtlAdjustPrivilege**|Calling RtlAdjustPrivilege to either prevent a debugger from attaching or to detect if a debugger is attached.|
|B0002.023|**Section Misalignment**|Some analysis tools cannot handle binaries with misaligned sections.|
|B0002.024|**Self-Debugging**|Debug itself to prevent another debugger to be attached.|
|B0002.025|**Self-Unmapping**|UnmapViewOfFile() on itself.|
|B0002.026|**Static Linking**|Copy locally the whole content of API code.|
|B0002.027|**Stolen API Code**|A variation of "byte stealing" where the first few instructions or bytes of an API are executed in user code, allowing the IAT to point into the middle of an API function. This confuses IAT rebuilders such as ImpRec and Scylla and may bypass breakpoints.|
|B0002.028|**Tampering**|Erase or corrupt specific file parts to prevent rebuilding (header, packer stub, etc.).|
|B0002.029|**Thread Timeout**|Setting dwMilliseconds in WaitForSingleObject to a small number will timeout the thread before the analyst can step through and analyze the code executing in the thread. Modifying this via patch, register, or stack to the value `0xFFFFFFFF`, the **INFINITE** constant circumvents this anti-debugging technique.|
|B0002.030|**Use Interrupts**|The unpacking code relies on use of int 1 or int 3, or it uses the interrupt vector table as part of the decryption "key".|

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|
|**Fake Adobe Flash Update OS X**|February 2016|[[2]](#2)|
|**Dridex**|March 2015|[[3]](#3)|
|[**Redhip**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/redhip.md)|2011|Redhip uses general approaches to detecting user level debuggers (e.g., Process Environment Block 'Being Debugged' field), as well as specific checks for kernel level debuggers like SOFICE. [[6]](#6)|

References
----------
<a name="1">[1]</a> https://anti-reversing.com/Downloads/Anti-Reversing/The_Ultimate_Anti-Reversing_Reference.pdf

<a name="2">[2]</a> https://www.synack.com/2016/02/17/analyzing-the-anti-analysis-logic-of-an-adware-installer/

<a name="3">[3]</a> http://phishme.com/dridex-code-breaking-modify-the-malware-to-bypass-the-vm-bypass/

<a name="4">[4]</a> http://antukh.com/blog/2015/01/19/malware-techniques-cheat-sheet/

<a name="5">[5]</a> http://unprotect.tdgt.org/index.php/Unprotect_Project
 
<a name="6">[6]</a> https://www.fireeye.com/blog/threat-research/2011/01/the-dead-giveaways-of-vm-aware-malware.html 