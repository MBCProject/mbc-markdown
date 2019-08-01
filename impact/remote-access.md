|||
|---------|------------------------|
|**ID**|**M0022**|
|**Objective(s)**| [Impact](https://github.com/MAECProject/malware-behaviors/tree/master/impact)|
|**Related ATT&CK Technique(s)**|None|


Remote Access
=============
Malware may provide an attacker with potentially full access to a system via a remote network connection. 

Malware may also provide specific commands. Given an "execute" command, the attacker may choose to delete files or corrupt data, power-off the machine, or upload and execute other applications. The malware may also provide specific commands to the attacker (e.g., Delete File). Explicit commands provided by the malware can be captured with Methods associated with the [Execution:Remote Commands](https://github.com/MAECProject/malware-behaviors/blob/master/execution/remote-commands.md) Behavior; examples include Execution:Remote Commands:Execute and Execution:Remote Commands:Delete File.

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|
| Poison-Ivy | 2005 | After the Poison-Ivy server is running on the target machine, the attacker can use a Windows GUI client to control the target computer. [[2]](#2)| 
|DarkComet | 2008 | Allows an attacker to control the system via a GUI. |

References
----------
<a name="1">[1]</a> https://en.wikipedia.org/wiki/Remote_access_trojan
<a name="2">[2]</a> https://www.cyber.nj.gov/threat-profiles/trojan-variants/poison-ivy
<a name="3">[3]</a> https://en.wikipedia.org/wiki/DarkComet