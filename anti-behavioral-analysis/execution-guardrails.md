|||
|---------|------------------------|
|**ID**|**E1480**|
|**Objective(s)**|[Anti-Behavioral Analysis](https://github.com/MAECProject/malware-behaviors/tree/master/anti-behavioral-analysis), [Defense Evasion](https://github.com/MAECProject/malware-behaviors/tree/master/defense-evasion)|
|**Related ATT&CK Technique(s)**|[Execution Guardrails](https://attack.mitre.org/techniques/T1480/)|

Execution Guardrails
====================
Malware may use execution guardrails (environmental conditions) to constrain execution. This behavior is related to the [Evade Dynamic Analysis](https://github.com/MAECProject/malware-behaviors/tree/master/anti-behavioral-analysis/evade-dynamic-analysis.md) behavior that obstructs dynamic analysis in a sandbox, emulator, or virtual machine.

**See ATT&CK:** [**Execution Guardrails**](https://attack.mitre.org/techniques/T1480/) (which under ATT&CK does not pertain to anti-behavioral analysis behaviors).

Methods
-------
* **Deposited Keys**: Parts of the code and/or data is encrypted or otherwise relies on data external to the file itself. For example, malware that contains code that is encrypted with a key that is downloaded from a server; malware that only runs if certain other software is installed on the system. Also see Environmental Keys Method.
* **Environmental Keys**: Malware reads certain attributes of the system (BIOS version string, hostname, MAC address, etc.) and encrypts/decrypts portions of its code or data using those attributes as input, thus preventing itself from being run on an unintended system (e.g., sandbox, emulator, etc.). Also see Deposited Keys Method.
* **GetVolumeInformation**: This Windows API call is used to get the GUID on a system drive. Malware compares it to a previous (targeted) GUID value and only executes maliciously if they match. This behavior can be mitigated in non-automated analysis environments.
* **Host Fingerprint Check**: Compare a previously computed host fingerprint(e.g., based on installed applications) to the current system's to determine if the malware instance is still executing on the same system. If not, execution stops, making debugging or sandbox analysis more difficult.
* **Secure Triggers**: Code and/or data is encrypted until the underlying system satisfies a preselected condition unknown to the analyst (this is a form of Deposited Keys).
* **Token Check**: Presence check to allow the program to run (ex: dongle, CD/DVD, key, file, network, etc.). If the token is specific to a hardware element (ex: disk, OS, CPU, NIC MAC, etc.), it is considered fingerprinting.


Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|-----------|-----------------------------|


References
----------


