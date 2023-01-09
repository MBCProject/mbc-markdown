<table>
<tr>
<td><b>ID</b></td>
<td><b>B0001</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../anti-behavioral-analysis">Anti-Behavioral Analysis</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
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
<td><b>21 November 2022</b></td>
</tr>
</table>


# Debugger Detection

Malware detects whether it's being executed inside a debugger. If so, conditional execution selects a benign execution path. [[1]](#1), [[2]](#2)

Details on methods of detecting debuggers are given in the references; many are listed below.

## Methods

|Name|ID|Description|
|---|---|---|
|**API Hook Detection**|B0001.001|Module bounds based [[7]](#7).|
|**Anti-debugging Instructions**|B0001.034|Malware code contains mnemonics related to anti-debugging (e.g., rdtsc, icebp).|
|**CheckRemoteDebuggerPresent**|B0001.002|The kernel32!CheckRemoteDebuggerPresent function calls NtQueryInformationProcess with ProcessInformationClass parameter set to 7 (ProcessDebugPort constant).|
|**Check Processes**|B0001.038|The malware may check running processes for specific strings such as "malw" to detect a analysis environment.|
|**CloseHandle**|B0001.003|(NtClose); If an invalid handle is passed to the CloseHandle function and a debugger is present, then an EXCEPTION_INVALID_HANDLE (0xC0000008) exception will be raised. [[7]](#7)|
|**Debugger Artifacts**|B0001.004|Malware may detect a debugger by its artifact (window title, device driver, exports, etc.).|
|**Hardware Breakpoints**|B0001.005|(SEH/GetThreadContext); Debug registers will indicate the presence of a debugger. See [[7]](#7) for details.|
|**Interruption**|B0001.006|If an interruption is mishandled by the debugger, it can cause a single-byte instruction to be inadvertently skipped, which can be detected by malware. Examples include Interrupt 0x2d and Interrupt 1 [7].|
|**IsDebuggerPresent**|B0001.008|The kernel32!IsDebuggerPresent API function call checks the PEB BeingDebugged flag to see if the calling process is being debugged. It returns 1 if the process is being debugged, 0 otherwise. This is one of the most common ways of debugger detection.|
|**Memory Breakpoints**|B0001.009|(PAGE_GUARD); Guard pages trigger an exception the first time they are accessed and can be used to detect a debugger. See [[7]](#7) for details.|
|**Memory Write Watching**|B0001.010|[[7]](#7)|
|**Monitoring Thread**|B0001.011|Malware may spawn a monitoring thread to detect tampering, breakpoints, etc.|
|**NtQueryInformationProcess**|B0001.012|Calling NtQueryInformationProcess with its ProcessInformationClass parameter set to 0x07 (ProcessDebugPort constant) will cause the system to set ProcessInformation to -1 if the process is being debugged. Calling with ProcessInformationClass set to 0x0E (ProcessDebugFlags) or 0x11 (ProcessDebugObject) are used similarly. Testing "ProcessDebugPort" is equivalent to using the kernel32!CheckRemoteDebuggerPresent API call (see next method).|
|**NtQueryObject**|B0001.013|The ObjectTypeInformation and ObjectAllTypesInformation flags are checked for debugger detection.|
|**NtSetInformationThread**|B0001.014|Calling this API with a fake class length or thread handle can indicate whether it is hooked. After calling NtSetInformationThread properly, the HideThreadFromDebugger flag is checked with the NtQueryInformationThread API. [[7]](#7)|
|**NtYieldExecution/SwitchToThread**|B0001.015|[[7]](#7)|
|**OutputDebugString**|B0001.016|(GetLastError); The OutputDebugString function will demonstrate different behavior depending whether or not a debugger is present. See [[7]](#7) for details.|
|**Page Exception Breakpoint Detection**|B0001.017|[[7]](#7)|
|**Parent Process**|B0001.018|(Explorer.exe); Executing an application by a debugger will result in the parent process being the debugger process rather than the shell process (Explorer.exe) or the command line. Malware checks its parent process; if it's not explorer.exe, it's assumed to be a debugger. [[7]](#7)|
|**Process Environment Block**|B0001.019|The Process Environment Block (PEB) is a Windows data structure associated with each process that contains several fields, such as "BeingDebugged," "NtGlobalFlag," and "IsDebugged". Testing the value of this PEB field of a particular process can indicate whether the process is being debugged. Testing "BeingDebugged" is equivalent to using the kernel32!IsDebuggerPresent API call (see separate method).|
|**Process Environment Block BeingDebugged**|B0001.035|The BeingDebugged field is tested to determine whether the process is being debugged.|
|**Process Environment Block IsDebugged**|B0001.037|The IsDebugged field is tested to determine whether the process is being debugged.|
|**Process Environment Block NtGlobalFlag**|B0001.036|The NtGlobalFlag field is tested to determine whether the process is being debugged.|
|**Process Jobs**|B0001.020|[[7]](#7)|
|**ProcessHeap**|B0001.021|Process heaps are affected by debuggers. Malware can detect a debugger by checking heap header fields such as Flags (debugger present if value greater than 2) or ForceFlags (debugger present if value greater than 0).|
|**RtlAdjustPrivilege**|B0001.022|Malware may call RtlAdjustPrivilege to detect if a debugger is attached (or to prevent a debugger from attaching).|
|**SeDebugPrivilege**|B0001.023|(Csrss.exe); Using the OpenProcess function on the csrss.exe process can detect a debugger. [[7]](#7)|
|**SetHandleInformation**|B0001.024|(Protected Handle)|
|**Software Breakpoints**|B0001.025|(INT3/0xCC)|
|**Stack Canary**|B0001.026|Similar to the anti-exploitation method of the same name, malware may try to detect mucking with values on the stack.|
|**TIB Aware**|B0001.027|Malware may access information in the Thread Information Block (TIB) for debug detection or process obfuscation detection. The TIB can be accessed as an offset of the segment register (e.g., fs:[20h]).|
|**TLS Callbacks**|B0001.029|[[7]](#7)|
|**Timing/Delay Check**|B0001.028|Malware may compare time between two points to detect unusual execution, such as the (relative) massive delays introduced by debugging.|
|**Timing/Delay Check GetTickCount**|B0001.032|Malware uses GetTickCount function in a timing/delay check.|
|**Timing/Delay Check QueryPerformanceCounter**|B0001.033|Malware uses QueryPerformanceCounter in a timing/delay check.|
|**UnhandledExceptionFilter**|B0001.030|The UnhandledExceptionFilter function is called if no registered exception handlers exist, but it will not be reached if a debugger is present. See [[7]](#7) for details.|
|**WudfIsAnyDebuggerPresent**|B0001.031|Includes use of WudfIsAnyDebuggerPresent, WudfIsKernelDebuggerPresent, WudfIsUserDebuggerPresent.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Redhip**](../xample-malware/rebhip.md)|January 2011|B0001, B0001.035, B0001.032|Please see the Redhip malware page for details. [[4]](#4)|
|[**Gamut**](../xample-malware/gamut.md)|2014|B0001.006, B0001.008|Please see the Gamut malware page for details. [[8]](#8)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|B0001.016, B0001.038, B0001.032|Please see the Rombertik malware page for details. [[9]](#9)|
|[**Poison-Ivy**](../xample-malware/poison-ivy.md)|2005|B0001.005, B0001.008|Please see the Poison-Ivy malware page for details. [[10]](#10)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|B0001.032|Check for time delay via GetTickCount (This capa rule had 4 matches) [[11]](#11)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|B0001.034, B0001.025, B0001.032|Please see the Hupigon malware page for details. [[11]](#11)|
|[**UP007 Malware Family**](../xample-malware/up007.md)|2016|B0001.032|Check for time delay via GetTickCount (This capa rule had 1 match) [[11]](#11)|
|[**Ursnif**](../xample-malware/ursnif.md)|2016|B0001.028|Manipulates TLS Callbacks while injecting to child process [[12]](#12)|

## References

<a name="1">[1]</a> Alexander Antukh, "Anti-debugging Techniques Cheat Sheet," 19 January 2015.  http://antukh.com/blog/2015/01/19/malware-techniques-cheat-sheet. 

<a name="2">[2]</a> Joshua Cannell, Malwarebytes Labs, "Five Anti-Analysis Tricks that sometimes Fool Analysts," 31 March 2016. https://blog.malwarebytes.com/threat-analysis/2014/09/five-anti-debugging-tricks-that-sometimes-fool-analysts.

<a name="3">[3]</a> Peter Ferrie, "The 'Ultimate' Anti-Debugging Reference," 4 May 2011. https://anti-reversing.com/Downloads/Anti-Reversing/The_Ultimate_Anti-Reversing_Reference.pdf.

<a name="4">[4]</a> Atif Mushtaq, FireEye, "The Dead Giveaways of VM-Aware Malware," 27 January 2011. https://www.fireeye.com/blog/threat-research/2011/01/the-dead-giveaways-of-vm-aware-malware.html. 

<a name="5">[5]</a> Ayoub Faouzi (LordNoteworthy), Al-Khaser v0.79. https://github.com/LordNoteworthy/al-khaser

<a name="6">[6]</a> Nicolas Falliere, Symantec, "Windows Anti-Debug Reference," 11 September 2007. https://www.symantec.com/connect/articles/windows-anti-debug-reference.

<a name="7">[7]</a> Anti Debugging Tricks, Al-Khaser. https://github.com/LordNoteworthy/al-khaser/wiki/Anti-Debugging-Tricks

<a name="8">[8]</a> https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/gamut-spambot-analysis/

<a name="9">[9]</a> https://blogs.cisco.com/security/talos/rombertik

<a name="10">[10]</a> https://www.mandiant.com/sites/default/files/2021-09/rpt-poison-ivy.pdf

<a name="11">[11]</a> capa v4.0, analyzed at MITRE on 10/12/2022

<a name="12">[12]</a> https://www.fireeye.com/blog/threat-research/2017/11/ursnif-variant-malicious-tls-callback-technique.html

