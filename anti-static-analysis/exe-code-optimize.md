|||
|---|---|
|**ID**|**B0034**|
|**Objective(s)**|[Anti-Static Analysis](https://github.com/MBCProject/mbc-markdown/tree/master/anti-static-analysis)|
|**Related ATT&CK Technique**|None|


Executable Code Optimization
============================
Code is optimized, making it harder to statically analyze.

Methods
-------
|ID|Name|Description|
|---|---|---|
|B0034.001|**Jump/Call Absolute Address**|Relative operands of jumps and calls into are made absolute (better compression). May confuse some basic block detection algorithms.|
|B0034.002|**Minification**|Minification is 'the process of removing all unnecessary characters from source code without changing its functionality.' [[1]](#1) A simple example is when all the unnecessary whitespace and comments are removed. Minification is distinguished from compression in that it neither adds to nor changes the code seen by the interpreter. Minification is often used for malware written in interpreted languages, such as JavaScript, PHP, or Python. Legitimate code that is transmitted many times a second, such as JavaScript on websites, often uses minification to simply reduce the number of bytes transmitted.|

References
----------
<a name="1">[1]</a> https://en.wikipedia.org/wiki/Minification_(programming)
