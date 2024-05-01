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
<td><b>2.2</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>14 January 2021</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>30 April 2024</b></td>
</tr>
</table>


# Resume Thread

Malware resumes a thread.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**CryptoLocker**](../../xample-malware/cryptolocker.md)|2013|--|CryptoLocker resumes thread. [[1]](#1)|
|[**Dark Comet**](../../xample-malware/dark-comet.md)|2008|--|Dark Comet resumes a thread. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[resume thread](https://github.com/mandiant/capa-rules/blob/master/host-interaction/thread/resume/resume-thread.yml)|Resume Thread (C0054)|kernel32.ResumeThread, ntdll.NtResumeThread, ntdll.ZwResumeThread, System.Threading.Thread::Resume|

### C0054 Snippet
<details>
<summary> Process::Resume Thread </summary>
SHA256: 465d3aac3ca4daa9ad4de04fcb999f358396efd7abceed9701c9c28c23c126db
Location: 0x41B345
<pre>
push    esi     ; Where to store return value
mov     ebx, param_1
mov     param_1, dword ptr [ebx + 0x4]
push    param_1 ; Handle to thread to resume
call    KERNEL32.DLL::ResumeThread      ; API call to resume thread
</pre>
</details>


## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

