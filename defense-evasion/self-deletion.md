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
<td><b>21 November 2022</b></td>
</tr>
</table>

</tr>
</table>


# Self Deletion

Malware may uninstall itself to avoid detection. 

See ATT&CK: **Indicator Removal on Host: Uninstall Malicious Application ([T1630.001](https://attack.mitre.org/techniques/T1630/001/)), Indicator Removal on Host: File Deletion ([T1070.004](https://attack.mitre.org/techniques/T1070/004/))**.

## Methods

|Name|ID|Description|
|---|---|---|
|**COMSPEC Environment Variable**|F0007.001|Uninstalls self via COMSPEC environment variable.|


## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Terminator**](../xample-malware/terminator.md)|2013|--|Evades sandboxes by terminating and removing itself (DW20.exe) after installation. [[1]](#1)|
|[**CozyCar**](../xample-malware/cozycar.md)|2010|--|CozyCar has a dll file that serves as a cleanup mechanism for its dropped binary [[2]](#2)|
|[**SearchAwesome**](../xample-malware/searchawesome.md)|2018|--|The malware will monitor if a specific file gets deleted, and then will delete itself. [[3]](#3)|


## References

<a name="1">[1]</a> https://www.mandiant.com/resources/hot-knives-through-butter-evading-file-based-sandboxes

<a name="2">[2]</a> https://unit42.paloaltonetworks.com/tracking-minidionis-cozycars-new-ride-is-related-to-seaduke

<a name="3">[3]</a> https://blog.malwarebytes.com/threat-analysis/2018/10/mac-malware-intercepts-encrypted-web-traffic-for-ad-injection/