<table>
<tr>
<td><b>ID</b></td>
<td><b>E1113</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../collection">Collection</a>, <a href="../credential-access">Credential Access</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Screen Capture (<a href="https://attack.mitre.org/techniques/T1113/">T1113</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.3</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>27 April 2024</b></td>
</tr>
</table>


# Screen Capture

Malware takes screen captures of the desktop. This technique is often used by cyber attackers to gather sensitive information, such as login credentials, personal data, or confidential documents. The malware can use various methods to capture the screen, including using built-in functions of the operating system or third-party libraries. The captured screenshots are then typically sent back to the attacker's command and control server. This technique is commonly used by spyware, information stealers, and advanced persistent threats (APTs).

See ATT&CK: **Screen Capture ([T1113](https://attack.mitre.org/techniques/T1113/))**.

## Methods

|Name|ID|Description|
|---|---|---|
|**WinAPI**|E1113.m01|Screen is captured using WinAPI functions (e.g., user32.GetDesktopWindow).|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|--|GoBotKR is capable of capturing screenshots. [[1]](#1)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|--|BlackEnergy's screenshot plugin allows for collection of screenshots. [[2]](#2)|
|[**DarkComet**](../xample-malware/dark-comet.md)|2008|E1113.m01|DarkComet can take screenshots of the victim's computer. [[3]](#3) [[5]](#5)|
|[**CHOPSTICK**](../xample-malware/chopstick.md)|2015|--|CHOPSTICK takes snapshots of deskop and window contents. [[4]](#4)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|E1113.m01|Malware captures screenshots. [[5]](#5)|
|[**Kovter**](../xample-malware/kovter.md)|2016|E1113.m01|Malware captures screenshots. [[5]](#5)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|E1113.m01|Malware captures screenshots. [[5]](#5)|
|[**Snake**](../xample-malware/snake.md)|2004|--|Malware captures screenshots. [[6]](#6)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[capture screenshot](https://github.com/mandiant/capa-rules/blob/master/collection/screenshot/capture-screenshot.yml)|Screen Capture::WinAPI (E1113.m01)|user32.GetWindowDC, user32.GetDC, gdi32.CreateDC, gdi32.BitBlt, gdi32.GetDIBits, gdi32.CreateCompatibleDC, gdi32.CreateCompatibleBitmap, user32.GetSystemMetrics = fetch screen dimensions, user32.GetDesktopWindow = get entire desktop, BitBlt, System.Drawing.Graphics::CopyFromScreen|
|[capture screenshot via keybd event](https://github.com/mandiant/capa-rules/blob/master/collection/screenshot/capture-screenshot-via-keybd-event.yml)|Screen Capture (E1113)|--|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[poullight_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/infostealer_poullight.py)|Screen Capture (E1113)|--|
|[captures_screenshot](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/infostealer_screenshot.py)|Screen Capture (E1113)|LdrGetProcedureAddress, NtCreateFile|

### E1113.m01 Snippet
<details>
<summary> Collection::Screen Capture::WinAPI </summary>
SHA256: c6930e298bba86c01d0fe2c8262c46b4fce97c6c5037a193904cfc634246fbec
Location: 0x4036de
<pre>
push    0xcc0020        ; Raster operation code to copy the source rectangle directly onto the destination rectangle
push    0x0     ; y-coordinate of upper left corner of source rectangle
push    0x0     ; x-coordinate of upper left corner of source rectangle
push    dword ptr [esi] ; handle to source device
push    eax     ; height of source/destination rectangles
mov     eax, dword ptr [esi + 0xc]
sub     eax, param_2
sub     param_2, ebx
push    eax     ; width of source/destination rectangles
push    param_1 ; y-coordinate of upper left corner of destination rectangle
push    param_2 ; x-coordinate of upper left corner of destination rectangle
push    dword ptr [ebp + local_28]      ; handle to destingation device
call    dword ptr [->GDI32.DLL::BitBlt] ; Windows API function to transfer a rectangle of pixels from one device to another
</pre>
</details>

## References

<a name="1">[1]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="2">[2]</a> https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/

<a name="3">[3]</a> https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/

<a name="4">[4]</a> https://web.archive.org/web/20210307034415/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf

<a name="5">[5]</a> capa v4.0, analyzed at MITRE on 10/12/2022

<a name="6">[6]</a> https://www.cybereason.com/blog/research/threat-analysis-report-snake-infostealer-malware

