<table>
<tr>
<td><b>ID</b></td>
<td><b>B0038</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../discovery">Discovery</a></b></td>
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
<td><b>7 October 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>17 August 2023</b></td>
</tr>
</table>


# Self Discovery

Malware may gather information about itself, such as its filename or size on disk. 

## Methods

|Name|ID|Description|
|---|---|---|
|**Use Hashquine**|B0038.001|Malware uses a hashquine (the file contains it's own hash) for use as an integrity check. [[1]](#1)|
|**Check Magic String**|B0038.002|Malware checks a static value (i.e., magic string or number) to verify integrity. [[2]](#2)|
|**Check Section Length**|B0038.003|Malware checks the length of a section to verify integrity. [[2]](#2)|

## Use in Malware

Name|Date|Method|Description|
|---|---|---|---|
|[**WannaCry**](../xample-malware/wannacry.md)|2017|--|WannaCry checks the size of the file it loads into memory. [[1]](#1)|
|[**WannaCry**](../xample-malware/wannacry.md)|2017|B0038.002|WannaCry checks a string, keylen and a magic number before decrypting a dll. [[2]](#2)|
|[**WannaCry**](../xample-malware/wannacry.md)|2017|B0038.003|WannaCry checks the data lengh of a section before decypting a dll. [[2]](#2)|


## References

<a name="1">[1]</a> https://github.com/Rogdham/gif-md5-hashquine

<a name="2">[2]</a> https://www.mandiant.com/resources/blog/wannacry-malware-profile