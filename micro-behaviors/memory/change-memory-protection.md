<table>
<tr>
<td><b>ID</b></td>
<td><b>C0008</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../memory">Memory</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>2 August 2022</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>21 November 2022</b></td>
</tr>
</table>


# Change Memory Protection

Malware may change memory protection. For example, read-write memory may be changed to read-execute. Changing memory protection may allow exploits (e.g., bypass Data Execution Prevention).

## Methods

|Name|ID|Description|
|---|---|---|
|**Executable Heap**|C0008.002|The heap is made executable.|
|**Executable Stack**|C0008.001|The stack is made executable.|


## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Ursnif**](../../xample-malware/ursnif.md)|2016|--|The malware changes the PE header of the child process to enable write access to that page and writes 18 bytes of buffer at offset 0x40 from the start of svchost.exe in the target child process. The region protection is changed back to "read only" to avoid suspicion. [[1]](#1)|
|[**SYNful Knock**](../../xample-malware/synful-knock.md)|2015|--|SYNful Knock modifies the translation lookaside buffer (TLB) Read/Write attributes. [[2]](#2)|


## References

<a name="1">[1]</a> https://www.fireeye.com/blog/threat-research/2017/11/ursnif-variant-malicious-tls-callback-technique.html

<a name="2">[2]</a> https://www.mandiant.com/resources/synful-knock-acis

