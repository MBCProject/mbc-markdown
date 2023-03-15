<table>
<tr>
<td><b>ID</b></td>
<td><b>B0027</b></td>
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


# Alternative Installation Location

Malware may install itself in areas other than the hard drive. [[1]](#1)

## Methods
 
|Name|ID|Description|
|---|---|---|
|**Fileless Malware**|B0027.001|Stores itself in memory. This method is related to Unprotect technique U1205.|
|**Registry Install**|B0027.002|Stores itself in the Windows registry.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Kovter**](../xample-malware/kovter.md)|2016|B0027.002|Kovter stores malware files in the Registry instead of on the hard drive. [[1]](#1)|
|[**SYNful Knock**](../xample-malware/synful-knock.md)|2015|B0027.001|100 memory-resident modules can be installed. [[2]](#2)|


## References

<a name="1">[1]</a> https://www.bleepingcomputer.com/virus-removal/remove-kovter-trojan

<a name="2">[2]</a> https://www.mandiant.com/resources/synful-knock-acis

