|||
|---|---|
|**ID**|**OB0004**|


# Command and Control
Behaviors malware may use to communicate with systems under its control within a target network. There are many ways malware can establish command and control with various levels of covertness, depending on system configuration and network topology. Behaviors may relate to C2 servers or a bot that is part of a botnet. As "server" and "client" are confusing terminology in this context, we use the terms **controller** and **implant**. The controller is the software running on adversary-controlled infrastructure and used to send commands to the implant. The implant is the software running on victim-controlled infrastructure that receives commands from the adversary, executes those commands on the victim, and optionally sends the results back to the adversary.

* **Command and Control Communication** [B0030](../command-and-control/command-control-comm.md)
* **Domain Name Generation** [B0031](../command-and-control/domain-name-generate.md)
* **Remote File Copy** [E1105](../command-and-control/remote-file-copy.md)


Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**TrickBot**](../command-and-control/README.md)|2016| new email addresses are collected automatically from the victim's address books [[1]](#1)|


References
----------
<a name="1">[1]</a> https://www.bitdefender.com/blog/labs/trickbot-is-dead-long-live-trickbot/
