<table>
<tr>
<td><b>ID</b></td>
<td><b>C0064</b></td>
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
<td><b>4 December 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>30 April 2024</b></td>
</tr>
</table>


# Enumerate Threads

Malware enumerates threads. 

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[enumerate threads](https://github.com/mandiant/capa-rules/blob/master/host-interaction/thread/list/enumerate-threads.yml)|Enumerate Threads (C0064)|kernel32.Thread32First, kernel32.Thread32Next, kernel32.CreateToolhelp32Snapshot|

### C0064 Snippet
<details>
<summary> Process::Enumerate Threads </summary>
SHA256: 3ac8c22eb7c59d35fe49c20f2a0eca06765543dfb15f455a5557af4428066641
Location: 0x180003675
<pre>
lea     rdx, [rsp + 0x48]       ; pointer to THREAD32ENTRY struct
mov     rcx, r15        ; handle to snapshot of system processes
call    qword ptr [->KERNEL32.DLL::Thread32First]      ; Windows API call to retrieve information about the first thread in a snapshot
lea     rdx, [rsp + 0x48]
mov     rcx, r15
call    qword ptr [->KERNEL32.DLL::Thread32Next]       ; takes the same arguments as Thread32First and gets the next thread from the snapshot
</pre>
</details>
