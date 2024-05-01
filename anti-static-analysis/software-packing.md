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
<td><b>2.3</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>27 April 2024</b></td>
</tr>
</table>

# Software Packing

This code characteristic - Software Packing - can make static and behavioral analysis difficult and includes packing with software protectors, such as Themida and Armadillo [[1]](#1). Methods related to anti-analysis are below. This behavior covers both characteristics of the malware (i.e., how it is packed) as well as behaviors of the malware (e.g., the malware packs another executable file).

This description refines the ATT&CK **Obfuscated Files or Information: Software Packing ([T1027.002](https://attack.mitre.org/techniques/T1027/002/), [T1406.002](https://attack.mitre.org/techniques/T1406/002/))** techniques.

## Methods

|Name|ID|Description|
|---|---|---|
|**Armadillo**|F0001.012|Uses Armadillo.|
|**ASPack**|F0001.013|Uses ASPack. This method is related to Unprotect technique U1411.|
|**Confuser**|F0001.009|Uses Confuser packer.|
|**Custom Compression**|F0001.005|Uses a custom algorithm to compress an executable file.|
|**Custom Compression of Code**|F0001.006|Uses a custom algorithm to compress opcode mnemonics.|
|**Custom Compression of Data**|F0001.007|Uses a custom algorithm to compress strings and variables (executable file data).|
|**Nested Packing**|F0001.001|The malware is packed by one packer, the result is packed, etc.|
|**Standard Compression**|F0001.002|Uses a standard algorithm, such as UPX or LZMA, to compress an executable file.|
|**Standard Compression of Code**|F0001.003|Uses a standard algorithm to compress the opcode mnemonics.|
|**Standard Compression of Data**|F0001.004|Uses a standard algorithm to compress strings and variables (executable file data).|
|**Themida**|F0001.011|Uses Themida.This method is related to Unprotect technique U1406.|
|**UPX**|F0001.008|Uses UPX packer. This method is related to Unprotect technique U1402.|
|**VMProtect**|F0001.010|Uses VMProtect. This method is related to Unprotect technique U1410.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Redhip**](../xample-malware/redhip.md)|2011|--|Redhip samples are packed with different custom packers. [[3]](#3)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|The malware comes packed by a crypter/FUD. [[4]](#4)|
|[**Conficker**](../xample-malware/conficker.md)|2008|F0001.008|Conficker is propagated as a DLL which has been backed using the UPX packer. [[5]](#5)|
|[**DarkComet**](../xample-malware/dark-comet.md)|2008|--|DarkComet has the option to compress its payload using UPX or MPRESS.  [[6]](#6)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|--|The malware has a custom packer to obfuscate itself. [[7]](#7)|
|[**Emotet**](../xample-malware/emotet.md)|2018|F0001.005|Emotet uses custom packers which first decrypt the loaders and the loaders decrypt and load Emotet's main payloads. [[8]](#8)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[packed with pebundle](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/packer/pebundle/packed-with-pebundle.yml)|Software Packing (F0001)|--|
|[packed with Themida](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/packer/themida/packed-with-themida.yml)|Software Packing::Themida (F0001.011)|--|
|[packed with VMProtect](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/packer/vmprotect/packed-with-vmprotect.yml)|Software Packing::VMProtect (F0001.010)|--|
|[packed with y0da crypter](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/packer/y0da/packed-with-y0da-crypter.yml)|Software Packing (F0001)|--|
|[packed with pelocknt](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/packer/pelocknt/packed-with-pelocknt.yml)|Software Packing (F0001)|--|
|[packed with GoPacker](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/packer/gopacker/packed-with-gopacker.yml)|Software Packing::Standard Compression (F0001.002)|--|
|[packed with Confuser](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/packer/confuser/packed-with-confuser.yml)|Software Packing::Confuser (F0001.009)|--|
|[packed with rlpack](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/packer/rlpack/packed-with-rlpack.yml)|Software Packing (F0001)|--|
|[packed with ASPack](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/packer/aspack/packed-with-aspack.yml)|Software Packing (F0001)|--|
|[packed with generic packer](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/packer/generic/packed-with-generic-packer.yml)|Software Packing::Standard Compression (F0001.002)|--|
|[packed with amber](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/packer/amber/packed-with-amber.yml)|Software Packing (F0001)|--|
|[packed with petite](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/packer/petite/packed-with-petite.yml)|Software Packing (F0001)|--|
|[packed with peshield](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/packer/peshield/packed-with-peshield.yml)|Software Packing (F0001)|--|
|[packed with UPX](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/packer/upx/packed-with-upx.yml)|Software Packing::UPX (F0001.008)|--|
|[packed with upack](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/packer/upack/packed-with-upack.yml)|Software Packing (F0001)|--|
|[packed with PECompact](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/packer/pecompact/packed-with-pecompact.yml)|Software Packing (F0001)|--|
|[packed with Huan](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/packer/huan/packed-with-huan.yml)|Software Packing (F0001)|--|
|[packed with nspack](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/packer/nspack/packed-with-nspack.yml)|Software Packing (F0001)|--|
|[packed with kkrunchy](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/packer/kkrunchy/packed-with-kkrunchy.yml)|Software Packing (F0001)|--|
|[packed with PESpin](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/packer/pespin/packed-with-pespin.yml)|Software Packing (F0001)|--|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[packer_nspack](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_nspack.py)|Software Packing (F0001)|--|
|[packer_vmprotect](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_vmprotect.py)|Software Packing (F0001)|--|
|[packer_vmprotect](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_vmprotect.py)|Software Packing::VMProtect (F0001.010)|--|
|[packer_confuser](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_confuser.py)|Software Packing (F0001)|--|
|[packer_confuser](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_confuser.py)|Software Packing::Confuser (F0001.009)|--|
|[packer_smartassembly](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_smartassembly.py)|Software Packing (F0001)|--|
|[packer_mpress](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_mpress.py)|Software Packing (F0001)|--|
|[packer_enigma](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_enigma.py)|Software Packing (F0001)|--|
|[packer_aspirecrypt](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_aspirecrypt.py)|Software Packing (F0001)|--|
|[packer_nate](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_nate.py)|Software Packing (F0001)|--|
|[packer_entropy](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_entropy.py)|Software Packing (F0001)|--|
|[packer_unknown_pe_section_name](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_anomaly.py)|Software Packing (F0001)|--|
|[packer_upx](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_upx.py)|Software Packing (F0001)|--|
|[packer_upx](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_upx.py)|Software Packing::UPX (F0001.008)|--|
|[packer_aspack](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_aspack.py)|Software Packing (F0001)|--|
|[packer_aspack](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_aspack.py)|Software Packing::ASPack (F0001.013)|--|
|[packer_bedsprotector](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_bedsprotector.py)|Software Packing (F0001)|--|
|[packer_themida](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_themida.py)|Software Packing (F0001)|FindWindowA|
|[packer_themida](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_themida.py)|Software Packing::Themida (F0001.011)|FindWindowA|
|[packer_themida](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_themida.py)|Software Packing (F0001)|--|
|[packer_themida](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_themida.py)|Software Packing::Themida (F0001.011)|--|
|[packer_spices](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_spices.py)|Software Packing (F0001)|--|
|[packer_yoda](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_yoda.py)|Software Packing (F0001)|--|
|[packer_titan](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/packer_titan.py)|Software Packing (F0001)|--|

## References

<a name="1">[1]</a> Ange Albertini, Packers, 5 April 2010, https://gironsec.com/code/packers.pdf

<a name="2">[2]</a> Jiang Ming et al, Towards Paving the Way for Large-Scale Windows Malware Analysis: Generic Binary Unpacking with Orders-of-Magnitude Performance Boost, October 2018, https://dl.acm.org/citation.cfm?id=3243771

<a name="3">[3]</a> https://web.archive.org/web/20200815134441/https://www.fireeye.com/blog/threat-research/2011/01/the-dead-giveaways-of-vm-aware-malware.html

<a name="4">[4]</a> https://blog.malwarebytes.com/threat-analysis/2016/07/untangling-kovter/

<a name="5">[5]</a> http://www.csl.sri.com/users/vinod/papers/Conficker/

<a name="6">[6]</a> https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/

<a name="7">[7]</a> https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf

<a name="8">[8]</a> https://documents.trendmicro.com/assets/white_papers/ExploringEmotetsActivities_Final.pdf

