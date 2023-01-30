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


# Prevent Concurrent Execution

To avoid running multiple instances of itself, malware may check a system to see if it is already running.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Bagle**](../xample-malware/bagle.md)|2004|--|Some variants look for an unnamed mutex to ensure only one copy of itself is running on a system. [[1]](#1)|

## References

<a name="1">[1]</a> https://www.trendmicro.com/vinfo/us/threat-encyclopedia/archive/malware/worm_bagle.u
