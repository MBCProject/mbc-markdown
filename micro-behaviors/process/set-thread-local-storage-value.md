<table>
<tr>
<td><b>ID</b></td>
<td><b>C0041</b></td>
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


# Set Thread Local Storage Value

Malware allocates thread local storage. 

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Dark Comet**](../../xample-malware/dark-comet.md)|2008|--|Dark Comet sets thread local storage values. [[1]](#1)|
|[**Gamut**](../../xample-malware/gamut.md)|2014|--|Gamut sets thread local storage values. [[1]](#1)|
|[**Hupigon**](../../xample-malware/hupigon.md)|2013|--|Hupigon sets thread local storage values. [[1]](#1)|
|[**Kovter**](../../xample-malware/kovter.md)|2016|--|Kovter sets thread local storage values. [[1]](#1)|
|[**Redhip**](../../xample-malware/redhip.md)|2011|--|Redhip sets thread local storage values. [[1]](#1)|
|[**Rombertik**](../../xample-malware/rombertik.md)|2015|--|Rombertik sets thread local storage values. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[set thread local storage value](https://github.com/mandiant/capa-rules/blob/master/host-interaction/thread/tls/set-thread-local-storage-value.yml)|Set Thread Local Storage Value (C0041)|kernel32.TlsSetValue|

### C0041 Snippet
<details>
<summary> Process::Set Thread Local Storage Value </summary>
SHA256: 3ac8c22eb7c59d35fe49c20f2a0eca06765543dfb15f455a5557af4428066641
Location: 0x180005B08
<pre>
mov     param_2, rbx    ; Value to be stored in TLS index
mov     param_1, edi    ; TLS index
call    qword ptr [->KERNEL32.DLL::TlsSetValue] ; Call Windows API function to store value in thread's thread local storage (TLS) at the specified index
</pre>
</details>

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

