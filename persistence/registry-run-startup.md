|||
|---|---|
|**ID**|**F0012**|
|**Objective(s)**|[Persistence](../persistence)|
|**Related ATT&CK Sub-Technique**|[Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/)|


Registry Run Keys / Startup Folder
==================================
Malware may add an entry to the Windows Registry run keys or startup folder to enable persistence. [[1]](#1)

See ATT&CK: [**Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder**](https://attack.mitre.org/techniques/T1547/001/). 

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|Trojan spyware program that has mainly been used for targeting banking sites.|
|[**Poison-Ivy**](../xample-malware/poison-ivy.md)|2005|After the Poison-Ivy server is running on the target machine, the attacker can use a Windows GUI client to control the target computer. [[2]](#2)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|Hupigon drops the file "Systen.dll" and adds the registry entry: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Notify\BITS DllName = "%System%\Systen.dll". [[3]](#3)|
|[**Terminator**](../xample-malware/terminator.md)|May 2013|The Terminator rat sets "2019" as Windows' startup folder by modifying a registry value. [[4]](#4)|
|[**CryptoLocker**](../persistence/registry-run-startup.md)|2013|The malware creates an "autorun" registry key [[5]](#5)|
|[**GotBotKR**](../persistence/registry-run-startup.md)|2019| GoBotKR installs itself under registry run keys to establish persistence. [[6]](#6)|
|[**Kovter**](../persistence/registry-run-startup.md)|2016|The malware writes an autorun registry entry [[7]](#7)|
|[**Rombertik**](../persistence/modify-service.md)|2015|it will proceed to install itself in order to ensure persistence across system reboots before continuing on to execute the payload. To install itself, Rombertik first creates a VBS script named “fgf.vbs”, which is used to kick off Rombertik every time the user logs in, and places the script into the user’s Startup folder. [[8]](#8)|
|[**Ursnif**](../persistence/registry-run-startup.md)|2016|Adds registry entries to ensure automatic execution at every system startup  [[9]](#9)|
|[**BlackEnergy**](../persistence/registry-run-startup.md)|2007|BlackEnergy 3 variant drops its main DLL component and then creates a .lnk shortcut to that file in the startup folder  [[10]](#10)|
|[**Conficker**](../persistence/registry-run-startup.md)|2008|To start itself at system boot, the virus saces a copy of its DLL form to a random filename in the Windows system folder, then adds registry keys to have svchost.exe invoke that DLL as an invisible network service  [[11]](#11)|

References
----------
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
