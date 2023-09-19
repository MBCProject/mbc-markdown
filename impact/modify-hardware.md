<table>
<tr>
<td><b>ID</b></td>
<td><b>B0042</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../impact">Impact</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
<tr>
<td><b>Impact Type</b></td>
<td><b>Breach</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.1</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>4 December 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>13 September 2023</b></td>
</tr>
</table>


# Modify Hardware

Malware modifies hardware.

## Methods

|Name|ID|Description|
|---|---|---|
|**CDROM**|B0042.001|The CD-ROM is modified.|
|**Mouse**|B0042.002|The mouse is modified.|
|**Printer**|B0042.003|The printer is modified.|

## Use in Malware

Name|Date|Method|Description|
|---|---|---|---|
|[**BadUSB**](../xample-malware/badusb.md)|2014|--| BadUSB can modify USB drives. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[swap mouse buttons](https://github.com/mandiant/capa-rules/blob/master/host-interaction/hardware/mouse/swap-mouse-buttons.yml)|Modify Hardware::Mouse (B0042.002)|user32.SwapMouseButton|
|[manipulate CD-ROM drive](https://github.com/mandiant/capa-rules/blob/master/host-interaction/hardware/cdrom/manipulate-cd-rom-drive.yml)|Modify Hardware::CDROM (B0042.001)|winmm.mciSendString|

## References

<a name="1">[1]</a> https://www.bleepingcomputer.com/news/security/fbi-hackers-use-badusb-to-target-defense-firms-with-ransomware/