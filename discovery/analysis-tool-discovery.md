<table>
<tr>
<td><b>ID</b></td>
<td><b>B0013</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../discovery">Discovery</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.1</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>5 December 2023</b></td>
</tr>
</table>


# Analysis Tool Discovery

Malware can employ various means to detect whether analysis tools are present or running on the system on which it is executing.S uch tools include Wireshark, Process Hacker, and IDA. 

Note that analysis tools are used to *analyze* malware whereas security software (see **Software Discovery: Security Software Discovery ([T1518](https://attack.mitre.org/techniques/T1518/001/))** aims to *detect/mitigate* malware on a system or network.

This behavior corresponds to simple, general discovery of analysis tools. Behaviors to find specific analysis tools (e.g., debuggers or disassemblers) are defined under the [Anti-Behavioral Analysis](../anti-behavioral-analysis) objective.

## Methods

|Name|ID|Description|
|---|---|---|
|**Known File Location**|B0013.008|Malware may detect an analysis tool by the presence of a file in a known location.|
|**Known Window**|B0013.009|Malware may detect an analysis tool via the presence of a known window.|
|**Known Windows Class Name**|B0013.010|Running program windows are checked to see if any windows class name contains a string indicating that an analysis tool is running. For example, 'WinDbgFrameClass' is Windbg main window’s class name. [2]|
|**Process detection**|B0013.001|Malware can scan for the process name associated with common analysis tools.|
|**Process detection - Debuggers**|B0013.002|Malware can scan for the process name associated with common analysis tools - OllyDBG / ImmunityDebugger / WinDbg / IDA Pro.|
|**Process detection - PCAP Utilities**|B0013.004|Malware can scan for the process name associated with common analysis tools - Wireshark / Dumpcap.|
|**Process detection - PE Utilities**|B0013.006|Malware can scan for the process name associated with common analysis tools - ImportREC / PETools / LordPE.|
|**Process detection - Process Utilities**|B0013.005|Malware can scan for the process name associated with common analysis tools - ProcessHacker / SysAnalyzer / HookExplorer / SysInspector.|
|**Process detection - Sandboxes**|B0013.007|Malware can scan for the process name associated with common analysis tools - Joe Sandbox, etc.|
|**Process detection - SysInternals Suite Tools**|B0013.003|Malware can scan for the process name associated with common analysis tools - Process Explorer / Process Monitor / Regmon / Filemon, TCPView, Autoruns.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Emotet**](../xample-malware/emotet.md)|2018|B0013.002|If Emotet receives a response from the C2 server stating a debugging-related tool is in the list of running processes, it receives an "upgrade" command which calls the ShellExecuteW function and exits. [[1]](#1)|
|[**Poison Ivy**](../xample-malware/poison-ivy.md)|2005|--|Poison Ivy Variant runs a threat to check if any analysis tools are running by creating specially named pipes that are created by various analysis tools. If one of the named pipes cannot be created, it means one of the analysis tools is running. [[2]](#2) [[3]](#3)|
|[**Poison Ivy**](../xample-malware/poison-ivy.md)|2005|B0013.010|Poison Ivy goes through all the running program windows to check if any Windows class name contains a special string to determine if an analysis tool is running. [[2]](#2) [[3]](#3)|
|[**WebCobra**](../xample-malware/webcobra.md)|2018|B0013.004|When infecting a x64 architecture system, the malware terminates if Wireshark is running on the system. [[4]](#4)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[reference analysis tools strings](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/reference-analysis-tools-strings.yml)|Analysis Tool Discovery::Process detection (B0013.001)|--|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[antianalysis_detectreg](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antianalysis_detectreg.py)|Analysis Tool Discovery (B0013)|--|
|[antidebug_devices](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antidebug_devices.py)|Analysis Tool Discovery (B0013)|--|
|[antidebug_windows](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antidebug_windows.py)|Analysis Tool Discovery (B0013)|--|
|[antidebug_windows](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antidebug_windows.py)|Analysis Tool Discovery::Process detection (B0013.001)|--|
|[antidebug_windows](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antidebug_windows.py)|Analysis Tool Discovery::Known Window (B0013.009)|--|
|[antivm_bochs_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_bochs_keys.py)|Analysis Tool Discovery (B0013)|--|
|[antianalysis_detectfile](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antianalysis_detectfile.py)|Analysis Tool Discovery (B0013)|--|
|[antianalysis_detectfile](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antianalysis_detectfile.py)|Analysis Tool Discovery::Known File Location (B0013.008)|--|

## References

<a name="1">[1]</a> https://www.fortinet.com/blog/threat-research/deep-analysis-of-new-emotet-variant-part-1

<a name="2">[2]</a> https://www.mandiant.com/sites/default/files/2021-09/rpt-poison-ivy.pdf

<a name="3">[3]</a> https://www.fortinet.com/blog/threat-research/deep-analysis-of-new-poison-ivy-variant

<a name="4">[4]</a> https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/
