|||
|---------|------------------------|
|**ID**|**E1045**|
|**Objective(s)**|[Anti-Behaviorial Analysis](https://github.com/MAECProject/malware-behaviors/tree/master/anti-behavioral-analysis), [Anti-Static Analysis](https://github.com/MAECProject/malware-behaviors/tree/master/anti-static-analysis), [Defense Evasion](https://github.com/MAECProject/malware-behaviors/tree/master/defense-evasion)|
|**Related ATT&CK Technique(s)**|[Software Packing](https://attack.mitre.org/techniques/T1045/)|

Executable Code Compression
===========================
Executable Code Compression can make static and behavioral analysis difficult [[1]](#1). Methods related to anti-analysis are below. 

See ATT&CK: [**Software Packing**](https://attack.mitre.org/techniques/T1045/).

Methods
-------
* **Nested Packing**: the malware is packed by one packer, the result is packed, etc.
* **Standard Compression**: Uses a standard algorithm, such as UPX or LZMA, to compress an executable file.
* **Standard Compression of Code**: Uses a standard algorithm to compress the opcode mnemonics.
* **Standard Compression of Data**: Uses a standard algorithm to compress strings and variables (executable file data).
* **Custom Compression**: Uses a custom algorithm to compress an executable file.
* **Custom Compression of Code**: Uses a custom algorithm to compress opcode mnemonics.
* **Custom Compression of Data**: Uses a custom algorithm to compress strings and variables (executable file data).

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|-----------|-----------------------------|

References
----------
<a name="1">[1]</a> Ange Albertini, Packers, 5 April 2010, https://gironsec.com/code/packers.pdf

<a name="2">[2]</a> Jiang Ming et al, Towards Paving the Way for Large-Scale Windows Malware Analysis: Generic Binary Unpacking with Orders-of-Magnitude Performance Boost, October 2018, https://dl.acm.org/citation.cfm?id=3243771.
 
