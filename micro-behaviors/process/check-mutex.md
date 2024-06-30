<table>
<tr>
<td><b>ID</b></td>
<td><b>C0043</b></td>
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


# Check Mutex

Malware checks a mutex. 

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Poison Ivy**](../../xample-malware/poison-ivy.md)|2005|--|Poison Ivy variant checks if the wireshark-is-running{} named mutex object exists. [[1]](#1)|
|[**Matanbuchus**](../../xample-malware/matanbuchus.md)|2021|--|Malware checks if multiple instances of the same mutex is running. If multiple instances are running, the malware exits. [[2]](#2) [[3]](#3)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[check mutex](https://github.com/mandiant/capa-rules/blob/master/host-interaction/mutex/check-mutex.yml)|Check Mutex (C0043)|kernel32.OpenMutex, System.Threading.Mutex::OpenExisting, System.Threading.Mutex::TryOpenExisting, kernel32.GetLastError|
|[check mutex and exit](https://github.com/mandiant/capa-rules/blob/master/host-interaction/mutex/check-mutex-and-exit.yml)|Check Mutex (C0043)|ExitProcess, exit, _Exit, _exit, WaitForSingleObject, GetLastError|

|Tool: CAPE|Class|Mapping|APIs|
|---|---|---|---|
|[antivm_vpc_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_vpc_mutex.py)|VPCDetectMutex|Check Mutex (C0043)|--|
|[antisandbox_sboxie_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antisandbox_sboxie_mutex.py)|AntisandboxSboxieMutex|Check Mutex (C0043)|--|
|[antivm_vmware_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_vmware_mutexes.py)|VMwareDetectMutexes|Check Mutex (C0043)|--|
|[infostealer_purplewave](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/infostealer_purplewave.py)|PurpleWaveMutexes|Check Mutex (C0043)|--|
|[antisandbox_sboxie_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antisandbox_sboxie_mutex.py)|AntisandboxSboxieMutex|Check Mutex (C0043)|--|

### C0043 Snippet
<details>
<summary> Process::Check Mutex </summary>
SHA256: 0b8e662e7e595ef56396a298c367b74721d66591d856e8a8241fcdd60d08373c
Location: 0x40294C
<pre>
  push    eax     ; name of mutex to be opened
push    0x0     ; whether to allow processes created by the process which owns the mutex to inherit it (false)
push    0x1f0001        ; mutex access rights (MUTEX_ALL_ACCESS)
call    dword ptr [->KERNEL32.DLL::OpenMutexW]  ; call function to open mutex
test    eax, eax        ; test to see if previous function call returned 0
jz      LAB_00402976    ; if it returned zero (error), jump to new memory location and execute from that point
</pre>
</details>

## References

<a name="1">[1]</a> https://www.fortinet.com/blog/threat-research/deep-analysis-of-new-poison-ivy-variant

<a name="2">[2]</a> https://www.0ffset.net/reverse-engineering/matanbuchus-loader-analysis/

<a name="3">[3]</a> https://www.cyberark.com/resources/threat-research-blog/inside-matanbuchus-a-quirky-loader
