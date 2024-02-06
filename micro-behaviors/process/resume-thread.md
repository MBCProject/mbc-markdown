<table>
<tr>
<td><b>ID</b></td>
<td><b>C0054</b></td>
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
<td><b>2.1</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>14 January 2021</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>6 February 2024</b></td>
</tr>
</table>


# Resume Thread

Malware resumes a thread.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**CryptoLocker**](../xample-malware/cryptolocker.md)|2013|--|CryptoLocker resumes thread. [[1]](#1)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|--|Dark Comet resumes a thread. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[resume thread](https://github.com/mandiant/capa-rules/blob/master/host-interaction/thread/resume/resume-thread.yml)|Resume Thread (C0054)|kernel32.ResumeThread, ntdll.NtResumeThread, ntdll.ZwResumeThread, System.Threading.Thread::Resume|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

