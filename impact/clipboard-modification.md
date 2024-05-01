<table>
<tr>
<td><b>ID</b></td>
<td><b>E1510</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../impact">Impact</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Clipboard Data (<a href="https://attack.mitre.org/techniques/T1115/">T1115</a>), Data Manipulation: Transmitted Data Manipulation (<a href="https://attack.mitre.org/techniques/T1641/001/">T1641.001</a>)</b></td>
</tr>
<tr>
<td><b>Impact Type</b></td>
<td><b>Integrity</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>3.1</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>4 December 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>12 February 2024</b></td>
</tr>
</table>


# Clipboard Modification

ATT&CK defines Clipboard Modification as a Mobile technique (Android platform). MBC extends it to the Windows platform.

After E1510 was defined, T1510 was replaced by T1641.001, and Clipboard Data (<a href="https://attack.mitre.org/techniques/T1115/">T1115</a>) was updated to include content modification.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Clipminer**](../xample-malware/clipminer.md)|2011|--|Clipminer monitors the clipboard for cryptocurrency addresses and replaces them with ones controlled by the adversary. [[1]](#1)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|--|The malware writes clipboard data.  [[2]](#2)|
|[**Emotet**](../xample-malware/emotet.md)|2018|--|Emotet writes clipboard data. [[2]](#2)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Hupigon replaces clipboard data. [[2]](#2)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|--|The malware replaces clipboard data. [[2]](#2)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[write clipboard data](https://github.com/mandiant/capa-rules/blob/master/host-interaction/clipboard/write-clipboard-data.yml)|Clipboard Modification (E1510)|user32.EmptyClipboard, System.Windows.Forms.Clipboard::Clear, user32.SetClipboardData, System.Windows.Forms.Clipboard::SetAudio, System.Windows.Forms.Clipboard::SetData, System.Windows.Forms.Clipboard::SetDataObject, System.Windows.Forms.Clipboard::SetFileDropList, System.Windows.Forms.Clipboard::SetImage, System.Windows.Forms.Clipboard::SetText|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[set_clipboard_data](https://github.com/CAPESandbox/community/tree/master/modules/signatures/set_clipboard_data.py)|Clipboard Modification (E1510)|SetClipboardData|

### E1510 Snippet
<details>
<summary> Impact::Clipboard Modification </summary>
SHA256: 0b8e662e7e595ef56396a298c367b74721d66591d856e8a8241fcdd60d08373c
Location: 0x402C0F
<pre>
push    0x0     ; associate clipboard with current task
call    dword ptr [->USER32.DLL::OpenClipboard] ; call function to open clipboard
test    eax, eax        ; test if the clipboard open returned 0
jz      LAB_00402c70    ; if the clipboard open operation returned 0 (failed), jump to another instruction and execute from that point
call    dword ptr [->USER32.DLL::EmptyClipboard]        ; call function to empty the clipboard
lea     eax, [esi * 0x2 + 0x2]
push    eax     ; Number of bytes of heap memory to allocate
push    0x2042  ; Memory allocation attributes.  Notably, 0x2000 is deprecated and only intended for use with 16-bit Windows and will be ignored, so the actual argument is 0x0042, which allocates moveable memory and initializes the contents to zero
call    dword ptr [->KERNEL32.DLL::GlobalAlloc] ; Allocates heap memory
mov     esi, eax        ; store pointer to allocated memory in esi
test    esi, esi        ; test to see if NULL (0) returned, indicating an error with allocation
jz      LAB_00402c6a    ; if error occurred, jump to memory address and begin execution there
push    esi     ; pass newly-allocated memory to lock function
call    dword ptr [->KERNEL32.DLL::GlobalLock]  ; lock the allocated heap memory
test    eax, eax        ; test to see if lock returned NULL (0), indicating an error occurred
jz      LAB_00402c6a    ; if an error occurred, jump to memory address and begin execution there
push    dword ptr [esp + local_26c]     ; number of characters that can be stored in the provided buffer
push    eax     ; buffer that will hold converted string
push    -0x1    ; size of the string to process.  -1 indicates that the input ends with a null-terminating character, so to process up through that point
push    edi     ; pointer to string to convert
push    0x0     ; conversion type flags (must be 0 for UTF-8)
push    0xfde9  ; code to use for conversion.  In this case, 65001 indicates UTF-8
call    dword ptr [->KERNEL32.DLL::MultiByteToWideChar] ; call function to map string from UTF-8 to UTF-16
push    esi     ; pointer to heap memory to unlock
call    dword ptr [->KERNEL32.DLL::GlobalUnlock]        ; call function to unlock heap memory
push    esi     ; handle to heap memory that will be written to clipboard
push    0xd     ; type of data to write (0xd indicates unicode)
call    dword ptr [->USER32.DLL::SetClipboardData]      ; call function to write data to clipboard
call    dword ptr [->USER32.DLL::CloseClipboard]        ; close the clipboard
</pre>
</details>

## References

<a name="1">[1]</a> https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/clipminer-bitcoin-mining-hijacking

<a name="2">[2]</a> capa v4.0, analyzed at MITRE on 10/12/2022

