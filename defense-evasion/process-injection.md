<table>
<tr>
<td><b>ID</b></td>
<td><b>E1055</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../defense-evasion">Defense Evasion</a>, <a href="../privilege-escalation">Privilege Escalation</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Process Injection (<a href="https://attack.mitre.org/techniques/T1055">T1055</a>, <a href="https://attack.mitre.org/techniques/T1631/">T1631</a>)</b></td>
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


# Process Injection

Malware may execute code in the address space of a separate process. 

See ATT&CK: **Process Injection ([T1055](https://attack.mitre.org/techniques/T1055/), [T1631](https://attack.mitre.org/techniques/T1631/))**. Notes on ATT&CK's sub-techniques in the context of [[1]](#1) are as follows:

|ID|ATT&CK Sub-Technique|Notes|
|---|---|---|
|E1055.001|Dynamic-link Library Injection|Malware creates a thread using CreateRemoteThread (or NtCreateThreadEx, RtlCreateUserThread) and LoadLibrary. The path to the malware's malicious dynamic-link library (DLL) is written in the virtual address space of another process; the malware ensures the remote process loads it by creating a remote thread in the target process. This is one of the most common process injection methods. Called *Classic DLL Injection via CreateRemoteThread and LoadLibrary* in [[1]](#1).|
|E1055.002|Portable Executable Injection|Malware copies its malicious code into an existing open process and causes it to execute via shellcode or by calling CreateRemoteThread (instead of passing the address of the LoadLibrary). Called *Portable Executable Injection* in [[1]](#1).|
|E1055.003|Thread Execution Hijacking|Malware targets an existing thread of a process, avoiding noisy process or thread creations operations. Called *Thread Execution Hijacking* in [[1]](#1).|
|E1055.004|Asynchronous Procedure Call|Malware may leverage Asynchronous Procedure Calls (APC) to force another thread to execute its code by attaching it to the APC Queue of the target thread (using QueueUserAPC / NtQueueApcThread); also called AtomBombing [[3]](#3). Called *APC Injection and AtomBombing* in [[1]](#1).|
|E1055.011|Extra Window Memory Injection|Malware may inject into Explorer tray window’s extra window memory. Called *Extra Window Memory Injection* in [[1]](#1).|
|E1055.012|Process Hollowing|Instead of injecting code into a program, malware can upmap (hollow out) legitimate code from memory of a target process, overwriting it with a malicious executable. Called *Process Hollowing* in [[1]](#1).|

Methods not captured by ATT&CK Process Injection sub-techniques are listed below. Note that IAT hooking and inline hooking (aka userland rootkits) are defined as methods under the [Hooking](../credential-access/hooking.md) behavior.

## Methods

|Name|ID|Description|
|---|---|---|
|**Hook Injection via SetWindowsHooksEx**|E1055.m01|Malware can leverage hooking functionality to have its malicious DLL loaded upon an event getting triggered in a specific thread, which is usually done by calling SetWindowsHookEx to install a hook routine into the hook chain. [[1]](#1)|
|**Injection and Persistence via Registry Modification**|E1055.m02|Malware may insert the location of its malicious library under a registry key (e.g., Appinit_DLL, AppCertDlls, IFEO) to have another process load its library. [[1]](#1)|
|**Injection via Windows Fibers**|E1055.m05|Malware executes shellcode via Windows fibers by converting a thread to a fiber. [[5]](#5)|
|**Injection using Shims**|E1055.m03|Malware may use shims to target an executable (shims are a way of hooking into APIs and targeting specific executables and are provided by Microsoft for backward compatibility, allowing developers to apply program fixes without rewriting code). [[1]](#1)|
|**Patch Process Command Line**|E1055.m04|Malware patches the PEB of a process to spoof the arguments.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**UP007**](../xample-malware/up007.md)|2016|E1055.001|The malware loads multiple DLLs into memory. [[4]](#4)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|--|The malware injects itself into svchost.exe. [[11]](#11)|
|[**Poison-Ivy**](../xample-malware/poison-ivy.md)|2005|--|Poison-Ivy code is injected into explorer.exe. [[2]](#2)|
|[**WebCobra**](../xample-malware/webcobra.md)|2018|--|Injects minor code into a running process.|
|[**CryptoWall**](../xample-malware/cryptowall.md)|2014|--|The malware injects code into a new svchost process. [[6]](#6)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|The malware injects itself into processes such as cmd.exe, notepad.exe [[7]](#7)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|--|Bypasses UAC using a Shim Database instructing SndVol.exe to execute cmd.exe instead, allowing for elevated execution. BlackEnergy injects its dll component into svchost.exe. [[8]](#8)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|E1055.001|Stuxnet injects the entire DLL into another process and then just calls the particular export  [[9]](#9)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|E1055.m02|The driver Stuxnet uses for persistence Mrxcls.sys is registered as a boot start service creating the registry key HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MRxCIs"ImagePath" = "%System%\drivers\mrxcls.sys." [[9]](#9)|
|[**Netwalker**](../xample-malware/netwalker.md)|2020|--|Netwalker uses reflective DLL loading to inject from memory [[10]](#10)|


## References

<a name="1">[1]</a> Ashkan Hosseini, *Ten Process Injection Techniques: A Technical Survey of Common and Trending Process Injection Techniques*, July 2017. https://www.elastic.co/blog/ten-process-injection-techniques-technical-survey-common-and-trending-process

<a name="2">[2]</a> https://www.cyber.nj.gov/threat-profiles/trojan-variants/poison-ivy

<a name="3">[3]</a> https://github.com/LordNoteworthy/al-khaser

<a name="4">[4]</a> https://citizenlab.ca/2016/04/between-hong-kong-and-burma/

<a name="5">[5]</a> https://www.ired.team/offensive-security/code-injection-process-injection/executing-shellcode-with-createfiber

<a name="6">[6]</a> https://news.sophos.com/en-us/2015/12/17/the-current-state-of-ransomware-cryptowall/

<a name="7">[7]</a> https://www.f-secure.com/v-descs/backdoor_w32_hupigon.shtml

<a name="8">[8]</a> https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf

<a name="9">[9]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en

<a name="10">[10]</a> https://www.trendmicro.com/en_us/research/20/e/netwalker-fileless-ransomware-injected-via-reflective-loading.html

<a name="11">[11]</a> https://www.cybereason.com/blog/research/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware
