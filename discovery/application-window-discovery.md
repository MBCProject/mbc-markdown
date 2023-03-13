<table>
<tr>
<td><b>ID</b></td>
<td><b>E1010</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../discovery">Discovery</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Application Window Discovery (<a href="https://attack.mitre.org/techniques/T1010/">T1010</a>)</b></td>
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


# Application Window Discovery

Malware may attempt to get a listing of open application windows.

## Methods

|Name|ID|Description|
|---|---|---|
|**Window Text**|E1010.m01|After finding an open application window, malware gets graphical window text.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|E1010.m01|Get graphical window text (This capa rule had 2 matches) [[1]](#1)|
|[**Gamut**](../xample-malware/gamut.md)|2014|E1010.m01|Get graphical window text (This capa rule had 1 match) [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|E1010.m01|Get graphical window text (This capa rule had 1 match) [[1]](#1)|
|[**Kovter**](../xample-malware/kovter.md)|2016|E1010.m01|Get graphical window text (This capa rule had 2 matches) [[1]](#1)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|E1010.m01|Get graphical window text (This capa rule had 2 matches) [[1]](#1)|
|[**UP007 Malware Family**](../xample-malware/up007.md)|2016|E1010.m01|Get graphical window text (This capa rule had 1 match) [[1]](#1)|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

