|||
|---|---|
|**ID**|**F0001**|
|**Objective(s)**|[Anti-Behavioral Analysis](https://github.com/MBCProject/mbc-markdown/tree/master/anti-behavioral-analysis), [Anti-Static Analysis](https://github.com/MBCProject/mbc-markdown/tree/master/anti-static-analysis), [Defense Evasion](https://github.com/MBCProject/mbc-markdown/tree/master/defense-evasion)|
|**Related ATT&CK Sub-Technique**|[Obfuscated Files or Information: Software Packing](https://attack.mitre.org/techniques/T1027/002)|

Software Packing
================
This code characteristic - Software Packing - can make static and behavioral analysis difficult and includes packing with software protectors, such as Themida and Armadillo [[1]](#1). Methods related to anti-analysis are below. This behavior covers both characteristics of the malware (i.e., how it is packed) as well as behaviors of the malware (e.g., the malware packs another executable file).

This description refines the ATT&CK [**Obfuscated Files or Information: Software Packing**](https://attack.mitre.org/techniques/T1027/002) sub-technique.

Methods
-------
|ID|Name|Description|
|---|---|---|
|F0001.001|**Nested Packing**|The malware is packed by one packer, the result is packed, etc.|
|F0001.002|**Standard Compression**|Uses a standard algorithm, such as UPX or LZMA, to compress an executable file.|
|F0001.003|**Standard Compression of Code**|Uses a standard algorithm to compress the opcode mnemonics.|
|F0001.004|**Standard Compression of Data**|Uses a standard algorithm to compress strings and variables (executable file data).|
|F0001.005|**Custom Compression**|Uses a custom algorithm to compress an executable file.|
|F0001.006|**Custom Compression of Code**|Uses a custom algorithm to compress opcode mnemonics.|
|F0001.007|**Custom Compression of Data**|Uses a custom algorithm to compress strings and variables (executable file data).|
|F0001.008|**UPX**|Uses UPX packer.|
|F0001.009|**Confuser**|Uses Confuser packer.|
|F0001.010|**VMProtect**|Uses VMProtect.|
|F0001.011|**Themida**|Uses Themida.|
|F0001.012|**Armadillo**|Uses Armadillo.|

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**Redhip**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/redhip.md)|2011|Redhip samples are packed with different custom packers. [[3]](#3)|

References
----------
<a name="1">[1]</a> Ange Albertini, Packers, 5 April 2010, https://gironsec.com/code/packers.pdf

<a name="2">[2]</a> Jiang Ming et al, Towards Paving the Way for Large-Scale Windows Malware Analysis: Generic Binary Unpacking with Orders-of-Magnitude Performance Boost, October 2018, https://dl.acm.org/citation.cfm?id=3243771.

<a name="3">[3]</a> https://www.fireeye.com/blog/threat-research/2011/01/the-dead-giveaways-of-vm-aware-malware.html
