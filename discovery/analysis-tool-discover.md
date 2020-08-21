|||
|---|---|
|**ID**|**B0013**|
|**Objective(s)**|[Discovery](https://github.com/MBCProject/mbc-markdown/tree/master/discovery)|
|**Related ATT&CK Technique**|None|


Analysis Tool Discovery
=======================
Malware can employ various means to detect whether analysis tools are present or running on the system on which it is executing. Note that analysis tools are used to *analyze* malware whereas security software (see [Software Discovery: Security Software Discovery](https://attack.mitre.org/techniques/T1518/001/)) aims to *detect/mitigate* malware on a system or network.

This behavior corresponds to simple, general discovery of analysis tools. Behaviors to find specific analysis tools (e.g., debuggers or disassemblers) are defined under the [Anti-Behavioral Analysis](https://github.com/MBCProject/mbc-markdown/tree/master/anti-behavioral-analysis) objective.

Methods
-------
|ID|Name|Description|
|---|---|---|
|B0013.001|**Process detection**|Malware can scan for the process name associated with common analysis tools.|
|B0013.002|**Process detection - Debuggers**|Malware can scan for the process name associated with common analysis tools. OllyDBG / ImmunityDebugger / WinDbg / IDA Pro|
|B0013.003|**Process detection - SysInternals Suite Tools**|Malware can scan for the process name associated with common analysis tools. Process Explorer / Process Monitor / Regmon / Filemon, TCPView, Autoruns|
|B0013.004|**Process detection - PCAP Utilities**|Malware can scan for the process name associated with common analysis tools. Wireshark / Dumpcap|
|B0013.005|**Process detection - Process Utilities**|Malware can scan for the process name associated with common analysis tools. ProcessHacker / SysAnalyzer / HookExplorer / SysInspector|
|B0013.006|**Process detection - PE Utilities**|Malware can scan for the process name associated with common analysis tools. ImportREC / PETools / LordPE|
|B0013.007|**Process detection - Sandboxes**|Malware can scan for the process name associated with common analysis tools. Joe Sandbox, etc.|
|B0013.008|**Known File Location**|Malware may detect an analysis tool by the presence of a file in a known location.|
|B0013.009|**Known Window**|Malware may detect an analysis tool via the presence of a known window.|
