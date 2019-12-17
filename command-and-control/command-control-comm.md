|||
|---------|------------------------|
|**ID**|**M0030**|
|**Objective(s)**|[Command and Control](https://github.com/MBCProject/mbc-markdown/tree/master/command-and-control)|
|**Related ATT&CK Technique**|None|

C2 Communication
================
All command and control malware use client/server communication. The methods listed below can be used to capture explicit communication details. Remote file copy behavior is captured separately, as is done in ATT&CK - see [Remote File Copy](https://github.com/MBCProject/mbc-markdown/blob/master/command-and-control/remote-file-copy.md).

Command and Control Communication relates to *autonomous* client/server communications, not explicit, on-demand commands that malware provides to an adversary (such commands should be captured with [Remote Commands](https://github.com/MBCProject/mbc-markdown/blob/master/execution/remote-commands.md) under the Execution objective).

Methods
-------
* **Check for Payload**
* **Send System Information**
* **Send Heartbeat**
* **Request Command**
* **Request Email Template**
* **Request Email Address List**