|||
|---|---|
|**ID**|**E1082**|
|**Objective(s)**|[Discovery](../discovery)|
|**Related ATT&CK Technique**|[System Information Discovery](https://attack.mitre.org/techniques/T1082)|


System Information Discovery
============================
Malware may attempt to get detailed information about the system. 

See ATT&CK: [**System Information Discovery**](https://attack.mitre.org/techniques/T1082).

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Generate Windows Exception**|E1082.m01|Malware may trigger an exception as a way of gathering system details.|

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|Trojan spyware program that has mainly been used for targeting banking sites.|
|[**WebCobra**](../xample-malware/webcobra.md)|2018|Learns about the system so it can drop compatible miner software.|
|[**Ursnif**](../discovery/system-info-discover.md)|2016|Uses windows command prompt commands to gather system info, task list, installed drivers, and installed programs  [[1]](#1)|
|[**BlackEnergy**](../discovery/system-info-discover.md)|2007|uses Systeminfo to gather OS version, system configuration, BIOS, the motherboard, and processor [ [[2]](#2)|

References
----------
<a name="1">[1]</a> https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/PE_URSNIF.A2?_ga=2.131425807.1462021705.1559742358-1202584019.1549394279

<a name="2">[2]</a> https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf
