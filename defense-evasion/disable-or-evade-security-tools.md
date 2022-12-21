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
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>21 November 2022</b></td>
</tr>
</table>


# Disable or Evade Security Tools

Malware may disable or evade security tools to avoid detection. Security tools include OS security features and updating tools, anti-virus (AV) tools, firewalls, tool components providing security related logging and/or reporting, and Antimalware Scan Interface (AMSI) related capabilities. 

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
|[**WebCobra**](../xample-malware/webcobra.md)|2018|--|WebCobra loads ntdll.dll and user32.dll as data files in memory and overwrites the first 8 bytes of those functions, which unhooks the APIs. [[1]](#1)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|--|Trojan spyware program that has mainly been used for targeting banking sites.|
|[**DNSChanger**](../xample-malware/dnschanger.md)|2011|--|DNSChanger prevents the infected system from installing anti-virus software updates. [[2]](#2)|
|[**Vobfus**](../xample-malware/vobfus.md)|2016|--|Vobfus uses GetModuleHandle API to check for presence of Avast Antivirus. [[5]](#5)|

## References

<a name="1">[1]</a> https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/

<a name="2">[2]</a> https://www.huffingtonpost.com/2011/11/09/click-hijack-hackers-online-ad-scam_n_1084497.html

<a name="3">[3]</a> Alexander Adamov, Stealthy WastedLocker: eluding behavior blockers, but not only. Online:   https://vblocalhost.com/conference/presentations/stealthy-wastedlocker-eluding-behaviour-blockers-but-not-only/

<a name="4">[4]</a> Carl Petty, Red Canary, 3/3/2020. Online: https://redcanary.com/blog/heavens-gate-technique-on-linux/

<a name="5">[5]</a> https://securitynews.sonicwall.com/xmlpost/revisiting-vobfus-worm-mar-8-2013/