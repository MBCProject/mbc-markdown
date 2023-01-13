<table>
<tr>
<td><b>ID</b></td>
<td><b>F0012</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../persistence">Persistence</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder (<a href="https://attack.mitre.org/techniques/T1547/001/">T1547.001</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>2 August 2022</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>21 November 2022</b></td>
</tr>
</table>


# Registry Run Keys / Startup Folder

Malware may add an entry to the Windows Registry run keys or startup folder to enable persistence. [[1]](#1)

See ATT&CK: **Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder ([T1547.001](https://attack.mitre.org/techniques/T1547/001/))**. 

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|F0012|Trojan spyware program that has mainly been used for targeting banking sites. [[15]](#15)|
|[**Poison-Ivy**](../xample-malware/poison-ivy.md)|2005|F0012|After the Poison-Ivy server is running on the target machine, the attacker can use a Windows GUI client to control the target computer. [[2]](#2)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|F0012, E1547.001|Please see the Hupigon malware page for details. [[3]](#3)|
|[**Terminator**](../xample-malware/terminator.md)|May 2013|F0012|The Terminator rat sets "2019" as Windows' startup folder by modifying a registry value. [[4]](#4)|
|[**CryptoLocker**](../xample-malware/cryptolocker.md)|2013|F0012|The malware creates an "autorun" registry key [[5]](#5)|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|F0012| GoBotKR installs itself under registry run keys to establish persistence. [[6]](#6)|
|[**Kovter**](../xample-malware/kovter.md)|2016|F0012|The malware writes an autorun registry entry [[7]](#7)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|F0012|The malware will proceed to install itself in order to ensure persistence across system reboots before continuing on to execute the payload. To install itself, Rombertik first creates a VBS script named “fgf.vbs”, which is used to kick off Rombertik every time the user logs in, and places the script into the user’s Startup folder. [[8]](#8)|
|[**Ursnif**](../xample-malware/ursnif.md)|2016|F0012|Adds registry entries to ensure automatic execution at every system startup  [[9]](#9)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|F0012|BlackEnergy 3 variant drops its main DLL component and then creates a .lnk shortcut to that file in the startup folder  [[10]](#10)|
|[**Conficker**](../xample-malware/conficker.md)|2008|F0012|To start itself at system boot, the virus saces a copy of its DLL form to a random filename in the Windows system folder, then adds registry keys to have svchost.exe invoke that DLL as an invisible network service  [[11]](#11)|
|[**Emotet**](../xample-malware/emotet.md)|2018|F0012|To start itself at system boot, Emotet adds the downloaded payload to the registry to maintain persistence [[13]](#13)|
|[**Bagle**](../xample-malware/bagle.md)|2004|F0012|Adds registry keys to enable its automatic execution at every system startup  [[14]](#14)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|F0012|Adds several registry entries to enable automatic execution at startup  [[12]](#12)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|E1547.001|Persist via Run registry key (This capa rule had 4 matches) [[16]](#16)|

## References

<a name="1">[1]</a> https://threatvector.cylance.com/en_us/home/windows-registry-persistence-part-2-the-run-keys-and-search-order.html

<a name="2">[2]</a> https://www.cyber.nj.gov/threat-profiles/trojan-variants/poison-ivy

<a name="3">[3]</a> https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/HUPIGON

<a name="4">[4]</a> https://www.fireeye.com/content/dam/fireeye-www/current-threats/pdfs/pf/file/fireeye-hot-knives-through-butter.pdf

<a name="5">[5]</a> https://www.secureworks.com/research/cryptolocker-ransomware

<a name="6">[6]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="7">[7]</a> https://blog.malwarebytes.com/threat-analysis/2016/07/untangling-kovter/

<a name="8">[8]</a> https://blogs.cisco.com/security/talos/rombertik

<a name="9">[9]</a> https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/PE_URSNIF.A2?_ga=2.131425807.1462021705.1559742358-1202584019.1549394279

<a name="10">[10]</a> https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf

<a name="11">[11]</a> https://en.wikipedia.org/wiki/Conficker

<a name="12">[12]</a> https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/

<a name="13">[13]</a> https://cofense.com/recent-geodo-malware-campaigns-feature-heavily-obfuscated-macros/

<a name="14">[14]</a> https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/WORM_BAGLE.U/

<a name="15">[15]</a> https://www.trendmicro.com/en_us/research/18/k/trickbot-shows-off-new-trick-password-grabber-module.html

<a name="16">[16]</a> capa v4.0, analyzed at MITRE on 10/12/2022

