
<table>
<tr>
<td><b>ID</b></td>
<td><b>B0010</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../anti-static-analysis">Anti-Static Analysis</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
</table>


Call Graph Generation Evasion
=============================
Malware code evades accurate call graph generation during disassembly. Call graphs are used by malware similarity tools and algorithms ([[1]](#1), [[4]](#4)), as well as for malware detection [[2]](#2).

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Invoke NTDLL System Calls via Encoded Table**|B0010.002|Invokes ntdll.dll functions without using an export table; an encoded translation table on the stack is used instead. [[3]](#3)|
|**Two-layer Function Return**|B0010.001|Two layer jumping confuses tools plotting call graphs. [[3]](#3)|

References
----------
<a name="1">[1]</a> K. Blokhin, D. Mentis, J. Saxe, "Malware Similarity Identification Using Call Graph Based System Call Subsequence Features," 2013 IEEE 33rd International Conference on Distributed Computing Systems Workshops, July 2013. https://www.researchgate.net/publication/269326967_Malware_Similarity_Identification_Using_Call_Graph_Based_System_Call_Subsequence_Features

<a name="2">[2]</a> P. Deshpande, M. Stamp, "Metamorphic Malware Detection Using Function Call Graph Analysis," MIS Review Vol. 21, Nos. 1/2, September(2015)/March(2016). https://pdfs.semanticscholar.org/8db2/69106ea6e1f59e4dac0889665dd3336ee9b1.pdf

<a name="3">[3]</a> http://fumalwareanalysis.blogspot.com/2012/01/malware-analysis-tutorial-10-tricks-for.html

<a name="4">[4]</a> S. Shang, N. Zheng, J. Xu, M. Xu, H. Zhang, "Detecting Malware Variants via Function-call Graph Similarity," IEEE 2010 5th International Conference on Malicious and Unwanted Software, 2010. http://seclab.hdu.edu.cn/static/uploads/paper/10-05.pdf
