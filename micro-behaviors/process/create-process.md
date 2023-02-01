<table>
<tr>
<td><b>ID</b></td>
<td><b>C0017</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../process">Process</a></b></td>
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
<td><b>21 November 2022</b></td>
</tr>
</table>


# Create Process

Malware creates a process. 

## Methods

|Name|ID|Description|
|---|---|---|
|**Create Process via Shellcode**|C0017.001|Malware uses shellcode to create a process.|
|**Create Process via WMI**|C0017.002|Malware uses WMI to create a process.|
|**Create Suspended Process**|C0017.003|Malware created a suspended process.|


## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|C0017.002|Stuxnet will use WMI operations with the explorere.exe token in order to copy itself and exscute on the remote share  [[1]](#1)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|--|Create process on Windows (This capa rule had 2 matches) [[2]](#2)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|--|Create process on Windows (This capa rule had 6 matches) [[2]](#2)|
|[**Gamut**](../xample-malware/gamut.md)|2014|--|Create process on Windows (This capa rule had 4 matches) [[2]](#2)|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|--|Create process on Windows (This capa rule had 4 matches) [[2]](#2)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Create process on Windows (This capa rule had 9 matches) [[2]](#2)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|Create process on Windows (This capa rule had 22 matches) [[2]](#2)|
|[**Mebromi**](../xample-malware/mebromi.md)|2011|--|Create process on Windows (This capa rule had 1 match) [[2]](#2)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|C0017, C0017.003|Please see the Redhip malware page for details. [[2]](#2)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|--|Create process on Windows (This capa rule had 2 matches) [[2]](#2)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|C0017, C0017.003|Please see the TrickBot malware page for details. [[2]](#2)|
|[**UP007 Malware Family**](../xample-malware/up007.md)|2016|--|Create process on Windows (This capa rule had 3 matches) [[2]](#2)|

## References

<a name="1">[1]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en

<a name="2">[2]</a> capa v4.0, analyzed at MITRE on 10/12/2022

