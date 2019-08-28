|||
|---------|------------------------|
|**ID**|**M0030**|
|**Objective(s)**|[Command and Control](https://github.com/MBCProject/mbc-markdown/tree/master/command-and-control)|
|**Related ATT&CK Technique(s)**|None|

C2 Communication
================
All command and control malware uses client/server communication. The methods listed below can be used to capture explicit communication details. Remote file copy behavior is captured separately, as is done in ATT&CK - see [Remote File Copy](https://github.com/MBCProject/mbc-markdown/blob/master/command-and-control/remote-file-copy.md).

Command and Control Communication relates to *autonomous* client/server communications, not commands that are provided to an adversary. Commands provided to an attacker should be captured under [Remote Commands](https://github.com/MBCProject/mbc-markdown/blob/master/execution/remote-commands.md) under the Execution objective.

Methods
-------
* **Check for Payload**
* **Send System Information**
* **Send Heartbeat**
* **Request Command**
* **Request Email Template**
* **Request Email Address List**