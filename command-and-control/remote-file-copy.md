|||
|---------|------------------------|
|**ID**|**E1105**|
|**Objective(s)**|[Command and Control](https://github.com/MBCProject/mbc-markdown/tree/master/command-and-control), [Lateral Movement](https://github.com/MBCProject/mbc-markdown/tree/master/lateral-movement), [Persistence](https://github.com/MBCProject/mbc-markdown/tree/master/persistence)|
|**Related ATT&CK Technique(s)**|[Remote File Copy](https://attack.mitre.org/techniques/T1105/)|

Remote File Copy
================
Malware may copy files from one system to another. 

Note that this behavior is separate from possible execution (installation) of the file, which is covered by the [Install Additional Program](https://github.com/MBCProject/mbc-markdown/blob/master/execution/install-prog.md) behavior. 

**See ATT&CK:** [**Remote File Copy**](https://attack.mitre.org/techniques/T1105/).

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|-----------|-----------------------------|
|[**TrickBot**](https://github.com/MBCProject/mbc-markdown/tree/master/xample-malware/trickbot.md)|2016|Trojan spyware program that has mainly been used for targeting banking sites.|
|[**Poison-Ivy**](https://github.com/MBCProject/mbc-markdown/tree/master/xample-malware/poison-ivy.md)|2005|After the Poison-Ivy server is running on the target machine, the attacker can use a Windows GUI client to control the target computer. [[1]](#1)|

References
----------
<a name="1">[1]</a> https://www.cyber.nj.gov/threat-profiles/trojan-variants/poison-ivy
