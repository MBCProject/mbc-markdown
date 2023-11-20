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
<td><b>13 September 2023</b></td>
</tr>
</table>


# Set Thread Local Storage Value

Malware allocates thread local storage. 

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|--|Dark Comet sets thread local storage values. [[1]](#1)|
|[**Gamut**](../xample-malware/gamut.md)|2014|--|Gamut sets thread local storage values. [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Hupigon sets thread local storage values. [[1]](#1)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|Kovter sets thread local storage values. [[1]](#1)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|--|Redhip sets thread local storage values. [[1]](#1)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|--|Rombertik sets thread local storage values. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[set thread local storage value](https://github.com/mandiant/capa-rules/blob/master/host-interaction/process/set-thread-local-storage-value.yml)|Set Thread Local Storage Value (C0041)|kernel32.TlsSetValue|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

