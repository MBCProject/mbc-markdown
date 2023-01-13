<table>
<tr>
<td><b>ID</b></td>
<td><b>C0025</b></td>
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
<td><b>13 October 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>31 October 2022</b></td>
</tr>
</table>


# Decompress Data

Malware may decompress data.

## Methods

|Name|ID|Description|
|---|---|---|
|**aPLib**|C0025.003|Malware decompresses data using aPLib.|
|**IEncodingFilterFactory**|C0025.002|Malware decompresses data using IEncodingFilterFactory.|
|**QuickLZ**|C0025.001|Malware decompresses data using QuickLZ.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Bagle**](../xample-malware/bagle.md)|2004|C0025.003|Decompress data using aPLib (This capa rule had 1 match) [[1]](#1)|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

