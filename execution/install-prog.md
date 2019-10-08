|||
|---------|------------------------|
|**ID**|**M0023**|
|**Objective(s)**| [Execution](https://github.com/MBCProject/mbc-markdown/tree/master/execution)|
|**Related ATT&CK Technique(s)**|None|


Install Additional Program
==========================
Installs another, different program on the system. The additional program can be any secondary module; examples include backdoors, malicious drivers, kernel modules, and OS X Apps. Malware that installs another component is called a "dropper."

Methods
-------
* **Single Stage**: The installed code is contained within the dropper.
* **Two Stage**: The dropper downloads the installed code to the target machine.

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|
| WebCobra| November 2018| Drops software to mine for cryptocurrency. [[1]](#1)|
| Geneio| August 2015| Tricks OS X keychain to create application files. |
| GoBotKR | July 2019 | GotBotKR reinstalls its running instance if it is removed. [[3]](#3)|

References
----------
<a name="1">[1]</a> https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/

<a name="2">[2]</a> https://www.fortinet.com/blog/threat-research/deep-analysis-of-driver-based-mitm-malware-itranslator.html

<a name="3">[3]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/
