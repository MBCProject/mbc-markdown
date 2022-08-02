|||
|---|---|
|**ID**|**E1083**|
|**Objective(s)**|[Discovery](../discovery)|
|**Related ATT&CK Technique**|[File and Directory Discovery](https://attack.mitre.org/techniques/T1083/) |


File and Directory Discovery
============================
Malware may enumerate files and directories or may search for specific files or in specific locations.

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Log File**|E1083.m01|Malware may look for system log files.|

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**CryptoWall**](../xample-malware/cryptowall.md)|2014| [[1]](#1)|
|[**CryptoLocker**](../xample-malware/cryptolocker.md)|2013|The malware searches for user files before encrypting them [[2]](#2)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|Collects local files with specified file extensions and information from the victim's machine [[3]](#3)|

References
----------
<a name="1">[1]</a> https://news.sophos.com/en-us/2015/12/17/the-current-state-of-ransomware-cryptowall/

<a name="2">[2]</a> https://www.secureworks.com/research/cryptolocker-ransomware

<a name="3">[3]</a> https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf
