<table>
<tr>
<td><b>ID</b></td>
<td><b>E1056</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../collection">Collection</a>, <a href="../credential-access">Credential Access</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Input Capture (<a href="https://attack.mitre.org/techniques/T1056">T1056</a>, <a href="https://attack.mitre.org/techniques/T1417/">T1417</a>)</b></td>
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
<td><b>5 December 2023</b></td>
</tr>
</table>


# Input Capture

Malware may record user inputs, typically without the user's knowledge. This is often used to capture sensitive information such as usernames, passwords, credit card numbers, and other personal data. The most common form of input capture is keylogging, where the malware records every keystroke made on a device. However, it can also involve capturing mouse clicks, touch screen interactions, or even voice inputs. The captured data is then usually transmitted to the attacker for use in further malicious activities like identity theft or unauthorized access.

See ATT&CK: **Input Capture ([T1056](https://attack.mitre.org/techniques/T1056), [T1417](https://attack.mitre.org/techniques/T1417/))**.

## Methods

|Name|ID|Description|
|---|---|---|
|**Mouse Events**|E1056.m01|Mouse events are captured.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|--|The malware injects itself into a browser and captures user input data. [[1]](#1)|
|[**Ursnif**](../xample-malware/ursnif.md)|2016|--|The malware injects HTML into a browser session to collect sensitive online banking information when the victim performs their online banking. [[2]](#2)|
|[**Poison Ivy**](../xample-malware/poison-ivy.md)|2005|--|Poison Ivy can capture audio and video. [[4]](#4)|
|[**Clipminer**](../xample-malware/clipminer.md)|2011|--|Clipminer monitors keyboard and mouse activity to determine if the machine is in use. [[5]](#5)|
|[**ElectroRAT**](../xample-malware/electrorat.md)|2020|--|ElectroRat monitors keyboard and mouse activity to determine whether the machine is in use. [[6]](#6)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[use .NET library SharpClipboard](https://github.com/mandiant/capa-rules/blob/master/collection/use-dotnet-library-sharpclipboard.yml)|Input Capture (E1056)|--|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[antisandbox_mouse_hook](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_mouse_hook.py)|Input Capture (E1056)|SetWindowsHookExA, SetWindowsHookExW|
|[antisandbox_mouse_hook](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_mouse_hook.py)|Input Capture::Mouse Events (E1056.m01)|SetWindowsHookExA, SetWindowsHookExW|
|[browser_scanbox](https://github.com/CAPESandbox/community/tree/master/modules/signatures/browser_scanbox.py)|Input Capture (E1056)|JsEval, COleScript_ParseScriptText, COleScript_Compile|

## References

<a name="1">[1]</a> https://blogs.cisco.com/security/talos/rombertik

<a name="2">[2]</a> https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/BKDR_URSNIF.SM?_ga=2.129468940.1462021705.1559742358-1202584019.1549394279

<a name="3">[3]</a> https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/clipminer-bitcoin-mining-hijacking

<a name="4">[4]</a> https://www.cyber.nj.gov/threat-center/threat-profiles/trojan-variants/poison-ivy

<a name="5">[5]</a> https://www.mandiant.com/sites/default/files/2021-09/rpt-poison-ivy.pdf

<a name="6">[6]</a> https://www.intezer.com/blog/research/operation-electrorat-attacker-creates-fake-companies-to-drain-your-crypto-wallets/

