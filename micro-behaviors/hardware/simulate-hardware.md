<table>
<tr>
<td><b>ID</b></td>
<td><b>C0057</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../hardware">Hardware</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>17 January 2021</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>13 September 2023</b></td>
</tr>
</table>


# Simulate Hardware

Malware simulates hardware.

## Methods

|Name|ID|Description|
|---|---|---|
|**Ctrl-Alt-Del**|C0057.001|Malware simulates Ctrl-Alt-Del.|
|**Mouse Click**|C0057.002|Malware simulates mouse click.|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[simulate CTRL ALT DEL](https://github.com/mandiant/capa-rules/blob/master/host-interaction/hardware/keyboard/simulate-ctrl-alt-del.yml)|Simulate Hardware::Ctrl-Alt-Del (C0057.001)|OpenDesktop, OpenInputDesktop, PostMessage|
