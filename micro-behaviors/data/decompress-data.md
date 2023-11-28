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
<td><b>13 September 2023</b></td>
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
|[**Bagle**](../xample-malware/bagle.md)|2004|C0025.003|Bagle decompresses data using aPLib. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[decompress data using aPLib](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/compression/decompress-data-using-aplib.yml)|Decompress Data::aPLib (C0025.003)|--|
|[decompress data via IEncodingFilterFactory](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/compression/decompress-data-via-iencodingfilterfactory.yml)|Decompress Data::IEncodingFilterFactory (C0025.002)|ole32.CoCreateInstance|
|[decompress data using LZO](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/compression/decompress-data-using-lzo.yml)|Decompress Data (C0025)|--|
|[decompress data using QuickLZ](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/compression/decompress-data-using-quicklz.yml)|Decompress Data::QuickLZ (C0025.001)|--|
|[decompress data using UCL](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/compression/decompress-data-using-ucl.yml)|Decompress Data (C0025)|--|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[compression](https://github.com/kevoreilly/CAPEv2/blob/master/modules/signatures/CAPE.py)|Decompress Data (C0025)|RtlDecompressBuffer|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

