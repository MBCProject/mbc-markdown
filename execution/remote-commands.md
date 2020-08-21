|||
|---|---|
|**ID**|**B0011**|
|**Objective(s)**|[Execution](https://github.com/MBCProject/mbc-markdown/tree/master/execution)|
|**Related ATT&CK Technique**|None|


Remote Commands
===============
Malware may provide an attacker with explicit commands. This behavior differs from the [Remote Access](https://github.com/MBCProject/mbc-markdown/blob/master/impact/remote-access.md) behavior under the [Impact](https://github.com/MBCProject/mbc-markdown/tree/master/impact) objective in that *Impact: Remote Access* is potentially much broader and may include full remote access.

Given an "execute" command, the attacker may choose to delete files or corrupt data, power-off the machine, or upload and execute other applications. The malware may also provide specific commands to the attacker (e.g., "delete file"). 

Commands provided by the malware can be captured with the methods defined below. For example, malware that enables an attacker to delete a file could be tagged with *Execution:Remote Commands:Delete File*.

It may be useful to capture remote commands along with related behaviors because the associated descriptions could provide details of how the malware implements the command. For example, *Defense Evasion:File Deletion* could be used to provide details and context to *Execution:Remote Commands:Delete File*.

Autonomous behaviors - those done by the malware without an active attacker - should not be captured with *Execution:Remote Commands*. For example, malware that *automatically* destroys data would be tagged with the [Impact: Data Destruction](https://github.com/MBCProject/mbc-markdown/blob/master/impact/data-destruction.md) behavior.

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Delete File**|B0011.001||
|**Download File**|B0011.002||
|**Execute**|B0011.003||
|**Shutdown**|B0011.004||
|**Sleep**|B0011.005||
|**Uninstall**|B0011.006||
|**Upload File**|B0011.007||
