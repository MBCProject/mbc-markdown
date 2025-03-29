# Malware Behavior Visualization

We investigated the [STIX Visualizer (STIXviz)](https://github.com/oasis-open/cti-stix-visualization) and the [Attack Flow Builder (AFB)](https://github.com/center-for-threat-informed-defense/attack-flow) for visualizing malware behaviors as defined by MBC and ATT&CK. Example graphs are given for [Lactrodectus]() and [IceID](). 

We assume the reader is familiar with [Structured Thrreat Information Expression (STIX)](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html) (a language and serialization format used to exchange cyber threat intelligence) and [Attack Flow](https://github.com/center-for-threat-informed-defense/attack-flow) (a language for describing how cyber adversaries combine and sequende offensive techniques to achieve their goals).

**Choosing between STIXviz and AFB**

The STIXviz user interface is more advanced than AFB's, so if STIX content is available or easy for the user to generate, STIXviz may be the better option. However, creating a behavior graph when a STIX representation is not available is much easier with AFB. Capturing temporal flow/chronology is also in AFB (AFB was designed for "flows").

Other considerations:
- Relationships in AFB are very basic (details not captured).
- For someone familiar with STIX, building a graph in AFB may take more time than generating STIX.
- AFB can be used as a tool for generating STIX. The AFB "Publish Attack Flow" option produces a STIX bundle. The resulting JSON output is not fully aligned with STIX (for example, STIX Relationship Objects are missing) but the output is a good start and can be displayed in STIXviz. 

## **[STIX Visualizer](https://github.com/oasis-open/cti-stix-visualization)**
The STIX Visualizer (STIXviz) displays STIX content supported by various schemas. Malware analysis information should be captured in STIX using the [Malware Behavior Extension](https://github.com/oasis-open/cti-stix-common-objects/tree/main/extension-definition-specifications/malware-behavior-8e9); details and its schema are available in the [OASIS Common Object Repository (COR)](https://github.com/oasis-open/cti-stix-common-objects/tree/main).

**Resources**

- [STIXviz online](https://oasis-open.github.io/cti-stix-visualization/) 
- [STIXviz download](https://github.com/oasis-open/cti-stix-visualization)
- [Malware Behavior Extension Definition Object](https://github.com/oasis-open/cti-stix-common-objects/tree/main/extension-definition-specifications/malware-behavior-8e9)
- [Custom STIXviz configuration file](stixviz-config.json)
- [STIX Validator](https://github.com/oasis-open/cti-stix-validator)
- [MBC STIX 2.1 representation](https://github.com/MBCProject/mbc-stix2.1)
- [ATT&CK STIX 2.0 representation](https://github.com/mitre/cti/tree/master/enterprise-attack)


**Usage Notes**
- For a node to be visable in STIXviz, the object's STIX JSON must be included in the STIX Bundle. The required JSON objects can be found in the STIX 2 representations for [MBC](https://github.com/MBCProject/mbc-stix2.1) and [ATT&CK](https://github.com/mitre/cti/tree/master/enterprise-attack).
- A custom STIXviz [configuation file - CONFIG FILE MADE AVAILABLE IN yvisualizaiton FOLDER]() is needed to display MBC content.

**Best Practices**

- Use STIX Relationship Objects (SROs) to show chronology between behaviors. 
    - For example, Behavior "leads-to" Behavior.
    - Relationship types are not defined in the malware behavior extension, but the *relationship_type* property can be any string. 
    - Explicit relationships between Behavior objects may be defined in a future version of the extension.
- Use SROs to capture relationships between Behavior and Malware objects. 
    - For example, a Behavior "delivers" Malware. 
- Use SROs to capture relationships between Malware objects
    - For example, Malware "drops" Malware.
- Use SROs to capture chronology information.
    - For example, Behavior "leads-to" Behavior.
    - The *created* and *modified* common properties could be used to capture chronology, but the properties are not displayed in the STIXviz graph.
- Use Grouping objects to specify AND and OR operations. 
    - The *context* property is set equal to "and" or "or." 
    - All objects referenced in a Grouping *object_refs* property are those being and-ed or or-ed. 
    - An SRO would be defined as a Behavior "chooses-from" Grouping.
- Use Grouping objects to capture components of modular malware or sets of C2 commands 
    - The *context* is set equal to "chooses-from".
- Use an SRO to capture a conditional operation.
    - Behavior "if-true" Behavior and Behavior "if-false" Behavior. 
- Use an Incident object (and associated Event and Impact objects) when capturing objects such as Threat Actors and Indicators.
    - See the [Incident Extension](https://github.com/oasis-open/cti-stix-common-objects/tree/main/extension-definition-specifications/incident-ef7) in the OASIS Common COR.


## **[Attack Flow Builder](https://github.com/center-for-threat-informed-defense/attack-flow)** 
The Attack Flow Builder allows a user to build a graph by inserting nodes and edges. Nodes can be Attack Flow objects (Action, Asset, AND/OR operators, and a Conditional object), STIX Domain Objects (SDOs), or STIX Cyber Observables (SCOs). The Attack Flow team defined a [STIX Extension Definition](https://github.com/center-for-threat-informed-defense/attack-flow/tree/main/stix) so that an AFB diagram can be saved as a STIX Bundle.

**Resources**

- [Online AFB tool](https://center-for-threat-informed-defense.github.io/attack-flow/ui/)
- [AFB STIX Extension Definition Object](https://github.com/center-for-threat-informed-defense/attack-flow/tree/main/stix)
- [Attack Flow STIX schema](https://github.com/center-for-threat-informed-defense/attack-flow/tree/main/stix)     

**Usage Note**

- ATT&CK Tactics and Techniques are available in property drop-down menus.
- MBC Behaviors and Methods must be manually entered.
- Any Action node without an incoming edge is considered a start_ref to the Flow.
- AFB relationships are all generic "related-to" (i.e., relationships have no properties).
- In the STIX output, relationships are only created between Attack Flow objects (Actions, Assets).
- The STIXviz configuration file would need to be modified to fully display Attack Flow objects.

**Best Practices**

- Used the description field for details that will help the viewer's understanding.
- When capturing ATT&CK content, Action objects are better than STIX objects because they offer drop-down menus of ATT&CK Tactics and Techniques.
- MBC content should be captured with Action objects to align with the capture of ATT&CK content. 
- STIX Observables should be used instead of AFB Assets because they have more properties for capturing details.
- An AFB graph may be disconnected (a collection of subgraphs) when capturing individual execution paths.