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
|[**CryptoWall**](../xample-malware/cryptowall.md)|2014|--| [[1]](#1)|
|[**CryptoLocker**](../xample-malware/cryptolocker.md)|2013|--|The malware searches for user files before encrypting them [[2]](#2)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|--|Collects local files with specified file extensions and information from the victim's machine [[3]](#3)|

## References

<a name="1">[1]</a> https://news.sophos.com/en-us/2015/12/17/the-current-state-of-ransomware-cryptowall/

<a name="2">[2]</a> https://www.secureworks.com/research/cryptolocker-ransomware

<a name="3">[3]</a> https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf
