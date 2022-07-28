|||
|---|---|
|**ID**|**E1059**|
|**Objective(s)**|[Execution](../execution)|
|**Related ATT&CK Technique**|[Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059)|


Command and Scripting Interpreter
=================================
Malware may abuse command and script interpreters to execute commands, scripts, or binaries.

**See ATT&CK Technique:** [**Command and Scripting Interpreter**](https://attack.mitre.org/techniques/T1059).

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**Poison-Ivy**](../xample-malware/poison-ivy.md)|2005|After the Poison-Ivy server is running on the target machine, the attacker can use a Windows GUI client to control the target computer. [[1]](#1)|
|[**WebCobra**](../xample-malware/webcobra.md)|2018|From the command line, drops and unzips a password-protected Cabinet archive file. [[1]](#1)|
|[**GotBotKR**](../execution/command-line.md)|2019|GoBotKR uses cmd.exe to execute commands. [[2]](#2)|
|[**Kovter**](../execution/command-line.md)|2016|The malware executes malicious javascript and powershell [[3]](#3)|
|[**SamSam**](../xample-malware/samsam.md)|2015|SamSam uses a batch file for executing the malware and deleting certain components   [[4]](#4)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|The wiper component of Shamoon creates a service to run the driver with the command: sc create hdv_725x type= kernel start= demand binpath= WINDOWS\hdv_725x.sys 2>&1 >nul and sends an additional reboot command after completion [[5]](#5)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|Stuxnet will store and execute SQL code that will extract and execute Stuxnet from the saved CAB file using xp_cmdshell  [[6]](#6)|

References
----------
<a name="1">[1]</a> https://www.cyber.nj.gov/threat-profiles/trojan-variants/poison-ivy

<a name="2">[2]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="3">[3]</a> https://www.bleepingcomputer.com/virus-removal/remove-kovter-trojan

<a name="4">[4]</a> https://www.sophos.com/en-us/medialibrary/PDFs/technical-papers/SamSam-ransomware-chooses-Its-targets-carefully-wpna.pdf

<a name="5">[5]</a> https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-returns-to-wipe-systems-in-middle-east-europe/

<a name="6">[6]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en
