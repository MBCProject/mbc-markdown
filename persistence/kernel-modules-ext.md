|||
|---|---|
|**ID**|**F0010**|
|**Objective(s)**|[Persistence](https://github.com/MBCProject/mbc-markdown/tree/master/persistence), [Privilege Escalation](https://github.com/MBCProject/mbc-markdown/tree/master/privilege-escalation)|
|**Related ATT&CK Sub-Technique**|[Boot or Logon Autostart Execution: Kernel Modules and Extensions](https://attack.mitre.org/techniques/T1547/006/)|


Kernel Modules and Extensions
=============================
Malware may use loadable kernel modules to persist on a system. For example, one type of module is the device driver, which allows the kernel to access hardware connected to the system. Malware may try to hide drivers or modules by creating them without a name.

See ATT&CK: [**Boot or Logon Autostart Execution: Kernel Modules and Extensions**](https://attack.mitre.org/techniques/T1547/006/).

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Device Driver**|F0010.001|Allows kernel to access hardware connected to the system.|
