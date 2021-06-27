|||
|---|---|
|**ID**|**OB0002**|


# Anti-Static Analysis
Behaviors and code characteristics that prevent static analysis or make it more difficult. Simple static analysis identifies features such as embedded strings, header information, hash values, and file metadata (e.g., creation date). More involved static analysis involves the disassembly of the binary code.

Two primary resources for anti-static analysis behaviors are [[1]](#1) and [[2]](#2).

* **Call Graph Generation Evasion** [B0010](../anti-static-analysis/evade-call-graph.md)
* **Disassembler Evasion** [B0012](../anti-static-analysis/evade-disassembler.md)
* **Data Flow Analysis Evasion** [B0045](../anti-static-analysis/evade-data-flow-analysis.md)
* **Executable Code Obfuscation** [B0032](../anti-static-analysis/exe-code-obfuscate.md)
* **Executable Code Optimization** [B0034](../anti-static-analysis/exe-code-optimize.md)
* **Executable Code Virtualization** [B0008](../anti-static-analysis/exe-code-virtualize.md)
* **Obfuscated Files or Information** [E1027](../defense-evasion/obfuscate-files.md)
* **Software Packing** [F0001](../anti-static-analysis/software-packing.md)

References
----------
<a name="1">[1]</a> Unprotect Project, a database about malware self-defense and protection. https://search.unprotect.it/map/sandbox-evasion/

<a name="2">[2]</a> InDepthUnpacking, course content for teaching malware anti-analysis techniques and mitigations, with emphasis on packers. https://github.com/knowmalware/InDepthUnpacking
