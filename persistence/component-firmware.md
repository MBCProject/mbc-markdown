|||
|---------|------------------------|
|**ID**|**E1109**|
|**Objective(s)**|[Impact](https://github.com/MAECProject/malware-behaviors/tree/master/impact), [Persistence](https://github.com/MAECProject/malware-behaviors/tree/master/persistence), [Defense Evasion](https://github.com/MAECProject/malware-behaviors/tree/master/defense-evasion)|
|**Related ATT&CK Technique(s)**|[Component Firmware](https://attack.mitre.org/techniques/T1109/)|

Component Firmware
==================
Malware may overwrite the flash memory contents of system BIOS or other firmware. [[1]](#1). Methods related to malware (extending ATT&CK's definitions) are below. 

see ATT&CK: [**Component Firmware**](https://attack.mitre.org/techniques/T1109/).

Methods
-------
* **Router Firmware**: Cisco routers can have their firmware images modified in order to maliciously infect and persist on end-user machines in a network. This is accomplished by using default or acquired credentials to gain access to a router and to install a backdoor. The implant resides within a modified Cisco IOS image and, when loaded, maintains its persistence in the environment, even after a system reboot. However, any further modules loaded by the attacker will only exist in the router's volatile memory and will not be available for use after reboot. Known affected hardware includes Cisco routers 1841, 2811, and 3825.

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|-----------|-----------------------------|
|SYNful Knock| September 2015| SYNful Knock is a stealthy modification of the router's firmware image that can be used to maintain persistence within a victim's network. [[2]](#2)

References
----------
<a name="1">[1]</a> https://www.scmagazine.com/home/opinions/are-synful-knock-style-router-attacks-set-to-become-the-new-normal/ 

<a name="2">[2]</a> https://www.fireeye.com/blog/threat-research/2015/09/synful_knock_-_acis.html