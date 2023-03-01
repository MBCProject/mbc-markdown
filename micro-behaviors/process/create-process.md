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
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|C0017.002|Stuxnet will use WMI operations with the explorer.exe token in order to copy itself and execute on the remote share. [[1]](#1)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|--|BlackEnergy creates a process on Windows. [[2]](#2)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|--|Dark Comet creates a process on Windows. [[2]](#2)|
|[**Gamut**](../xample-malware/gamut.md)|2014|--|Gamut creates a process on Windows. [[2]](#2)|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|--|GoBotKR creates a process on Windows. [[2]](#2)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Hupigon creates a process on Windows. [[2]](#2)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|Kovter creates a process on Windows. [[2]](#2)|
|[**Mebromi**](../xample-malware/mebromi.md)|2011|--|Mebromi creates a process on Windows. [[2]](#2)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|--|Redhip creates a process on Windows. [[2]](#2)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|C0017.003|Redhip creates a suspended process. [[2]](#2)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|--|Shamoon creates a process on Windows. [[2]](#2)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|--|TrickBot creates a process on Windows. [[2]](#2)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|C0017.003|TrickBot creates a suspended process. [[2]](#2)|
|[**UP007**](../xample-malware/up007.md)|2016|--|The malware creates a process on Windows. [[2]](#2)|


## References

<a name="1">[1]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en

<a name="2">[2]</a> capa v4.0, analyzed at MITRE on 10/12/2022

