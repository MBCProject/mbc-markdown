<table>
<tr>
<td><b>ID</b></td>
<td><b>B0033</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../impact">Impact</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Network Denial of Service (<a href="https://attack.mitre.org/techniques/T1498/">T1498</a>)</b></td>
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
<td><b>31 October 2022</b></td>
</tr>
</table>


Denial of Service
=================
Malware may make a network unavailable, for example, by launching a network-based denial of service (DoS) attack. 

Endpoint denial of service behaviors are captured by the **Endpoint Denial of Service ([T1499](https://attack.mitre.org/techniques/T1499/))** technique.

The related **Network Denial of Service ([T1498](https://attack.mitre.org/techniques/T1498/))** ATT&CK technique was defined subsequent to this MBC behavior.

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|October 2007|Launches distributed denial of service attacks that can target more than one IP address per hostname. [[1]](#1)|
|[**GotBotKR**](../xample-malware/gobotkr.md)|2019|GoBotKR has been used to execute endpoint DDoS attacks – for example, TCP Flood or SYN Flood. [[2]](#2)|

References
----------
<a name="1">[1]</a> http://atlas-public.ec2.arbor.net/docs/BlackEnergy+DDoS+Bot+Analysis.pdf
 
<a name="2">[2]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/
