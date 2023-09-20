<table>
<tr>
<td><b>ID</b></td>
<td><b>C0056</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../file-system">File System</a></b></td>
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
<td><b>13 September 2023</b></td>
</tr>
</table>


# Read Virtual Disk

Malware reads a virtual disk. 

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[read virtual disk](https://github.com/mandiant/capa-rules/blob/master/host-interaction/file-system/read/read-virtual-disk.yml)|Read Virtual Disk (C0056)|OpenVirtualDisk, AttachVirtualDisk, GetVirtualDiskPhysicalPath|
