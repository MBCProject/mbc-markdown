|||
|---|---|
|**ID**|**F0002**|
|**Objective(s)**|[Collection](../collection), [Credential Access](../credential-access)|
|**Related ATT&CK Sub-Technique**|[Input Capture: Keylogging](https://attack.mitre.org/techniques/T1056/001)|


Keylogging
==========
Malware captures user keyboard input.

**See ATT&CK:** [**Input Capture: Keylogging**](https://attack.mitre.org/techniques/T1056/001).

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Application Hook**|F0002.001|Keystrokes are captured with an application hook.|
|**Polling**|F0002.002|Keystrokes are captured via polling (e.g., user32.GetAsyncKeyState, user32.GetKeyState).|


Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**Hupigon**](../collection/keylogging.md)|2013|Certain variants of the malware may have keylogging functionality [[1]](#1)|
|[**UP007**](../collection/keylogging.md)|2016|The malware logs keystrokes to a file  [[2]](#2)|
|[**BlackEnergy**](../collection/keylogging.md)|2007|Keylogger plugin allows for collection of keystrokes [[3]](#3)|

References
----------
<a name="1">[1]</a> https://www.f-secure.com/v-descs/backdoor_w32_hupigon.shtml

<a name="2">[2]</a> https://citizenlab.ca/2016/04/between-hong-kong-and-burma/

<a name="3">[3]</a> https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/
