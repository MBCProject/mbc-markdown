|||
|--|-----|
|**ID**|**M9002**|

# Anti-Static Analysis
Behaviors and methods that prevent static analysis or make it more difficult. Simpler static analysis identifies features such as embedded strings, header information, hash values, and file metadata (e.g., creation date). More involved static analysis involves the disassembly of the binary code.

Two primary resources for anti-static analysis behaviors are [[1]](#1) and [[2]](#2).

* **Call Graph Generation Evasion** [M0010](https://github.com/MAECProject/malware-behaviors/blob/master/anti-static-analysis/evade-call-graph.md)
* **Disassembler Evasion** [M0012](https://github.com/MAECProject/malware-behaviors/blob/master/anti-static-analysis/evade-disassembler.md)
* **Executable Code Compression** [E1045](https://github.com/MAECProject/malware-behaviors/blob/master/anti-static-analysis/exe-code-compression.md)
* **Executable Code Obfuscation** [M0032](https://github.com/MAECProject/malware-behaviors/blob/master/anti-static-analysis/exe-code-obfuscate.md)
* **Executable Code Optimization** [M0034](https://github.com/MAECProject/malware-behaviors/blob/master/anti-static-analysis/exe-code-optimize.md)
* **Executable Code Virtualization** [M0008](https://github.com/MAECProject/malware-behaviors/blob/master/anti-static-analysis/exe-code-virtualize.md)


References
----------
<a name="1">[1]</a> Unprotect Project, a database about malware self-defense and protection. http://unprotect.tdgt.org/index.php/Unprotect_Project

<a name="2">[2]</a> InDepthUnpacking, course content for teaching malware anti-analysis techniques and mitigations, with emphasis on packers. https://github.com/knowmalware/InDepthUnpacking