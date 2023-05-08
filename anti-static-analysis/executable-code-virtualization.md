<table>
<tr>
<td><b>ID</b></td>
<td><b>B0008</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../anti-behavioral-analysis">Anti-Behavioral Analysis</a>, <a href="../anti-static-analysis">Anti-Static Analysis</a></b></td>
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
<td><b>30 April 2023</b></td>
</tr>
</table>


# Executable Code Virtualization

Code virtualization obfuscates code to hinder static analysis and reverse engineering of the binary, allowing successful masking of the code’s malicious behavior.  Code virtualization selects specific parts of original executable code and transforms them “to bytecode in a new, custom virtual instruction set architecture (ISA)”[[1]](#1).  As explained further in [[1]](#), “At execution time, the bytecode is emulated by an embedded virtual machine (or interpreter) on the real machine. The new ISA can be designed independently, and thus the bytecode and interpreter greatly differ from those in every protected instance. In this way, the program’s original code never reappears.” 

While malicious actors can create a custom VM-based obfuscator as observed in Wslink [[2]](#2), other options are available to them such as Themida, a commercial tool, and VMProtect, an open source tool.

## Methods

|Name|ID|Description|
|---|---|---|
|**Multiple VMs**|B0008.001|Multiple virtual machines with different architectures (CISC, RISC, etc.) can be used inside of a single executable in order to make reverse engineering even more difficult.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Locky Bart**](../xample-malware/locky-bart.md)|2017|--|Code virtualization is added to the Locky Bart binary using WPProtect. [[3]](#3)|

## References

<a name="1">[1]</a> D. Xu, J. Ming, Y. Fu, and D. Wu, "Verifiable Approach to Partially-Virtualized Binary Code Simplification," in 2018 ACM SIGSAC Conference on Computer and Communications Security (CCS ’18),Toronto, ON, Canada, pp. 442-458, [Online]. Available: https://doi.org/10.1145/3243734.3243827.

<a name="2">[2]</a> V. Hrčka, "Under the hood of Wslink’s multilayered virtual machine," welivesecurity.com, 28 March 2022. [Online]. Available: https://www.welivesecurity.com/2022/03/28/under-hood-wslink-multilayered-virtual-machine.

<a name="3">[3]</a> https://blog.malwarebytes.com/threat-analysis/2017/01/locky-bart-ransomware-and-backend-server-analysis/
