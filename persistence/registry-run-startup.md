|||
|---------|------------------------|
|**ID**|**E1060**|
|**Objective(s)**| [Persistence](https://github.com/MBCProject/mbc-markdown/tree/master/persistence)|
|**Related ATT&CK Technique(s)**|[Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1060)|


Registry Run Keys / Startup Folder
==================================
Malware may add an entry to the Windows Registry run keys or startup folder to enable persistence. [[1]](#1)

See ATT&CK: [**Registry Run Keys / Startup Folder**](https://attack.mitre.org/techniques/T1060). 

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|-----------|-----------------------------|
|[**TrickBot**](https://github.com/MBCProject/mbc-markdown/tree/master/xample-malware/trickbot.md)|2016|Trojan spyware program that has mainly been used for targeting banking sites.|
|[**Poison-Ivy**](https://github.com/MBCProject/mbc-markdown/tree/master/xample-malware/poison-ivy.md)|2005|After the Poison-Ivy server is running on the target machine, the attacker can use a Windows GUI client to control the target computer. [[2]](#2)|

References
----------
<a name="1">[1]</a> https://threatvector.cylance.com/en_us/home/windows-registry-persistence-part-2-the-run-keys-and-search-order.html

<a name="2">[2]</a> https://www.cyber.nj.gov/threat-profiles/trojan-variants/poison-ivy
