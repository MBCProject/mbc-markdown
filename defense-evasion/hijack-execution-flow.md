<table>
<tr>
<td><b>ID</b></td>
<td><b>F0015</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../anti-behavioral-analysis">Anti-Behavioral Analysis</a>, <a href="../collection">Collection</a>, <a href="../credential-access">Credential Access</a>, <a href="../defense-evasion">Defense Evasion</a>, <a href="../persistence">Persistence</a>, <a href="../privilege-escalation">Privilege Escalation</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Hijack Execution Flow (<a href="https://attack.mitre.org/techniques/T1574">T1574</a>, <a href="https://attack.mitre.org/techniques/T1625">T1625</a>)</b></td>
</tr>
<tr>
<td><b>Anti-Analysis Type</b></td>
<td><b>Evasion</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>8 November 2021</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>21 November 2022</b></td>
</tr>
</table>


# Hijack Execution Flow

Malware may execute by hijacking the way operating systems run programs. Malware (e.g. rootkit) alters API behavior or redirects execution (i.e., hooking) to a malicious API version for a variety of purposes. Malware may use hooking to load and execute code within the context of another process, hiding execution and gaining elevated privileges and access to the process's memory. Different types of hooking are defined as methods below.

Note that in MBC, Hooking is also associated with the [Defense Evasion](../defense-evasion), [Persistence](../persistence), [Privilege Escalation](../privilege-escalation), and [Anti-Behavioral Analysis](../anti-behavioral-analysis) objectives.

For discussion related to the Credential Access and Collection objectives, see **Input Capture: Credential API Hooking ([T1056.004](https://attack.mitre.org/techniques/T1056/004/))**.

For hooking related to memory dump evasion, see **Memory Dump Evasion ([B0006](../anti-behavioral-analysis/memory-dump-evasion.md))**.

See ATT&CK: **Hijack Execution Flow ([T1574](https://attack.mitre.org/techniques/T1574), [T1625](https://attack.mitre.org/techniques/T1625))**.

## Methods

|Name|ID|Description|
|---|---|---|
|**Abuse Windows Function Calls**|F0015.006|Malware abuses native Windows function calls to transfer execution to shellcode that it loads into memory. A pointer to the callback function is used to supply the memory address of the shellcode. Functions that can be abused include EnumResourceTypesA and EnumUILanguagesW. [[4]](#4)|
|**Export Address Table Hooking**|F0015.001|Malware (e.g. rootkit) hooks the export address table (EAT).|
|**Import Address Table Hooking**|F0015.003|Malware (e.g. rootkit) modifies a process's import address table (IAT), which stores pointers to imported API functions.[[1]](#1)|
|**Inline Patching**|F0015.002|Inline patching (inline hooking) is done by modifying the beginning of a function (e.g., first bytes) in order to redirect the execution flow to custom code (i.e. redirecting code flow) before jumping back to the original function.[[2]](#2)|
|**Procedure Hooking**|F0015.007|Intercepts and executes designated code in response to events such as messages, keystrokes, and mouse inputs. [[5]](#5)|
|**Shadow System Service Dispatch Table Hooking**|F0015.004|The Shadow System Service Dispatch Table (SSDT) can be hooked similarly to how the SSDT and IAT are hooked. The target of the hooking with the Shadow SSDT is the Windows subsystem (win32k.sys).[[3]](#3)|
|**System Service Dispatch Table Hooking**|F0015.005|Malware (e.g. rootkit, malicious drivers) may hook the system service dispatch table (SSDT), also called the system service descriptor table. The SSDT contains information about the service tables used by the operating system for dispatching system calls. Hooking the SSDT enables malware to hide files, registry keys, and network connections.[[3]](#3)|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|**Kronos**|June 2014|--|Kronos hooks the API of processes to prevent detection. [[6]](#6)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|--|Trojan spyware program that has mainly been used for targeting banking sites.|
|[**Ursnif**](../xample-malware/ursnif.md)|2016|--|The malware hooks various DLL exported functions when the DLL component is loaded into their respective Browser application process to monitor network traffic. [[7]](#7)|
|[**GravityRAT**](../xample-malware/gravity-rat.md)|2018|--|Abuses Microsoft's Dynamic Data Exchange (DDE) protocol  [[8]](#8)|
|[**SYNfulKnock**](../xample-malware/synful-knock.md)|2015|--|SYNful Knock hooks IOS functions to call and initialize the malware. [[9]](#9)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|F0015.006|Malware escalates privileges by impersonating the token through first using LogonUser and ImpersonateLoggedOnUser, then ImpersonateNamedPipeClient. [[10]](#10)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|F0015.003|Stuxnet hooks ntdll.dll to monitor for requests to load specially crafted file names which are mapped to a location specified by Stuxnet.  [[11]](#11)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|F0015.007|WTR4141.tmp hooks APIs from kernel32.dll and ntdll.dll and replaces the original code for these functions with code that checks for files with properties pertaining to Stuxnet files. If a request is made to list a file with the specified properties, the response from these APIs is altered to state that the file does not exist, thereby hiding all files with these properties. [[11]](#11)|

## References

<a name="1">[1]</a> https://www.sans.org/media/score/checklists/rootkits-investigation-procedures.pdf

<a name="2">[2]</a> https://www.oreilly.com/library/view/learning-malware-analysis/9781788392501/a0a506d6-d062-48c1-a0a8-57d6acb77785.xhtml

<a name="3">[3]</a> https://www.mdpi.com/1999-5903/4/4/971/html

<a name="4">[4]</a> http://ropgadget.com/posts/abusing_win_functions.html

<a name="5">[5]</a> https://docs.microsoft.com/en-us/windows/win32/winmsg/about-hooks?redirectedfrom=MSDN#hook-procedures

<a name="6">[6]</a> https://blog.malwarebytes.com/cybercrime/2017/08/inside-kronos-malware/

<a name="7">[7]</a> https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/PE_URSNIF.A2?_ga=2.131425807.1462021705.1559742358-1202584019.1549394279

<a name="8">[8]</a> https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html

<a name="9">[9]</a> https://www.mandiant.com/resources/synful-knock-acis

<a name="10">[10]</a> https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-returns-to-wipe-systems-in-middle-east-europe/

<a name="11">[11]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en
