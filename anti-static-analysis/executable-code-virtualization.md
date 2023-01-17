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
<td><b>21 November 2022</b></td>
</tr>
</table>


# Executable Code Virtualization

Original executable code is virtualized by translating the code into a special format that only a special virtual machine (VM) can run; the VM uses a customized virtual instruction set. A "stub" function calls the VM when the code is run. Virtualized code makes static analysis and reverse engineering more difficult; dumped code won’t run without the VM.

Virtualized code is a software protection technique. Themida is a commercial tool; VMProtect is an open source tool. [[1]](#1) 

## Methods

|Name|ID|Description|
|---|---|---|
|**Multiple VMs**|B0008.001|Multiple virtual machines with different architectures (CISC, RISC, etc.) can be used inside of a single executable in order to make reverse engineering even more difficult.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Locky Bart**](../xample-malware/locky-bart.md)|2017|--|Code virtualization is added to the Locky Bart binary using WPProtect. [[2]](#2)|

## References

<a name="1">[1]</a> https://github.com/xiaoweime/WProtect

<a name="2">[2]</a> https://blog.malwarebytes.com/threat-analysis/2017/01/locky-bart-ransomware-and-backend-server-analysis/
