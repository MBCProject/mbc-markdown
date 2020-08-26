|||
|---|---|
|**ID**|**B0006**|
|**Objective(s)**|[Anti-Behavioral Analysis](../anti-behavioral-analysis)|
|**Related ATT&CK Technique**|None|


Memory Dump Evasion
===================
Malware hinders retrieval and/or discovery of the contents of the physical memory of the system on which the malware instance is executing [[1]](#1).

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Code Encryption in Memory**|B0006.001|Encrypt the executing malware instance code in memory.|
|**Erase the PE header**|B0006.002|Erase PE header from memory.|
|**Feed Misinformation**|B0006.008|API behavior can be altered to prevent memory dumps. For example, inaccurate data can be reported when the contents of the physical memory of the system on which the malware instance is executing is retrieved. See [Hooking](../credential-access/hooking.md).|
|**Flow Opcode Obstruction**|B0006.009|Flow opcodes (e.g., jumps, loops) are removed and emulated (or decrypted) by the packer during execution, resulting in incorrect dumps. [[4]](#4).|
|**Guard Pages**|B0006.006|Encrypt blocks of code individually and decrypt temporarily only upon execution.|
|**Hide virtual memory**|B0006.003|Hide arbitrary segments of virtual memory.|
|**On-the-Fly APIs**|B0006.007|Resolve API addresses before each use to prevent complete dumping.|
|**SizeOfImage**|B0006.004|Set the SizeOfImage field of PEB.LoaderData to be huge.|
|**Tampering**|B0006.005|Erase or corrupt specific file parts to prevent rebuilding (header, packer stub, etc.).|

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[Kraken](../xample-malware/kraken.md)|April 2008|Dumping Kraken's c.dll module from the heap of its own process is tricky because its PE-header is erased in memory. [[2]](#2)|

References
----------
<a name="1">[1]</a> J. Stuttgen, M. Cohen, Anti-forensic resilient memory acquisition, https://www.dfrws.org/sites/default/files/session-files/paper-anti-forensic_resilient_memory_acquisition.pdf

<a name="2">[2]</a> http://blog.threatexpert.com/2008/04/kraken-changes-tactics.html

<a name="3">[3]</a> http://waleedassar.blogspot.com/search/label/anti-dump

<a name="4">[4]</a> https://www.gironsec.com/code/packers.pdf
