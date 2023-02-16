<table>
<tr>
<td><b>ID</b></td>
<td><b>C0032</b></td>
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


# Checksum

Malware may derive a checksum from some block of data. The checksum is often used for data validation.

## Methods

|Name|ID|Description|
|---|---|---|
|**Adler**|C0032.005|Malware computes an Adler checksum.|
|**BSD**|C0032.003|Malware computes a BSD checksum.|
|**CRC32**|C0032.001|Malware computes a CRC32 checksum.|
|**Luhn**|C0032.002|Malware uses Luhn algorithm, often to validate identification numbers (e.g, credit card number).| 

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|C0032.001|Dark Comet hashes data with CRC32. [[1]](#1)|
|[**Gamut**](../xample-malware/gamut.md)|2014|C0032.001|Gamut hashes data with CRC32. [[1]](#1)|
|[**Locky Bart**](../xample-malware/locky-bart.md)|2017|C0032.001|Hash data with CRC32 (This capa rule had 2 matches) [[1]](#1)|
|[**UP007 Malware Family**](../xample-malware/up007.md)|2016|C0032.001|Hash data with CRC32 (This capa rule had 1 match) [[1]](#1)|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

