<table>
<tr>
<td><b>ID</b></td>
<td><b>C0040</b></td>
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


# Allocate Thread Local Storage

Malware allocates thread local storage. 

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Kovter**](../../xample-malware/kovter.md)|2016|--|Kovter allocates thread local storage. [[1]](#1)|
|[**Shamoon**](../../xample-malware/shamoon.md)|2012|--|Shamoon allocates thread local storage. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[allocate thread local storage](https://github.com/mandiant/capa-rules/blob/master/host-interaction/process/allocate-thread-local-storage.yml)|Allocate Thread Local Storage (C0040)|kernel32.TlsAlloc|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

