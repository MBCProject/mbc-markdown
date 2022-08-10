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
|[**GotBotKR**](../xample-malware/gotbotkr.md)|2019| GoBotKR is capable of capturing screenshots. [[1]](#1)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|Screenshot plugin allows for collection of screenshots  [[2]](#2)|
|[**DarkComet**](../xample-malware/dark-comet.md)|2008|Can take screenshots of victim's computer [[3]](#3)|

References
----------
<a name="1">[1]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="2">[2]</a> https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/

<a name="3">[3]</a> https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/
