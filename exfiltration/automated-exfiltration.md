<table>
<tr>
<td><b>ID</b></td>
<td><b>E1020</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../exfiltration">Exfiltration</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Automated Exfiltration (<a href="https://attack.mitre.org/techniques/T1020/">T1020</a>)</b></td>
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
<td><b>4 June 2023</b></td>
</tr>
</table>


# Automated Exfiltration

Malware may exfiltrate data via automated processing or scripting.

See ATT&CK Technique: **Automated Exfiltration ([T1020](https://attack.mitre.org/techniques/T1020/))**.

## Methods

|Name|ID|Description|
|---|---|---|
|**Exfiltrate via File Hosting Service**|E1020.m01|Malware may exfiltrate files to a file hosting location.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Attor**](../xample-malware/attor.md)|2013|--|Attor has a file uploader plugin that automatically exfiltrates collected data and log files to a C2 server.[[1]](#1)|


## References

<a name="1">[1]</a> https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf