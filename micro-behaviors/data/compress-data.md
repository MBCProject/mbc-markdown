<table>
<tr>
<td><b>ID</b></td>
<td><b>C0024</b></td>
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
<td><b>5 December 2023</b></td>
</tr>
</table>


# Compress Data

Malware may compress data.

## Methods

|Name|ID|Description|
|---|---|---|
|**IEncodingFilterFactory**|C0024.002|Malware compresses data using IEncodingFilterFactory.|
|**QuickLZ**|C0024.001|Malware compresses data using QuickLZ.|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[compress data via WinAPI](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/compression/compress-data-via-winapi.yml)|Compress Data (C0024)|RtlDecompressBuffer, RtlDecompressBufferEx, RtlDecompressBufferEx2, RtlCompressBuffer, RtlCompressBufferLZNT1|
|[compress data via ZLIB inflate or deflate](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/compression/compress-data-via-zlib-inflate-or-deflate.yml)|Compress Data (C0024)|--|
|[compress data using LZO](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/compression/compress-data-using-lzo.yml)|Compress Data (C0024)|--|
