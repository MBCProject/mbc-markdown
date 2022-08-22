
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
</table>


System Services
===============
Malware may abuse system services or daemons to execute. 

See ATT&CK: **System Services ([T1569](https://attack.mitre.org/techniques/T1569/))**.

Methods
-------
|Name|ID|Description|
|---|---|---|
|**MSDTC**|E1569.m01|The Distributed Transaction Coordinator (MSDTC) coordinates transaction across multiple resource managers (databases, message queues and file systems). This legitimate Microsoft service is part of Windows 2000 and later and can be used to import and load DLLs. Malware may abuse MSDTC to import and load DLLs.[[1]](#1)|


References
----------
<a name="1">[1]</a> https://support.resolver.com/hc/en-ca/articles/207161116-Configure-Microsoft-Distributed-Transaction-Coordinator-MSDTC-