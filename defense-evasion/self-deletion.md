<table>
<tr>
<td><b>ID</b></td>
<td><b>F0007</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../defense-evasion">Defense Evasion</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Indicator Removal on Host: Uninstall Malicious Application (<a href="https://attack.mitre.org/techniques/T1630/001/">T1630.001</a>), Indicator Removal on Host: File Deletion
(<a href="https://attack.mitre.org/techniques/T1070/004/">T1070.004</a>)</b></td>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>14 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>31 October 2022</b></td>
</tr>
</table>

</tr>
</table>


Self Deletion
=============
Malware may uninstall itself to avoid detection. 

See ATT&CK: **Indicator Removal on Host: Uninstall Malicious Application ([T1630.001](https://attack.mitre.org/techniques/T1630/001/)), Indicator Removal on Host: File Deletion ([T1070.004](https://attack.mitre.org/techniques/T1070/004/))**.

Methods
-------
|Name|ID|Description|
|---|---|---|
|**COMSPEC Environment Variable**|F0007.001|Uninstalls self via COMSPEC environment variable.|


Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**Terminator**](../xample-malware/terminator.md)|2013|Evades sandboxes by terminating and removing itself (DW20.exe) after installation. [[1]](#1)|


References
----------
<a name="1">[1]</a> https://www.mandiant.com/resources/hot-knives-through-butter-evading-file-based-sandboxes
