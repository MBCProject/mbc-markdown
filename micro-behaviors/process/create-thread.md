<table>
<tr>
<td><b>ID</b></td>
<td><b>C0038</b></td>
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
<td><b>14 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>5 December 2023</b></td>
</tr>
</table>


# Create Thread

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|--|Dark Comet creates a thread. [[1]](#1)|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|--|GoBotKR creates a thread. [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Hupigon creates a thread. [[1]](#1)|
|[**Locky Bart**](../xample-malware/locky-bart.md)|2017|--|Locky Bart creates a thread. [[1]](#1)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|--|Rombertik creates a thread. [[1]](#1)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|--|Shamoon creates a thread. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[create thread](https://github.com/mandiant/capa-rules/blob/master/host-interaction/thread/create/create-thread.yml)|Create Thread (C0038)|kernel32.CreateThread, _beginthread, _beginthreadex, PsCreateSystemThread, SHCreateThread, SHCreateThreadWithHandle, kernel32.CreateRemoteThread, kernel32.CreateRemoteThreadEx, RtlCreateUserThread, ntdll.NtCreateThread, ntdll.NtCreateThreadEx, ntdll.ZwCreateThread, ntdll.ZwCreateThreadEx, pthread_create, System.Threading.Thread::Start, System.Threading.Thread::ctor|
|[spawn thread to RWX shellcode](https://github.com/mandiant/capa-rules/blob/master/load-code/shellcode/spawn-thread-to-rwx-shellcode.yml)|Create Thread (C0038)|--|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[injection_create_remote_thread](https://github.com/kevoreilly/CAPEv2/blob/master/modules/signatures/CAPE.py)|Create Thread (C0038)|--|
|[antidebug_ntcreatethreadex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antidebug_ntcreatethreadex.py)|Create Thread (C0038)|NtCreateThreadEx|
|[antidebug_ntsetinformationthread](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antidebug_ntsetinformationthread.py)|Create Thread (C0038)|NtSetInformationThread|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

