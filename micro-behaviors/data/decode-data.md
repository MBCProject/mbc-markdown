<table>
<tr>
<td><b>ID</b></td>
<td><b>C0053</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../data">Data</a></b></td>
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
<td><b>29 December 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>1 March 2023</b></td>
</tr>
</table>


# Decode Data

Malware may decode data.

## Methods

|Name|ID|Description|
|---|---|---|
|**Base64**|C0053.001|Malware may decode data using base64.|
|**XOR**|C0053.002|Malware may use XOR to decode data.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Snake**](../xample-malware/snake.md)|2004|C0053.001|Snake decodes data stored in base64 during the unpacking process [[1]](#1)|

## References

<a name="1">[1]</a> https://www.cybereason.com/blog/research/threat-analysis-report-snake-infostealer-malware
