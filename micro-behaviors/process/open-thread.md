<table>
<tr>
<td><b>ID</b></td>
<td><b>C0066</b></td>
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
<td><b>13 September 2023</b></td>
</tr>
</table>


# Open Thread

Malware opens a thread. 

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[open thread](https://github.com/mandiant/capa-rules/blob/master/lib/open-thread.yml)|Open Thread (C0066)|kernel32.OpenThread, NtOpenThread, ZwOpenThread|
