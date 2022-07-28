|||
|---|---|
|**ID**|**F0005**|
|**Objective(s)**|[Defense Evasion](../defense-evasion), [Persistence](../persistence)|
|**Related ATT&CK Sub-Technique**|[Hide Artifacts: Hidden Files and Directories](https://attack.mitre.org/techniques/T1564/001/)|


Hidden Files and Directories
============================
Malware may hide files and folders to avoid detection and/or to persist on the system. See potential methods below. 

See ATT&CK: [**Hide Artifacts: Hidden Files and Directories**](https://attack.mitre.org/techniques/T1564/001/).

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Attribute**|F0005.003|Malware may change or choose an attribute to hide a file or directory.|
|**Extension**|F0005.001|Malware may change or use a particular file extension to hide a file.|
|**Location**|F0005.002|Malware may change or choose the location of itself, another file, or a directory to prevent detection.|
|**Timestamp**|F0005.004|Malware may change the timestamp on a file to prevent detection.|


Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**GotBotKR**](../defense-evasion/hidden-files.md)|2019| GoBotKR stores itself in a file with Hidden and System attributes. [[1]](#1)|

|[**Shamoon**](../xample-malware/shamoon.md)|2012|Modifies target files' time to August 2012 as an antiforensic trick  [[2]](#2)|

References
----------
<a name="1">[1]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="2">[2]</a> https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-returns-to-wipe-systems-in-middle-east-europe/
