<table>
<tr>
<td><b>ID</b></td>
<td><b>E1569</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../execution">Execution</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>System Services (<a href="https://attack.mitre.org/techniques/T1569/">T1569</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>8 November 2021</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>12 June 2023</b></td>
</tr>
</table>


# System Services

Malware may manipulate, create, or interact with system services to achieve persistence, gain higher privileges, or execute malicious code. System services are background processes that are integral parts of an operating system's functionality. Malware can exploit these services by modifying their configurations, replacing legitimate service binaries with malicious ones, or creating new services that run malicious code. 

See ATT&CK: **System Services ([T1569](https://attack.mitre.org/techniques/T1569/))**.

## Methods

|Name|ID|Description|
|---|---|---|
|**MSDTC**|E1569.m01|The Distributed Transaction Coordinator (MSDTC) coordinates transaction across multiple resource managers (databases, message queues and file systems). This legitimate Microsoft service is part of Windows 2000 and later and can be used to import and load DLLs. Malware may abuse MSDTC to import and load DLLs.[[1]](#1)|

## References

<a name="1">[1]</a> https://cyware.com/news/catb-ransomware-exploits-msdtc-service-to-steal-data-3bb46fc0