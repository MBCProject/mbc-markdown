<table>
<tr>
<td><b>ID</b></td>
<td><b>B0016</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../impact">Impact</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Data Manipulation: Stored Data Manipulation (<a href="https://attack.mitre.org/techniques/T1565/001/">T1565.001</a>)</b></td>
</tr>
<tr>
<td><b>Impact Type</b></td>
<td><b>Integrity</b></td>
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
<td><b>3 June 2023</b></td>
</tr>
</table>


# Compromise Data Integrity

Data stored on the file system of a compromised system is manipulated to compromise its integrity. Manipulative actions in this context include unauthorized insertion, deletion, or modification of data [[1]](#1). 

The related **Data Manipulation: Stored Data Manipulation ([T1565.001](https://attack.mitre.org/techniques/T1565/001/))** ATT&CK sub-technique was defined subsequent to this MBC behavior.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**DYEPACK**](../xample-malware/dyepack.md)|2015|--|DYEPACK alters records in databases used for SWIFT transactions. [[2]](#2)|


## References

<a name="1">[1]</a> "TRISIS Malware: Analysis of Safety System Targeted Malware, version 1.20171213," Dragos, 13 Dec. 2017. [Online]. Available: https://www.dragos.com/wp-content/uploads/TRISIS-01.pdf.

<a name="2">[2]</a> https://content.fireeye.com/apt/rpt-apt38