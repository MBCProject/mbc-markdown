# <a name="faq"></a>Malware Behavior Catalog Frequently Asked Questions # 

* [MBC's Relationship to ATT&CK](./#relationship)
* [MBC Origins](./#origin)
* [MBC Content](./#content)
* [Using MBC](./#use)

## <a name="relationship"><a/>MBC's Relationship to ATT&CK ##

### We have [ATT&CK](https://attack.mitre.org), so why do we need the [Malware Behavior Catalog?](https://github.com/MAECProject/malware-behaviors) ###

As a publicly available framework, The Malware Behavior Catalog (MBC) aims to directly and explicitly define malware behaviors and code characteristics to support malware analysis-oriented use cases. MBC includes behaviors defined by ATT&CK, as well as those outside ATT&CK's scope. 

Operationally, most malware behaviors are identified via analysis, either direct analysis or from outside reporting or threat feeds. Subsequent tagging with MBC behaviors supports a variety of malware-related use cases: detection, mitigation and remediation, attribution, provenance and similarity scoring, and standardized reporting. Clearly defining methods malware uses to compromise systems or defeat analysis can also drive research toward improved detection, analysis, and prevention capabilities.

### Why not merge malware behaviors into ATT&CK? ###

It's not feasible for ATT&CK to expand to cover *all* problem spaces, including the malware analysis space. As stated in the ATT&CK design and philosophy document [[1]](#1), "The basis of ATT&CK is the set of individual techniques that represent actions that adversaries can perform to accomplish objectives." This differs from the malware community's need to capture information discovered via *analysis* of malware code. 

While malware sometimes acts as a surrogate for an adversary (i.e., there is overlap between malware and adversary behavior), there are aspects unique to malware, mostly notably anti-analysis characteristics that are only identified during analysis: [Anti-Behavioral Analysis](https://github.com/MAECProject/malware-behaviors/tree/master/anti-behavioral-analysis) and [Anti-Static Analysis](https://github.com/MAECProject/malware-behaviors/tree/master/anti-static-analysis). Some MBC behaviors may be appropriate for inclusion in ATT&CK, but it is up to the ATT&CK team to identify them and integrate the content.

### Why does MBC include ATT&CK Techniques? Why not create a stand-alone supplement to ATT&CK? ###

We believe that to most effectively support malware analysis, MBC should aim to provide a complete set of malware-related behaviors. Consequently, MBC defines new, malware-related behaviors, but also leverages ATT&CK as much as possible, identifying the reduced set of ATT&CK techniques pertaining to malware.

### Is there a formal relationship between ATT&CK and MBC? ###

No. Given that MBC aims to serve as a model and test case for how ATT&CK can be extended by second parties, we consult with the ATT&CK team to keep them apprised of our work, but there is no formal relationship between ATT&CK and MBC. While content of MBC was not coordinated with the ATT&CK team, we borrowed from ATT&CK's philosophy and methodology [[1]](#1). Namely, MBC will maintain a malware, code-oriented perspective; focus on real-world use of behaviors through empirical malware examples, drawing upon publicly available analysis and reporting; and maintain a level of abstraction appropriate for supporting malware analysis use cases (e.g., develop malware signatures, mitigate infection, drive analytics, attribution).  

### Will MBC be updated when ATT&CK is updated? ###

Yes. New and updated ATT&CK content supporting malware analysis use cases will be integrated into MBC. When a new ATT&CK Technique is defined *after* an MBC Behavior has been defined, the preexisting MBC identifier will be preserved and the ATT&CK identifier will be appended (e.g., M0123:T1234). See the [Identifier](https://github.com/MAECProject/malware-behaviors#ids) section for details.

### Will MBC *always* remain distinct from ATT&CK, or someday might its content be merged into ATT&CK? ###

We can't predict what will happen in the long run, but currently there are no plans to merge MBC into ATT&CK. Over time, new ATT&CK techniques will be defined and some may directly pertain to malware in expanded ways. For example, the April 2019 ATT&CK update included a new technique - [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497/) - which may seem to blur the line between ATT&CK and MBC. However, the technique focuses on checks made by a human adversary (although malware is mentioned), and it's defined in the context of Defense Evasion and Discovery. Two related MBC behaviors pertain to malware anti-analysis objectives: [[Sandbox Detection]](https://github.com/MAECProject/malware-behaviors/blob/master/anti-behavioral-analysis/detect-sandbox.md) and [[Virtual Machine Detection]](https://github.com/MAECProject/malware-behaviors/blob/master/anti-behavioral-analysis/detect-vm.md) (ATT&CK doesn't define anti-analysis tactics). 

##<a name="origin">MBC Origins ##

### What is the relationship between MAEC, EMA, and MBC? ###

In short, the [Malware Attribute Enumeration and Characterization (MAEC)](http://maecproject.github.io/) led to the [Encyclopedia of Malware Attributes (EMA)](https://collaborate.mitre.org/ema/index.php/ema:Main_Page), and EMA led to the Malware Behavior Catalog.

MAEC is a community-developed structured language for encoding and sharing high-fidelity information about malware based upon attributes such as behaviors, artifacts, and relationships between malware samples. The vocabularies associated with MAEC define malware capabilities and behaviors, which are further defined and specified in EMA, along with "behavior instances" that capture specific malware instances/families exhibiting behaviors.

After noting clear overlap between EMA and ATT&CK, we initially decided that EMA would only capture malware behaviors *not* captured by ATT&CK (primarily anti-analysis behaviors). However, ATT&CK defines many techniques not applicable to malware, so to provide a well-defined, single collection of *malware* behaviors, MBC was created. MBC differs from EMA in that MBC was created in ATT&CK's image with the hope that by following ATT&CK's philosophy and methodology, MBC would be more useful and readily adopted (see previous question). 

### How were MBC Behaviors identified? ###

Many MBC Behaviors stemmed from the MAEC and EMA work, with the collection evolving to mesh with ATT&CK Tactics and Techniques. We also identified MBC Behaviors by studying publicly available analyses, reports, and output of automated analysis engines (some of which map behavior indicators to ATT&CK). Such resources enabled identification of malware-related ATT&CK Techniques, as well as definition of new Behaviors for results that could not be mapped to ATT&CK. Also, EMA Behaviors for which a real-world example could not be found are captured as proof-of-concept in the [Theoretical Behavior List](https://github.com/MAECProject/malware-behaviors/tree/master/theoretical-behaviors). 

##<a name="content">MBC Content ##

### Why aren't ATT&CK [Initial Access](https://github.com/MAECProject/malware-behaviors/tree/master/initial-access) Techniques included in MBC? ###

Initial Access - the way malware gains an initial foothold within a system - is not typically determined by analyzing the malware's code. For example, in ATT&CK's [Spearphishing Attachment](https://attack.mitre.org/techniques/T1193/) Technique, the attachment may be a malicious executable file, but the *code* of the attached file's isn't related to its email delivery. This is not to say an analyst can't surmise initial access by studying a malware instance, but determining initial access requires evidence beyond the malware's code. 

Some malware self-replicates or distributes other malware, but in keeping with MBC's *malware, code-oriented perspective*, such behaviors would be associated with the [Lateral Movement](https://github.com/MAECProject/malware-behaviors/tree/master/lateral-movement/), [Execution](https://github.com/MAECProject/malware-behaviors/tree/master/execution/), and/or [Effects](https://github.com/MAECProject/malware-behaviors/tree/master/effects/) Objectives in MBC. For example, if malware sends spearphishing email, its behavior would be captured by the [Send Email](https://github.com/MAECProject/malware-behaviors/tree/master/execution/send-email.md) Behavior, which is associated with execution and lateral movement.

### Why aren't [PRE-ATT&CK](https://attack.mitre.org/techniques/pre/) Techniques used by malware authors included in MBC? ###
**For example, why doesn't the [Obfuscate or Encrypt Code](https://attack.mitre.org/techniques/T1319/) Technique under the [Adversary OPSEC](https://attack.mitre.org/tactics/TA0021/) Tactic apply to malware showing signs of anti-analysis techniques?**

PRE_ATT&CK is independent of technology and models an adversary's behavior as they attempt to gain access. By contrast, MBC captures behaviors associated with malware executable *code*. It does not capture human behaviors, even if the behaviors relate to malware. (Malware with obfuscated code, which makes analysis difficult, would be captured using the MBC [Executable Code Obfuscation](https://github.com/MAECProject/malware-behaviors/blob/master/anti-static-analysis/exe-code-obfuscate.md) Behavior.) 

### ATT&CK defines "tactics" and "techniques." Why does MBC define "objectives" and "behaviors" instead? ###

The cyber adversary behavior and malware analysis realms each have their own vocabulary, and MBC aims to reflect malware analysis common word usage. Just as "tactics," "techniques," and "procedures" (TTPs) are considered when discussing advanced persistent threats (APTs), "objectives" and "behaviors" commonly considered when analyzing malware.

### ATT&CK is organized by the Enterprise and Mobile technology domains. Why isn't MBC? ###

To support malware analysis use cases, we didn't see value in distinguishing between enterprise and mobile malware.

### ATT&CK is a mid-level adversary model. Does MBC model malware in a similar way? ###

ATT&CK models the lifecycle of a human adversary, which results in an ordering of tactics (not necessarily strict), starting with Initial Access and ending with Impact. Software (malware code) executes sequentially but from a timing, lifecycle perspective, it executes simultaneously. Therefore, MBC objectives are presented alphabetically, and MBC doesn't provide a model in the same sense as ATT&CK: rather MBC captures an unordered collection of objections and behaviors applicable to a malware sample.

### Some MBC Behaviors seem to be characteristics of code, not actual behaviors (e.g., [Executable Code Optimization](https://github.com/MAECProject/malware-behaviors/blob/master/anti-static-analysis/exe-code-optimize.md)). Why are they captured and why are they called behaviors? ###

MBC captures traits of malware that are evident through analysis and that support one or more malware analysis use cases. For example, capturing a characteristic such as Executable Code Optimization supports use cases such as attribution and detection by indicating that optimization has been used to make the code harder to analyze. Such "characteristics" are called "behaviors" to simplify terminology.

### Do malware behaviors and adversary behaviors overlap? ###

Sometimes malware behaviors and adversary behaviors overlap because adversaries sometimes use malware to achieve their goals. However, MBC only captures behaviors associated with malware *code*. In other words, MBC Behaviors are identified through analysis of a malware sample's binary code or by observing the malware on a network (or in a disassembler), whereas adversary behaviors may be derived from a variety of indicators on a system or network. 

### Why don't MBC Behavior names always match ATT&CK Technique names? ###

MBC maintains a malware, code-oriented perspective, so MBC behavior names will not always match related ATT&CK names (although they usually do).

### Are individual MBC Behaviors linked (related) to more than one ATT&CK Technique? ###

No. An objective of MBC is to encompass all ATT&CK Techniques pertaining to malware; therefore a single MBC Behavior is never mapped to multiple ATT&CK Techniques (except when an ATT&CK *Enterprise* Technique is similar to an ATT&CK *Mobile* Technique). 

This means additional MBC Techniques must sometimes be defined. For example, MBC initially defined one Denial of Service Behavior, but after an update to ATT&CK included two related Techniques - [Endpoint Denial of Service](https://attack.mitre.org/techniques/T1499/) and [Network Denial of Service](https://attack.mitre.org/techniques/T1498/) - MBC was expanded to include both as Behaviors.

### Are different MBC Behaviors linked (related) to the same ATT&CK Technique? ###

Yes. Sometimes an ATT&CK Technique does not provide enough granularity for malware analysis-oriented use cases; therefore, multiple, more granular MBC Behaviors may link to the same ATT&CK Technique. 

For example, MBC defines separate behaviors for detecting sandboxes ([Sandbox Detection](https://github.com/MAECProject/malware-behaviors/blob/master/anti-behavioral-analysis/detect-sandbox.md)) and virtual machines ([Virtual Machine Detection](https://github.com/MAECProject/malware-behaviors/blob/master/anti-behavioral-analysis/detect-vm.md)). When ATT&CK was updated to include the  [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497/) Technique, which includes detection of virtualization and sandboxes (although not obstruction in the sense of MBC's Dynamic Analysis Evasion behavior), the MBC Behaviors were not combined. Rather, both were updated to show a relationship to the new ATT&CK Technique.

##<a name="use">Using MBC ##

### What are the primary use cases of MBC? ###

MBC enables consistency in reporting and consequently, supports analytics and similarity analysis. MBC's well-defined behaviors also support the definition of indicator signatures for detecting behaviors during analysis.

### Can Behaviors be used without Objectives? Or must Objectives and Behaviors be specified in pairs? ###

Objectives correspond to the intentions behind malware Behaviors. For example, malware may use [Hooking](https://github.com/MAECProject/malware-behaviors/blob/master/credential-access/hooking.md) to load and execute code within the context of another process either to hide its execution (defense evasion), to gain elevated privileges (privilege escalation), or to access the process's memory (credential access). Because it's not always possible to know intent, Behaviors can be used without Objectives. For example, automated sandbox analysis may indicate hooking behavior without corresponding information on intent, in which case objectives might not be specified, or *all* objectives associated with a Behavior might be noted.

### Can malware behaviors identified via analysis map to multiple MBC Behaviors, or should correspondence be one-to-one? ###


### How are MBC behaviors at different levels of abstraction associated?###

Association of behaviors is done at the reporting level. 


### How should information in the Methods section be used? ###

Methods are variations of behaviors and are provided to help explain Behaviors. Methods aren't intended to be referenced in analyses in the same way that Behaviors are, in part because it would be hard to enumerate all Methods associated with a Behavior. 

MBC aims to support the malware analysis community so eventually, Methods could be expanded and refined to serve as "sub-behaviors." If the expansion of Methods is warranted, it may be they are used for manual mapping of behaviors while higher-level Behaviors are used by automated analysis systems (which is not to say that some Methods could not be identified automatically).

### If malware displays only some attributes defining a Behavior, it is correct to say it exhibits the Behavior? ###

Yes. In many cases, malware will display only a subset of a Behavior's attributes. For example, the [System Information Discovery](https://github.com/MAECProject/malware-behaviors/blob/master/discovery/system-info-discovery.md) Behavior includes discovery of a hostname, operating system version, patch information, processor architecture, etc. Malware that gathers only a hostname would still be said to exhibit the System Information Discovery Behavior.

### What if no MBC Behavior is defined for something I need to capture? ###

The MBC will evolve to better support the malware analysis community. If you have a suggestion for a new behavior (or any content change), please open an [issue](https://github.com/MAECProject/malware-behaviors/issues) on GitHub.

References
----------
<a name="1">[1]</a> MITRE ATT&CK(TM): Design and Philosophy, https://www.mitre.org/sites/default/files/publications/pr-18-0944-11-mitre-attack-design-and-philosophy.pdf
