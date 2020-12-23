|||
|---|---|
|**ID**|**B0030**|
|**Objective(s)**|[Command and Control](../command-and-control)|
|**Related ATT&CK Technique**|None|


C2 Communication
================
All command and control malware use client/server communication. The methods listed below can be used to capture explicit communication details. Remote file copy behavior is captured separately, as is done in ATT&CK - see [Remote File Copy](../command-and-control/remote-file-copy.md).

Command and Control Communication relates to *autonomous* client/server communications, not explicit, on-demand commands that malware provides to an adversary (such commands should be captured with [Remote Commands](../execution/remote-commands.md) under the Execution objective).

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Check for Payload**|B0030.005|Check for payload.|
|**Client to Server File Transfer**|B0030.004|File is transferred from client to server.|
|**Receive Data**|B0030.002|Receive data or command from a C2 server.|
|**Request Command**|B0030.008|Client requests a command.|
|**Request Email Address List**|B0030.010|Request email address list.|
|**Request Email Template**|B0030.009|Request email template.|
|**Send Data**|B0030.001|Send data to a C2 server.|
|**Send Heartbeat**|B0030.007|Heartbeat sent.|
|**Send System Information**|B0030.006|Client sends system information.|
|**Server to Client File Transfer**|B0030.003|File is transferred from server to client.|
