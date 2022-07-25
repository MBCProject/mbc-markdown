|||
|---|---|
|**ID**|**E1204**|
|**Objective(s)**|[Execution](../execution)|
|**Related ATT&CK Technique**|[User Execution](https://attack.mitre.org/techniques/T1204)|


User Execution
==============
Malware may include code that relies on specific actions by a user to execute. Note that this MBC behavior differs from [User Execution](https://attack.mitre.org/techniques/T1204) in that it does do not include direct code execution (user action for *initial* execution) - MBC does not encompass ATT&CK's Initial Access Tactic.  

**See ATT&CK Technique:** [**User Execution**](https://attack.mitre.org/techniques/T1204).

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|Trojan spyware program that has mainly been used for targeting banking sites.|
|[**GotBotKR**](../execution/user-interaction.md)|2019| GoBotKR makes their malware look like the torrent content that the user intended to download, in order to entice a user to click on it. [[1]](#1)|

|[**Rombertik**](../execution/user-interaction.md)|2015|The malware relies on a victim to execute itself [[2]](#2)|
|[**Terminator**](../execution/user-interaction.md)|2013|The malware relies on user interaction to execute [[3]](#3)|

References
----------
<a name="1">[1]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="2">[2]</a> https://blogs.cisco.com/security/talos/rombertik

<a name="3">[3]</a> https://www.mandiant.com/resources/hot-knives-through-butter-evading-file-based-sandboxes
