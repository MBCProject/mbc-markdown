|||
|---|---|
|**ID**|**C0008**|
|**Objective(s)**|[Memory](../memory)|
|**Related ATT&CK Technique**|None|


Change Memory Protection
========================
Malware may change memory protection. For example, read-write memory may be changed to read-execute. Changing memory protection may exploits (e.g., bypass Data Execution Prevention).

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Executable Heap**|C0008.002|The heap is made executable.|
|**Executable Stack**|C0008.001|The stack is made executable.|
