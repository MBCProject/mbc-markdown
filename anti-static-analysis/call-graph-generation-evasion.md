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
<tr>
<td><b>Anti-Analysis Type</b></td>
<td><b>Evasion</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.1</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>31 August 2023</b></td>
</tr>
</table>


# Call Graph Generation Evasion

Malicious code evades accurate call graph generation, which can be used for malware detection during disassembly of the binary [[1]](#1). Evading accurate call graph generation can also hinder follow-on analysis. For instance, using randomization of call graphs, malware can defeat call graph-based similarity analysis in which analysts calculate similarity between pairs of malicious binaries [[2]](#2), [[3]](#3). Application of clustering algorithms to malware call graphs has also resulted in the discovery of malware families [[4]] (#4). 

## Methods

|Name|ID|Description|
|---|---|---|
|**Invoke NTDLL System Calls via Encoded Table**|B0010.002|Invokes ntdll.dll functions without using an export table; an encoded translation table on the stack is used instead. [[5]](#5)|
|**Two-layer Function Return**|B0010.001|Two layer jumping confuses tools plotting call graphs. [[5]](#5)|
|**Shadow Process Communication**|B0010.003| Uses multiple processes (instead of one process) to make behavior detection more difficult. [[6]](#6)|

## References

<a name="1">[1]</a> P. Deshpande and M. Stamp,"Metamorphic Malware Detection Using Function Call Graph Analysis," MIS Review, Vol. 21, Nos. 1/2, Sept.(2015)/Mar.(2016), [Online]. Available: https://pdfs.semanticscholar.org/8db2/69106ea6e1f59e4dac0889665dd3336ee9b1.pdf.

<a name="2">[2]</a> K. Blokhin, D. Mentis, and J. Saxe,"Malware Similarity Identification Using Call Graph Based System Call Subsequence Features," 2013 IEEE 33rd International Conference on Distributed Computing Systems Workshops, July 2013. [Online]. Available: https://www.researchgate.net/publication/269326967_Malware_Similarity_Identification_Using_Call_Graph_Based_System_Call_Subsequence_Features.

<a name="3">[3]</a> S. Shang, N. Zheng, J. Xu, M. Xu, and H. Zhang,"Detecting Malware Variants via Function-call Graph Similarity," IEEE 2010 5th International Conference on Malicious and Unwanted Software, 2010. [Online]. Available: https://seclab.hdu.edu.cn/static/uploads/paper/10-05.pdf.

<a name="4">[4]</a> J. Kinable, "Malware Detection Through Call Graphs," Master thesis, Department of Telematics, Norwegian University of Science and Technology, Norway, June 2010. [Online]. Available: https://ntnuopen.ntnu.no/ntnu-xmlui/bitstream/handle/11250/262290/353049_FULLTEXT01.pdf?sequence=1&isAllowed=y.

<a name="5">[5]</a> http://fumalwareanalysis.blogspot.com/2012/01/malware-analysis-tutorial-10-tricks-for.html

<a name="6">[6]</a> Weiqin Ma, Pu Duan, Sanmin Liu, Guofei Gu and Jyh-Charn Liu,"Shadow Attacks: Automatically Evading System-Call-Behavior Based Malware Detection" https://people.engr.tamu.edu/guofei/paper/ShadowAttacks_final-onecolumn.pdf