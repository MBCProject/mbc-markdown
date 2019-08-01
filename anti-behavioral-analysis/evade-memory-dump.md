|||
|---------|------------------------|
|**ID**|**M0006**|
|**Objective(s)**|[Anti-Behavioral Analysis](https://github.com/MAECProject/malware-behaviors/tree/master/anti-behavioral-analysis)|
|**Related ATT&CK Technique(s)**|None|

Memory Dump Evasion
===================
Malware hinders retrieval and/or discovery of the contents of the physical memory of the system on which the malware instance is executing [[1]](#1).

Methods
-------
* **Code Encryption in Memory**: Encrypt the executing malware instance code in memory.
* **Erase the PE header**: Erase PE header from memory.
* **Hide virtual memory**: Hide arbitrary segments of virtual memory.
* **SizeOfImage**: Set the SizeOfImage field of PEB.LoaderData to be huge.
* **Tampering**: Erase or corrupt specific file parts to prevent rebuilding (header, packer stub, etc.).
* **Guard Pages**: Encrypt blocks of code individually and decrypt temporarily only upon execution.
* **On-the-Fly APIs**: Resolve API addresses before each use to prevent complete dumping.
* **Feed Misinformation**: API behavior can be altered to prevent prevent memory dumps. For example, inaccurate data can be reported when the contents of the physical memory of the system on which the malware instance is executing is retrieved. See [Hooking](https://github.com/MAECProject/malware-behaviors/blob/master/anti-behavioral-analysis/hooking.md).
* **Flow Opcode Obstruction**: flow opcodes (e.g., jumps, loops) are removed and emulated (or decrypted) by the packer during execution, resulting in incorrect dumps. [[4]](#4)

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|-----------|-----------------------------|
|Kraken| April 2008| Dumping Kraken's c.dll module from the heap of its own process is tricky because its PE-header is erased in memory. [[2]](#2)|

References
----------
<a name="1">[1]</a> J. Stuttgen, M. Cohen, Anti-forensic resilient memory acquisition, www.dfrws.org/sites/default/files/session-files/paper-anti-forensic_resilient_memory_acquisition.pdf

<a name="2">[2]</a> http://blog.threatexpert.com/2008/04/kraken-changes-tactics.html

<a name="3">[3]</a> http://waleedassar.blogspot.com/search/label/anti-dump

<a name="4">[4]</a> https://www.gironsec.com/code/packers.pdf
 
 
