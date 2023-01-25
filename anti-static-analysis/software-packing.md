<table>
<tr>
<td><b>ID</b></td>
<td><b>F0001</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../anti-behavioral-analysis">Anti-Behavioral Analysis</a>, <a href="../anti-static-analysis">Anti-Static Analysis</a>, <a href="../defense-evasion">Defense Evasion</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Obfuscated Files or Information: Software Packing (<a href="https://attack.mitre.org/techniques/T1027/002/">T1027.002</a>, <a href="https://attack.mitre.org/techniques/T1406/002/">T1406.002</a>)</b></td>
</tr>
<tr>
<td><b>Anti-Analysis Type</b></td>
<td><b>Evasion</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>21 November 2022</b></td>
</tr>
</table>

# Software Packing

This code characteristic - Software Packing - can make static and behavioral analysis difficult and includes packing with software protectors, such as Themida and Armadillo [[1]](#1). Methods related to anti-analysis are below. This behavior covers both characteristics of the malware (i.e., how it is packed) as well as behaviors of the malware (e.g., the malware packs another executable file).

This description refines the ATT&CK **Obfuscated Files or Information: Software Packing ([T1027.002](https://attack.mitre.org/techniques/T1027/002/), [T1406.002](https://attack.mitre.org/techniques/T1406/002/))** techniques.

## Methods

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

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Redhip**](../xample-malware/redhip.md)|2011|--|Redhip samples are packed with different custom packers. [[3]](#3)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|The malware comes packed by a crypter/FUD. [[4]](#4)|
|[**Conficker**](../xample-malware/conficker.md)|2008|F0001.008|Conficker is propagated as a DLL which has been backed using the UPX packer. [[5]](#5)|
|[**DarkComet**](../xample-malware/dark-comet.md)|2008|--|DarkComet has the option to compress its payload using UPX or MPRESS.  [[6]](#6)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|--|The malware has a custom packer to obfuscate itself. [[7]](#7)|
|[**Emotet**](../xample-malware/emotet.md)|2018|F0001.005|Emotet uses custom packers which first decrypt the loaders and the loaders decrypt and load Emotet's main payloads. [[8]](#8)|

## References

<a name="1">[1]</a> Ange Albertini, Packers, 5 April 2010, https://gironsec.com/code/packers.pdf

<a name="2">[2]</a> Jiang Ming et al, Towards Paving the Way for Large-Scale Windows Malware Analysis: Generic Binary Unpacking with Orders-of-Magnitude Performance Boost, October 2018, https://dl.acm.org/citation.cfm?id=3243771.

<a name="3">[3]</a> https://www.fireeye.com/blog/threat-research/2011/01/the-dead-giveaways-of-vm-aware-malware.html

<a name="4">[4]</a> https://www.bleepingcomputer.com/virus-removal/remove-kovter-trojan

<a name="5">[5]</a> http://www.csl.sri.com/users/vinod/papers/Conficker/

<a name="6">[6]</a> https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/

<a name="7">[7]</a> https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf

<a name="8">[8]</a> https://documents.trendmicro.com/assets/white_papers/ExploringEmotetsActivities_Final.pdf
