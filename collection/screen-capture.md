|||
|---|---|
|**ID**|**E1113**|
|**Objective(s)**|[Collection](../collection), [Credential Access](../credential-access)|
|**Related ATT&CK Technique**|[Screen Capture](https://attack.mitre.org/techniques/T1113/)|


Screen Capture
=============
Malware takes screen captures of the desktop.

**See ATT&CK:** [**Screen Capture**](https://attack.mitre.org/techniques/T1113/).

Methods
-------
|Name|ID|Description|
|---|---|---|
|**WinAPI**|E1113.m01|Screen is captured using WinAPI functions (e.g., user32.GetDesktopWindow).|


Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**GotBotKR**](../collection/screen-capture.md)|2019| GoBotKR is capable of capturing screenshots. [[1]](#1)|
|[**BlackEnergy**](../collection/screen-capture.md)|2007|Screenshot plugin allows for collection of screenshots  [[2]](#2)|

References
----------
<a name="1">[1]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="2">[2]</a> https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/
