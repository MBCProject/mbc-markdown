<table>
<tr>
<td><b>ID</b></td>
<td><b>C0017</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../process">Process</a></b></td>
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
<td><b>4 December 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>21 November 2022</b></td>
</tr>
</table>


# Create Process

Malware creates a process. 

## Methods

|Name|ID|Description|
|---|---|---|
|**Create Process via Shellcode**|C0017.001|Malware uses shellcode to create a process.|
|**Create Process via WMI**|C0017.002|Malware uses WMI to create a process.|
|**Create Suspended Process**|C0017.003|Malware created a suspended process.|


## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|C0017.002|Stuxnet will use WMI operations with the explorer.exe token in order to copy itself and execute on the remote share. [[1]](#1)|


## References

<a name="1">[1]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en
