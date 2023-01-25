<table>
<tr>
<td><b>ID</b></td>
<td><b>B0036</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../anti-behavioral-analysis">Anti-Behavioral Analysis</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
<tr>
<td><b>Anti-Analysis Type</b></td>
<td><b>Evasion</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>18 November 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>28 October 2022</b></td>
</tr>
</table>


# Capture Evasion

Malware has characteristics enabling it to evade capture from the infected system.

## Methods

|Name|ID|Description|
|---|---|---|
|**Encrypted Payloads**|B0036.002|The decryption key is stored external to the executable or never touches the disk.|
|**Memory-only Payload**|B0036.001|Malware is never written to disk (e.g., RAT plugins received from the controller are never written to disk).|
|**Multiple Stages of Loaders**|B0036.003|Multiple stages of loaders are used with an encoded payload.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Vobfus**](../xample-malware/vobfus.md)|2016|B0036.002|Vobfus is downloaded in an encrypted form then decrypted. [[1]](#1)|
|[**TEARDROP**](../xample-malware/teardrop.md)|2018|B0036.001|TEARDROP loads its payload only into memory. [[2]](#2)|
|[**Matanbuchus**](../xample-malware/matanbuchus.md)|2021|B0036.003|Matanbuchus consists of 2 loaders. The malware downloads multiple payloads (as files and DLLs) that are stored in a memory buffer. [[3]](#3) [[4]](#4)|


## References

<a name="1">[1]</a> https://securitynews.sonicwall.com/xmlpost/revisiting-vobfus-worm-mar-8-2013/

<a name="2">[2]</a> https://www.cisa.gov/uscert/ncas/analysis-reports/ar21-039b

<a name="3">[3]</a> https://www.0ffset.net/reverse-engineering/matanbuchus-loader-analysis/

<a name="4">[4]</a> https://www.cyberark.com/resources/threat-research-blog/inside-matanbuchus-a-quirky-loader