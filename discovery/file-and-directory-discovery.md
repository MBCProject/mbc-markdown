<table>
<tr>
<td><b>ID</b></td>
<td><b>E1083</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../discovery">Discovery</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>File and Directory Discovery (<a href="https://attack.mitre.org/techniques/T1083/">T1083</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.1</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>2 August 2022</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>6 June 2022</b></td>
</tr>
</table>


# File and Directory Discovery

Malware may enumerate files and directories or may search for specific files or in specific locations.

## Methods

|Name|ID|Description|
|---|---|---|
|**Log File**|E1083.m01|Malware may look for system log files.|
|**Filter by Extension**|E1083.m02|Malware may filter by extension (common in ransomware).|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**CryptoWall**](../xample-malware/cryptowall.md)|2014|--|The malware searches for user files before encrypting them. [[1]](#1)|
|[**CryptoLocker**](../xample-malware/cryptolocker.md)|2013|--|The malware searches for user files before encrypting them. [[2]](#2)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|--|The malware collects machine information and local files with specified file extensions. [[3]](#3)|
|[**Matanbuchus**](../xample-malware/matanbuchus.md)|2021|--|Malware verifies that the folder from the first stage loader exists on the system. The malware also checks for the path for the Opera web browser. If it exists, the malware exits. [[4]](#4) [[5]](#5)|
|[**GravityRAT**](../xample-malware/gravity-rat.md)|2018|--|GravityRAT enumerates files on Windows. [[6]](#6)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Hupigon enumerates files recursively. [[6]](#6)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|E1083.m01|Hupigon accesses the Windows event log. [[6]](#6)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|Kovter gets file version info. [[6]](#6)|
|[**Kovter**](../xample-malware/kovter.md)|2016|E1083.m01|Kovter accesses the Windows event log. [[6]](#6)|
|[**SamSam**](../xample-malware/samsam.md)|2015|--|SamSam enumerates files on Windows. [[6]](#6)|
|[**UP007**](../xample-malware/up007.md)|2016|--|The malware enumerates files on Windows. [[6]](#6)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|--|The malware gets the common file path. [[6]](#6)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|--|The malware gets file version info. [[6]](#6)|
|[**Gamut**](../xample-malware/gamut.md)|2014|--|Gamut gets the common file path. [[6]](#6)|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|--|GoBotKR checks if a file exists. [[6]](#6)|
|[**Locky Bart**](../xample-malware/locky-bart.md)|2017|--|The malware gets a file size. [[6]](#6)|
|[**Mebromi**](../xample-malware/mebromi.md)|2011|--|Mebromi gets a file size. [[6]](#6)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|--|Redhip gets a file size. [[6]](#6)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|--|The malware gets the file version info. [[6]](#6)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|--|Shamoon gets a common file path. [[6]](#6)|
|[**ElectroRAT**](../xample-malware/electrorat.md)|2020|--|ElectroRat looks for wallets to steal cryptocurrency. [[7]](#7)|


## References

<a name="1">[1]</a> https://news.sophos.com/en-us/2015/12/17/the-current-state-of-ransomware-cryptowall/

<a name="2">[2]</a> https://www.secureworks.com/research/cryptolocker-ransomware

<a name="3">[3]</a> https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf

<a name="4">[4]</a> https://www.0ffset.net/reverse-engineering/matanbuchus-loader-analysis/

<a name="5">[5]</a> https://www.cyberark.com/resources/threat-research-blog/inside-matanbuchus-a-quirky-loader

<a name="6">[6]</a> capa v4.0, analyzed at MITRE on 10/12/2022

<a name="7">[7]</a> https://www.intezer.com/blog/research/operation-electrorat-attacker-creates-fake-companies-to-drain-your-crypto-wallets/