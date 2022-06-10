|||
|---|---|
|**ID**|**E1105**|
|**Objective(s)**|[Command and Control](../command-and-control), [Lateral Movement](../lateral-movement), [Persistence](../persistence)|
|**Related ATT&CK Technique**|[Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105/)|


Ingress Tool Transfer
================
Malware may copy files from an external system to a system on a compromised network. 

Note that this behavior is separate from possible execution (installation) of the file, which is covered by the [Install Additional Program](../execution/install-prog.md) behavior. 

**See ATT&CK:** [**Ingress Tool Transfer**](https://attack.mitre.org/techniques/T1105/).

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|Trojan spyware program that has mainly been used for targeting banking sites.|
|[**Poison-Ivy**](../xample-malware/poison-ivy.md)|2005|After the Poison-Ivy implant is running on the target machine, the attacker can use a Windows GUI controller to control the target computer. [[1]](#1)|

References
----------
<a name="1">[1]</a> https://www.cyber.nj.gov/threat-profiles/trojan-variants/poison-ivy
