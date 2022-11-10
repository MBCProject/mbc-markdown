<table>
<tr>
<td><b>ID</b></td>
<td><b>B0003</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../anti-behavioral-analysis">Anti-Behavioral Analysis</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Virtualization/Sandbox Evasion (<a href="https://attack.mitre.org/techniques/T1497/">T1497</a>, <a href="https://attack.mitre.org/techniques/T1633/">T1633</a>)</b></td>
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
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>28 October 2022</b></td>
</tr>
</table>


# Dynamic Analysis Evasion

Malware may obstruct dynamic analysis in a sandbox, emulator, or virtual machine. 

See **Emulator Evasion ([B0004](../anti-behavioral-analysis/emulator-evasion.md))** for an  emulator-specific evasion behavior, and see **Conditional Execution ([B0025](../anti-behavioral-analysis/execution-guardrails.md))** for a behavior that constrains dynamic execution based on environmental conditions. 

The related **Virtualization/Sandbox Evasion ([T1497](https://attack.mitre.org/techniques/T1497/), [T1633](https://attack.mitre.org/techniques/T1633/))** ATT&CK techniques were defined subsequent to this MBC behavior.

## Methods

|Name|ID|Description|
|---|---|---|
|**Alternative ntdll.dll**|B0003.001|A copy of ntdll.dll is dropped to the filesystem and then loaded. This alternative DLL is used to execute function calls to evade sandboxes which use hooking in the operating system's ntdll.dll.|
|**API Hammering**|B0003.012|Uses of a huge number of calls to Windows APIs as a form of extended sleep to evade analysis in sandbox environments.|
|**Code Integrity Check**|B0003.011|Compares memory-based and disk-based versions of itself. If differences are detected, the malware alters its execution, possibly acting destructively.|
|**Data Flood**|B0003.002|Overloads a sandbox by generating a flood of meaningless behavioral data. [[1]](#1)|
|**Delayed Execution**|B0003.003|Stalling code is typically executed before any malicious behavior. The malware's aim is to delay the execution of the malicious activity long enough so that an automated dynamic analysis system fails to extract the interesting malicious behavior. This method is very similar to ATT&CK's [Virtualization/Sandbox Evasion: Time Based Evasion](https://attack.mitre.org/techniques/T1497/003/) sub-technique.|
|**Demo Mode**|B0003.004|Inclusion of a demo binary/mode that is executed when token is absent or not privileged enough.|
|**Drop Code**|B0003.005|Original file is written to disk then executed. May confuse some sandboxes, especially if the dropped executable must be provided specific arguments and the original dropper is not associated with the drop file(s).|
|**Encode File**|B0003.006|Encode a file on disk, such as an implant's config file.|
|**Hook File System**|B0003.007|Execution happens when a particular file or directory is accessed, often through hooking certain API calls such as CreateFileA and CreateFileW.|
|**Hook Interrupt**|B0003.008|Modification of interrupt vector or descriptor tables.|
|**Illusion**|B0003.009|Creates an illusion; makes the analyst think something happened when it didn't.|
|**Restart**|B0003.010|Restarts or shuts down system to bypass sandboxing.|


## Use in Malware

|Name|Date|Description|
|---|---|---|
|[**Ursnif**](../xample-malware/ursnif.md)|May 2016|Ursnif uses malware macros to evade sandbox detection. [[2]](#2)|
|[**Terminator**](../xample-malware/terminator.md)|October 2013|The Terminator rat evades a sandbox by not executing until after a reboot. Most sandboxes don't reboot during an analysis. [[3]](#3)|
|**Nap**|2013|Trojan Nap (tied to the Kelihos Botnet) uses extended sleep calls to evade sandbox analysis. [[3]](#3)|
|**Smokeloader**|2019|Smokeloader drops a copy of ntdll.dll to %APPDATA%\Local\Temp\ [[4]](#4)|
|[**WebCobra**](../xample-malware/webcobra.md)|2018|Evades dynamic analysis.)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|The malware stalls by writing a byte of random data to memory 960 million times which complicates analysis. It also calls specific Windows API functions [[5]](#5)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|Uses numerous printf loops to delay the execution process and overload the sandbox with junk data (API Hammering) [[6]](#6)|


## References

<a name="1">[1]</a> http://joe4security.blogspot.com/2013/06/overloading-sandboxes-new-generic.html

<a name="2">[2]</a> https://www.cyber.nj.gov/threat-profiles/trojan-variants/ursnif

<a name="3">[3]</a> https://www.fireeye.com/content/dam/fireeye-www/current-threats/pdfs/pf/file/fireeye-hot-knives-through-butter.pdf

<a name="4">[4]</a> https://research.checkpoint.com/2019-resurgence-of-smokeloader/

<a name="5">[5]</a> https://blogs.cisco.com/security/talos/rombertik

<a name="6">[6]</a> https://www.joesecurity.org/blog/498839998833561473
