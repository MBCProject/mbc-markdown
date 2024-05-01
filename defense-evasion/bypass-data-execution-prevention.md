<table>
<tr>
<td><b>ID</b></td>
<td><b>B0037</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../defense-evasion">Defense Evasion</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.2</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>14 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>28 April 2024</b></td>
</tr>
</table>


# Bypass Data Execution Prevention

Malware may bypass Data Execution Prevention (DEP).

## Methods

|Name|ID|Description|
|---|---|---|
|**ROP Chains**|B0037.001|Return-Oriented Programming can be used to bypass DEP. It can also be used to bypass code signing. [[1]](#1)|

## Detection

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[dep_bypass](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/dep_bypass.py)|Bypass Data Execution Prevention (B0037)|VirtualProtectEx, NtProtectVirtualMemory|

## References

<a name="1">[1]</a> https://medium.com/cybersecurityservices/dep-bypass-using-rop-chains-garima-chopra-e8b3361e50ce