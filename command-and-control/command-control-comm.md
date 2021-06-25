|||
|---|---|
|**ID**|**B0030**|
|**Objective(s)**|[Command and Control](../command-and-control)|
|**Related ATT&CK Technique**|None|


C2 Communication
================
All command and control malware use implant/controller communication. The methods listed below can be used to capture explicit communication details. Remote file copy behavior is captured separately, as is done in ATT&CK - see [Remote File Copy](../command-and-control/remote-file-copy.md).

Command and Control Communication relates to *autonomous* communications, not explicit, on-demand commands that malware provides to an adversary (such commands should be captured with [Remote Commands](../execution/remote-commands.md) under the Execution objective).

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Authenticate**|B0030.011|Implant may authenticate itself to the controller, controller may authenticate itself to implant, or both. This is often at or near the start of communication. Examples include but are not limited to a simple shared secret (e.g. password), challenge-response with symmetric encryption, or challenge-response with asymmetric encryption.|
|**Check for Payload**|B0030.005|Check for payload.|
|**Directory Listing**|B0030.012|Controller requests a directory listing from the implant, optionally from a given path, optionally recursive.|
|**Execute File**|B0030.013|Execute/run/open the file using default operating system functionality, optionally with provided command-line arguments. The file may or may not already exist on the victim.|
|**Execute Shell Command**|B0030.014|Execute/run the given command using a built-in program (e.g. cmd.exe, PowerShell, bash). This differs from Start Interactive Shell because the shell process is started only for the received command or set of commands and then exits. There is no loop looking for additional commands while the shell process is still running.|
|**File search**|B0030.015|Controller requests the implant to search for a given filename pattern, often a [glob](https://en.wikipedia.org/wiki/Glob_(programming)).|
|**Implant to Controller File Transfer**|B0030.004|File is transferred from implant to controller.|
|**Receive Data**|B0030.002|Receive data or command from a controller.|
|**Request Command**|B0030.008|Implant requests a command.|
|**Request Email Address List**|B0030.010|Request email address list.|
|**Request Email Template**|B0030.009|Request email template.|
|**Send Data**|B0030.001|Send data to a controller.|
|**Send Heartbeat**|B0030.007|Heartbeat sent.|
|**Send System Information**|B0030.006|Implant sends system information.|
|**Server to Client File Transfer**|B0030.003|File is transferred from controller to implant.|
|**Start Interactive Shell**|B0030.016|Start an interactive shell using a built-in program (e.g. cmd.exe, PowerShell, bash). This is often implemented with polling the network connection from the controller for text commands to redirect to the shell's stdin and polling the shell's stdout and stderr to redirect over the network to the controller. This differs from Execute Shell Command because the shell process runs across multiple iterations of the recv-command(s)-send-result loop.|

Code Snippets
-------------
**C2 Communication::Recieve Data** (B0030.02)
 <br/>MD5: b6e1a2048ea6bd6a941a72300b2d41ce
```asm
loc_401981
mov ecx, s
mov edx, edi
sub edx, esi
push 0 ; flags
lea eax, [esi+ebx]
push edx ;len
push eax ;buf
push ecx ;s
call recv
jmp short loc_4019A2
```

