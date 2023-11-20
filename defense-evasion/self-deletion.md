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
<td><b>Indicator Removal on Host: Uninstall Malicious Application (<a href="https://attack.mitre.org/techniques/T1630/001/">T1630.001</a>), Indicator Removal on Host: File Deletion (<a href="https://attack.mitre.org/techniques/T1070/004/">T1070.004</a>)</b></td>
<tr>
<td><b>Version</b></td>
<td><b>2.1</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>14 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>13 September 2023</b></td>
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
|[**Terminator**](../xample-malware/terminator.md)|2013|F0007.001|The RAT evades sandboxes by terminating and removing itself (DW20.exe) after installation. [[1]](#1)|
|[**CozyCar**](../xample-malware/cozycar.md)|2010|--|CozyCar has a dll file that serves as a cleanup mechanism for its dropped binary. [[2]](#2)|
|[**SearchAwesome**](../xample-malware/searchawesome.md)|2018|--|The malware will monitor if a specific file gets deleted and then will delete itself. [[3]](#3)|
|[**WannaCry**](../xample-malware/wannacry.md)|2017|--|WannaCry looks for a DNS entry and if the entry exists, it terminates and deletes itself. [[4]](#4)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[self delete](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-forensic/self-deletion/self-delete.yml)|Self Deletion::COMSPEC Environment Variable (F0007.001)| |

## References

<a name="1">[1]</a> https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2013/FireEye-Terminator_RAT.pdf

<a name="2">[2]</a> https://unit42.paloaltonetworks.com/tracking-minidionis-cozycars-new-ride-is-related-to-seaduke

<a name="3">[3]</a> https://www.malwarebytes.com/blog/news/2018/10/mac-malware-intercepts-encrypted-web-traffic-for-ad-injection

<a name="4">[4]</a> https://www.mandiant.com/resources/blog/wannacry-malware-profile