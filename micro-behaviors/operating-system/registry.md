<table>
<tr>
<td><b>ID</b></td>
<td><b>C0036</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../operating-system">Operating System</a></b></td>
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
<td><b>4 December 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>31 October 2022</b></td>
</tr>
</table>


# Registry

Malware modifies the registry. 

## Methods

|Name|ID|Description|
|---|---|---|
|**Create Registry Key**|C0036.004|Malware creates a registry key.|
|**Delete Registry Key**|C0036.002|Malware deletes a registry key.|
|**Delete Registry Value**|C0036.007|Malware deletes a registry value.|
|**Open Registry Key**|C0036.003|Malware opens a registry key.|
|**Query Registry Key**|C0036.005|Malware queries a registry key.|
|**Query Registry Value**|C0036.006|Malware queries a registry value.|
|**Set Registry Key**|C0036.001|Malware sets a registry key.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|C0036.005, C0036.006|Please see the BlackEnergy malware page for details. [[1]](#1)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|C0036.002, C0036.007, C0036.005, C0036.006, C0036.001|Please see the Dark Comet malware page for details. [[1]](#1)|
|[**DNSChanger**](../xample-malware/dnschanger.md)|2011|C0036.006, C0036.001|Please see the DNSChanger malware page for details. [[1]](#1)|
|[**Gamut**](../xample-malware/gamut.md)|2014|C0036.002, C0036.007, C0036.005, C0036.006, C0036.001|Please see the Gamut malware page for details. [[1]](#1)|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|C0036.006|Query or enumerate registry value (This capa rule had 1 match) [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|C0036.002, C0036.007, C0036.005, C0036.006, C0036.001|Please see the Hupigon malware page for details. [[1]](#1)|
|[**Kovter**](../xample-malware/kovter.md)|2016|C0036.004, C0036.006|Please see the Kovter malware page for details. [[1]](#1)|
|[**Locky Bart**](../xample-malware/locky-bart.md)|2017|C0036.001|Set registry value (This capa rule had 1 match) [[1]](#1)|
|[**Poison-Ivy**](../xample-malware/poison-ivy.md)|2005|C0036.006|Query or enumerate registry value (This capa rule had 1 match) [[1]](#1)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|C0036.002, C0036.006, C0036.001|Please see the Redhip malware page for details. [[1]](#1)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|C0036.002, C0036.006, C0036.001|Please see the Rombertik malware page for details. [[1]](#1)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|C0036.007, C0036.006|Please see the Shamoon malware page for details. [[1]](#1)|
|[**UP007 Malware Family**](../xample-malware/up007.md)|2016|C0036.006, C0036.001|Please see the UP007 Malware Family malware page for details. [[1]](#1)|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

