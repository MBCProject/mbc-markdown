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
<td><b>31 October 2022</b></td>
</tr>
</table>


# System Services

Malware may abuse system services or daemons to execute. 

See ATT&CK: **System Services ([T1569](https://attack.mitre.org/techniques/T1569/))**.

## Methods

|Name|ID|Description|
|---|---|---|
|**MSDTC**|E1569.m01|The Distributed Transaction Coordinator (MSDTC) coordinates transaction across multiple resource managers (databases, message queues and file systems). This legitimate Microsoft service is part of Windows 2000 and later and can be used to import and load DLLs. Malware may abuse MSDTC to import and load DLLs.[[1]](#1)|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Earth Lusca**](../xample-malware/)|2019|B0044.001|This malware uses scheduled tasks for exeuction. [[2]](#2)|

## References

<a name="1">[1]</a> https://support.resolver.com/hc/en-ca/articles/207161116-Configure-Microsoft-Distributed-Transaction-Coordinator-MSDTC-
<a name="2">[2]</a> https://attack.mitre.org/groups/G1006/