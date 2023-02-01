<table>
<tr>
<td><b>ID</b></td>
<td><b>B0029</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../defense-evasion">Defense Evasion</a></b></td>
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
<td><b>21 November 2022</b></td>
</tr>
</table>


# Polymorphic Code

Polymorphic code, a file with the same functionality but different execution, is created, often on the fly, making it difficult to detect. This behavior includes metamorphic code where the code is changed (not just executed differently), but with the behavior the same. Polymorphic Code behavior is typically identified through analysis of related samples.

## Methods

|Name|ID|Description|
|---|---|---|
|**Call Indirections**|B0029.002|[[1]](#1)|
|**Code Reordering**|B0029.003|[[1]](#1)|
|**Packer Stub**|B0029.001|A packer stub can generate polymorphic code.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**EvilBunny**](../xample-malware/evilbunny.md)|2011|--|EvilBunny utilizes Lua scripts to exhibit polymorphism [[2]](#2)|

## References

<a name="1">[1]</a> https://www.mccormick.northwestern.edu/eecs/documents/tech-reports/2010-2014/evaluating-android-anti-malware-against-transformation-attacks.pdf

<a name="2">[2]</a> https://web.archive.org/web/20150311013500/http://www.cyphort.com/evilbunny-malware-instrumented-lua/

