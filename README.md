# <a name="mbc"></a>Malware Behavior Catalog #
The Malware Behavior Catalog (MBC) is a catalog of malware objectives and behaviors, created to support malware analysis-oriented use cases, such as labeling, similarity analysis, and standardized reporting. Please see the [FAQ](https://github.com/MBCProject/mbc-markdown/blob/master/yfaq/README.md) page for answers to common questions.

### Objectives ###
As shown below, malware objectives are based on [ATT&CK Tactics](https://attack.mitre.org/tactics/enterprise/), and are tailored for the malware analysis use case of characterizing malware based on known objectives and behaviors. Two malware analysis-specific objectives not in ATT&CK are also defined (ANTI-BEHAVIORAL ANALYSIS and ANTI-STATIC ANALYSIS). 

### Behaviors ###
Under each objective, MBC captures all behaviors and code characteristics discovered during malware analysis, with links to [ATT&CK Techniques](https://attack.mitre.org/techniques/enterprise/) as appropriate. Names of MBC behaviors may or may not match related ATT&CK techniques. Any content provided on behavior pages is *supplemental* to ATT&CK content. In other words, ATT&CK content is not duplicated in MBC, and MBC users will want to reference ATT&CK while capturing malware behaviors.

### <a name="ids"></a>Identifiers ###
The first letter of a behavior identifier indicates whether the behavior is a stub referencing an ATT&CK technique ("T", matching the ATT&CK identifier; e.g. T1234), whether it enhances an ATT&CK technique with malware-specific details ("E"; e.g. E1234), or whether it is a newly defined behavior in MBC ("M"; e.g. M1234). When two or more MBC behaviors refine the same ATT&CK technique, each is given an MBC identifier; when a new ATT&CK technique is defined *after* an MBC behavior has been defined, the preexisting MBC identifier is preserved. 

### Example Malware ###
The MBC also contains a collection of [example malware](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/) that are characterized with malware behaviors.

## Malware Objective Descriptions ##
Malware objectives are defined below. Follow the links to view associated behaviors. Please see the [MBC Matrix](http://maecproject.github.io/ema/index.html) to view all behaviors.

|**Objective**|**Description**|
|------------------------------------------------------------------|----------------------------|
|[**Anti-Behavioral Analysis**](https://github.com/MBCProject/mbc-markdown/blob/master/anti-behavioral-analysis/README.md) |Malware aims to prevent, obstruct, or evade behavioral analysis done in a sandbox, debugger, etc.|
|[**Anti-Static Analysis**](https://github.com/MBCProject/mbc-markdown/blob/master/anti-static-analysis/README.md)| Malware aims to prevent static analysis or make it more difficult. Simpler static analysis identifies features such as embedded strings, executable header information, hash values, and file metadata. More involved static analysis involves the disassembly of the binary code.|
|[**Collection**](https://github.com/MBCProject/mbc-markdown/blob/master/collection/README.md) | Malware aims to identify and gather information, such as sensitive files, from a target network prior to exfiltration. This objective includes locations on a system or network where the malware may look for information to exfiltrate.|
|[**Command and Control**](https://github.com/MBCProject/mbc-markdown/blob/master/command-and-control/README.md) |Malware aims to communicate (receive and/or execute remotely submitted commands) with controlling or controlled systems within a target network (C2 servers, bots, etc.).|
|[**Credential Access**](https://github.com/MBCProject/mbc-markdown/blob/master/credential-access/README.md)|Malware aims to obtain credential access, allowing it or its underlying threat actor to assume control of an account, with the associated system and network permissions.|
|[**Defense Evasion**](https://github.com/MBCProject/mbc-markdown/blob/master/defense-evasion/README.md)|Malware aims to evade detection or avoid other cybersecurity defenses.|
|[**Discovery**](https://github.com/MBCProject/mbc-markdown/blob/master/discovery/README.md)|Malware aims to gain knowledge about the system and internal network.|
|[**Execution**](https://github.com/MBCProject/mbc-markdown/blob/master/execution/README.md)| Malware aims to execute its code on a system to achieve a variety of goals.|
|[**Exfiltration**](https://github.com/MBCProject/mbc-markdown/blob/master/exfiltration/README.md)|  Malware aims to steal data from the system on which it executes. This includes stored data (e.g., files) as well as data input into applications (e.g., web browser).|
|[**Impact**](https://github.com/MBCProject/mbc-markdown/blob/master/impact/README.md)| Malware aims to achieve its mission of manipulating, interrupting, or destroying systems and data.|
|[**Lateral Movement**](https://github.com/MBCProject/mbc-markdown/blob/master/lateral-movement/README.md)|Malware aims to propagate through the infection of a system or is able to infect a file after executing on a system. The malware may infect actively (e.g., gain access to a machine directly) or passively (e.g., send malicious email).|
|[**Persistence**](https://github.com/MBCProject/mbc-markdown/blob/master/persistence/README.md)|Malware aims to remain on a system regardless of system events.|
|[**Privilege Escalation**](https://github.com/MBCProject/mbc-markdown/blob/master/privilege-escalation/README.md)|Malware aims to obtain a higher level of privilege for execution.|

