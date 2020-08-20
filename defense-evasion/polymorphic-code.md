|||
|---|---|
|**ID**|**B0029**|
|**Objective(s)**|[Defense Evasion](https://github.com/MBCProject/mbc-markdown/tree/master/defense-evasion)|
|**Related ATT&CK Technique**|None|


Polymorphic Code
================
Polymorphic code, a file with the same functionality but different execution, is created, often on the fly, making it difficult to detect. This behavior includes metamorphic code where the code is changed (not just executed differently), but with the behavior the same. Polymorphic Code behavior is typically identified through analysis of related samples.

Methods
-------
|ID|Name|Description|
|---|---|---|
|B0029.001|**Packer Stub**|A packer stub can generate polymorphic code.|
|B0029.002|**Call Indirections**|[[1]](#1)|
|B0029.003|**Code Reordering**|[[1]](#1)|

References
----------
<a name="1">[1]</a> https://www.mccormick.northwestern.edu/eecs/documents/tech-reports/2010-2014/evaluating-android-anti-malware-against-transformation-attacks.pdf
