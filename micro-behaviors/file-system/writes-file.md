<table>
<tr>
<td><b>ID</b></td>
<td><b>C0052</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../file-system">File System</a></b></td>
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
<td><b>4 December 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>30 April 2024</b></td>
</tr>
</table>


# Writes File

Malware writes to a file.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**CryptoLocker**](../../xample-malware/cryptolocker.md)|2013|--|CryptoLocker writes Fileon Windows. [[1]](#1)|
|[**Dark Comet**](../../xample-malware/dark-comet.md)|2008|--|Dark Comet writes Fileon Windows. [[1]](#1)|
|[**DNSChanger**](../../xample-malware/dnschanger.md)|2011|--|DNSChanger writes Fileon Windows. [[1]](#1)|
|[**Gamut**](../../xample-malware/gamut.md)|2014|--|Gamut writes files on Windows. [[1]](#1)|
|[**GravityRAT**](../../xample-malware/gravity-rat.md)|2018|--|GravityRAT writes files on Windows. [[1]](#1)|
|[**Hupigon**](../../xample-malware/hupigon.md)|2013|--|Hupigon writes files on Windows. [[1]](#1)|
|[**Locky Bart**](../../xample-malware/locky-bart.md)|2017|--|Locky Bart writes files on Windows. [[1]](#1)|
|[**Poison Ivy**](../../xample-malware/poison-ivy.md)|2005|--|Poison Ivy writes files on Windows. [[1]](#1)|
|[**Redhip**](../../xample-malware/redhip.md)|2011|--|Redhip writes files on Windows. [[1]](#1)|
|[**Rombertik**](../../xample-malware/rombertik.md)|2015|--|Rombertik writes files on Windows. [[1]](#1)|
|[**Shamoon**](../../xample-malware/shamoon.md)|2012|--|Shamoon writes files on Windows. [[1]](#1)|
|[**UP007**](../../xample-malware/up007.md)|2016|--|UP007 writes files on Windows. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[write file on Linux](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/write/write-file-on-linux.yml)|Writes File (C0052)|fputc, fputs, putc, write, fputwc, putwc, fputws, write, fwrite, putwchar|
|[write file on Windows](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/write/write-file-on-windows.yml)|Writes File (C0052)|kernel32.WriteFile, kernel32.WriteFileEx, NtWriteFile, ZwWriteFile, _fwrite, fwrite, System.IO.File::WriteAllBytes, System.IO.File::WriteAllBytesAsync, System.IO.File::WriteAllLines, System.IO.File::WriteAllLinesAsync, System.IO.File::WriteAllText, System.IO.File::WriteAllTextAsync, System.IO.File::AppendAllLines, System.IO.File::AppendAllLinesAsync, System.IO.File::AppendAllText, System.IO.File::AppendAllTextAsync, System.IO.File::AppendText, System.IO.FileInfo::AppendText|
|[create process memory minidump](https://github.com/mandiant/capa-rules/blob/master/host-interaction/process/dump/create-process-memory-minidump.yml)|Writes File (C0052)|dbghelp.MiniDumpWriteDump|

|Tool: CAPE|Class|Mapping|APIs|
|---|---|---|---|
|[upatre_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/upatre_files.py)|UpatreFiles|Writes File (C0052)|--|
|[wiper](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/wiper.py)|WiperZeroedBytes|Writes File (C0052)|NtWriteFile|
|[modifies_hostsfile](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/modifies_hostsfile.py)|Modifies_HostFile|Writes File (C0052)|--|
|[accesses_sysvol](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/accesses_sysvol.py)|WritesSysvol|Writes File (C0052)|--|
|[trojan_ursnif](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/trojan_ursnif.py)|UrsnifBehavior|Writes File (C0052)|--|
|[infostealer_poullight](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/infostealer_poullight.py)|PoullightFiles|Writes File (C0052)|--|
|[infostealer_echelon](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/infostealer_echelon.py)|EchelonFiles|Writes File (C0052)|--|
|[infostealer_apocalypse](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/infostealer_apocalypse.py)|ApocalypseStealerFileBehavior|Writes File (C0052)|--|
|[infostealer_masslogger](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/infostealer_masslogger.py)|MassLoggerVersion|Writes File (C0052)|NtWriteFile|
|[infostealer_masslogger](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/infostealer_masslogger.py)|MassLoggerArtifacts|Writes File (C0052)|FindFirstFileExW, CryptDecrypt|

### C0052 Snippet
<details>
<summary> File System::Writes File </summary>
SHA256: e5897829835f3e9fbab71674ca06f48ff127ec014d1629817f0566203c93b732
Location: 0x4016A7
<pre>
mov     r9, rdi         ; variable that will hold number of bytes actually written
mov     r8d, ebx        ; number of bytes to write
mov     param_2, rsi    ; pointer to buffer containing data that will be written to the file
mov     param_1, r12    ; handle to the device/file to write to
mov     qword ptr [rsp + local_58], 0x0 ; optional pointer to OVERLAPPED structure (in this case, it is NULL)
call    qword ptr [->KERNEL32.DLL::WriteFile] ; API call to write to file specified in param_1
</pre>
</details>

### C0052 Snippet
<details>
<summary> File System::Writes File </summary>
SHA256: e5897829835f3e9fbab71674ca06f48ff127ec014d1629817f0566203c93b732
Location: 0x4016A7
<pre>
mov     r9, rdi         ; variable that will hold number of bytes actually written
mov     r8d, ebx        ; number of bytes to write
mov     param_2, rsi    ; pointer to buffer containing data that will be written to the file
mov     param_1, r12    ; handle to the device/file to write to
mov     qword ptr [rsp + local_58], 0x0 ; optional pointer to OVERLAPPED structure (in this case, it is NULL)
call    qword ptr [->KERNEL32.DLL::WriteFile] ; API call to write to file specified in param_1
</pre>
</details>

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

