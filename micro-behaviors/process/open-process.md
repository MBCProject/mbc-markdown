<table>
<tr>
<td><b>ID</b></td>
<td><b>C0065</b></td>
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
<td><b>30 August 2021</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>13 September 2023</b></td>
</tr>
</table>


# Open Process

Malware opens a process. 

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[open process](https://github.com/mandiant/capa-rules/blob/master/lib/open-process.yml)|Open Process (C0065)|kernel32.OpenProcess, NtOpenProcess, ZwOpenProcess|
