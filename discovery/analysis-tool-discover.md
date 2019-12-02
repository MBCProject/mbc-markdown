|||
|---------|------------------------|
|**ID**|**M0013**|
|**Objective(s)**|[Discovery](https://github.com/MBCProject/mbc-markdown/tree/master/discovery)|
|**Related ATT&CK Technique(s)**|None|


Analysis Tool Discovery
=======================
Malware can employ various means to detect whether analysis tools are present or running on the system on which it is executing. Note that analysis tools are used to *analyze* malware whereas security software (see [Security Software Discovery](https://github.com/MBCProject/mbc-markdown/blob/master/discovery/security-sw-discover.md)) aims to *detect/mitigate* malware on a system or network.

Methods
-------
* **Process detection**: Malware can scan for the process name associated with common analysis tools: 
   * Debuggers: OllyDBG / ImmunityDebugger / WinDbg / IDA Pro
   * SysInternals Suite Tools (Process Explorer / Process Monitor / Regmon / Filemon, TCPView, Autoruns)
   * PCAP Utilities: Wireshark / Dumpcap
   * Process Utilities: ProcessHacker / SysAnalyzer / HookExplorer / SysInspector
   * PE Utilities: ImportREC / PETools / LordPE
   * Sandboxes: Joe Sandbox, etc.

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|


References
----------
