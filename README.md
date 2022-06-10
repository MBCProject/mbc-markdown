# <a name="mbc"></a>Malware Behavior Catalog v2.2 #
The Malware Behavior Catalog (MBC) is a catalog of malware objectives and behaviors, created to support malware analysis-oriented use cases, such as labeling, similarity analysis, and standardized reporting. Please see the [FAQ](./yfaq/README.md) page for answers to common questions.

Check out the MBC presentations:

* [Standardized Reporting with the Malware Behavior Catalog](https://youtu.be/qZef-SoREdY), VB2020 localhost (October 2020)
* [Malware Behavior Catalog](https://youtu.be/KY8Ty-0sdVU), BSides DC (October 2019)

We've also mapped MBC (and ATT&CK) to two open-source malware analysis tools:

* [Cuckoo community signatures](https://github.com/MBCProject/community)
* [capa rules](https://github.com/fireeye/capa-rules)

To join the **MBC mailing list**, please send a request to mbc@mitre.org.

### Objectives ###
As shown below, malware objectives are based on [ATT&CK tactics](https://attack.mitre.org/tactics/enterprise/), and are tailored for the malware analysis use case of characterizing malware based on known objectives and behaviors. Two malware analysis-specific objectives not in ATT&CK are also defined (ANTI-BEHAVIORAL ANALYSIS and ANTI-STATIC ANALYSIS). 

### Behaviors ###
Under each objective, MBC captures all behaviors and code characteristics discovered during malware analysis, with links to [ATT&CK techniques](https://attack.mitre.org/techniques/enterprise/) as appropriate. Names of MBC behaviors may or may not match related ATT&CK techniques. Any content provided on behavior pages is *supplemental* to ATT&CK content. In other words, ATT&CK content is not duplicated in MBC, and MBC users will reference ATT&CK while capturing malware behaviors.

### Methods ###
Methods are associated with behaviors and serve different roles, depending on the behavior. In some cases, a method further refines a behavior (i.e., sub-behavior); in other cases, a method is an implementation of a behavior. Previously, methods had no ATT&CK counterpart, but beginning in April 2020, ATT&CK defines sub-techniques, which are similar to methods.

Note that a method cannot be used without a behavior.

### Micro-behaviors ###
Some malware behaviors are low-level, support many objectives and other behaviors, and aren't necessarily malicious. For example, a TCP socket may be created, or a string may be checked for some condition. Because such behaviors are often noted in malware analysis, they are captured in MBC. See [Micro-behaviors](./micro-behaviors/README.md) for details.

### <a name="ids"></a>Identifiers ###
As shown below, the letter of an identifier relays information about a behavior. Note that letters used in MBC 2.0 are changed from previous versions.

|**Letter**|**Example**|**Description**|
|---|---|---|
|**B**|*B0040*|An MBC behavior.|
|**C**|*C0015*|An MBC micro-behavior.|
|**T**|*T1234*|An ATT&CK technique.|
|**E**|*E1234*|An ATT&CK technique that has been enhanced with malware-specific details. The numerical portion of the identifier will match the ATT&CK ID (e.g., E1234 enhances T1234).|
|**F**|*F0004*|An ATT&CK sub-technique that has been enhanced with malware-specific details.|

Two letters of an identifier relay information about an objective.

|**Letter**|**Example**|**Description**|
|---|---|---|
|**OB**|*OB0001*|An MBC objective.|
|**OC**|*OC0003*|An MBC micro-objective.|

Identifiers of methods are formatted in the same way as ATT&CK sub-techniques. If MBC defines a new method for an existing ATT&CK technique, the identifier is changed from "T" to "E" and an "m" identifier is added (e.g., a method added to T1234 would be denoted *E1234.m01* and is different than *T1234.001*, although both refer to the T1234 ATT&CK technique). Method identifiers of "B", "C", and "F" behaviors are defined without the "m" (e.g., *B0008.009*; *C0005.002*; *F0001.005*).

When two or more MBC behaviors refine the same ATT&CK technique, each is given an MBC identifier and each references the ATT&CK identifier. When a new ATT&CK technique is defined *after* an MBC behavior has been defined, the preexisting MBC identifier is preserved and the new ATT&CK identifier is referenced.

### Canonical Representation ###
The canonical representation for MBC content is **OBJECTIVE::Behavior::Method**. For example, *ANTI-BEHAVIORAL ANALYSIS::Debugger Detection::Process Environment Block*. 

Objectives and behaviors can be used alone, but a method *must* be associated with a behavior.

### Example Malware ###
The MBC also contains a collection of [example malware](./xample-malware/README.md) that are characterized with malware behaviors.

## Micro-behavior Objectives ##
[Micro-behaviors](./micro-behaviors/README.md) and their associated objectives are under development.

## Malware Objective Descriptions ##
Malware objectives are defined in the table below. Follow the links to view associated behaviors. A visual representation of the MBC Matrix is also available (opens in a new window). There is another version under [FAQ](./yfaq/) with behavior ids.

<img src="https://raw.githubusercontent.com/MBCProject/mbc-markdown/v2.2/yfaq/mbc_matrix_without_ids.svg" alt="mbc matrix without ids">

|**Objective**|**Description**|
|---|---|
|[**Anti-Behavioral Analysis**](./anti-behavioral-analysis/README.md)|Malware aims to prevent, obstruct, or evade behavioral analysis done in a sandbox, debugger, etc.|
|[**Anti-Static Analysis**](./anti-static-analysis/README.md)|Malware aims to prevent static analysis or make it more difficult. Simpler static analysis identifies features such as embedded strings, executable header information, hash values, and file metadata. More involved static analysis involves the disassembly of the binary code.|
|[**Collection**](./collection/README.md)|Malware aims to identify and gather information, such as sensitive files, from a target network prior to exfiltration. This objective includes locations on a system or network where the malware may look for information to exfiltrate.|
|[**Command and Control**](./command-and-control/README.md)|Malware aims to communicate (receive and/or execute remotely submitted commands) with controlling or controlled systems within a target network (C2 servers, bots, etc.).|
|[**Credential Access**](./credential-access/README.md)|Malware aims to obtain credential access, allowing it or its underlying threat actor to assume control of an account, with the associated system and network permissions.|
|[**Defense Evasion**](./defense-evasion/README.md)|Malware aims to evade detection or avoid other cybersecurity defenses.|
|[**Discovery**](./discovery/README.md)|Malware aims to gain knowledge about the system and internal network.|
|[**Execution**](./execution/README.md)|Malware aims to execute its code on a system to achieve a variety of goals.|
|[**Exfiltration**](./exfiltration/README.md)|Malware aims to steal data from the system on which it executes. This includes stored data (e.g., files) as well as data input into applications (e.g., web browser).|
|[**Impact**](./impact/README.md)|Malware aims to achieve its mission of manipulating, interrupting, or destroying systems and data.|
|[**Lateral Movement**](./lateral-movement/README.md)|Malware aims to propagate through the infection of a system or is able to infect a file after executing on a system. The malware may infect actively (e.g., gain access to a machine directly) or passively (e.g., send malicious email).|
|[**Persistence**](./persistence/README.md)|Malware aims to remain on a system regardless of system events.|
|[**Privilege Escalation**](./privilege-escalation/README.md)|Malware aims to obtain a higher level of privilege for execution.|


**Copyright 2021 The MITRE Corporation. [Terms of Use](./tou.md)**

