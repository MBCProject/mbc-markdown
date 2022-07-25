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
**C2 Communication::Receive Data** (B0030.02)
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


Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**CryptoWall**](../command-and-control/command-control-comm.md)|2014|The malware sends a hash value generated from system information [[1]](#1)|
|[**GotBotKR**](../command-and-control/command-control-comm.md)|2019|GoBotKR receives data from the C2 [[2]](#2)|
|[**Terminator**](../command-and-control/command-control-comm.md)|2013|The malware sends data to C2 [[3]](#3)|
|[**UP007**](../command-and-control/command-control-comm.md)|2016|The malware receives payloads [[4]](#4)|
|[**YiSpecter**](../command-and-control/command-control-comm.md)|2015|Connects to the command and control server using HTTP to send device information [[5]](#5)|
|[**Ursnif**](../command-and-control/command-control-comm.md)|2016|Ursnif variant Dreambot authenticates and encrypts traffic to C2 server using TOR [[6]](#6)|

References
----------
<a name="1">[1]</a> https://news.sophos.com/en-us/2015/12/17/the-current-state-of-ransomware-cryptowall/

<a name="2">[2]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="3">[3]</a> https://www.mandiant.com/resources/hot-knives-through-butter-evading-file-based-sandboxes

<a name="4">[4]</a> https://citizenlab.ca/2016/04/between-hong-kong-and-burma/

<a name="5">[5]</a> http://researchcenter.paloaltonetworks.com/2015/10/yispecter-first-ios-malware-attacks-non-jailbroken-ios-devices-by-abusing-private-apis/

<a name="6">[6]</a> https://www.proofpoint.com/us/threat-insight/post/ursnif-variant-dreambot-adds-tor-functionality
