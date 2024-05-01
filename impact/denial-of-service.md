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
<td><b>Impact Type</b></td>
<td><b>Availability</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.2</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>30 April 2024</b></td>
</tr>
</table>


# Denial of Service

Malware may make a network unavailable, for example, by launching a network-based denial of service (DoS) attack. 

Endpoint denial of service behaviors are captured by the **Endpoint Denial of Service ([T1499](https://attack.mitre.org/techniques/T1499/))** technique.

The related **Network Denial of Service ([T1498](https://attack.mitre.org/techniques/T1498/))** ATT&CK technique was defined subsequent to this MBC behavior.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|--|BlackEnergy launches distributed denial of service attacks that can target more than one IP address per hostname. [[1]](#1)|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|--|GoBotKR has been used to execute endpoint DDoS attacks – for example, TCP Flood or SYN Flood. [[2]](#2)|

## Detection

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[cve_2016_7200](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/cve_2016_7200.py)|Denial of Service (B0033)|JsEval, COleScript_ParseScriptText, COleScript_Compile|
|[network_cnc_http](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/network_cnc_http.py)|Denial of Service (B0033)|--|
|[cve_2015_2419_js](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/cve_2015_2419.py)|Denial of Service (B0033)|JsEval, COleScript_ParseScriptText, COleScript_Compile|
|[cve_2016-0189](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/cve_2016-0189.py)|Denial of Service (B0033)|JsEval, COleScript_ParseScriptText, COleScript_Compile|

## References

<a name="1">[1]</a> https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf

<a name="2">[2]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

