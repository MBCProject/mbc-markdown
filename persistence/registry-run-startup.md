|||
|---------|------------------------|
|**ID**|**F0012**|
|**Objective(s)**| [Persistence](https://github.com/MBCProject/mbc-beta/tree/master/persistence)|
|**Related ATT&CK Sub-Technique**|[Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/)|


Registry Run Keys / Startup Folder
==================================
Malware may add an entry to the Windows Registry run keys or startup folder to enable persistence. [[1]](#1)

See ATT&CK: [**Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder**](https://attack.mitre.org/techniques/T1547/001/). 

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|-----------|-----------------------------|
|[**TrickBot**](https://github.com/MBCProject/mbc-beta/tree/master/xample-malware/trickbot.md)|2016|Trojan spyware program that has mainly been used for targeting banking sites.|
|[**Poison-Ivy**](https://github.com/MBCProject/mbc-beta/tree/master/xample-malware/poison-ivy.md)|2005|After the Poison-Ivy server is running on the target machine, the attacker can use a Windows GUI client to control the target computer. [[2]](#2)|
|[**Hupigon**](https://github.com/MBCProject/mbc-beta/blob/master/xample-malware/hupigon.md)|2013|Hupigon drops the file "Systen.dll" and adds the registry entry: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Notify\BITS DllName = "%System%\Systen.dll". [[3]](#3)|
|[**Terminator**](https://github.com/MBCProject/mbc-beta/blob/master/xample-malware/terminator.md)|May 2013|The Terminator rat sets "2019" as Windows' startup folder by modifying a registry value. [[4]](#4) |

References
----------
<a name="1">[1]</a> https://threatvector.cylance.com/en_us/home/windows-registry-persistence-part-2-the-run-keys-and-search-order.html

<a name="2">[2]</a> https://www.cyber.nj.gov/threat-profiles/trojan-variants/poison-ivy

<a name="3">[3]</a> https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/HUPIGON

<a name="4">[4]</a> https://www.fireeye.com/content/dam/fireeye-www/current-threats/pdfs/pf/file/fireeye-hot-knives-through-butter.pdf 
