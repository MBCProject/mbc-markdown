# <a name="mbc"></a>Malware Behavior Catalog v3.0 #
The Malware Behavior Catalog (MBC) is a catalog of malware objectives and behaviors, created to support malware analysis-oriented use cases, such as labeling, similarity analysis, and standardized reporting. Please see the [FAQ](./yfaq/README.md) page for answers to common questions, and read the [newsletters](./ynewsletters/README.md) for information on the most recent MBC updates and activity.

Open-source malware analysis tools map their output to MBC and ATT&CK:

* [capa](https://github.com/fireeye/capa-rules) - see the [capa rule mapping distribution](./capa.md)
* [CAPE](https://github.com/kevoreilly/community/tree/master/modules/signatures) - see the [CAPE signature mapping distribution](./cape.md)

MBC supports other community efforts:

* [CACAO](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cacao) - a [playbook](https://github.com/oasis-tcs/cacao/tree/master/Examples/CACAO-2.0) for the MBC corpus malware [Locky Bart](./xample-malware/locky-bart.md) shows how CACAO can reference MBC behaviors.
* [Attack Flow](https://github.com/center-for-threat-informed-defense/attack-flow/tree/main/corpus) - flow diagrams for the MBC corpus malware [Shamoon](./xample-malware/shamoon.md) and [SearchAwesome](./xample-malware/searchawesome.md) illustrate how Attack Flow can reference MBC behaviors.

Check out MBC presentations:

* [Standardized Reporting with the Malware Behavior Catalog](https://youtu.be/qZef-SoREdY), VB2020 localhost (October 2020)
* [Malware Behavior Catalog](https://youtu.be/KY8Ty-0sdVU), BSides DC (October 2019)

To join the **MBC mailing list**, please send a request to mbc@mitre.org.

### Objectives ###
As shown below, malware objectives are based on [ATT&CK tactics](https://attack.mitre.org/tactics/enterprise/), and are tailored for the malware analysis use case of characterizing malware based on known objectives and behaviors. Two malware analysis-specific objectives not in ATT&CK are also defined (ANTI-BEHAVIORAL ANALYSIS and ANTI-STATIC ANALYSIS). 

### Behaviors ###
Under each objective, MBC captures all behaviors and code characteristics discovered during malware analysis, with links to [ATT&CK techniques](https://attack.mitre.org/techniques/enterprise/) as appropriate. Names of MBC behaviors may or may not match related ATT&CK techniques. Any content provided on behavior pages is *supplemental* to ATT&CK content. In other words, ATT&CK content is not duplicated in MBC, and MBC users will reference ATT&CK while capturing malware behaviors.

### Methods ###
Methods are associated with behaviors and serve different roles, depending on the behavior. In some cases, a method further refines a behavior (i.e., sub-behavior); in other cases, a method is an implementation of a behavior. Previously, methods had no ATT&CK counterpart, but beginning in April 2020, ATT&CK defines sub-techniques, which are similar to methods.

Note that a method cannot be used without a behavior.

### Micro-objectives / Micro-behaviors ###
Some malware behaviors are low-level, support many objectives and other behaviors, and aren't necessarily malicious. For example, a TCP socket may be created, or a string may be checked for some condition. Because such behaviors are often noted in malware analysis, they are captured in MBC. See [Micro-behaviors](./micro-behaviors/README.md) for details.

### <a name="ids"></a>Identifiers ###
As shown below, the letter of an identifier relays information about a behavior. Note that letters used in MBC v2 and v3 are changed from MBC v1.

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

In cases where an MBC behavior enhances a technique/sub-technique that is defined in both ATT&CK Mobile and Enterprise, the "E" identifier used in MBC corresponds to the Enterprise identifier. For example, the Obfuscated Files or Information technique has identifier <a href="https://attack.mitre.org/techniques/T1027/">T1027</a> in Enterprise, identifier <a href="https://attack.mitre.org/techniques/T1406/">T1406</a> in Mobile, and identifier <a href="./defense-evasion/obfuscated-files-or-information.md">E1027</a> in MBC.

### Canonical Representation ###
The canonical representation for MBC content is **OBJECTIVE::Behavior::Method**. For example, *ANTI-BEHAVIORAL ANALYSIS::Debugger Detection::Process Environment Block*. 

Objectives and behaviors can be used alone, but a method *must* be associated with a behavior.

### STIX 2.1 Representation ###
A refined STIX 2.1 [Malware Behavior Extension](https://docs.google.com/document/d/1azr8ewNXhWyLt1a2wE2cG964QuFSPdIBSqCJFJrwEVo/) includes new STIX domain objects for MBC objectives, behaviors, and methods.

### Navigator View ###
This visual representation of the MBC Matrix is based on the ATT&CK Navigator. Two views are available: 

* <a href="https://raw.githubusercontent.com/MBCProject/mbc-markdown/master/yfaq/mbc_matrix_with_ids.svg" target="_blank">Matrix with identifiers</a>
* <a href="https://raw.githubusercontent.com/MBCProject/mbc-markdown/master/yfaq/mbc_matrix_without_ids.svg" target="_blank">Matrix without identifiers</a>

### Malware Corpus ###
The MBC contains a [malware corpus](./xample-malware/README.md) where each malware entry is decomposed into behaviors that are mapped to ATT&CK and MBC. The mappings are based on open source malware analysis reports. Note that some malware types are also present in the ATT&CK software page. We refer readers to the corresponding ATT&CK page for a list of identified ATT&CK techniques. However, we will list any newly identified ATT&CK techniques in the MBC malware page. 

## Malware Objective Descriptions ##
Malware objectives are defined in the table below. Follow the links to view associated behaviors. 

|**Objective**|**Description**|
|---|---|
|[**Anti-Behavioral Analysis**](./anti-behavioral-analysis/README.md)|Malware aims to prevent, obstruct, or evade behavioral analysis, such as analysis done using a sandbox or debugger.|
|[**Anti-Static Analysis**](./anti-static-analysis/README.md)|Malware aims to prevent static analysis or make it more difficult.|
|[**Collection**](./collection/README.md)|Malware aims to identify and gather information from a machine or network.|
|[**Command and Control**](./command-and-control/README.md)|Malware aims to communicate with compromised systems to control them.|
|[**Credential Access**](./credential-access/README.md)|Malware aims to steal account names and passwords.|
|[**Defense Evasion**](./defense-evasion/README.md)|Malware aims to evade detection.|
|[**Discovery**](./discovery/README.md)|Malware aims to gain knowledge about the environment.|
|[**Execution**](./execution/README.md)|Malware aims to execute code on a system.|
|[**Exfiltration**](./exfiltration/README.md)|Malware aims to steal data.|
|[**Impact**](./impact/README.md)|Malware aims to manipulate, interrupt, or destroy systems or data.|
|[**Lateral Movement**](./lateral-movement/README.md)|Malware aims to propagate or otherwise move through an environment. Lateral movement may be active, happening via direct machine access, or may be passive (for example, done via malicious email).|
|[**Persistence**](./persistence/README.md)|Malware aims to remain on a system.|
|[**Privilege Escalation**](./privilege-escalation/README.md)|Malware aims to obtain higher level permissions.|

## MBC Behaviors ##
The table below lists MBC behaviors and related ATT&CK techniques. In most cases, related ATT&CK techniques were defined *after* the MBC behavior was defined. Please see the [MBC Summary](./mbc_summary.md) for a listing of all MBC content.

|**ID**|**Objective(s)**|**Behavior**|**Related ATT&CK Technique**|
|---|---|---|---|
|**B0001**|ANTI-BEHAVIORAL ANALYSIS|**Debugger Detection**|*none*|
|**B0002**|ANTI-BEHAVIORAL ANALYSIS|**Debugger Evasion**|Debugger Evasion ([T1622](https://attack.mitre.org/techniques/T1622))|
|**B0003**|ANTI-BEHAVIORAL ANALYSIS|**Dynamic Analysis Evasion**|Virtualization/Sandbox Evasion ([T1497](https://attack.mitre.org/techniques/T1497),[T1633](https://attack.mitre.org/techniques/T1633))|
|**B0004**|ANTI-BEHAVIORAL|**Emulator Detection**|*none*|
|**B0005**|ANTI-BEHAVIORAL|**Emulator Evasion**|*none*|
|**B0006**|ANTI-BEHAVIORAL|**Memory Dump Evasion**|*none*|
|**B0007**|ANTI-BEHAVIORAL|**Sandbox Detection**|Virtualization/Sandbox Evasion: System Checks ([T1497.001](https://attack.mitre.org/techniques/T1497/001),[T1633.001](https://attack.mitre.org/techniques/T1633/001)); Virtualization/Sandbox Evasion: User Activity Based Checks ([T1497.002](https://attack.mitre.org/techniques/T1497/002))|
|**B0008**|ANTI-BEHAVIORAL ANALYSIS, ANTI-STATIC ANALYSIS|**Executable Code Virtualization**|*none*|
|**B0009**|ANTI-BEHAVIORAL ANALYSIS|**Virtual Machine Detection**|Virtualization/Sandbox Evasion ([T1497](https://attack.mitre.org/techniques/T1497),[T1633](https://attack.mitre.org/techniques/T1633))|
|**B0010**|ANTI-STATIC ANALYSIS|**Call Graph Generation Evasion**|*none*|
|**B0011**|EXECUTION|**Remote Commands**|Virtualization/Sandbox Evasion ([T1497](https://attack.mitre.org/techniques/T1497),[T1633](https://attack.mitre.org/techniques/T1633))|
|**B0012**|ANTI-STATIC ANALYSIS|**Disassembler Evasion**|*none*|
|**B0013**|DISCOVERY|**Analysis Tool Discovery**|*none*|
|**B0014**|DISCOVERY|**SMTP Connection Discovery**|*none*|
|**B0015**|*not defined*|---|---|
|**B0016**|IMPACT|**Compromise Data Integrity**|Data Manipulation: Stored Data Manipulation ([T1565.001](https://attack.mitre.org/techniques/T1565/001))|
|**B0017**|IMPACT|**Destroy Hardware**|*none*|
|**B0018**|IMPACT|**Resource Hijacking**|Resource Hijacking ([T1496](https://attack.mitre.org/techniques/T1496))|
|**B0019**|IMPACT|**Manipulate Network Traffic**|Data Manipulation: Transmitted Data Manipulation ([T1565.002](https://attack.mitre.org/techniques/T1565/002))|
|**B0020**|EXECUTION, LATERAL MOVEMENT|**Send Email**|Phishing ([T1566](https://attack.mitre.org/techniques/T1566))|
|**B0021**|EXECUTION, LATERAL MOVEMENT|**Send Poisoned Email**|*none*|
|**B0022**|IMPACT, PERSISTENCE|**Remote Access**|*none*|
|**B0023**|EXECUTION|**Install Additional Program**|*none*|
|**B0024**|EXECUTION|**Prevent Concurrent Execution**|*none*|
|**B0025**|ANTI-BEHAVIORAL ANALYSIS//EXECUTION|**Conditional Execution**|Execution Guardrails ([T1480](https://attack.mitre.org/techniques/T1480))|
|**B0026**|LATERAL MOVEMENT, PERSISTENCE|**Malicious Network Driver**|*none*|
|**B0027**|DEFENSE EVASION|**Alternative Installation Location**|*none*|
|**B0028**|CREDENTIAL ACCESS|**Cryptocurrency**|*none*|
|**B0029**|DEFENSE EVASION|**Polymorphic Code**|*none*|
|**B0030**|COMMAND AND CONTROL|**Command and Control Communication**|*none*|
|**B0031**|COMMAND AND CONTROL|**Domain Name Generation**|Dynamic Resolution: Domain Name Generation ([T1568.002](https://attack.mitre.org/techniques/T1568/002))|
|**B0032**|ANTI-STATIC ANALYSIS|**Executable Code Obfuscation**|*none*|
|**B0033**|IMPACT|**Denial of Service**|Network Denial of Service ([T1498](https://attack.mitre.org/techniques/T1498))|
|**B0034**|ANTI-STATIC ANALYSIS|**Executable Code Obfuscation**|*none*|
|**B0035**|PERSISTENCE|**Shutdown Event**|*none*|
|**B0036**|ANTI-BEHAVIORAL ANALYSIS|**Capture Evasion**|*none*|
|**B0037**|DEFENSE EVASION|**Bypass Data Execution Prevention**|*none*|
|**B0038**|DISCOVERY|**Self Discovery**|*none*|
|**B0039**|IMPACT|**Spamming**|*none*|
|**B0040**|DEFENSE EVASION|**Covert Location**|*none*|
|**B0041**|*not defined*|---|---|
|**B0042**|IMPACT|**Modify Hardware**|*none*|
|**B0043**|DISCOVERY|**Taskbar Discovery**|*none*|
|**B0044**|EXECUTION|**Execution Dependency**|*none*|
|**B0045**|ANTI-STATIC ANALYSIS|**Data Flow Analysis Evasion**|*none*|
|**B0046**|DISCOVERY|**Code Discovery**|*none*|
|**B0047**|DEFENSE EVASION, PERSISTENCE|**Install Insecure or Malicious Code**|*none*|

**Copyright © 2021-2023, The MITRE Corporation.  [Terms of Use.](./tou.md)**

