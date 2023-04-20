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
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>4 December 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>31 October 2022</b></td>
</tr>
</table>


# Modify Hardware

Malware modifies hardware. This mostly happens due to the modification of the firmware.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**SonicWall Malware**](../xample-malware/)|2023|--|This malware checks for a firmware update and appedns itself to the update for loading and persistance. [[1]](#1)|

## Methods

|Name|ID|Description|
|---|---|---|
|**CDROM**|B0042.001|The CD-ROM is modified.|
|**Mouse**|B0042.002|The mouse is modified.|
|**Printer**|B0042.003|The printer is modified.|
|**Firmware**|B0042.004|The firmware is modified.|


## References

<a name="1">[1]</a> https://www.mandiant.com/resources/blog/suspected-chinese-persist-sonicwall
