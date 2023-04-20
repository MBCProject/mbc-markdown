<table>
<tr>
<td><b>ID</b></td>
<td><b>B0045</b></td>
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
<td><b>26 June 2021</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>31 October 2022</b></td>
</tr>
</table>


# Data Flow Analysis Evasion

Malware code evades data flow analysis (also known as information flow analysis and taint-tracking).

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**SonicWall Malware**](../xample-malware/)|2023|B0045.001|This malware uses a large if/then/else clause to hide control depenence[[2]](#2)|

## Methods

|Name|ID|Description|
|---|---|---|
|**Control Dependence**|B0045.001|Data is propagated via an if-then-else clause instead of direct assignment.[[1]](#1)|
|**Implicit Flows**|B0045.002|Data is propagated via semantic relationships, for example one variable not changing its state could imply the state of another variable.[[1]](#1)|
|**Arbitrary Memory Corruption**|B0045.003|Data is propagated by corrupting memory, for example overwriting a region of stack space where a file pointer is held.[[1]](#1)|

## References

<a name="1">[1]</a> http://www.seclab.cs.sunysb.edu/seclab/pubs/antitaint.pdf
<a name="2">[1]</a> https://www.ironnet.com/blog/malware-analysis-nspps-a-go-rat-backdoor