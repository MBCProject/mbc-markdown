|||
|---------|------------------------|
|**ID**|**M0012**|
|**Objective(s)**| [Anti-Static Analysis](https://github.com/MAECProject/malware-behaviors/tree/master/anti-static-analysis)|
|**Related ATT&CK Technique(s)**|None|


Disassembler Evasion
====================
Malware code evades disassembly in a recursive or linear disassembler. Some methods apply to both types of disassemblers; others apply to one type and not the other.

Methods
-------
* **Conditional Misdirection**: Conditional jumps are sometimes used to confuse disassembly engines, resulting in the wrong instruction boundaries and thus wrong mnemonic and operands; identified by instructions *jmp/jcc to a label+#* (e.g., JNE loc_401345fe+2).
* **Value Dependent Jumps**: Explicit use of computed values for control flow, often many times in the same basic block or function.
* **Argument Obfuscation**: Simple number or string arguments to API calls are calculated at runtime, making linear disassembly more difficult.
* **Variable Recomposition**: Variables, often strings, are broken into multiple parts and store out of order, in different memory ranges, or both. They must then be recomposed before use.
* **VBA Stomping**: Typically, VBA source code is compiled into p-code, which is stored with compressed sourced code in the OLE file with VBA macros. VBA Stomping - when the VBA source code is removed and only the p-code remains - makes analysis much harder. See [[3]](#3) for an analysis of a VBA-Stomped malicious VBA Office document. See [[4]](#4) for information on Evil Clippy, a tool that creates malicious MS Office documents.
   
Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|

References
----------
<a name="1">[1]</a> http://staff.ustc.edu.cn/~bjhua/courses/security/2014/readings/anti-disas.pdf

<a name="2">[2]</a> http://www.kernelhacking.com/rodrigo/docs/blackhat2012-paper.pdf

<a name="3">[3]</a> https://isc.sans.edu/diary/Malicious+VBA+Office+Document+Without+Source+Code/24870

<a name="4">[4]</a> https://boingboing.net/2019/05/05/p-code-r-us.html 