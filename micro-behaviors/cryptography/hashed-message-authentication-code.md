<table>
<tr>
<td><b>ID</b></td>
<td><b>C0061</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../cryptography">Cryptography</a></b></td>
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
<td><b>5 December 2023</b></td>
</tr>
</table>


# Hashed Message Authentication Code

Malware uses a hashed message authentication code (HMAC) schema.

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[authenticate HMAC](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/hmac/authenticate-hmac.yml)|Hashed Message Authentication Code (C0061)|--|
