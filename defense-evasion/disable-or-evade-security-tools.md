<table>
<tr>
<td><b>ID</b></td>
<td><b>F0004</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../defense-evasion">Defense Evasion</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Impair Defenses: Disable or Modify Tools (<a href="https://attack.mitre.org/techniques/T1562/001">T1562.001</a>, <a href="https://attack.mitre.org/techniques/T1629/003/">T1629.003</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.1</b></td>
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


# Disable or Evade Security Tools

Malware may disable or evade security tools to avoid detection. Security tools include OS security features and updating tools, anti-virus (AV) tools, firewalls, tool components providing security related logging and/or reporting, and Antimalware Scan Interface (AMSI) related capabilities. This behavior is related to Unprotect technique U0508. 

Malware-related methods extending ATT&CK's definition are below. 

See ATT&CK: **Impair Defenses: Disable or Modify Tools ([T1562.001](https://attack.mitre.org/techniques/T1562/001), [T1629.003](https://attack.mitre.org/techniques/T1629/003/))**.

## Methods

|Name|ID|Description|
|---|---|---|
|**AMSI Bypass**|F0004.004|Malware bypasses AMSI (Anti-malware Scan Interface).|
|**Disable Kernel Patch Protection**|F0004.001|Bypasses or disables kernel patch protection mechanisms such as Windows' PatchGuard, enabling the malware instance to operate at the same level as the operating system kernel and kernel mode drivers (KMD).|
|**Disable System File Overwrite Protection**|F0004.002|Disables system file overwrite protection mechanisms such as Windows file protection, thereby enabling system files to be modified or replaced.|
|**Force Lazy Writing**|F0004.006|Some operating systems will sometimes use a form of "lazy writing" for disk I/O, which may obscure the true provenance of the write operation. This method occurs when code intentionally forces the operating system to perform a lazy writing operation. For example, in Windows, a file may be opened, memory mapped, and closed, but the memory map will still exist and can be written to, which will cause a lazy write that looks like it is coming from the System process. [[3]](#3)|
|**Heavens Gate**|F0004.008|Malware evades endpoint security products by invoking 64-bit code in 32-bit processes, effectively bypassing user-mode hooks. [[4]](#4)|
|**Modify Policy**|F0004.005|Malware may modify policies to make software less effective. This is similar to ATT&CK's Subvert Trust Controls: Code Signing Policy Modification ([T1553.006](https://attack.mitre.org/techniques/T1553/006/), [T1632.001](https://attack.mitre.org/techniques/T1632/001/))|
|**Unhook APIs**|F0004.003|Security products may hook APIs to monitor the behavior of malware. To avoid being found, malware may load DLLs in memory and overwrite their bytes.|
|**Bypass Windows File Protection**|F0004.007|Malware bypasses Windows file protection.|
|**Disable Code Integrity**|F0004.009|Malware disables Code Integrity driver.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**WebCobra**](../xample-malware/webcobra.md)|2018|--|Most security products hook some APIs to monitor the behavior of malware. To avoid being identified by this technique, WebCobra loads ntdll.dll and user32.dll as data files in memory and overwrites the first 8 bytes of those functions, which unhooks the APIs. [[1]](#1)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|--|The malware terminates the following anti-malware services: Window Defender, MBamService (Malwarebytes), SAVService (Sophos AV). [[6]](#6)|
|[**DNSChanger**](../xample-malware/dnschanger.md)|2011|--|DNSChanger prevents the infected system from installing anti-virus software updates. [[2]](#2)|
|[**Vobfus**](../xample-malware/vobfus.md)|2016|--|Vobfus uses GetModuleHandle API to check for the presence of Avast Antivirus. [[5]](#5)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[64-bit execution via heavens gate](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-disasm/64-bit-execution-via-heavens-gate.yml)|Disable or Evade Security Tools::Heavens Gate (F0004.008)|--|
|[patch Event Tracing for Windows function](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-av/patch-event-tracing-for-windows-function.yml)|Disable or Evade Security Tools (F0004)|kernel32.VirtualProtect, ntdll.NtProtectVirtualMemory, ZwProtectVirtualMemory|
|[block operations on executable memory pages using Arbitrary Code Guard](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-av/block-operations-on-executable-memory-pages-using-arbitrary-code-guard.yml)|Disable or Evade Security Tools::Modify Policy (F0004.005)|SetProcessMitigationPolicy|
|[protect spawned processes with mitigation policies](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-av/protect-spawned-processes-with-mitigation-policies.yml)|Disable or Evade Security Tools::Modify Policy (F0004.005)|UpdateProcThreadAttribute|
|[bypass Windows File Protection](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/windows-file-protection/bypass-windows-file-protection.yml)|Disable or Evade Security Tools::Bypass Windows File Protection (F0004.007)|--|
|[disable driver code integrity](https://github.com/mandiant/capa-rules/blob/master/host-interaction/driver/disable-driver-code-integrity.yml)|Disable or Evade Security Tools::Disable Code Integrity (F0004.009)|--|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[browser_security](https://github.com/CAPESandbox/community/tree/master/modules/signatures/browser_security.py)|Disable or Evade Security Tools (F0004)|--|
|[disables_notificationcenter](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_notificationcenter.py)|Disable or Evade Security Tools (F0004)|--|
|[clickfraud_volume](https://github.com/CAPESandbox/community/tree/master/modules/signatures/clickfraud_volume.py)|Disable or Evade Security Tools (F0004)|CoInternetSetFeatureEnabled|
|[volatility_svcscan_1](https://github.com/CAPESandbox/community/tree/master/modules/signatures/volatility_svcscan_1.py)|Disable or Evade Security Tools (F0004)|--|
|[volatility_svcscan_2](https://github.com/CAPESandbox/community/tree/master/modules/signatures/volatility_svcscan_2.py)|Disable or Evade Security Tools (F0004)|--|
|[antisandbox_suspend](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_suspend.py)|Disable or Evade Security Tools (F0004)|NtSuspendThread|
|[antiav_servicestop](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antiav_servicestop.py)|Disable or Evade Security Tools (F0004)|OpenServiceA, ControlService, OpenServiceW|
|[disables_security](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_security.py)|Disable or Evade Security Tools (F0004)|--|
|[antiav_whitespace](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antiav_whitespace.py)|Disable or Evade Security Tools (F0004)|--|
|[disables_smartscreen](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_smartscreen.py)|Disable or Evade Security Tools (F0004)|--|
|[disables_windows_file_protection](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_windows_file_protection.py)|Disable or Evade Security Tools (F0004)|--|
|[disables_winfirewall](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_winfirewall.py)|Disable or Evade Security Tools (F0004)|--|
|[disables_crashdumps](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_crashdumps.py)|Disable or Evade Security Tools (F0004)|--|
|[disables_app_launch](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_app_launch.py)|Disable or Evade Security Tools (F0004)|--|
|[disables_app_launch](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_app_launch.py)|Disable or Evade Security Tools::Modify Policy (F0004.005)|--|
|[clickfraud_cookies](https://github.com/CAPESandbox/community/tree/master/modules/signatures/clickfraud_cookies.py)|Disable or Evade Security Tools (F0004)|InternetSetOptionA|
|[disables_wfp](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_wfp.py)|Disable or Evade Security Tools (F0004)|NtWriteFile, CopyFileA, CopyFileExW, CopyFileW|
|[disables_wfp](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_wfp.py)|Disable or Evade Security Tools::Bypass Windows File Protection (F0004.007)|NtWriteFile, CopyFileA, CopyFileExW, CopyFileW|
|[modify_attachment_manager](https://github.com/CAPESandbox/community/tree/master/modules/signatures/modify_attachment_manager.py)|Disable or Evade Security Tools (F0004)|--|
|[modify_attachment_manager](https://github.com/CAPESandbox/community/tree/master/modules/signatures/modify_attachment_manager.py)|Disable or Evade Security Tools::Modify Policy (F0004.005)|--|
|[office_security](https://github.com/CAPESandbox/community/tree/master/modules/signatures/office_security.py)|Disable or Evade Security Tools (F0004)|--|
|[disables_event_logging](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_event_logging.py)|Disable or Evade Security Tools (F0004)|--|
|[antisandbox_unhook](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_unhook.py)|Disable or Evade Security Tools (F0004)|--|
|[antisandbox_unhook](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antisandbox_unhook.py)|Disable or Evade Security Tools::Unhook APIs (F0004.003)|--|
|[modify_security_center_warnings](https://github.com/CAPESandbox/community/tree/master/modules/signatures/modify_security_center_warnings.py)|Disable or Evade Security Tools (F0004)|--|
|[disables_wer](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_wer.py)|Disable or Evade Security Tools (F0004)|--|
|[disables_windows_defender](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_windows_defender.py)|Disable or Evade Security Tools (F0004)|--|
|[disables_windows_defender_dism](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_windows_defender_dism.py)|Disable or Evade Security Tools (F0004)|--|
|[disables_windows_defender_logging](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_windows_defender_logging.py)|Disable or Evade Security Tools (F0004)|--|
|[removes_windows_defender_contextmenu](https://github.com/CAPESandbox/community/tree/master/modules/signatures/removes_windows_defender_contextmenu.py)|Disable or Evade Security Tools (F0004)|--|
|[windows_defender_powershell](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows_defender_powershell.py)|Disable or Evade Security Tools (F0004)|--|
|[disables_browser_warn](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_browser_warn.py)|Disable or Evade Security Tools (F0004)|--|
|[antiav_srp](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antiav_srp.py)|Disable or Evade Security Tools (F0004)|--|
|[antiav_srp](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antiav_srp.py)|Disable or Evade Security Tools::Modify Policy (F0004.005)|--|
|[bypass_firewall](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bypass_firewall.py)|Disable or Evade Security Tools (F0004)|--|

## References

<a name="1">[1]</a> https://www.mcafee.com/blogs/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/

<a name="2">[2]</a> https://www.huffingtonpost.com/2011/11/09/click-hijack-hackers-online-ad-scam_n_1084497.html

<a name="3">[3]</a> Alexander Adamov, Stealthy WastedLocker: eluding behavior blockers, but not only. Online:   https://vb2020.vblocalhost.com/conference/presentations/stealthy-wastedlocker-eluding-behaviour-blockers-but-not-only/

<a name="4">[4]</a> Carl Petty, Red Canary, 3/3/2020. Online: https://redcanary.com/blog/heavens-gate-technique-on-linux/

<a name="5">[5]</a> https://securitynews.sonicwall.com/xmlpost/revisiting-vobfus-worm-mar-8-2013/

<a name="6">[6]</a> https://www.trendmicro.com/en_us/research/18/k/trickbot-shows-off-new-trick-password-grabber-module.html

