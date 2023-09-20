<table>
<tr>
<td><b>ID</b></td>
<td><b>C0018</b></td>
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
<td><b>14 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>13 September 2023</b></td>
</tr>
</table>


# Terminate Process

Malware terminates a process.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|--|BlackEnergy terminates a process via fastfail. [[1]](#1)|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|--|GoBotKR terminates processes. [[1]](#1)|
|[**GravityRAT**](../xample-malware/gravity-rat.md)|2018|--|GravityRAT terminates processes. [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Hupigon terminates processes. [[1]](#1)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|Kovter terminates processes. [[1]](#1)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|--|Shamoon terminates processes. [[1]](#1)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|--|Stuxnet terminates processes. [[1]](#1)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|--|TrickBot terminates processes. [[1]](#1)|
|[**UP007**](../xample-malware/up007.md)|2016|--|UP007 terminates processes. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[check mutex and exit](https://github.com/mandiant/capa-rules/blob/master/host-interaction/mutex/check-mutex-and-exit.yml)|Terminate Process (C0018)|ExitProcess, exit, _Exit, _exit, WaitForSingleObject, GetLastError|
|[terminate process via kill](https://github.com/mandiant/capa-rules/blob/master/host-interaction/process/terminate/terminate-process-via-kill.yml)|Terminate Process (C0018)|kill|
|[terminate process](https://github.com/mandiant/capa-rules/blob/master/host-interaction/process/terminate/terminate-process.yml)|Terminate Process (C0018)|System.Diagnostics.Process::Kill, System.Diagnostics.Process::WaitForExit, System.Diagnostics.Process::WaitForExitAsync, System.Environment::Exit, System.Windows.Forms.Application::Exit, kernel32.TerminateProcess, ntdll.NtTerminateProcess, kernel32.ExitProcess|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

