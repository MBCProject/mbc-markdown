|||
|---------|------------------------|
|**ID**|**M0030**|
|**Objective(s)**|[Command and Control](https://github.com/MAECProject/malware-behaviors/tree/master/command-and-control)|
|**Related ATT&CK Technique(s)**|None|

C2 Communication
================
All command and control malware uses client/server communication. The methods listed below can be used to capture explicit communication details. 

Command and Control Communication relates to *autonomous* client/server communications, not commands that are provided to an adversary. Commands provided to an attacker should be captured under [Remote Commands](https://github.com/MAECProject/malware-behaviors/blob/master/execution/remote-commands.md) under the Execution objective.

Methods
-------
* **Check for Payload**
* **Send System Information**
* **Send Heartbeat**
* **Request Command**
* **Request Email Template**
* **Request Email Address List**