# <a name="mbc"></a>Malware Behavior Catalog #
The Malware Behavior Catalog (MBC) is a catalog of malware Objectives and Behaviors, created to support malware analysis-oriented use cases, such as labeling, similarity analysis, and standardized reporting. Please see the [FAQ](https://github.com/MAECProject/malware-behaviors/blob/master/yfaq/README.md) page for answers to common questions.

### Objectives ###
As shown below, malware Objectives are based on [ATT&CK Tactics](https://attack.mitre.org/tactics/enterprise/), and are tailored for the malware analysis use case of characterizing malware based on known Objectives and Behaviors. Two malware analysis-specific Objectives (Anti-Behavioral Analysis and Anti-Static Analysis) not in ATT&CK are also defined. 

### Behaviors ###
Under each Objective, MBC captures all behaviors and code characteristics discovered during malware analysis, with links to [ATT&CK Techniques](https://attack.mitre.org/techniques/enterprise/) as appropriate. Names of MBC Behaviors may or may not match related ATT&CK Techniques. Any content provided on Behavior pages is *supplemental* to ATT&CK content. In other words, ATT&CK content is not duplicated in MBC, and MBC users will want to reference ATT&CK while capturing malware Behaviors.

### <a name="ids"></a>Identifiers ###
The first letter of a Behavior identifier indicates whether the Behavior is a stub referencing an ATT&CK Technique ("T", matching the ATT&CK identifier; e.g. T1234), whether it enhances an ATT&CK Technique with malware-specific details ("E"; e.g. E1234), or whether it is a newly defined Behavior in MBC ("M"; e.g. M1234). 

When two or more MBC Behaviors refine the same ATT&CK Technique, they are given concatenated identifiers where the MBC portion distinguishes them (e.g. T1234:M0123, T1234:M0124). When a new ATT&CK Technique is defined *after* an MBC Behavior has been defined, the preexisting MBC identifier is preserved and the ATT&CK identifier is appended (e.g., M0123:T1234). 

### Example Malware ###
The MBC also contains a collection of [example malware](https://github.com/MAECProject/malware-behaviors/blob/master/xample-malware/) that are characterized with malware Behaviors.

## Malware Objective Descriptions ##
Malware Objectives are defined below. Follow the links to view associated Behaviors. Please see the [MBC Matrix](http://maecproject.github.io/ema/index.html) to view all Behaviors.

|**Objective**|**Description**|
|------------------------------------------------------------------|----------------------------|
|[**Anti-Behavioral Analysis**](https://github.com/MAECProject/malware-behaviors/blob/master/anti-behavioral-analysis/README.md) |Malware aims to prevent, obstruct, or evade behavioral analysis done in a sandbox, debugger, etc.|
|[**Anti-Static Analysis**](https://github.com/MAECProject/malware-behaviors/blob/master/anti-static-analysis/README.md)| Malware aims to prevent static analysis or make it more difficult. Simpler static analysis identifies features such as embedded strings, executable header information, hash values, and file metadata. More involved static analysis involves the disassembly of the binary code.|
|[**Collection**](https://github.com/MAECProject/malware-behaviors/blob/master/collection/README.md) | Malware aims to identify and gather information, such as sensitive files, from a target network prior to exfiltration. This Objective includes locations on a system or network where the malware may look for information to exfiltrate.|
|[**Command and Control**](https://github.com/MAECProject/malware-behaviors/blob/master/command-and-control/README.md) |Malware aims to communicate (receive and/or execute remotely submitted commands) with systems under its control within a target network or other systems (C2 servers, etc.).|
|[**Credential Access**](https://github.com/MAECProject/malware-behaviors/blob/master/credential-access/README.md)|Malware aims to obtain credential access, allowing it or its underlying threat actor to assume control of an account, with the associated system and network permissions.|
|[**Defense Evasion**](https://github.com/MAECProject/malware-behaviors/blob/master/defense-evasion/README.md)|Malware aims to evade detection or avoid other cybersecurity defenses.|
|[**Discovery**](https://github.com/MAECProject/malware-behaviors/blob/master/discovery/README.md)|Malware aims to gain knowledge about the system and internal network.|
|[**Execution**](https://github.com/MAECProject/malware-behaviors/blob/master/execution/README.md)|Malware aims to execute its code on a system to achieve secondary objectives, in conjunction with its primary objectives.|
|[**Exfiltration**](https://github.com/MAECProject/malware-behaviors/blob/master/exfiltration/README.md)|  Malware aims to steal data from the system on which it executes. This includes stored data (e.g., files) as well as data input into applications (e.g., web browser).|
|[**Impact**](https://github.com/MAECProject/malware-behaviors/blob/master/impact/README.md)|Malware aims to execute its mission.|
|[**Lateral Movement**](https://github.com/MAECProject/malware-behaviors/blob/master/lateral-movement/README.md)|Malware aims to propagate through the infection of a system or is able to infect a file after executing on a system. The malware may infect actively (e.g., gain access to a machine directly) or passively (e.g., send malicious email).|
|[**Persistence**](https://github.com/MAECProject/malware-behaviors/blob/master/persistence/README.md)|Malware aims to remain on a system regardless of system events.|
|[**Privilege Escalation**](https://github.com/MAECProject/malware-behaviors/blob/master/privilege-escalation/README.md)|Malware aims to obtain a higher level of privilege for execution.|

