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
<td><b>2.1</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>4 December 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>24 May 2023</b></td>
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
|**Set Registry Value**|C0036.001|Malware sets a registry value.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|C0036.005|BlackEnergy queries or enumerates a registry key. [[1]](#1)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|C0036.006|BlackEnergy queries or enumerates a registry value. [[1]](#1)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|C0036.001|Dark Comet sets registry values. [[1]](#1)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|C0036.002|Dark Comet deletes registry keys. [[1]](#1)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|C0036.005|Dark Comet queries or enumerates registry keys. [[1]](#1)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|C0036.006|Dark Comet queries or enumerates registry values. [[1]](#1)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|C0036.007|Dark Comet deletes registry values. [[1]](#1)|
|[**DNSChanger**](../xample-malware/dnschanger.md)|2011|C0036.001|DNSChanger sets registry keys. [[1]](#1)|
|[**DNSChanger**](../xample-malware/dnschanger.md)|2011|C0036.006|DNSChanger queries or enumerates registry values. [[1]](#1)|
|[**Gamut**](../xample-malware/gamut.md)|2014|C0036.001|Gamut sets registry values. [[1]](#1)|
|[**Gamut**](../xample-malware/gamut.md)|2014|C0036.002|Gamut deletes registry keys. [[1]](#1)|
|[**Gamut**](../xample-malware/gamut.md)|2014|C0036.005|Gamut queries or enumerates registry keys. [[1]](#1)|
|[**Gamut**](../xample-malware/gamut.md)|2014|C0036.006|Gamut queries or enumerates registry values. [[1]](#1)|
|[**Gamut**](../xample-malware/gamut.md)|2014|C0036.007|Gamut deletes registry values. [[1]](#1)|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|C0036.006|GoBotKR queries or enumerates registry values. [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|C0036.001|Hupigon sets registry values. [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|C0036.002|Hupigon deletes registry keys. [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|C0036.005|Hupigon queries or enumerates registry keys. [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|C0036.006|Hupigon queries or enumerates registry values. [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|C0036.007|Hupigon deletes registry values. [[1]](#1)|
|[**Kovter**](../xample-malware/kovter.md)|2016|C0036.004|Kovter creates or opens registry keys. [[1]](#1)|
|[**Kovter**](../xample-malware/kovter.md)|2016|C0036.006|Kovter queries or enumerates registry values. [[1]](#1)|
|[**Locky Bart**](../xample-malware/locky-bart.md)|2017|C0036.001|Locky Bart sets registry values. [[1]](#1)|
|[**Poison Ivy**](../xample-malware/poison-ivy.md)|2005|C0036.006|Poison Ivy queries or enumerates registry values. [[1]](#1)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|C0036.001|Redhip set registry values. [[1]](#1)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|C0036.002|Redhip deletes registry keys. [[1]](#1)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|C0036.006|Redhip queries or enumerates registry values. [[1]](#1)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|C0036.001|Rombertik sets registry values. [[1]](#1)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|C0036.002|Rombertik deletes registry keys. [[1]](#1)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|C0036.006|Rombertik queries or enumerates registry values. [[1]](#1)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|C0036.006|Shamoon queries or enumerates registry values. [[1]](#1)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|C0036.007|Shamoon deletes registry values. [[1]](#1)|
|[**UP007**](../xample-malware/up007.md)|2016|C0036.001|UP007 sets registry values. [[1]](#1)|
|[**UP007**](../xample-malware/up007.md)|2016|C0036.006|UP007 queries or enumerates registry values. [[1]](#1)|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

