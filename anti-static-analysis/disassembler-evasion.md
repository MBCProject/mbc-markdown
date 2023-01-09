<table>
<tr>
<td><b>ID</b></td>
<td><b>B0012</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../anti-static-analysis">Anti-Static Analysis</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
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
<td><b>31 October 2022</b></td>
</tr>
</table>

# Disassembler Evasion

Malware code evades disassembly in a recursive (flow-oriented) or linear disassembler, resulting in inaccurate or incomplete disassembly. The Disassembler Evasion behavior may also result in the disassembly process halting with an error.

Some methods apply to both types of disassemblers; others apply to one type and not the other. 

## Methods

|Name|ID|Description|
|---|---|---|
|**Conditional Misdirection**|B0012.002|Conditional jumps are sometimes used to confuse disassembly engines, resulting in the wrong instruction boundaries and thus wrong mnemonic and operands; may be identified by instructions *jmp/jcc to a label+#* (e.g., JNE loc_401345fe+2).|
|**Desynchronizing Opaque Predicates**|B0012.006|Opaque predicates inject superfluous branches into the disassembly, resulting in disassembly desynchronization, as well as code bloat. The junk bytes introduced damage the disassembly process when the bytes are treated as code. [[5]](#5)|
|**VBA Stomping**|B0012.005|Typically, VBA source code is compiled into p-code, which is stored with compressed sourced code in the OLE file with VBA macros. VBA Stomping - when the VBA source code is removed and only the p-code remains - makes analysis much harder. See [[3]](#3) for an analysis of a VBA-Stomped malicious VBA Office document. See [[4]](#4) for information on Evil Clippy, a tool that creates malicious MS Office documents.|
|**Value Dependent Jumps**|B0012.003|Explicit use of computed values for control flow, often in the same basic block or function.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|B0012.001|Contain obfuscated stackstrings (This capa rule had 3 matches) [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|B0012.001|Contain obfuscated stackstrings (This capa rule had 1 match) [[6]](#6)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|B0012.001|Contain obfuscated stackstrings (This capa rule had 1 match) [[6]](#6)|

## References

<a name="1">[1]</a> http://staff.ustc.edu.cn/~bjhua/courses/security/2014/readings/anti-disas.pdf

<a name="2">[2]</a> http://www.kernelhacking.com/rodrigo/docs/blackhat2012-paper.pdf

<a name="3">[3]</a> https://isc.sans.edu/diary/Malicious+VBA+Office+Document+Without+Source+Code/24870

<a name="4">[4]</a> https://boingboing.net/2019/05/05/p-code-r-us.html

<a name="5">[5]</a> https://www.ndss-symposium.org/wp-content/uploads/2020/04/bar2020-23004-paper.pd

<a name="6">[6]</a> capa v4.0, analyzed at MITRE on 10/12/2022

