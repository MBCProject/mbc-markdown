|||
|---------|------------------------|
|**ID**|**M0003**|
|**Objective(s)**|[Anti-Behavioral Analysis](https://github.com/MAECProject/malware-behaviors/tree/master/anti-behavioral-analysis)|
|**Related ATT&CK Technique(s)**|None|

Dynamic Analysis Evasion
========================
Malware may obstruct dynamic analysis in a sandbox, emulator, or virtual machine. 

See [Emulator Evasion](https://github.com/MAECProject/malware-behaviors/tree/master/anti-behavioral-analysis/emulator-evade.md) for an  emulator-specific evasion behavior, and see [Execution Guardrails](https://github.com/MAECProject/malware-behaviors/blob/master/anti-behavioral-analysis/execution-guardrails.md) for a behavior that constrains dynamic execution based on environmental conditions. 

Methods
-------
* **Data Flood**: Overloads a sandbox by generating a flood of meaningless behavioral data. [[1]](#1)
* **Delayed Execution** - Stalling code is typically executed before any malicious behavior. The malware's aim is to delay the execution of the malicious activity long enough so that an automated dynamic analysis system fails to extract the interesting malicious behavior. 
* **Demo Mode**: Inclusion of a demo binary/mode that is executed when token is absent or not enough privileged.
* **Drop Code**: Original file is written to disk then executed. May confuse some sandboxes, especially if the dropped executable must be provided specific arguments and the original dropper is not associated with the drop file(s).
* **Encode File**: Encode a file on disk, such as an implant's config file.
* **Hook File System**: do something when particular file/dir is accessed; often through hooking certain API calls such as CreateFileA and CreateFileW.
* **Hook Interrupt**: modification of interrupt vector or descriptor tables.
* **Illusion**: Creates an illusion; makes the analyst think something happened when it didn't.
* **Timing/Date Checks**: Calling GetSystemTime or equiv and only executing code if the current date/hour/minute/second passes some check. Often this is for running only after or only until a specific date. This behavior can be mitigated in non-automated analysis environments.
* **Timing/Uptime Check**: Comparing single GetTickCount with some value to see if system has been started at least *X* amount ago. This behavior can be mitigated in non-automated analysis environments.


Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|-----------|-----------------------------|
|[**Ursnif**](https://github.com/MAECProject/malware-behaviors/blob/master/xample-malware/ursnif.md) | May 2016 | Ursnif uses malware macros to evade sandbox detection. [[2]](#2)|
|[**Terminator**](https://github.com/MAECProject/malware-behaviors/blob/master/xample-malware/terminator.md) | October 2013 | The Terminator rat evades a sandbox by not executing until after a reboot. Most sandboxes don't reboot during an analysis. [[3]](#3)|
|**Nap**| 2013 | Trojan Nap (tied to the Kelihos Botnet) uses extended sleep calls to evade sandbox analysis. [[3]](#3)|

References
----------
<a name="1">[1]</a> http://joe4security.blogspot.com/2013/06/overloading-sandboxes-new-generic.html

<a name="2">[2]</a> https://www.cyber.nj.gov/threat-profiles/trojan-variants/ursnif

<a name="3">[3]</a> https://www.fireeye.com/content/dam/fireeye-www/current-threats/pdfs/pf/file/fireeye-hot-knives-through-butter.pdf

