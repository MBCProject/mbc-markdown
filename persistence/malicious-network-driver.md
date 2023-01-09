<table>
<tr>
<td><b>ID</b></td>
<td><b>B0026</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../lateral-movement">Lateral Movement</a>, <a href="../persistence">Persistence</a></b></td>
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
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>21 November 2022</b></td>
</tr>
</table>


# Malicious Network Driver

Malicious network drivers can be installed on several machines on a network via an exploited server with high uptime. Once the drivers are installed on the host machines, they can re-infect the server if it is restarted (persistence), can infect other machines on the network (lateral movement), and can redirect traffic on the network. 

A malicious network driver can tunnel outside traffic into the network, allowing the attackers to access remote desktop sessions or to connect to servers inside the domain by using previously acquired credentials. Using the credentials, they can re-deploy the entire platform following a massive shutdown or power loss and as a result, the malware will persist on network-connected machines even after reboot: after the machine connects to the server, the malware repopulates itself on the server; this, in turn, (re)infects the remaining machines on the network.  

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|**Malicious NDISProxy drivers**|June 2018|--|The LuckyMouse APT (aka APT27) spreads Trojans via malicious NDISProxy drivers. [[1]](#1)|

## References

<a name="1">[1]</a> https://www.zdnet.com/article/luckymouse-targets-govt-entities-through-malicious-ndisproxy-driver/
