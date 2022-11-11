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
<td><b>31 October 2022</b></td>
</tr>
</table>


# Create Mutex

Malware creates a mutex. 

## Use in Malware

|Name|Date|Description|
|---|---|---|
|[**Poison-Ivy**](../xample-malware/poison-ivy.md)|2005|Poison Ivy has a default process mutex, but can be altered at build time [2] [[1]](#1)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|Creates global mutexes signal that rootkit installation has occurred successfully  [[2]](#2)|

## References

<a name="1">[1]</a> https://www.mandiant.com/sites/default/files/2021-09/rpt-poison-ivy.pdf

<a name="2">[2]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en
