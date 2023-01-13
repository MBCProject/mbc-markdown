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
|[**CryptoWall**](../xample-malware/cryptowall.md)|2014|E1083|The malware searches for user files before encrypting them [[1]](#1)|
|[**CryptoLocker**](../xample-malware/cryptolocker.md)|2013|E1083|The malware searches for user files before encrypting them [[2]](#2)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|E1083|Collects local files with specified file extensions and information from the victim's machine [[3]](#3)|
|[**GravityRAT**](../xample-malware/gravity-rat.md)|2018|E1083|Enumerate files on windows (This capa rule had 3 matches) [[4]](#4)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|E1083, E1083.m01|Please see the Hupigon malware page for details. [[4]](#4)|
|[**Kovter**](../xample-malware/kovter.md)|2016|E1083.m01|Access the Windows event log (This capa rule had 2 matches) [[4]](#4)|
|[**SamSam**](../xample-malware/samsam.md)|2015|E1083|Enumerate files on windows (This capa rule had 1 match) [[4]](#4)|
|[**UP007 Malware Family**](../xample-malware/up007.md)|2016|E1083|Enumerate files on windows (This capa rule had 1 match) [[4]](#4)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|E1083|Get common file path (This capa rule had 3 matches) [[4]](#4)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|E1083|Get file version info (This capa rule had 1 match) [[4]](#4)|
|[**Gamut**](../xample-malware/gamut.md)|2014|E1083|Get common file path (This capa rule had 5 matches) [[4]](#4)|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|E1083|Check if file exists (This capa rule had 1 match) [[4]](#4)|
|[**Locky Bart**](../xample-malware/locky-bart.md)|2017|E1083|Get file size (This capa rule had 1 match) [[4]](#4)|
|[**Mebromi**](../xample-malware/mebromi.md)|2011|E1083|Get file size (This capa rule had 1 match) [[4]](#4)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|E1083|Get file size (This capa rule had 3 matches) [[4]](#4)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|E1083|Get file version info (This capa rule had 1 match) [[4]](#4)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|E1083|Get common file path (This capa rule had 1 match) [[4]](#4)|

## References

<a name="1">[1]</a> https://news.sophos.com/en-us/2015/12/17/the-current-state-of-ransomware-cryptowall/

<a name="2">[2]</a> https://www.secureworks.com/research/cryptolocker-ransomware

<a name="3">[3]</a> https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf

<a name="4">[4]</a> capa v4.0, analyzed at MITRE on 10/12/2022

