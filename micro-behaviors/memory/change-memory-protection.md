<table>
<tr>
<td><b>ID</b></td>
<td><b>C0008</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../memory">Memory</a></b></td>
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
<td><b>2 August 2022</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>5 December 2023</b></td>
</tr>
</table>


# Change Memory Protection

Malware may change memory protection. For example, read-write memory may be changed to read-execute. Changing memory protection may allow exploits (e.g., bypass Data Execution Prevention).

## Methods

|Name|ID|Description|
|---|---|---|
|**Executable Heap**|C0008.002|The heap is made executable.|
|**Executable Stack**|C0008.001|The stack is made executable.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Ursnif**](../../xample-malware/ursnif.md)|2016|--|The malware changes the PE header of the child process to enable write access to that page and writes 18 bytes of buffer at offset 0x40 from the start of svchost.exe in the target child process. The region protection is changed back to "read only" to avoid suspicion. [[1]](#1)|
|[**SYNful Knock**](../../xample-malware/synful-knock.md)|2015|--|SYNful Knock modifies the translation lookaside buffer (TLB) Read/Write attributes. [[2]](#2)|

## Detection

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[antidebug_guardpages](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antidebug_guardpages.py)|Change Memory Protection (C0008)|VirtualProtectEx, NtAllocateVirtualMemory, NtProtectVirtualMemory|

### C0008 Snippet
<details>
<summary> Memory::Change Memory Protection </summary>
SHA256: 905b9db8cf5a3001318b28ee5dc674f8f65ca1e4306aab9e331b3bba24e7b8a8
Location: 0x41AB74
<pre>
push    ecx     ; pointer to return value
push    0x40    ; new memory protection option to apply -- in this case, read, write, and execute permissions will be applied to the pages
mov     [DAT_01f56ff0], eax
mov     eax, [DAT_00492fc4]
push    edx     ; size of region to change access protection attributes (in bytes)
push    eax     ; Address of first page in region where access protection attributes are to be changed
; instructions from 0x41ab83 to 0x41abb4 omitted
call    dword ptr [->KERNEL32.DLL::VirtualProtect]      ; call function to change memory protection attributes
</pre>
</details>

## References

<a name="1">[1]</a> https://www.fireeye.com/blog/threat-research/2017/11/ursnif-variant-malicious-tls-callback-technique.html

<a name="2">[2]</a> https://www.mandiant.com/resources/synful-knock-acis

