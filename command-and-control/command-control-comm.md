|||
|---------|------------------------|
|**ID**|**B0030**|
|**Objective(s)**|[Command and Control](https://github.com/MBCProject/mbc-markdown/tree/master/command-and-control)|
|**Related ATT&CK Technique**|None|

C2 Communication
================
All command and control malware use client/server communication. The methods listed below can be used to capture explicit communication details. Remote file copy behavior is captured separately, as is done in ATT&CK - see [Remote File Copy](https://github.com/MBCProject/mbc-markdown/blob/master/command-and-control/remote-file-copy.md).

Command and Control Communication relates to *autonomous* client/server communications, not explicit, on-demand commands that malware provides to an adversary (such commands should be captured with [Remote Commands](https://github.com/MBCProject/mbc-markdown/blob/master/execution/remote-commands.md) under the Execution objective).

Methods
-------
|ID|Name|Description|
|-----------------------------|--------|-----------------------------|
|B0030.001|**Send Data**|Send data to a C2 server.|
|B0030.002|**Receive Data**|Receive data from a C2 server.|
|B0030.003|**Server to Client File Transfer**|File is transferred from server to client.|
|B0030.004|**Client to Server File Transfer**|File is transferred from client to server.|
|B0030.005|**Check for Payload**|Check for payload.|
|B0030.006|**Send System Information**|Client sends system information.|
|B0030.007|**Send Heartbeat**|Heartbeat sent.|
|B0030.008|**Request Command**|Client requests a command.|
|B0030.009|**Request Email Template**|Request email template.|
|B0030.010|**Request Email Address List**|Request email address list.|