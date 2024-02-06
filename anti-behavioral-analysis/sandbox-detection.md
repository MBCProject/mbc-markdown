<table>
<tr>
<td><b>ID</b></td>
<td><b>B0007</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../anti-behavioral-analysis">Anti-Behavioral Analysis</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Virtualization/Sandbox Evasion: System Checks (<a href="https://attack.mitre.org/techniques/T1497/001/">T1497.001</a>, <a href="https://attack.mitre.org/techniques/T1633/001/">T1633.001</a>), Virtualization/Sandbox Evasion: User Activity Based Checks (<a href="https://attack.mitre.org/techniques/T1497/002/">T1497.002</a>)</b></td>
</tr>
<tr>
<td><b>Anti-Analysis Type</b></td>
<td><b>Detection</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.2</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>6 February 2024</b></td>
</tr>
</table>

# Sandbox Detection

Malware checks whether it is being executed inside an instrumented and isolated sandbox (test) environment. In performing reconnaissance of its environment, the malware will check a variety of user or system based artifacts. Examples include monitoring for user action as reflected by mouse clicks or timing checks [[1]](#1), [[2]](#2). Upon detection of the sandbox, conditional execution will change the malware’s behavior. For example, execution may terminate, or activity may appear benign, e.g., connecting to a benign domain. 

The related **Virtualization/Sandbox Evasion ([T1497](https://attack.mitre.org/techniques/T1497/), [T1633](https://attack.mitre.org/techniques/T1633/))** ATT&CK techniques were defined subsequent to this MBC behavior.
 
## Methods

|Name|ID|Description|
|---|---|---|
|**Check Clipboard Data**|B0007.001|Checks clipboard data which can be used to detect whether execution is inside a sandbox.|
|**Check Files**|B0007.002|Sandboxes create files on the file system. Malware can check the different folders to find sandbox artifacts.|
|**Human User Check**|B0007.003|Detects whether there is any "user" activity on the machine, such as the movement of the mouse cursor, non-default wallpaper, or recently opened Office files. Directories or file might be counted. If there is no human activity, the machine is suspected to be a virtualized machine and/or sandbox. Other items used to detect a user: mouse clicks (single/double), DialogBox, scrolling, color of background pixel [[5]](#5). This method is similar to ATT&CK's [Virtualization/Sandbox Evasion: User Activity Based Checks](https://attack.mitre.org/techniques/T1497/002/) sub-technique. This method is also related to Unprotect techniques U1316 and U1317.|
|**Injected DLL Testing**|B0007.004|Testing for the name of a particular DLL that is known to be injected by a sandbox for API hooking is a common way of detecting sandbox environments. This can be achieved through the kernel32!GetModuleHandle API call and other means.|
|**Product Key/ID Testing**|[B0007.005](#b0007005-snippet)|Checking for a particular product key/ID associated with a sandbox environment (commonly associated with the Windows host OS used in the environment) can be used to detect whether a malware instance is being executed in a particular sandbox. This can be achieved through several means, including testing for the Key/ID in the Windows registry.|
|**Screen Resolution Testing**|B0007.006|Sandboxes aren't used in the same manner as a typical user environment, so most of the time the screen resolution stays at the minimum 800x600 or lower. No one is actually working on a such small screen. Malware could potentially detect the screen resolution to determine if it's a user machine or a sandbox. This method is related to Unprotect technique U1315.|
|**Self Check**|B0007.007|Malware may check its own characteristics to determine whether it's running in a sandbox. For example, a malicious Office document might check its file name or VB project name. This method is related to Unprotect technique U1303.|
|**Timing/Date Check**|B0007.008|Calling GetSystemTime or equiv and only executing code if the current date/hour/minute/second passes some check. Often this is for running only after or only until a specific date. This behavior can be mitigated in non-automated analysis environments. This method is related to Unprotect technique U1005.|
|**Timing/Uptime Check**|B0007.009|Comparing single GetTickCount with some value to see if system has been started at least *X* amount ago. This behavior can be mitigated in non-automated analysis environments.|
|**Test API Routines**|B0007.010|Calls Windows API routines with invalid arguments to identify error supression.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Redhip**](../xample-malware/redhip.md)|2011|B0007.005|Redhip detects publicly available automated analysis workbenches (e.g., Joe Box) by considering OS product keys and special DLLs and checks for sandboxes and AV modules. [[3]](#3)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|B0007.010|The malware checks for sandboxes that suppress errors returned from API routine calls the using ZwGetWriteWatch routine. [[4]](#4)|
|[**Terminator**](../xample-malware/terminator.md)|2013|--|The Terminator RAT evades a sandbox by not executing until after a reboot. Most sandboxes don't reboot during an analysis. [[6]](#6)|
|[**Ursnif**](../xample-malware/ursnif.md)|2016|B0007.007|Ursnif uses malware macros to evade sandbox detection - checking whether the filename contains only hexadecimal characters before the extension. [[10]](#10)|
|[**GotBotKR**](../xample-malware/gobotkr.md)|2019|--|GoBotKR performs several checks on the compromised machine to avoid being emulated or executed in a sandbox. [[7]](#7)|
|[**EvilBunny**](../xample-malware/evilbunny.md)|2011|--|EvilBunny hooks time retrieval APIs and calls each API twice to calculate a delta. Execution aborts depending on the delta value. [[8]](#8)|
|[**Vobfus**](../xample-malware/vobfus.md)|2016|--|Vobfus uses GetModuleHandle API to check for the presence of a sandbox. [[9]](#9)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[check for microsoft office emulation](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-vm/vm-detection/check-for-microsoft-office-emulation.yml)|Sandbox Detection::Product Key/ID Testing (B0007.005)|CreateFile|
|[check for sandbox and av modules](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-av/check-for-sandbox-and-av-modules.yml)|Sandbox Detection (B0007)|GetModuleHandle|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[antisandbox_joe_anubis_files.py](https://github.com/kevoreilly/community/blob/master/modules/signatures/antisandbox_joe_anubis_files.py)|Sandbox Detection::Check Files (B0007.002)|--|
|[antisandbox_cuckoo_files](https://github.com/kevoreilly/community/blob/master/modules/signatures/antisandbox_cuckoo_files.py)|Sandbox Detection::Check Files (B0007.002)|--|
|[antisandbox_cuckoo_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_cuckoo_files.py)|Sandbox Detection (B0007)|--|
|[antisandbox_cuckoo_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_cuckoo_files.py)|Sandbox Detection::Check Files (B0007.002)|--|
|[antisandbox_threattrack_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_threattrack_files.py)|Sandbox Detection (B0007)|--|
|[antisandbox_threattrack_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_threattrack_files.py)|Sandbox Detection::Check Files (B0007.002)|--|
|[antisandbox_sleep](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_sleep.py)|Sandbox Detection (B0007)|NtDelayExecution|
|[antisandbox_sleep](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_sleep.py)|Sandbox Detection::Timing/Date Check (B0007.008)|NtDelayExecution|
|[antisandbox_mouse_hook](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_mouse_hook.py)|Sandbox Detection (B0007)|SetWindowsHookExA, SetWindowsHookExW|
|[antisandbox_mouse_hook](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_mouse_hook.py)|Sandbox Detection::Human User Check (B0007.003)|SetWindowsHookExA, SetWindowsHookExW|
|[antisandbox_foregroundwindows](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_foregroundwindows.py)|Sandbox Detection (B0007)|GetForegroundWindow, NtDelayExecution|
|[antisandbox_sboxie_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_sboxie_mutex.py)|Sandbox Detection (B0007)|--|
|[antisandbox_script_timer](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_script_timer.py)|Sandbox Detection (B0007)|--|
|[antisandbox_sboxie_libs](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_sboxie_libs.py)|Sandbox Detection (B0007)|LdrGetDllHandle, LdrLoadDll|
|[antisandbox_cuckoocrash](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_cuckoocrash.py)|Sandbox Detection (B0007)|--|
|[antisandbox_joe_anubis_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_joe_anubis_files.py)|Sandbox Detection (B0007)|--|
|[antisandbox_joe_anubis_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_joe_anubis_files.py)|Sandbox Detection::Check Files (B0007.002)|--|
|[antisandbox_fortinet_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_fortinet_files.py)|Sandbox Detection (B0007)|--|
|[antisandbox_fortinet_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_fortinet_files.py)|Sandbox Detection::Check Files (B0007.002)|--|
|[antisandbox_sunbelt_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_sunbelt_files.py)|Sandbox Detection (B0007)|--|
|[antisandbox_sunbelt_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_sunbelt_files.py)|Sandbox Detection::Check Files (B0007.002)|--|
|[antisandbox_sboxie_objects](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_sboxie_objects.py)|Sandbox Detection (B0007)|NtOpenDirectoryObject|
|[antisandbox_sunbelt_libs](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_sunbelt_libs.py)|Sandbox Detection (B0007)|LdrGetDllHandle, LdrLoadDll|
|[antisandbox_cuckoo](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_cuckoo.py)|Sandbox Detection (B0007)|--|

## Code Snippets

### B0007.005 Snippet
<details>
<summary> Sandbox Detection::Product Key/ID Testing </summary>
<pre>
asm
push    ebx
add     esp, 0FFFFFEF4h
xor     ebx, ebx
push    esp             ; phkResult
push    1               ; samDesired
push    0               ; ulOptions
push    offset SubKey   ; "Software\Microsoft\Windows\CurrentVersi"...
push    80000002h       ; hKey
call    RegOpenKeyExA
test    eax, eax
jnz     short loc_405387
mov     [esp+110h+cbData], 101h
lea     eax, [esp+110h+cbData]
push    eax             ; lpcbData
lea     eax, [esp+114h+Data]
push    eax             ; lpData
push    0               ; lpType 
push    0               ; lpReserved
push    offset ValueName ; "ProductId"
mov     eax, [esp+124h+hKey]
push    eax             ; hKey
call    RegQueryValueExA
lea     eax, [esp+110h+Data]
cmp     eax, offset a55274640267306 ; "55274-640-2673064-23950"
jnz     short loc_405387
mov     bl, 1
</pre>
</details>

## References

<a name="1">[1]</a> Check Point Research,"CP<r>: Evasion Techniques," evasions.checkpoint.com, [Online]. Available: https://evasions.checkpoint.com.

<a name="2">[2]</a> Splunk Threat Research Team,"From Macros to No Macros: Continuous Malware Improvements by QakBot," Splunk, blog,, 01 December 2022. [Online]. Available: https://www.splunk.com/en_us/blog/security/from-macros-to-no-macros-continuous-malware-improvements-by-qakbot.html.

<a name="3">[3]</a> https://web.archive.org/web/20200815134441/https://www.fireeye.com/blog/threat-research/2011/01/the-dead-giveaways-of-vm-aware-malware.html 

<a name="4">[4]</a> https://blogs.cisco.com/security/talos/rombertik

<a name="5">[5]</a> https://github.com/LordNoteworthy/al-khaser

<a name="6">[6]</a> https://www.fireeye.com/content/dam/fireeye-www/current-threats/pdfs/pf/file/fireeye-hot-knives-through-butter.pdf

<a name="7">[7]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="8">[8]</a> https://web.archive.org/web/20150311013500/http://www.cyphort.com/evilbunny-malware-instrumented-lua/

<a name="9">[9]</a> https://securitynews.sonicwall.com/xmlpost/revisiting-vobfus-worm-mar-8-2013/

<a name="10">[10]</a> https://www.proofpoint.com/us/threat-insight/post/ursnif-banking-trojan-campaign-sandbox-evasion-techniques
