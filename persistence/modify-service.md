|||
|---|---|
|**ID**|**F0011**|
|**Objective(s)**|[Persistence](../persistence), [Privilege Escalation](../privilege-escalation)|
|**Related ATT&CK Sub-Technique**|[Create or Modify System Process::Windows Service](https://attack.mitre.org/techniques/T1543/003/)|


Modify Existing Service
=======================
Malware may modify an existing service to gain persistence. Modification may include disabling a service.

See ATT&CK: [**Create or Modify System Process::Windows Service**](https://attack.mitre.org/techniques/T1543/003/).

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**Poison-Ivy**](../xample-malware/poison-ivy.md)|2005|After the Poison-Ivy server is running on the target machine, the attacker can use a Windows GUI client to control the target computer. [[1]](#1)|
|[**YiSpecter**](../persistence/modify-service.md)|2015|Hijacks other installed applications' launch routines to use "ADPage" (an installed malicious app) to display advertisements  [[2]](#2)|
|[**BlackEnergy**](../persistence/modify-service.md)|2007|Locates an inactive driver service to Hijack and set it to start automatically [[3]](#3)|
|[**Conficker**](../persistence/modify-service.md)|2008|Copies itself into the $systemroot%\system32 directory and registers as a service  [[4]](#4)|

References
----------
<a name="1">[1]</a> https://www.cyber.nj.gov/threat-profiles/trojan-variants/poison-ivy

<a name="2">[2]</a> http://researchcenter.paloaltonetworks.com/2015/10/yispecter-first-ios-malware-attacks-non-jailbroken-ios-devices-by-abusing-private-apis/

<a name="3">[3]</a> https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf

<a name="4">[4]</a> https://en.wikipedia.org/wiki/Conficker
