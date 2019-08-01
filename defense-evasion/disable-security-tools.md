|||
|---------|------------------------|
|**ID**|**E1089**|
|**Objective(s)**|[Defense Evasion](https://github.com/MAECProject/malware-behaviors/tree/master/defense-evasion)|
|**Related ATT&CK Technique(s)**|[Disabling Security Tools](https://attack.mitre.org/techniques/T1089/)|

Disabling Security Tools
========================
Malware may disable security tools to avoid detection. Malware-related methods extending ATT&CK's definition are below. 

See ATT&CK: [**Disabling Security Tools**](https://attack.mitre.org/techniques/T1089/).

Methods
-------
* **Disable Kernel Patch Protection**: Bypasses or disables kernel patch protection mechanisms such as Windows' PatchGuard, enabling the malware instance to operate at the same level as the operating system kernel and kernel mode drivers (KMD).

* **Disable System File Overwrite Protection**: Disables system file overwrite protection mechanisms such as Windows file protection, thereby enabling system files to be modified or replaced.

* **Unhook APIs**: Security products may hook APIs to monitor the behavior of malware. To avoid being found, malware may load DLLs in memory and overwrite their bytes. 

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|-----------|-----------------------------|
|[**WebCobra**](https://github.com/MAECProject/malware-behaviors/blob/master/xample-malware/webcobra.md)| 2018 | Loads ntdll.dll and user32.dll as data files in memory and overwrites the first 8 bytes of those functions, which unhooks the APIs. [[1]](#1)|

References
----------
<a name="1">[1]</a> https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/