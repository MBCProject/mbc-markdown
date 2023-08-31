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
<td><b>17 August 2023</b></td>
</tr>
</table>


# Process Injection

Malware may execute code in the address space of a separate process. 

See ATT&CK: **Process Injection ([T1055](https://attack.mitre.org/techniques/T1055/), [T1631](https://attack.mitre.org/techniques/T1631/))**.

The methods table includes existing ATT&CK sub-techniques, which have been enhanced with malware-specific details, as well as new methods. Note that IAT hooking and inline hooking (aka userland rootkits) are defined as methods under the [Hijack Execution Flow](../defense-evasion/hijack-execution-flow.md) behavior. 

## Methods

|Name|ID|Description|
|---|---|---|
|**Dynamic-link Library Injection**|E1055.001|(Enhanced ATT&CK sub-technique) Malware creates a thread using CreateRemoteThread (or NtCreateThreadEx, RtlCreateUserThread) and LoadLibrary. The path to the malware's malicious dynamic-link library (DLL) is written in the virtual address space of another process; the malware ensures the remote process loads it by creating a remote thread in the target process. This is one of the most common process injection methods, called *Classic DLL Injection via CreateRemoteThread and LoadLibrary* in [[1]](#1). This method is related to Unprotect technique U1226.|
|**Portable Executable Injection**|E1055.002|(Enhanced ATT&CK sub-technique) Malware copies its malicious code into an existing open process and causes it to execute via shellcode or by calling CreateRemoteThread (instead of passing the address of the LoadLibrary), called *Portable Executable Injection* in [[1]](#1). This method is related to Unprotect technique U1216.|
|**Thread Execution Hijacking**|E1055.003|(Enhanced ATT&CK sub-technique) Malware targets an existing thread of a process, avoiding noisy process or thread creations operations, called *Thread Execution Hijacking* in [[1]](#1). This method is related to Unprotect technique U1223.|
|**Asynchronous Procedure Call**|E1055.004|(Enhanced ATT&CK sub-technique) Malware may leverage Asynchronous Procedure Calls (APC) to force another thread to execute its code by attaching it to the APC Queue of the target thread (using QueueUserAPC / NtQueueApcThread). AtomBombing [[1]](#1)[[3]](#3), a variant of APC injection, occurs when the attacker stores malicious code in the global atom table. The APC gets the targeted process to retrieve the code that will be injected to the memory of the targeted process. This method is related to Unprotect technique U1221 and U1220.|
|**Extra Window Memory Injection**|E1055.011|(Enhanced ATT&CK sub-technique) Malware may inject into Explorer tray window’s extra window memory, called *Extra Window Memory Injection* in [[1]](#1). This method is related to Unprotect technique U1219.|
|**Process Hollowing**|E1055.012|(Enhanced ATT&CK sub-technique) Instead of injecting code into a program, malware can upmap (hollow out) legitimate code from memory of a target process, overwriting it with a malicious executable, called *Process Hollowing* in [[1]](#1). This method is related to Unprotect technique U1225.|
|**Hook Injection via SetWindowsHooksEx**|E1055.m01|Malware can leverage hooking functionality to have its malicious DLL loaded upon an event getting triggered in a specific thread, which is usually done by calling SetWindowsHookEx to install a hook routine into the hook chain. [[1]](#1) This method is related to Unprotect technique 1227.|
|**Injection and Persistence via Registry Modification**|E1055.m02|Malware may insert the location of its malicious library under a registry key (e.g., Appinit_DLL, AppCertDlls, IFEO) to have another process load its library. [[1]](#1)|
|**Injection via Windows Fibers**|E1055.m05|Malware executes shellcode via Windows fibers by converting a thread to a fiber. [[5]](#5)|
|**Injection using Shims**|E1055.m03|Malware may use shims to target an executable (shims are a way of hooking into APIs and targeting specific executables and are provided by Microsoft for backward compatibility, allowing developers to apply program fixes without rewriting code). [[1]](#1) This method is related to Unprotect technique U1218.|
|**Patch Process Command Line**|E1055.m04|Malware patches the PEB of a process to spoof the arguments.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**UP007**](../xample-malware/up007.md)|2016|E1055.001|The malware loads multiple DLLs into memory. [[4]](#4)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|--|The malware injects itself into svchost.exe. [[11]](#11)|
|[**Poison Ivy**](../xample-malware/poison-ivy.md)|2005|--|Poison Ivy code is injected into explorer.exe. [[2]](#2)|
|[**WebCobra**](../xample-malware/webcobra.md)|2018|--|The malware injects miner code into a running process. [[12]](#12)|
|[**CryptoWall**](../xample-malware/cryptowall.md)|2014|--|The malware injects code into a new svchost process. [[6]](#6)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|The malware injects itself into processes such as cmd.exe and notepad.exe [[7]](#7)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|E1055.012|The malware uses process replacement. [[13]](#13)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|E1055.m05|BlackEnergy bypasses UAC using a Shim Database instructing SndVol.exe to execute cmd.exe instead, allowing for elevated execution. [[8]](#8)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|--|BlackEnergy injects its dll component into svchost.exe. [[8]](#8)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|E1055.001|Stuxnet injects the entire DLL into another process and then just calls the particular export. [[9]](#9)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|E1055.m02|Stuxnet uses Mrxcls.sys driver for persistence. It is registered as a boot start service by creating the registry key HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MRxCIs\"ImagePath" = "%System%\drivers\mrxcls.sys". [[9]](#9)|
|[**Netwalker**](../xample-malware/netwalker.md)|2020|E1055.001|Netwalker uses reflective DLL loading to inject from memory. [[10]](#10)|
|[**DNSChanger**](../xample-malware/dnschanger.md)|2011|--|The malware can attach user process memory. [[13]](#13)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|E1055.003|The malware can inject threads. [[13]](#13)|


## References
<a name="1">[1]</a> Ashkan Hosseini, *Ten Process Injection Techniques: A Technical Survey of Common and Trending Process Injection Techniques*, July 2017. https://www.elastic.co/blog/ten-process-injection-techniques-technical-survey-common-and-trending-process

<a name="2">[2]</a> https://www.mandiant.com/sites/default/files/2021-09/rpt-poison-ivy.pdf

<a name="3">[3]</a> https://github.com/LordNoteworthy/al-khaser

<a name="4">[4]</a> https://citizenlab.ca/2016/04/between-hong-kong-and-burma/

<a name="5">[5]</a> https://www.ired.team/offensive-security/code-injection-process-injection/executing-shellcode-with-createfiber

<a name="6">[6]</a> https://news.sophos.com/en-us/2015/12/17/the-current-state-of-ransomware-cryptowall/

<a name="7">[7]</a> https://www.f-secure.com/v-descs/backdoor_w32_hupigon.shtml

<a name="8">[8]</a> https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf

<a name="9">[9]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en

<a name="10">[10]</a> https://www.trendmicro.com/en_us/research/20/e/netwalker-fileless-ransomware-injected-via-reflective-loading.html

<a name="11">[11]</a> https://www.cybereason.com/blog/research/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware

<a name="12">[12]</a> https://www.mcafee.com/blogs/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/

<a name="13">[13]</a> capa v4.0, analyzed at MITRE on 10/12/2022
