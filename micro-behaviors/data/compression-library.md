<table>
<tr>
<td><b>ID</b></td>
<td><b>C0060</b></td>
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
<td><b>17 January 2021</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>13 September 2023</b></td>
</tr>
</table>


# Compression Library


## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|--|DarkComet linked against ZLIB. [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Linked against ZLIB (This capa rule had 1 match) [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[linked against aPLib](https://github.com/mandiant/capa-rules/blob/master/linking/static/aplib/linked-against-aplib.yml)|Compression Library (C0060)| |
|[linked against ZLIB](https://github.com/mandiant/capa-rules/blob/master/linking/static/zlib/linked-against-zlib.yml)|Compression Library (C0060)| |

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

