<table>
<tr>
<td><b>ID</b></td>
<td><b>C0014</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../communication">Communication</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
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
<td><b>5 December 2023</b></td>
</tr>
</table>


# ICMP Communication

This micro-behavior is related to ICMP communication. 

## Methods

|Name|ID|Description|
|---|---|---|
|**Echo Request**|C0014.002|Send ICMP echo request.|
|**Generate Traffic**|C0014.001|Generate ICMP traffic.|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[send ICMP echo request](https://github.com/mandiant/capa-rules/blob/master/communication/icmp/send-icmp-echo-request.yml)|ICMP Communication::Echo Request (C0014.002)|IcmpSendEcho, IcmpSendEcho2, IcmpSendEcho2Ex, Icmp6SendEcho2, IcmpCreateFile, Icmp6CreateFile, IcmpCloseHandle|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[suspicious_ping_use](https://github.com/CAPESandbox/community/tree/master/modules/signatures/suspicious_ping_use.py)|ICMP Communication (C0014)|--|
|[network_icmp](https://github.com/CAPESandbox/community/tree/master/modules/signatures/network_icmp.py)|ICMP Communication (C0014)|--|
