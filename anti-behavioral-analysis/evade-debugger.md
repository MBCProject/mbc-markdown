|||
|---------|------------------------|
|**ID**|**M0002**|
|**Objective(s)**|[Anti-Behavioral Analysis](https://github.com/MAECProject/malware-behaviors/tree/master/anti-behavioral-analysis)|
|**Related ATT&CK Technique(s)**|None|


Debugger Evasion
================
Behaviors that make debugging difficult.

A thorough reference for anti-debugging, both detection and evasion, is given in [[1]](#1).

Methods
-------
* **Block Interrupts**: Block interrupt (via hooking) 1 and/or 3 to prevent debuggers from working.
* **Break Point Clearing**: Intentionally clearing software or hardware breakpoints.
* **Byte Stealing**: Move or copy the first bytes / instructions of the original code elsewhere. AKA stolen bytes or code splicing. For example, a packer may incorporate the first few instructions of the original EntryPoint (EP) into its unpacking stub before the tail transition in order to confuse automated unpackers and novice analysts. This can make it harder for rebuilding and may bypass breakpoints if set prematurely.
* **Change SizeOfImage**: Changinging this value during run time can prevent some debuggers from attaching. Also confuses some unpackers and dumpers.
* **Code Integrity Check**: Check that the unpacking code is unmodified. Variation exists where unpacking code is part of the “key” used to unpack, therefore any Software Breakpoints during debugging causes unpacking to completely fail or result in malformed unpacked code.
* **Exception Misdirection**: Using exception handling (SEH) to cause flow of program to non-obvious paths.
* **Get Base Indirectly**: CALL to a POP; finds base of code or data, often the packed version of the code; also used often in obfuscated/packed shellcode.
* **Guard Pages**: Encrypt blocks of code individually and decrypt temporarily only upon execution.
* **Hook File System**: execution happens when a particular file or directory is accessed, often through hooking certain API calls such as CreateFileA and CreateFileW.
* **Hook Interrupt**: modification of interrupt vector or descriptor tables.
* **Import Obfuscation**: Add obfuscation between imports calls and APIs.
* **Inlining**: variation of static linking where full API code inserted everywhere it would have been called.
* **Loop Escapes**: Use SEH or other methods to break out of a loop instead of a conditional jump.
* **Malloc Use**: Instead of unpacking into a pre-defined section/segment (ex: .text) of the binary, use malloc() / VirtualAlloc() to create a new segment. This makes keeping track of memory locations across different runs more difficult, as there is no guarantee that malloc/VirtualAlloc will assign the same address range each time.
* **Modify PE Header**: Any part of the header is changed or erased.
* **Nanomites**: int3 with code replacement table; debugs itself.
* **Obfuscate Library Use**: LoadLibrary API calls or direct access of kernel32 via PEB (fs[0]) pointers, used to rebuild IAT or just obfuscate library use.
* **Parallel Threads**: Use several parallel threads to make analysis harder.
* **Pipeline Misdirection**: Take advantage of pipelining in modern processors to misdirect debugging, emulation, or static analysis tools. An unpacker can assume a certain number of opcodes will be cached and then proceed to overwrite them in memory, causing a debugger/emulator/analyzer to follow different code than is normally executed.
* **Pre-Debug**: Prevents debugger from attaching to process or to break until after the code of interest has been executed
* **Relocate API Code**: relocate API code in separate buffer (calls don’t lead to imported DLLs).
* **Return Obfuscation**: Overwrite the RET address on the stack or the code at the RET address. Variation seen that writes to the start-up code or main module that called the malware's WinMain or DllMain.
* **RtlAdjustPrivilege**: Calling RtlAdjustPrivilege to either prevent a debugger from attaching or to detect if a debugger is attached.
* **Section Misalignment**: Some analysis tools cannot handle binaries with misaligned sections.
* **Self-Debugging**: Debug itself to prevent another debugger to be attached.
* **Self-Unmapping**: UnmapViewOfFile() on itself
* **Static Linking**: Copy locally the whole content of API code.
* **Stolen API Code**: A variation of “byte stealing” where the first few instructions or bytes of an API are executed in user code, allowing the IAT to point into the middle of an API function. This confuses IAT rebuilders such as ImpRec and Scylla and may bypass breakpoints.
* **Tampering**: Erase or corrupt specific file parts to prevent rebuilding (header, packer stub, etc.).
* **Thread Timeout**: Setting dwMilliseconds in WaitForSingleObject to a small number will timeout the thread before the analyst can step through and analyze the code executing in the thread. Modifying this via patch, register, or stack to the value `0xFFFFFFFF`, the **INFINITE** constant circumvents this anti-debugging technique.
* **TIB Aware**: Accessing thread information (fs:[20h]) for debug detection or process obfuscation.
* **Use Interrupts**: The unpacking code relies on use of int 1 or int 3, or it uses the interrupt vector table as part of the decryption “key”.

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|
|Fake Adobe Flash Update OS X | February 2016| [[2]](#2)|
|Dridex| March 2015| [[3]](#3)|

References
----------
<a name="1">[1]</a> https://anti-reversing.com/Downloads/Anti-Reversing/The_Ultimate_Anti-Reversing_Reference.pdf

<a name="2">[2]</a> https://www.synack.com/2016/02/17/analyzing-the-anti-analysis-logic-of-an-adware-installer/

<a name="3">[3]</a> http://phishme.com/dridex-code-breaking-modify-the-malware-to-bypass-the-vm-bypass/

<a name="4">[4]</a> http://antukh.com/blog/2015/01/19/malware-techniques-cheat-sheet/

<a name="5">[5]</a> http://unprotect.tdgt.org/index.php/Unprotect_Project
 
