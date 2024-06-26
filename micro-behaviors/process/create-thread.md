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
<td><b>2.3</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>14 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>30 April 2024</b></td>
</tr>
</table>


# Create Thread

Malware creates a thread.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Dark Comet**](../../xample-malware/dark-comet.md)|2008|--|Dark Comet creates a thread. [[1]](#1)|
|[**GoBotKR**](../../xample-malware/gobotkr.md)|2019|--|GoBotKR creates a thread. [[1]](#1)|
|[**Hupigon**](../../xample-malware/hupigon.md)|2013|--|Hupigon creates a thread. [[1]](#1)|
|[**Locky Bart**](../../xample-malware/locky-bart.md)|2017|--|Locky Bart creates a thread. [[1]](#1)|
|[**Rombertik**](../../xample-malware/rombertik.md)|2015|--|Rombertik creates a thread. [[1]](#1)|
|[**Shamoon**](../../xample-malware/shamoon.md)|2012|--|Shamoon creates a thread. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[create thread](https://github.com/mandiant/capa-rules/blob/master/host-interaction/thread/create/create-thread.yml)|Create Thread (C0038)|kernel32.CreateThread, _beginthread, _beginthreadex, PsCreateSystemThread, SHCreateThread, SHCreateThreadWithHandle, kernel32.CreateRemoteThread, kernel32.CreateRemoteThreadEx, RtlCreateUserThread, ntdll.NtCreateThread, ntdll.NtCreateThreadEx, ntdll.ZwCreateThread, ntdll.ZwCreateThreadEx, pthread_create, System.Threading.Thread::Start, System.Threading.Thread::ctor|
|[spawn thread to RWX shellcode](https://github.com/mandiant/capa-rules/blob/master/load-code/shellcode/spawn-thread-to-rwx-shellcode.yml)|Create Thread (C0038)|--|

|Tool: CAPE|Class|Mapping|APIs|
|---|---|---|---|
|[injection_create_remote_thread](https://github.com/kevoreilly/CAPEv2/blob/master/modules/signatures/CAPE.py)|CAPE_InjectionCreateRemoteThread|Create Thread (C0038)|--|
|[antidebug_ntcreatethreadex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antidebug_ntcreatethreadex.py)|antidebug_ntcreatethreadex|Create Thread (C0038)|NtCreateThreadEx|
|[antidebug_ntsetinformationthread](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antidebug_ntsetinformationthread.py)|antidebug_ntsetinformationthread|Create Thread (C0038)|NtSetInformationThread|

### C0038 Snippet
<details>
<summary> Process::Create Thread </summary>
SHA256: 465d3aac3ca4daa9ad4de04fcb999f358396efd7abceed9701c9c28c23c126db
Location: 0x404915
<pre>
mov     param_2, dword ptr [ebp + param_4]
push    param_2 ; Pointer to location where thread handler will be returned
mov     param_2, dword ptr [ebp + param_5]
push    param_2 ; Flags controlling thread creation
push    param_1 ; Pointer to variable to be passed to thread
mov     param_1, FUN_004048b8
push    param_1 ; Pointer to function where thread will begin execution
push    esi     ; Size of stack for new thread
push    ebx     ; Pointer to security attributes for thread.  If null, the handle to the thread cannot be inherited
call    KERNEL32.DLL::CreateThread ; Call to thread creation API
</pre>
</details>


## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

