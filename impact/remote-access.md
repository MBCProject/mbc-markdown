|||
|---|---|
|**ID**|**B0022**|
|**Objective(s)**|[Impact](https://github.com/MBCProject/mbc-markdown/tree/master/impact), [Persistence](https://github.com/MBCProject/mbc-markdown/tree/master/persistence)|
|**Related ATT&CK Technique**|None|


Remote Access
=============
Malware may provide an attacker with potentially full access to a system via a remote network connection, which may also provide persistence.

A RAT (Remote Access Trojan) is an example of malware that provides a degree of remote access. If the malware provides an "execute" command, the attacker may choose to delete files or corrupt data, power-off the machine, or upload and execute other applications. The malware may also provide specific commands to the attacker (e.g., Delete File). Explicit commands provided by the malware can be captured with Methods associated with the [**Execution::Remote Commands**](https://github.com/MBCProject/mbc-markdown/blob/master/execution/remote-commands.md) behavior; examples include *Execution:Remote Commands:Execute* and *Execution:Remote Commands:Delete File*.

Note that the [**Ingress Tool Transfer**](https://attack.mitre.org/techniques/T1105/) technique defined under the Command and Control tactic is no longer specific to "legitimate desktop support and remote access software” as it was under a previous version of ATT&CK. However, *Ingress Tool Transfer* relates only to files copied; this MBC behavior is broader, allowing for remote access behaviors beyond file transfers (i.e., *Impact:Remote Access* and *Command and Control: Ingress Tool Transfer* are not equivalent).

Methods
-------
|ID|Name|Description|
|---|---|---|
|B0022.001|**Reverse Shell**|Malware may create a reverse shell. For example, malware can invoke cmd.exe and create three pipes (stdin, stdout, stderr) to forward data between cmd.exe and an adversary.|

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**Poison-Ivy**](https://github.com/MBCProject/mbc-markdown/tree/master/xample-malware/poison-ivy.md)|2005|After the Poison-Ivy server is running on the target machine, the attacker can use a Windows GUI client to control the target computer. [[2]](#2)|
|[**Dark Comet**](https://github.com/MBCProject/mbc-markdown/tree/master/xample-malware/dark-comet.md)|2008|Allows an attacker to control the system via a GUI.|

References
----------
<a name="1">[1]</a> https://en.wikipedia.org/wiki/Remote_access_trojan

<a name="2">[2]</a> https://www.cyber.nj.gov/threat-profiles/trojan-variants/poison-ivy

<a name="3">[3]</a> https://en.wikipedia.org/wiki/DarkComet
