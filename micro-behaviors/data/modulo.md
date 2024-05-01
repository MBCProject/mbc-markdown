<table>
<tr>
<td><b>ID</b></td>
<td><b>C0058</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../data">Data</a></b></td>
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
<td><b>17 January 2021</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>30 April 2024</b></td>
</tr>
</table>


# Modulo

Malware calculates a modulo value.

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[calculate modulo 256 via x86 assembly](https://github.com/mandiant/capa-rules/blob/master/lib/calculate-modulo-256-via-x86-assembly.yml)|Modulo (C0058)|--|

### C0058 Snippet
<details>
<summary> Data::Modulo </summary>
SHA256: 465d3aac3ca4daa9ad4de04fcb999f358396efd7abceed9701c9c28c23c126db
Location: 0x403135
<pre>
and     param_3, 0xff   ; Taking the bitwise AND of any number x with a number equivalent to (2^n - 1) where n is a whole number is congruent to taking x % 2^n.  In this case, x = param_3 and 0xff = 255 which satisfies (2^n - 1) for n = 8.
</pre>
</details>
