|||
|---------|------------------------|
|**ID**|**M0011**|
|**Objective(s)**| [Execution](https://github.com/MAECProject/malware-behaviors/tree/master/execution)|
|**Related ATT&CK Technique(s)**|None|


Remote Commands
===============
Malware may provide an attacker with explicit commands.  

Given an "execute" command, the attacker may choose to delete files or corrupt data, power-off the machine, or upload and execute other applications. The malware may also provide specific commands to the attacker (e.g., "delete file"). 

Commands provided by the malware can be captured with the Methods defined below. For example, malware that enables an attacker to delete a file could be tagged with Execution:Remote Commands:Delete File.

It may still be useful to capture non-autonomous behaviors (commands) with autonomously-oriented behaviors because the associated descriptions could provide details of how the malware implements the behavior. Using autonomous behaviors in combination with the Execution:Remote Commands Behavior gives context.

Autonomous behaviors - those done by the malware without an active attacker - should not be captured with Execution:Remote Commands. For example, malware that *automatically* destroys data would be tagged with the [Destroy Data](https://github.com/MAECProject/malware-behaviors/blob/master/impact/destroy-data.md) Behavior.

Methods
-------
* **Delete File**
* **Download File**
* **Execute**
* **Shutdown**
* **Sleep**
* **Uninstall**
* **Upload File**

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|


References
----------
