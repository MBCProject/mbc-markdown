
<table>
<tr>
<td><b>ID</b></td>
<td><b>B0024</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../execution">Execution</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
</table>


Prevent Concurrent Execution
============================
To avoid running multiple instances of itself, malware may check a system to see if it is already running.

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**Bagle**](../xample-malware/bagle.md)|2004|Some variants look for an unnamed mutex to ensure only one copy of itself is running on a system. [1](#1)|

References
----------
<a name="1">[1]</a> https://www.trendmicro.com/vinfo/us/threat-encyclopedia/archive/malware/worm_bagle.u
