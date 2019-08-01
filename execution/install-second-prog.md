|||
|---------|------------------------|
|**ID**|**M0023**|
|**Objective(s)**| [Execution](https://github.com/MAECProject/malware-behaviors/tree/master/execution), [Persistence](https://github.com/MAECProject/malware-behaviors/tree/master/persistence)|
|**Related ATT&CK Technique(s)**|None|


Install Additional Program
==========================
Installs another, different program on the system.

Methods
-------
* **Backdoor**: Installs a server that accepts incoming connections.
* **Secondary module**: Installs a secondary module, typically related to the malware instance itself.
* **Dropper**: Installs (executes) a dropped executable file.
* **Malicious Driver**: Installs a malicious driver. [[2]](#2)
* **OS X Apps**: Installs application directories and files without the user knowing.

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|
| WebCobra| November 2018| Drops software to mine for cryptocurrency. [[1]](#1)|
| Geneio| August 2015| Tricks OS X keychain to create application files. |
| GoBotKR | July 2019 | Installs two instances of itself on the system. The second instance (watchdog) monitors whether the first instance is still active and reinstalls it if it has been removed from the system. [[3]](#3)|

References
----------
<a name="1">[1]</a> https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/

<a name="2">[2]</a> https://www.fortinet.com/blog/threat-research/deep-analysis-of-driver-based-mitm-malware-itranslator.html

<a name="3">[3]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/
