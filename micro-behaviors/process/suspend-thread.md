<table>
<tr>
<td><b>ID</b></td>
<td><b>C0055</b></td>
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


# Suspend Thread

This behavior is related to Unprotect technique U0101.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Dark Comet**](../../xample-malware/dark-comet.md)|2008|--|Dark Comet suspends threads. [[1]](#1)|
|[**GoBotKR**](../../xample-malware/gobotkr.md)|2019|--|GoBotKR suspends threads. [[1]](#1)|
|[**GravityRAT**](../../xample-malware/gravity-rat.md)|2018|--|GravityRAT suspends threads. [[1]](#1)|
|[**Hupigon**](../../xample-malware/hupigon.md)|2013|--|Hupigon suspends threads. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[suspend thread](https://github.com/mandiant/capa-rules/blob/master/host-interaction/thread/suspend/suspend-thread.yml)|Suspend Thread (C0055)|kernel32.SuspendThread, ntdll.NtSuspendThread, ntdll.ZwSuspendThread, System.Threading.Thread::Suspend, System.Threading.Thread::Sleep|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

