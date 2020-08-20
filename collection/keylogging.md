|||
|---|---|
|**ID**|**F0002**|
|**Objective(s)**|[Collection](https://github.com/MBCProject/mbc-markdown/tree/master/collection), [Credential Access](https://github.com/MBCProject/mbc-markdown/tree/master/credential-access)|
|**Related ATT&CK Sub-Technique**|[Input Capture: Keylogging](https://attack.mitre.org/techniques/T1056/001)|


Keylogging
==========
Malware captures user keyboard input.

**See ATT&CK:** [**Input Capture: Keylogging**](https://attack.mitre.org/techniques/T1056/001).

Methods
-------
|ID|Name|Description|
|---|---|---|
|F0002.001|**Application Hook**|Keystrokes are captured with an application hook.|
|F0002.002|**Polling**|Keystrokes are captured via polling (e.g., user32.GetAsyncKeyState, user32.GetKeyState).|
