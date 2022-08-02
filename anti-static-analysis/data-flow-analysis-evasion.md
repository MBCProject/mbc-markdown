|||
|---|---|
|**ID**|**B0045**|
|**Objective(s)**|[Anti-Static Analysis](../anti-static-analysis)|
|**Related ATT&CK Technique**|None|


Data Flow Analysis Evasion
==========================
Malware code evades data flow analysis (also known as information flow analysis and taint-tracking).

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Control Dependence**|B0045.001|Data is propagated via an if-then-else clause instead of direct assignment.[[1]](#1)|
|**Implicit Flows**|B0045.002|Data is propagated via semantic relationships, for example one variable not changing its state could imply the state of another variable.[[1]](#1)|
|**Arbitrary Memory Corruption**|B0045.003|Data is propagated by corrupting memory, for example overwriting a region of stack space where a file pointer is held.[[1]](#1)|

References
----------
<a name="1">[1]</a> http://www.seclab.cs.sunysb.edu/seclab/pubs/antitaint.pdf
