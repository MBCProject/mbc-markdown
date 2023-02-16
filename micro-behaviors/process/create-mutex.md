<table>
<tr>
<td><b>ID</b></td>
<td><b>C0042</b></td>
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


# Create Mutex

Malware creates a mutex. 

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Poison-Ivy**](../xample-malware/poison-ivy.md)|2005|--|Poison Ivy has a default process mutex, but can be altered at build time. [[1]](#1)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|--|Malware creates global mutexes signal that rootkit installation has occurred successfully. [[2]](#2)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Hupigon creates a mutex. [[3]](#3)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|Kovter creates a mutex. [[3]](#3)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|--|Redhip creates a mutex. [[3]](#3)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|--|Rombertik creates a mutex. [[3]](#3)|


## References

<a name="1">[1]</a> https://www.mandiant.com/sites/default/files/2021-09/rpt-poison-ivy.pdf

<a name="2">[2]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en

<a name="3">[3]</a> capa v4.0, analyzed at MITRE on 10/12/2022
