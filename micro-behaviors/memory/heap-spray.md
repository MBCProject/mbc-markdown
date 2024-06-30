<table>
<tr>
<td><b>ID</b></td>
<td><b>C0006</b></td>
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
<td><b>2.1</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>14 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>5 December 2023</b></td>
</tr>
</table>


# Heap Spray

Malware may use heap spraying to write a sequence of bytes on the heap section of a process.

## Detection

|Tool: CAPE|Class|Mapping|APIs|
|---|---|---|---|
|[exploit_heapspray](https://github.com/CAPESandbox/community/tree/master/modules/signatures/exploit_heapspray.py)|ExploitHeapspray|Heap Spray (C0006)|NtAllocateVirtualMemory|

