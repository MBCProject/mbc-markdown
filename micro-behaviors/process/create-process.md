<table>
<tr>
<td><b>ID</b></td>
<td><b>C0017</b></td>
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
<td><b>4 December 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>30 April 2024</b></td>
</tr>
</table>


# Create Process

Malware creates a process. 

## Methods

|Name|ID|Description|
|---|---|---|
|**Create Process via Shellcode**|C0017.001|Malware uses shellcode to create a process.|
|**Create Process via WMI**|C0017.002|Malware uses WMI to create a process.|
|**Create Suspended Process**|C0017.003|Malware created a suspended process.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Stuxnet**](../../xample-malware/stuxnet.md)|2010|C0017.002|Stuxnet will use WMI operations with the explorer.exe token in order to copy itself and execute on the remote share. [[1]](#1)|
|[**BlackEnergy**](../../xample-malware/blackenergy.md)|2007|--|BlackEnergy creates a process on Windows. [[2]](#2)|
|[**Dark Comet**](../../xample-malware/dark-comet.md)|2008|--|Dark Comet creates a process on Windows. [[2]](#2)|
|[**Gamut**](../../xample-malware/gamut.md)|2014|--|Gamut creates a process on Windows. [[2]](#2)|
|[**GoBotKR**](../../xample-malware/gobotkr.md)|2019|--|GoBotKR creates a process on Windows. [[2]](#2)|
|[**Hupigon**](../../xample-malware/hupigon.md)|2013|--|Hupigon creates a process on Windows. [[2]](#2)|
|[**Kovter**](../../xample-malware/kovter.md)|2016|--|Kovter creates a process on Windows. [[2]](#2)|
|[**Mebromi**](../../xample-malware/mebromi.md)|2011|--|Mebromi creates a process on Windows. [[2]](#2)|
|[**Redhip**](../../xample-malware/redhip.md)|2011|--|Redhip creates a process on Windows. [[2]](#2)|
|[**Redhip**](../../xample-malware/redhip.md)|2011|C0017.003|Redhip creates a suspended process. [[2]](#2)|
|[**Shamoon**](../../xample-malware/shamoon.md)|2012|--|Shamoon creates a process on Windows. [[2]](#2)|
|[**TrickBot**](../../xample-malware/trickbot.md)|2016|--|TrickBot creates a process on Windows. [[2]](#2)|
|[**TrickBot**](../../xample-malware/trickbot.md)|2016|C0017.003|TrickBot creates a suspended process. [[2]](#2)|
|[**UP007**](../../xample-malware/up007.md)|2016|--|The malware creates a process on Windows. [[2]](#2)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[create process on Windows](https://github.com/mandiant/capa-rules/blob/master/host-interaction/process/create/create-process-on-windows.yml)|Create Process (C0017)|kernel32.WinExec, kernel32.CreateProcess, shell32.ShellExecute, shell32.ShellExecuteEx, advapi32.CreateProcessAsUser, advapi32.CreateProcessWithLogon, advapi32.CreateProcessWithToken, kernel32.CreateProcessInternal, ntdll.NtCreateUserProcess, ntdll.NtCreateProcess, ntdll.NtCreateProcessEx, ntdll.ZwCreateProcess, ZwCreateProcessEx, ntdll.ZwCreateUserProcess, ntdll.RtlCreateUserProcess, System.Diagnostics.Process::Start|
|[create process on Linux](https://github.com/mandiant/capa-rules/blob/master/host-interaction/process/create/create-process-on-linux.yml)|Create Process (C0017)|execve, execl, execlp, execle, execv, execvp, execvpe, posix_spawn, posix_spawnp, popen, fork|
|[execute command](https://github.com/mandiant/capa-rules/blob/master/host-interaction/process/create/execute-command.yml)|Create Process (C0017)|system, _system, wsystem, _wsystem|
|[create a process with modified I/O handles and window](https://github.com/mandiant/capa-rules/blob/master/host-interaction/process/create/create-a-process-with-modified-io-handles-and-window.yml)|Create Process (C0017)|kernel32.CreateProcess, kernel32.CreateProcessInternal, advapi32.CreateProcessAsUser, advapi32.CreateProcessWithLogon, advapi32.CreateProcessWithToken, kernel32.GetStartupInfo, System.Diagnostics.Process::Start|
|[create process suspended](https://github.com/mandiant/capa-rules/blob/master/host-interaction/process/create/create-process-suspended.yml)|Create Process::Create Suspended Process (C0017.003)|kernel32.CreateProcess, advapi32.CreateProcessAsUser|

|Tool: CAPE|Class|Mapping|APIs|
|---|---|---|---|
|[stealth_system_procname](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/stealth_system_procname.py)|StealthSystemProcName|Create Process (C0017)|ShellExecuteExW, CreateProcessInternalW|
|[stack_pivot](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/stack_pivot.py)|StackPivotProcessCreate|Create Process (C0017)|CreateProcessInternalW,  NtCreateUserProcess|
|[wmi](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/wmi.py)|WMICreateProcess|Create Process:Create Process via WMI (C0017.002)| CreateProcessInternalW, NtCreateUserProcess|
|[script_downloader](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/script_downloader.py)|ScriptCreatedProcess|Create Process (C0017)|CreateProcessInternalW, NtCreateUserProcess|

### C0049 Snippet
<details>
<summary> Process::Create Process </summary>
SHA256: 465d3aac3ca4daa9ad4de04fcb999f358396efd7abceed9701c9c28c23c126db
Location: 0x458C26
<pre>
lea     param_1, [ebp + 0xfffffeb0]
push    param_1 ; pointer to PROCESS_INFORMATION struct to hold information about the new process
lea     param_1, [ebp + 0xfffffec0]
push    param_1 ; pointer to STARTUPINFO struct
push    0x0     ; path to directory for new process -- if null, use same directory as calling process
push    0x0     ; environment block for new process -- if null, use the calling process's environment block
push    0x4     ; process creation flags (CREATE_SUSPENDED in this case)
push    0x0     ; if heritable handles in the calling process should be inherited by the new process.  If false, inheritance will not occur.
push    0x0     ; security attributes for new process.  If null, child processes cannot inherit thread running new process
push    0x0     ; security attributes for new process.  If null, child processes cannot inherit handle for new process
mov     param_1, dword ptr [ebp + local_8]
call    FUN_00404dfc
push    param_1 ; command line for new process to execute
push    0x0     ; application name to be executed.  If null, use command line provided in another argument
call    KERNEL32.DLL::CreateProcessA    ; Call Windows API function to create new process
</pre>
</details>

## References

<a name="1">[1]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en

<a name="2">[2]</a> capa v4.0, analyzed at MITRE on 10/12/2022

