# <a name="faq"></a>Malware Behavior Catalog Frequently Asked Questions # 

* [MBC's Relationship to ATT&CK](./#relationship)
* [MBC Origins](./#origin)
* [MBC Content](./#content)
* [Using MBC](./#use)
* [What's Next for MBC?](./#next)

## <a name="relationship"><a/>MBC's Relationship to ATT&CK ##

### We have [ATT&CK](https://attack.mitre.org), so why do we need the [Malware Behavior Catalog?](https://github.com/MBCProject/mbc-markdown) ###

As a publicly available framework, The Malware Behavior Catalog (MBC) aims to directly and explicitly define malware behaviors and code characteristics to support malware analysis-oriented use cases. MBC includes behaviors defined by ATT&CK, as well as those outside ATT&CK's scope. 

Operationally, most malware behaviors are identified via analysis, either direct analysis or from outside reporting or threat feeds. Subsequent tagging with MBC behaviors supports a variety of malware-related use cases: detection, mitigation and remediation, attribution, provenance and similarity scoring, and standardized reporting. Clearly defining methods malware uses to compromise systems or defeat analysis can also drive research toward improved detection, analysis, and prevention capabilities.

### Why not merge malware behaviors into ATT&CK? ###

It's not feasible for ATT&CK to expand to cover *all* problem spaces, to include the malware analysis space. As stated in the ATT&CK design and philosophy document [[1]](#1), "The basis of ATT&CK is the set of individual techniques that represent actions that adversaries can perform to accomplish objectives." This differs from the malware community's need to capture information discovered via *analysis* of malware code. 

While malware sometimes acts as a surrogate for an adversary (i.e., there is overlap between malware and adversary behavior), there are aspects unique to malware, mostly notably anti-analysis characteristics that are only identified during analysis: [ANTI-BEHAVIORAL ANALYSIS](https://github.com/MBCProject/mbc-markdown/tree/master/anti-behavioral-analysis) and [ANTI-STATIC ANALYSIS](https://github.com/MBCProject/mbc-markdown/tree/master/anti-static-analysis). Some MBC behaviors may be appropriate for inclusion in ATT&CK, but it is up to the ATT&CK team to identify them and integrate the content.

### Why does MBC include ATT&CK techniques? Why not create a stand-alone supplement to ATT&CK? ###

We believe that to most effectively support malware analysis, MBC should aim to provide a complete set of malware-related behaviors. Consequently, MBC defines new, malware-related behaviors, but also leverages ATT&CK as much as possible, identifying the reduced set of ATT&CK techniques pertaining to malware.

### Is there a formal relationship between ATT&CK and MBC? ###

No. Given that MBC aims to serve as a model and test case for how ATT&CK can be extended by second parties, we consult with the ATT&CK team to keep them apprised of our work, but there is no formal relationship between ATT&CK and MBC. While content of MBC was not coordinated with the ATT&CK team, we borrowed from ATT&CK's philosophy and methodology [[1]](#1). Namely, MBC will maintain a malware, code-oriented perspective; focus on real-world use of behaviors through empirical malware examples, drawing upon publicly available analysis and reporting; and maintain a level of abstraction appropriate for supporting malware analysis use cases (e.g., develop malware signatures, mitigate infection, drive analytics, attribution).  

### Will MBC be updated when ATT&CK is updated? ###

Yes. New and updated ATT&CK content supporting malware analysis use cases will be integrated into MBC. When a new ATT&CK technique is defined *after* an MBC behavior has been defined, the preexisting MBC identifier will be preserved. See the [Identifier](https://github.com/MBCProject/mbc-markdown#ids) section for details.

### Will MBC *always* remain distinct from ATT&CK, or someday might its content be merged into ATT&CK? ###

We can't predict what will happen in the long run, but currently there are no plans to merge MBC into ATT&CK. Over time, new ATT&CK techniques will be defined and some may directly pertain to malware in expanded ways. For example, the April 2019 ATT&CK update included a new technique - [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497/) - which may seem to blur the line between ATT&CK and MBC. However, the technique focuses on checks made by a human adversary (although malware is mentioned), and it's defined in the context of Defense Evasion and Discovery. Two related MBC behaviors pertain to malware anti-analysis objectives: [[Sandbox Detection]](https://github.com/MBCProject/mbc-markdown/blob/master/anti-behavioral-analysis/detect-sandbox.md) and [[Virtual Machine Detection]](https://github.com/MBCProject/mbc-markdown/blob/master/anti-behavioral-analysis/detect-vm.md) (ATT&CK doesn't define anti-analysis tactics). 

## <a name="origin"></a>MBC Origins ##

### What is the relationship between MAEC, EMA, and MBC? ###

In short, the [Malware Attribute Enumeration and Characterization (MAEC)](http://maecproject.github.io/) led to the [Encyclopedia of Malware Attributes (EMA)](https://collaborate.mitre.org/ema/index.php/ema:Main_Page), and EMA led to the Malware Behavior Catalog.

MAEC is a community-developed structured language for encoding and sharing high-fidelity information about malware based upon attributes such as behaviors, artifacts, and relationships between malware samples. The vocabularies associated with MAEC define malware capabilities and behaviors, which are further defined and specified in EMA, along with "behavior instances" that capture specific malware instances/families exhibiting behaviors.

After noting clear overlap between EMA and ATT&CK, we initially decided that EMA would only capture malware behaviors *not* captured by ATT&CK (primarily anti-analysis behaviors). However, ATT&CK defines many techniques not applicable to malware, so to provide a well-defined, single collection of *malware* behaviors, MBC was created. MBC differs from EMA in that MBC was created in ATT&CK's image with the hope that by following ATT&CK's philosophy and methodology, MBC would be more useful and readily adopted (see previous question). 

### How were MBC behaviors identified? ###

Many MBC behaviors stemmed from the MAEC and EMA work, with the collection evolving to mesh with ATT&CK tactics and techniques. We also identified MBC behaviors by studying publicly available analyses, reports, and output of automated analysis engines (some of which map behavior indicators to ATT&CK). Such resources enabled identification of malware-related ATT&CK techniques, as well as definition of new behaviors for results that could not be mapped to ATT&CK. Also, EMA behaviors for which a real-world example could not be found are captured as proof-of-concept in the [Theoretical Behavior List](https://github.com/MBCProject/mbc-markdown/tree/master/theoretical-behaviors). 

## <a name="content"></a>MBC Content ##

### Why aren't ATT&CK [Initial Access](https://github.com/MBCProject/mbc-markdown/tree/master/initial-access) techniques included in MBC? ###

Initial Access - the way malware gains an initial foothold within a system - is not typically determined by analyzing the malware's code. For example, in ATT&CK's [Spearphishing Attachment](https://attack.mitre.org/techniques/T1193/) technique, the attachment may be a malicious executable file, but the *code* of the attached file's isn't related to its email delivery. This is not to say an analyst can't surmise initial access by studying a malware instance, but determining initial access requires evidence beyond the malware's code. 

Some malware self-replicates or distributes other malware, but in keeping with MBC's *malware, code-oriented perspective*, such behaviors would be associated with the [LATERAL MOVEMENT](https://github.com/MBCProject/mbc-markdown/tree/master/lateral-movement/), [EXECUTION](https://github.com/MBCProject/mbc-markdown/tree/master/execution/), and/or [IMPACT](https://github.com/MBCProject/mbc-markdown/tree/master/impact/) objectives in MBC. For example, if malware sends spearphishing email, its behavior would be captured by the [Send Email](https://github.com/MBCProject/mbc-markdown/tree/master/execution/send-email.md) behavior, which is associated with execution and lateral movement.

### Why aren't [PRE-ATT&CK](https://attack.mitre.org/techniques/pre/) techniques used by malware authors included in MBC? ###
**For example, why doesn't the [Obfuscate or Encrypt Code](https://attack.mitre.org/techniques/T1319/) technique under the [Adversary OPSEC](https://attack.mitre.org/tactics/TA0021/) tactic apply to malware showing signs of anti-analysis techniques?**

PRE_ATT&CK is independent of technology and models an adversary's behavior as they attempt to gain access. By contrast, MBC captures behaviors associated with malware executable *code*. It does not capture human behaviors, even if the behaviors relate to malware. (Malware with obfuscated code, which makes analysis difficult, would be captured using the MBC [Executable Code Obfuscation](https://github.com/MBCProject/mbc-markdown/blob/master/anti-static-analysis/exe-code-obfuscate.md) behavior.) 

### ATT&CK defines "tactics" and "techniques." Why does MBC define "objectives" and "behaviors" instead? ###

The cyber adversary behavior and malware analysis realms each have their own vocabulary, and MBC aims to reflect malware analysis common word usage. Just as "tactics," "techniques," and "procedures" (TTPs) are considered when discussing advanced persistent threats (APTs), "objectives" and "behaviors" commonly considered when analyzing malware.

### ATT&CK is organized by the Enterprise and Mobile technology domains. Why isn't MBC? ###

Although both domains are included in MBC, we didn't see value in distinguishing between enterprise and mobile malware for supporting malware analysis use cases.

### ATT&CK is a mid-level adversary model. Does MBC model malware in a similar way? ###

ATT&CK models the life cycle of a human adversary, which results in an ordering of tactics (not necessarily strict), starting with Initial Access and ending with Impact. Software (malware code) executes sequentially but from a timing, life cycle perspective, it executes simultaneously. Therefore, MBC objectives are presented alphabetically, and MBC doesn't provide a model in the same sense as ATT&CK: rather MBC captures an unordered collection of objections and behaviors applicable to a malware sample.

### Some MBC behaviors seem to be characteristics of code, not actual behaviors (e.g., [Executable Code Optimization](https://github.com/MBCProject/mbc-markdown/blob/master/anti-static-analysis/exe-code-optimize.md)). Why are they captured and why are they called behaviors? ###

MBC captures traits of malware that are evident through code analysis to support malware analysis use cases. For example, capturing a characteristic such as Executable Code Optimization supports use cases such as attribution and detection by indicating that optimization has been used to make the code harder to analyze. Such "characteristics" are captured as "behaviors" to simplify MBC's structure; however, their descriptions identify them as "characteristics."

Characteristics are evident by looking at the code and may not relate to specific code snippets. For example, a high-level look at a malware instance can reveal it is encrypted ([Obfuscated Files or Information](https://github.com/MBCProject/mbc-markdown/blob/master/defense-evasion/obfuscate-files.md) ). 

Observables that do not reflect on the malware's *code* are not captured in MBC; for example, strings and data in the code are not captured in MBC.

### Do malware behaviors and adversary behaviors overlap? ###

Malware behaviors and adversary behaviors can overlap because adversaries sometimes use malware to achieve their goals. However, MBC only captures behaviors associated with malware *code*. In other words, MBC behaviors are identified through analysis of a malware sample's binary code or by observing the malware on a network (or in a disassembler), whereas adversary behaviors may be derived from a variety of indicators on a system or network. 

### Why don't MBC behavior names always match ATT&CK technique names? ###

MBC maintains a malware, code-oriented perspective, so MBC behavior names will not always match related ATT&CK names (although they usually do).

### Are individual MBC behaviors linked (related) to more than one ATT&CK technique? ###

No. An objective of MBC is to encompass all ATT&CK techniques pertaining to malware; therefore a single MBC behavior is never mapped to multiple ATT&CK techniques (except when an ATT&CK *Enterprise* technique is similar to an ATT&CK *Mobile* technique). 

This means additional MBC behaviors must sometimes be defined. For example, MBC initially defined one [Denial of Service](https://github.com/MBCProject/mbc-markdown/blob/master/impact/denial-of-service.md) behavior, which was not defined in ATT&CK. After an update to ATT&CK defined two related techniques - [Endpoint Denial of Service](https://attack.mitre.org/techniques/T1499/) and [Network Denial of Service](https://attack.mitre.org/techniques/T1498/) (equivalent to MBC's Denial of Service behavior), MBC was expanded to include the Endpoint Denial of Service behavior.

### Are different MBC behaviors linked (related) to the same ATT&CK technique? ###

Yes. Sometimes an ATT&CK technique does not provide enough granularity for malware analysis-oriented use cases; therefore, multiple, more granular MBC behaviors may link to the same ATT&CK technique. 

For example, MBC defines separate behaviors for detecting sandboxes ([Sandbox Detection](https://github.com/MBCProject/mbc-markdown/blob/master/anti-behavioral-analysis/detect-sandbox.md)) and virtual machines ([Virtual Machine Detection](https://github.com/MBCProject/mbc-markdown/blob/master/anti-behavioral-analysis/detect-vm.md)). When ATT&CK was updated to include the  [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497/) technique, which includes detection of virtualization and sandboxes (although not obstruction in the sense of MBC's Dynamic Analysis Evasion behavior), the MBC behaviors were not combined. Rather, both were updated to show a relationship to the new ATT&CK technique.

## <a name="use"></a>Using MBC ##

### What are the primary use cases of MBC? ###

* **Standardized reporting**: Enables consistent interpretation of result data to improve detection, mitigation, and remediation.
* **Correlation of malware analysis results**: Correlates results of automated tools (e.g., sandboxes) or manual analysis, validating results or identifying areas for further investigation.
* **Labeled data sets for malware research**: Using MBC to label malware samples provides a collection of malware meeting chosen criteria that can support research (e.g., assessment of tool effectiveness, similarity analysis).
* **Malware analysis support**: MBC's set of identified, organized behaviors helps an analyst know what to look for, informing the malware analysis process.

### How should information in the Methods section be used? ###

Methods are variations of behaviors and are provided to help explain behaviors. Methods aren't intended to be referenced in analyses in the same way that behaviors are, in part because it would be hard to enumerate all methods associated with a behavior. 

MBC aims to support the malware analysis community so eventually, methods could be expanded and refined to serve as "sub-behaviors." If the expansion of methods is warranted, it may be they are used for manual mapping of behaviors while higher-level behaviors are used by automated analysis systems (which is not to say that some methods could not be identified automatically).

### Can MBC behaviors be used without MBC objectives? Can objectives be used without behaviors? Or must objectives and behaviors be specified in pairs? Can methods be used alone? ###

Objectives correspond to the intentions behind malware behaviors. For example, malware may use [Hooking](https://github.com/MBCProject/mbc-markdown/blob/master/credential-access/hooking.md) (behavior) to load and execute code within the context of another process either to hide its execution (defense evasion objective), to gain elevated privileges (privilege escalation objective), or to access the process's memory (credential access objective). Because it's not always possible to know intent, MBC behaviors can be used without objectives. For example, automated sandbox analysis may indicate hooking behavior without corresponding information on intent, in which case objectives might not be specified; alternatively, *all* objectives associated with a behavior might be noted. 

If lower level behaviors are not known, it may be appropriate to only reference an MBC objective. For example, if a sandbox reports that a malware sample exhibits "self-defense" with no other details, the information is best captured by the Defense Evasion objective, without specifying any specific behaviors.

Because methods are specific to a behavior, they're always associated with a behavior and aren’t used on their own.

### <a name="gotbotkr"><a/>Can malware behaviors identified via manual analysis map to multiple MBC behaviors, or should correspondence be one-to-one? ###

Each malware behavior identified during analysis and associated with a specific code snippet should map to a single MBC behavior. If multiple behaviors seem to apply, the reported behavior should be considered to see whether it can be broken into smaller components that lead to one-to-one mappings.

For example, a [GotBotKR](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/gotbotkr.md) report reflecting manual analysis reads, "The malware installs two instances of itself on the system. The second instance (watchdog) monitors whether the first instance is still active and reinstalls it if it has been removed from the system" [[2]](#2). Initially, one might think this is a single behavior, but it can be broken apart and mapped into three MBC behaviors:

* [PERSISTENCE::Redundant Access](https://github.com/MBCProject/mbc-markdown/blob/master/defense-evasion/redundant-access.md) ("installs two instances of itself")

* [DISCOVERY::Process Discovery](https://github.com/MBCProject/mbc-markdown/blob/master/discovery/process-discover.md) ("monitors whether the first instance is still active")

* [EXECUTION::Install Additional Program](https://github.com/MBCProject/mbc-markdown/blob/master/execution/install-prog.md) ("reinstalls [itself] if it has been removed")

### Can malware behaviors identified by automated sandboxes and tools map to multiple MBC behaviors or should correspondence be one-to-one? ###

Behaviors identified by automated tools are often intentionally broad to give an overview of the malware sample's behavior. Broad behaviors will often map to multiple MBC behaviors. For example, if a tool reports that Armadillo was used on the sample, both [Executable Code Obfuscation](https://github.com/MBCProject/mbc-markdown/blob/master/anti-static-analysis/exe-code-obfuscate.md) and [Software Packing](https://github.com/MBCProject/mbc-markdown/blob/master/anti-static-analysis/software-packing.md) behaviors apply.

### How are MBC behaviors, possibly at different levels of abstraction, associated? ###

MBC does not define relationships between behaviors, so association of behaviors must be done at the reporting level. The [GotBotKR](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/gotbotkr.md) example [above](./gotbotkr) illustrates how multiple (three) behaviors can be associated by the human-readable text: "The malware installs two instances of itself on the system. The second instance (watchdog) monitors whether the first instance is still active and reinstalls it if it has been removed from the system" [[2]](#2).

### How do I map an analysis product's output to MBC when I don't know the details behind the behavior indicators? ###

Ideally, the product vendor will provide the MBC mapping, but if not and it's not possible to ask the signature developer for details, it may be best to map the indicator to all potentially relevant MBC behaviors (a one-to-many mapping). For example, the indicator "opened listening port" could be mapped to both [COMMAND AND CONTROL::C2 Communication](https://github.com/MBCProject/mbc-markdown/blob/master/command-and-control/command-control-comm.md) and [IMPACT::Remote Access](https://github.com/MBCProject/mbc-markdown/blob/master/impact/remote-access.md).

### Can variant names captured by an anti-virus tool be captured in MBC? ###

No. MBC captures behaviors and characteristics directly associated with malware code. Variant names are outside MBC's scope. A variant name may lead to published reports, in which case, one could map the sample to its associated behaviors.

### Can MBC capture specific data values associated with a behavior? ###

No. For example, MBC might capture the behavior ANTI-BEHAVIORAL ANALYSIS::Emulator Detection::Registry Keys, but the specific registry key (e.g., SYSTEM\ControlSet001\Services\VBoxMouse (VBOX)) would be captured outside of MBC (e.g., as STIX Windows Registry Key Object). 

### If malware displays only some attributes defining a behavior, it is correct to say it exhibits the behavior? ###

Yes. In many cases, malware will display only a subset of a behavior's attributes. For example, the [System Information Discovery](https://github.com/MBCProject/mbc-markdown/blob/master/discovery/system-info-discovery.md) behavior includes discovery of a hostname, operating system version, patch information, processor architecture, etc. Malware that gathers only a hostname would still be said to exhibit the System Information Discovery behavior.

### What if no MBC behavior is defined for something I need to capture? ###

The MBC will evolve to better support the malware analysis community. If you have a suggestion for a new behavior (or any content change), please open an [issue](https://github.com/MBCProject/mbc-markdown/issues) on GitHub.

## <a name="use"></a>MBC and STIX 2 ##

### How are MBC behaviors captured in STIX 2? ###



## <a name="next"><a/>What's Next for MBC? ##

* **MBC Mailing List** - To join the MBC mailing list, please send a request to mbc@mitre.org.

* **Cuckoo-MBC Mappings** - Cuckoo Sandbox 2.0.7 includes mappings between its signatures and ATT&CK. The MBC team is defining Cuckoo-MBC mappings; accuracy will be increased because of MBC’s malware focus. We hope to have the full set of mappings on GitHub by the end of 2019.

* **STIX 2 Representation** - MBC content will soon be available in STIX 2 format - see the [mbc-stix2](https://github.com/MBCProject/mbc-stix2) repository.

* **MBC Website** - An MBC website will replace markdown documents by the end of 2019.

* **Code Snippets** - In addition to associating malware samples to behaviors, we plan to capture code snippets that illustrate behavior implementation.

* **Version Control** - Once MBC's initial development is completed at the end of 2019, all further changes will be tracked and released on a regular schedule.


References
----------
<a name="1">[1]</a> MITRE ATT&CK(TM): Design and Philosophy, https://www.mitre.org/sites/default/files/publications/pr-18-0944-11-mitre-attack-design-and-philosophy.pdf

<a name="2">[2]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/
