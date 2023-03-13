<table>
<tr>
<td><b>ID</b></td>
<td><b>C0041</b></td>
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


# Set Thread Local Storage Value

Malware allocates thread local storage. 

This micro behavior is a lower level counterpart to ATT&CK's [**Process Injection::Thread Local Storage (T1055.005)**](https://attack.mitre.org/techniques/T1055/005) technique.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|--|Set thread local storage value (This capa rule had 1 match) [[1]](#1)|
|[**Gamut**](../xample-malware/gamut.md)|2014|--|Set thread local storage value (This capa rule had 1 match) [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Set thread local storage value (This capa rule had 1 match) [[1]](#1)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|Set thread local storage value (This capa rule had 3 matches) [[1]](#1)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|--|Set thread local storage value (This capa rule had 1 match) [[1]](#1)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|--|Set thread local storage value (This capa rule had 1 match) [[1]](#1)|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

