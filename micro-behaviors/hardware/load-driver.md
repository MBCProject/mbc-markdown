<table>
<tr>
<td><b>ID</b></td>
<td><b>C0023</b></td>
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
<td><b>2.1</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>14 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>5 December 2023</b></td>
</tr>
</table>


# Load Driver

Malware loads a device driver or minifilter.

## Methods

|Name|ID|Description|
|---|---|---|
|**Minifilter**|C0023.001|Malware starts a minifilter.|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[start minifilter driver](https://github.com/mandiant/capa-rules/blob/master/host-interaction/filter/start-minifilter-driver.yml)|Load Driver::Minifilter (C0023.001)|FltStartFiltering|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[driver_load](https://github.com/CAPESandbox/community/tree/master/modules/signatures/driver_load.py)|Load Driver (C0023)|NtLoadDriver|
