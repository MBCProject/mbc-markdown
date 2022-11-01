<table>
<tr>
<td><b>ID</b></td>
<td><b>B0034</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../anti-static-analysis">Anti-Static Analysis</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>31 October 2022</b></td>
</tr>
</table>


Executable Code Optimization
============================
Code is optimized, making it harder to statically analyze.

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Jump/Call Absolute Address**|B0034.001|Relative operands of jumps and calls into are made absolute (better compression). May confuse some basic block detection algorithms.|
|**Minification**|B0034.002|Minification is 'the process of removing all unnecessary characters from source code without changing its functionality.' [[1]](#1) A simple example is when all the unnecessary whitespace and comments are removed. Minification is distinguished from compression in that it neither adds to nor changes the code seen by the interpreter. Minification is often used for malware written in interpreted languages, such as JavaScript, PHP, or Python. Legitimate code that is transmitted many times a second, such as JavaScript on websites, often uses minification to simply reduce the number of bytes transmitted.|

References
----------
<a name="1">[1]</a> https://en.wikipedia.org/wiki/Minification_(programming)
