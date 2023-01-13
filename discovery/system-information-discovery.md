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
<td><b>21 November 2022</b></td>
</tr>
</table>


# System Information Discovery

Malware may attempt to get detailed information about the system. 

See ATT&CK: **System Information Discovery ([T1082](https://attack.mitre.org/techniques/T1082/))**.

## Methods

|Name|ID|Description|
|---|---|---|
|**Generate Windows Exception**|E1082.m01|Malware may trigger an exception as a way of gathering system details.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|E1082|Trojan spyware program that has mainly been used for targeting banking sites. [[7]](#7)|
|[**WebCobra**](../xample-malware/webcobra.md)|2018|E1082|Learns about the system so it can drop compatible miner software. [[8]](#8)|
|[**Ursnif**](../xample-malware/ursnif.md)|2016|E1082|Uses windows command prompt commands to gather system info, task list, installed drivers, and installed programs  [[1]](#1)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|E1082|Uses Systeminfo to gather OS version, system configuration, BIOS, the motherboard, and processor [ [[2]](#2)|
|[**Emotet**](../xample-malware/emotet.md)|2018|E1082|Collects information related to OS, processes, and sometimes mail client information and sends it to c2 [[4]](#4)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|E1082|Gathers information (OS version, workgroup status, computer name, domain/workgroup name, file name of infected project file) about each computer in the net to spread itself  [[5]](#5)|
|[**CHOPSTICK**](../xample-malware/chopstick.md)|2015|E1082|CHOPSTICK collects information from the host including Windows version, CPU architecture, and UAC settings [[6]](#6)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|E1082|Can collect information about the compter, resources, and operating system version  [[3]](#3)|
|[**CryptoLocker**](../xample-malware/cryptolocker.md)|2013|E1082|Query environment variable (This capa rule had 1 match) [[9]](#9)|
|[**Gamut**](../xample-malware/gamut.md)|2014|E1082|Query environment variable (This capa rule had 1 match) [[9]](#9)|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|E1082|GoBotKR uses wmic, systeminfo and ver commands to collect information about the system and the installed software. [[10]](#10)query environment variable (This capa rule had 2 matches) [[9]](#9)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|E1082|Query environment variable (This capa rule had 1 match) [[9]](#9)|
|[**Kovter**](../xample-malware/kovter.md)|2016|E1082|Get disk information (This capa rule had 1 match) [[9]](#9)|
|[**Mebromi**](../xample-malware/mebromi.md)|2011|E1082|Check OS version (This capa rule had 1 match) [[9]](#9)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|E1082|Check OS version (This capa rule had 1 match) [[9]](#9)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|E1082|Get disk size (This capa rule had 1 match) [[9]](#9)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|E1082|Get hostname (This capa rule had 1 match) [[9]](#9)|
|[**UP007 Malware Family**](../xample-malware/up007.md)|2016|E1082|Query environment variable (This capa rule had 1 match) [[9]](#9)|

## References

<a name="1">[1]</a> https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/PE_URSNIF.A2?_ga=2.131425807.1462021705.1559742358-1202584019.1549394279

<a name="2">[2]</a> https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf

<a name="3">[3]</a> https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/

<a name="4">[4]</a> https://documents.trendmicro.com/assets/white_papers/ExploringEmotetsActivities_Final.pdf

<a name="5">[5]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en

<a name="6">[6]</a> https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf

<a name="7">[7]</a> https://www.trendmicro.com/en_us/research/18/k/trickbot-shows-off-new-trick-password-grabber-module.html

<a name="8">[8]</a> https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/

<a name="9">[9]</a> capa v4.0, analyzed at MITRE on 10/12/2022

<a name="10">[10]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

