<table>
<tr>
<td><b>ID</b></td>
<td><b>C0011</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../communication">Communication</a></b></td>
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
<td><b>14 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>1 March 2023</b></td>
</tr>
</table>


# DNS Communication

The DNS Communication micro-behavior focuses on DNS communication. 

## Methods

|Name|ID|Description|
|---|---|---|
|**DDNS Domain Connect**|C0011.003|Connects to dynamic DNS domain.|
|**Resolve**|C0011.001|Resolves a domain.|
|**Resolve Free Hosting Domain**|C0011.005|Resolves a free hosting domain (e.g., freeiz.com).|
|**Resolve TLD**|C0011.004|Resolves top level domain.|
|**Server Connect**|C0011.002|Connects to DNS server.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|C0011.001|Hupigon resolves DNS. [[1]](#1)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|C0011.001|Shamoon resolves DNS. [[1]](#1)|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

