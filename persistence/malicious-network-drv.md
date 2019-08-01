|||
|---------|------------------------|
|**ID**|**M0026**|
|**Objective(s)**|[Lateral Movement](https://github.com/MAECProject/malware-behaviors/tree/master/lateral-movement), [Persistence](https://github.com/MAECProject/malware-behaviors/tree/master/persistence)|
|**Related ATT&CK Technique(s)**|None|

Malicious Network Driver
========================
Malicious network drivers can be installed on several machines on a network via an exploited server with high uptime. Once the drivers are installed on the host machines, they can re-infect the server if it is restarted (persistence), can infect other machines on the network (lateral movement), and can redirect traffic on the network. 

A malicious network driver can tunnel outside traffic into the network, allowing the attackers to access remote desktop sessions or to connect to servers inside the domain by using previously acquired credentials. Using the credentials, they can re-deploy the entire platform following a massive shutdown or power loss and as a result, the malware will persist on network-connected machines even after reboot: after the machine connects to the server, the malware repopulates itself on the server; this, in turn, (re)infects the remaining machines on the network.  

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|-----------|-----------------------------|
|Malicious NDISProxy drivers| June 2018| The LuckyMouse APT (aka APT27) spreads Trojans via malicious NDISProxy drivers. [[1]](#1)|

References
----------
<a name="1">[1]</a> https://www.zdnet.com/article/luckymouse-targets-govt-entities-through-malicious-ndisproxy-driver/