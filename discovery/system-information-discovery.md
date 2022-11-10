<table>
<tr>
<td><b>ID</b></td>
<td><b>E1082</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../discovery">Discovery</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>System Information Discovery (<a href="https://attack.mitre.org/techniques/T1082">T1082</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>2 August 2022</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>31 October 2022</b></td>
</tr>
</table>


System Information Discovery
============================
Malware may attempt to get detailed information about the system. 

See ATT&CK: **System Information Discovery ([T1082](https://attack.mitre.org/techniques/T1082/))**.

## Methods

|Name|ID|Description|
|---|---|---|
|**Generate Windows Exception**|E1082.m01|Malware may trigger an exception as a way of gathering system details.|

## Use in Malware

|Name|Date|Description|
|---|---|---|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|Trojan spyware program that has mainly been used for targeting banking sites.|
|[**WebCobra**](../xample-malware/webcobra.md)|2018|Learns about the system so it can drop compatible miner software.|
|[**Ursnif**](../xample-malware/ursnif.md)|2016|Uses windows command prompt commands to gather system info, task list, installed drivers, and installed programs  [[1]](#1)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|uses Systeminfo to gather OS version, system configuration, BIOS, the motherboard, and processor [ [[2]](#2)|
|[**DarkComet**](../xample-malware/darkcomet.md)|2008|Can collect information about the compter, resources, and operating system version  [[3]](#3)|
|[**Emotet**](../xample-malware/emotet.md)|2018|Collects information related to OS, processes, and sometimes mail client information and sends it to c2 [[4]](#4)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|Gathers information (OS version, workgroup status, computer name, domain/workgroup name, file name of infected project file) about each computer in the net to spread itself  [[5]](#5)|

## References

<a name="1">[1]</a> https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/PE_URSNIF.A2?_ga=2.131425807.1462021705.1559742358-1202584019.1549394279

<a name="2">[2]</a> https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf

<a name="3">[3]</a> https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/

<a name="4">[4]</a> https://documents.trendmicro.com/assets/white_papers/ExploringEmotetsActivities_Final.pdf

<a name="5">[5]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en
