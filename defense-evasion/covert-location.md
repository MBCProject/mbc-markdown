<table>
<tr>
<td><b>ID</b></td>
<td><b>B0040</b></td>
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
<td><b>10 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>31 October 2022</b></td>
</tr>
</table>


# Covert Location

Malware may hide data or binary files within other files, the registry, etc. 

Name|Date|Method|Description|
|---|---|---|---|
|[**Agent Tesla**](../xample-malware/)|2023|B0040.001|This malware can achieve persistence by modifying Registry key entries.[[1]](#1)|

## Methods

|Name|ID|Description|
|---|---|---|
|**Hide Data in Registry**|B0040.001|Malware may use a registry key to store a long sequence of bytes. ([T112](https://attack.mitre.org/techniques/T1112/)|
|**Steganography**|B0040.002|Malware may store information in an image. See related ATT&CK techniques: Data Obfuscation: Steganography [T1001.002](https://attack.mitre.org/techniques/T1001/002), Obfuscated Files or Information: Steganography ([T1027.003](https://attack.mitre.org/techniques/T1027/003), [T1406.001](https://attack.mitre.org/techniques/T1406/001)).|


<a name="1">[1]</a> https://www.sentinelone.com/labs/agent-tesla-old-rat-uses-new-tricks-to-stay-on-top/
