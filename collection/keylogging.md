<table>
<tr>
<td><b>ID</b></td>
<td><b>F0002</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../collection">Collection</a>, <a href="../credential-access">Credential Access</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Input Capture: Keylogging (<a href="https://attack.mitre.org/techniques/T1056/001">T1056.001</a>, <a href="https://attack.mitre.org/techniques/T1417/001/">T1417.001</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.2</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>14 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>6 February 2024</b></td>
</tr>
</table>


# Keylogging

Malware captures user keyboard input.

See ATT&CK: **Input Capture: Keylogging ([T1056.001](https://attack.mitre.org/techniques/T1056/001), [T1417.001](https://attack.mitre.org/techniques/T1417/001/))**

## Methods

|Name|ID|Description|
|---|---|---|
|**Application Hook**|F0002.001|Keystrokes are captured with an application hook.|
|**Polling**|F0002.002|Keystrokes are captured via polling (e.g., user32.GetAsyncKeyState, user32.GetKeyState).|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Certain variants of the malware may have keylogging functionality. [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|F0002.002|Malware logs keystrokes via polling. [[9]](#9)|
|[**UP007**](../xample-malware/up007.md)|2016|--|The malware logs keystrokes to a file. [[2]](#2)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|--|BlackEnergy's keylogger plugin allows for the collection of keystrokes. [[3]](#3)|
|[**DarkComet**](../xample-malware/dark-comet.md)|2008|--|DarkComet can capture keystrokes.  [[4]](#4)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|F0002.002|Malware logs keystrokes via polling. [[9]](#9)|
|[**Poison Ivy**](../xample-malware/poison-ivy.md)|2005|--|Poison Ivy can capture keystrokes.  [[5]](#5)|
|[**CHOPSTICK**](../xample-malware/chopstick.md)|2015|--|CHOPSTICK collects user keystrokes. [[6]](#6)|
|[**Kovter**](../xample-malware/kovter.md)|2016|F0002.002|Malware logs keystrokes via polling. [[9]](#9)|
|[**Redhip**](../xample-malware/redhip.md)|2011|F0002.001|Malware logs keystrokes via application hook. [[9]](#9)|
|[**Redhip**](../xample-malware/redhip.md)|2011|F0002.002|Malware logs keystrokes via polling. [[9]](#9)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|F0002.002|Malware logs keystrokes via polling. [[9]](#9)|
|[**Ursnif**](../xample-malware/ursnif.md)|2016|F0002.002|Malware logs keystrokes via polling. [[9]](#9)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[log keystrokes via polling](https://github.com/mandiant/capa-rules/blob/master/collection/keylog/log-keystrokes-via-polling.yml)|Keylogging::Polling (F0002.002)|user32.GetAsyncKeyState, user32.GetKeyState, user32.GetKeyboardState, user32.VkKeyScan, user32.VkKeyScanEx, user32.GetKeyNameText|
|[log keystrokes via application hook](https://github.com/mandiant/capa-rules/blob/master/collection/keylog/log-keystrokes-via-application-hook.yml)|Keylogging::Application Hook (F0002.001)|--|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[infostealer_keylog](https://github.com/CAPESandbox/community/tree/master/modules/signatures/infostealer_keylog.py)|Keylogging (F0002)|SetWindowsHookExA, GetAsyncKeyState, SetWindowsHookExW|
|[infostealer_keylog](https://github.com/CAPESandbox/community/tree/master/modules/signatures/infostealer_keylog.py)|Keylogging::Application Hook (F0002.001)|SetWindowsHookExA, GetAsyncKeyState, SetWindowsHookExW|
|[browser_scanbox](https://github.com/CAPESandbox/community/tree/master/modules/signatures/browser_scanbox.py)|Keylogging (F0002)|JsEval, COleScript_ParseScriptText, COleScript_Compile|

### F0002.002 Snippet
<details>
<summary> Collection::Keylogging::Polling </summary>
SHA256: 000b535ab2a4fec86e2d8254f8ed65c6ebd37309ed68692c929f8f93a99233f6
  
Location: 0x438af1
<pre>
push    0x11    ; provide argument for function call.  In this case, 0x11 is the Windows keyboard code for indicating the 'CTRL' key
call    USER32.DLL::GetKeyState ; call function to get the state of the control key
test    ax, 0x8000      ; test to see what the previous function returned.  In this case, we are seeing if the return value's high-order bit is a 1, which would mean the ctrl key is pressed
setnz   al      ; if the previous condition is not met (the zero flag is 1), a 1 is stored in byte al
</pre>
</details>

## References

<a name="1">[1]</a> https://www.f-secure.com/v-descs/backdoor_w32_hupigon.shtml

<a name="2">[2]</a> https://citizenlab.ca/2016/04/between-hong-kong-and-burma/

<a name="3">[3]</a> https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/

<a name="4">[4]</a> https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/

<a name="5">[5]</a> https://www.cyber.nj.gov/threat-center/threat-profiles/trojan-variants/poison-ivy

<a name="6">[6]</a> https://web.archive.org/web/20210307034415/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf

<a name="7">[7]</a> capa v4.0, analyzed at MITRE on 10/12/2022

<a name="8">[8]</a> https://www.mandiant.com/sites/default/files/2021-09/rpt-poison-ivy.pdf

<a name="9">[9]</a> capa v4.0, analyzed at MITRE on 10/12/2022

