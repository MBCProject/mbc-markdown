|||
|---|---|
|**ID**|**B0013**|
|**Objective(s)**|[Discovery](../discovery)|
|**Related ATT&CK Technique**|None|


Analysis Tool Discovery
=======================
Malware can employ various means to detect whether analysis tools are present or running on the system on which it is executing. Note that analysis tools are used to *analyze* malware whereas security software (see [Software Discovery: Security Software Discovery](https://attack.mitre.org/techniques/T1518/001/)) aims to *detect/mitigate* malware on a system or network.

This behavior corresponds to simple, general discovery of analysis tools. Behaviors to find specific analysis tools (e.g., debuggers or disassemblers) are defined under the [Anti-Behavioral Analysis](../anti-behavioral-analysis) objective.

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Known File Location**|B0013.008|Malware may detect an analysis tool by the presence of a file in a known location.|
|**Known Window**|B0013.009|Malware may detect an analysis tool via the presence of a known window.|
|**Process detection**|B0013.001|Malware can scan for the process name associated with common analysis tools.|
|**Process detection - Debuggers**|B0013.002|Malware can scan for the process name associated with common analysis tools. OllyDBG / ImmunityDebugger / WinDbg / IDA Pro|
|**Process detection - PCAP Utilities**|B0013.004|Malware can scan for the process name associated with common analysis tools. Wireshark / Dumpcap|
|**Process detection - PE Utilities**|B0013.006|Malware can scan for the process name associated with common analysis tools. ImportREC / PETools / LordPE|
|**Process detection - Process Utilities**|B0013.005|Malware can scan for the process name associated with common analysis tools. ProcessHacker / SysAnalyzer / HookExplorer / SysInspector|
|**Process detection - Sandboxes**|B0013.007|Malware can scan for the process name associated with common analysis tools. Joe Sandbox, etc.|
|**Process detection - SysInternals Suite Tools**|B0013.003|Malware can scan for the process name associated with common analysis tools. Process Explorer / Process Monitor / Regmon / Filemon, TCPView, Autoruns|
