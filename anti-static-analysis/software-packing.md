|||
|---|---|
|**ID**|**F0001**|
|**Objective(s)**|[Anti-Behavioral Analysis](../anti-behavioral-analysis), [Anti-Static Analysis](../anti-static-analysis), [Defense Evasion](../defense-evasion)|
|**Related ATT&CK Sub-Technique**|Obfuscated Files or Information: Software Packing ([T1027.002](https://attack.mitre.org/techniques/T1027/002/), [T1406.002](https://attack.mitre.org/techniques/T1406/002/))|

Software Packing
================
This code characteristic - Software Packing - can make static and behavioral analysis difficult and includes packing with software protectors, such as Themida and Armadillo [[1]](#1). Methods related to anti-analysis are below. This behavior covers both characteristics of the malware (i.e., how it is packed) as well as behaviors of the malware (e.g., the malware packs another executable file).

This description refines the ATT&CK **Obfuscated Files or Information: Software Packing ([T1027.002](https://attack.mitre.org/techniques/T1027/002/), [T1406.002](https://attack.mitre.org/techniques/T1406/002/))** techniques.

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Armadillo**|F0001.012|Uses Armadillo.|
|**ASPack**|F0001.013|Uses ASPack.|
|**Confuser**|F0001.009|Uses Confuser packer.|
|**Custom Compression**|F0001.005|Uses a custom algorithm to compress an executable file.|
|**Custom Compression of Code**|F0001.006|Uses a custom algorithm to compress opcode mnemonics.|
|**Custom Compression of Data**|F0001.007|Uses a custom algorithm to compress strings and variables (executable file data).|
|**Nested Packing**|F0001.001|The malware is packed by one packer, the result is packed, etc.|
|**Standard Compression**|F0001.002|Uses a standard algorithm, such as UPX or LZMA, to compress an executable file.|
|**Standard Compression of Code**|F0001.003|Uses a standard algorithm to compress the opcode mnemonics.|
|**Standard Compression of Data**|F0001.004|Uses a standard algorithm to compress strings and variables (executable file data).|
|**Themida**|F0001.011|Uses Themida.|
|**UPX**|F0001.008|Uses UPX packer.|
|**VMProtect**|F0001.010|Uses VMProtect.|

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**Redhip**](../xample-malware/redhip.md)|2011|Redhip samples are packed with different custom packers. [[3]](#3)|

References
----------
<a name="1">[1]</a> Ange Albertini, Packers, 5 April 2010, https://gironsec.com/code/packers.pdf

<a name="2">[2]</a> Jiang Ming et al, Towards Paving the Way for Large-Scale Windows Malware Analysis: Generic Binary Unpacking with Orders-of-Magnitude Performance Boost, October 2018, https://dl.acm.org/citation.cfm?id=3243771.

<a name="3">[3]</a> https://www.fireeye.com/blog/threat-research/2011/01/the-dead-giveaways-of-vm-aware-malware.html
