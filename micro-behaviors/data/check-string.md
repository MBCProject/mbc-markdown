<table>
<tr>
<td><b>ID</b></td>
<td><b>C0019</b></td>
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
<td><b>2.0</b></td>
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


# Check String

Malware may check a string for some characteristics, such as being ASCII content, credit card number, or length.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Locky Bart**](../../xample-malware/locky-bart.md)|2017|--|Locky Bart references Base64 strings. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[reference Base64 string](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/encoding/base64/reference-base64-string.yml)|Check String (C0019)|--|
|[parse credit card information](https://github.com/mandiant/capa-rules/blob/master/collection/credit-card/parse-credit-card-information.yml)|Check String (C0019)|--|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022
