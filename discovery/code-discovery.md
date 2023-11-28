<table>
<tr>
<td><b>ID</b></td>
<td><b>B0046</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../discovery">Discovery</a></b></td>
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
<td><b>10 November 2021</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>13 September 2023</b></td>
</tr>
</table>


# Code Discovery

Malware may inspect code or enumerate aspects.

## Methods

|Name|ID|Description|
|---|---|---|
|**Enumerate PE Sections**|B0046.001|Malware enumerates virtual offsets of code sections.|
|**Inspect Section Memory Permissions**|B0046.002|Malware identifies section memory permissions from image section header.|
|**Parse PE Header**|B0046.003|Malware parses the PE header.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|B0046.001|BlackEnergy enumerates PE sections. [[1]](#1)|
|[**CryptoLocker**](../xample-malware/cryptolocker.md)|2013|B0046.001|CryptoLocker enumerates PE sections. [[1]](#1)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|B0046.001|DarkComet enumerates PE sections. [[1]](#1)|
|[**Emotet**](../xample-malware/emotet.md)|2018|B0046.001|Emotet enumerates PE sections. [[1]](#1)|
|[**Gamut**](../xample-malware/gamut.md)|2014|B0046.001|Gamut enumerates PE sections. [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|B0046.001|Hupigon enumerates PE sections. [[1]](#1)|
|[**Locky Bart**](../xample-malware/locky-bart.md)|2017|B0046.001|Locky Bart enumerates PE sections. [[1]](#1)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|B0046.002|Redhip inspects section memory permissions. [[1]](#1)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|B0046.001|Stuxnet enumerates PE sections. [[1]](#1)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|B0046.002|TrickBot inspects section memory permissions. [[1]](#1)|
|[**Ursnif**](../xample-malware/ursnif.md)|2016|B0046.001|Ursnif enumerates PE sections. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[enumerate PE sections](https://github.com/mandiant/capa-rules/blob/master/load-code/pe/enumerate-pe-sections.yml)|Code Discovery::Enumerate PE Sections (B0046.001)|--|
|[inspect section memory permissions](https://github.com/mandiant/capa-rules/blob/master/load-code/pe/inspect-section-memory-permissions.yml)|Code Discovery::Inspect Section Memory Permissions (B0046.002)|--|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

