|||
|---------|------------------------|
|**ID**|**B0013**|
|**Objective(s)**|[Discovery](https://github.com/MBCProject/mbc-beta/tree/master/discovery)|
|**Related ATT&CK Technique**|None|


Analysis Tool Discovery
=======================
Malware can employ various means to detect whether analysis tools are present or running on the system on which it is executing. Note that analysis tools are used to *analyze* malware whereas security software (see [Software Discovery: Security Software Discovery](https://attack.mitre.org/techniques/T1518/001/)) aims to *detect/mitigate* malware on a system or network.

This behavior corresponds to simple, general discovery of analysis tools. Behaviors to find specific analysis tools (e.g., debuggers or disassemblers) are defined under the [Anti-Behavioral Analysis](https://github.com/MBCProject/mbc-beta/tree/master/anti-behavioral-analysis) objective.

Methods
-------
|ID|Name|Description|
|-----------------------------|--------|-----------------------------|
|B0013.001|**Process detection**|Malware can scan for the process name associated with common analysis tools.|

| | | | |
|----------|-----------------------------|--------|-----------------------------| 
| |B0013.002|*Debuggers*|OllyDBG / ImmunityDebugger / WinDbg / IDA Pro|
| |B0013.003|*SysInternals Suite Tools*|Process Explorer / Process Monitor / Regmon / Filemon, TCPView, Autoruns|
| |B0013.004|*PCAP Utilities*|Wireshark / Dumpcap|
| |B0013.005|*Process Utilities*|ProcessHacker / SysAnalyzer / HookExplorer / SysInspector|
| |B0013.006|*PE Utilities*|ImportREC / PETools / LordPE|
| |B0013.007|*Sandboxes*|Joe Sandbox, etc.|

|  |    |           |
|-----------------------------|--------|-----------------------------|
|B0013.008|**Known File Location**|Malware may detect an analysis tool by the presence of a file in a known location.|
|B0013.009|**Known Window**|Malware may detect an analysis tool via the presence of a known window.|