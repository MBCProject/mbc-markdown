|||
|---------|------------------------|
|**ID**|**E1195**|
|**Objective(s)**|[Lateral Movement](https://github.com/MAECProject/malware-behaviors/tree/master/lateral-movement)|
|**Related ATT&CK Technique(s)**|[Supply Chain Compromise](https://attack.mitre.org/techniques/T1195/)|

Supply Chain Compromise
=======================
The supply chain may be compromised to enable initial malware infection. Malware-related methods are listed below to supplement the information available defined in ATT&CK: [**Supply Chain Compromise**](https://attack.mitre.org/techniques/T1195/).  

Methods
-------
* **Abuse Enterprise Certificates**: Abusing enterprise certificates enables malware to exploit private APIs and infect a wide range of users (see *Exploit Private APIs* below).
* **Exploit Private APIs**: Malware can exploit private APIs to infect jailbroken and non-jailbroken iOS devices. Research shows that over 100 apps in the App Store have abused private APIs and bypassed Apple’s strict code review. 

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|-----------|-----------------------------|
|YiSpecter| October 2015| Attacks both jailbroken and non-jailbroken iOS devices by exploiting private APIs. [[1]](#1)|

References
----------
<a name="1">[1]</a> http://researchcenter.paloaltonetworks.com/2015/10/yispecter-first-ios-malware-attacks-non-jailbroken-ios-devices-by-abusing-private-apis/