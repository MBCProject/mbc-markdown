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
