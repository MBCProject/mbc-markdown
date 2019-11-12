|||
|---------|------------------------|
|**ID**|**M0022**|
|**Objective(s)**| [Impact](https://github.com/MBCProject/mbc-markdown/tree/master/impact)|
|**Related ATT&CK Technique(s)**|None|


Remote Access
=============
Malware may provide an attacker with potentially full access to a system via a remote network connection. 

A RAT (Remote Access Trojan) is an example of malware that provides a degree of remote access. If the malware provides an "execute" command, the attacker may choose to delete files or corrupt data, power-off the machine, or upload and execute other applications. The malware may also provide specific commands to the attacker (e.g., Delete File). Explicit commands provided by the malware can be captured with Methods associated with the [**Execution:Remote Commands**](https://github.com/MBCProject/mbc-markdown/blob/master/execution/remote-commands.md) behavior; examples include *Execution:Remote Commands:Execute* and *Execution:Remote Commands:Delete File*.

A [Backdoor](https://github.com/MBCProject/mbc-markdown/blob/master/persistence/backdoor.md), defined under the [Persistence](https://github.com/MBCProject/mbc-markdown/tree/master/persistence) objective, provides remote access for persistence purposes. *Installation* of a backdoor falls under *Impact: Remote Access*.

Note that the [**Remote Access Tools**](https://github.com/MBCProject/mbc-markdown/blob/master/command-and-control/remote-access-tools.md) behavior defined under the Command and Control tactic is specific to "legitimate desktop support and remote access software” – which is different than a RAT malware. Therefore, *Impact:Remote Access* and *Command and Control: Remote Access Tools* are not equivalent.

Methods
-------
* **Reverse Shell**: Malware may create a reverse shell. For example, malware can invoke cmd.exe and create three pipes (stdin, stdout, stderr) to forward data between cmd.exe and an adversary. 

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|
|[**Poison-Ivy**](https://github.com/MBCProject/mbc-markdown/tree/master/xample-malware/poison-ivy.md)|2005|After the Poison-Ivy server is running on the target machine, the attacker can use a Windows GUI client to control the target computer. [[2]](#2)|
|[**Dark Comet**](https://github.com/MBCProject/mbc-markdown/tree/master/xample-malware/dark-comet.md)|2008|Allows an attacker to control the system via a GUI.|

References
----------
<a name="1">[1]</a> https://en.wikipedia.org/wiki/Remote_access_trojan
<a name="2">[2]</a> https://www.cyber.nj.gov/threat-profiles/trojan-variants/poison-ivy
<a name="3">[3]</a> https://en.wikipedia.org/wiki/DarkComet