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
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>7 October 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>31 October 2022</b></td>
</tr>
</table>


# Self Discovery

Malware may gather information about itself, such as its filename or size on disk.

## Methods

|Name|ID|Description|
|---|---|---|
|**Use hashquine to determine intregity**|B0038.001| Creates a hash of a file and embedds it into the malware so that integrity can be checked. [[1]](#1)|
|**Use magic string or number to determine intregity**|B0038.002| Checks for static values in malware to ensure integrity. [[2]](#2)|
|**Use lengh of section to determine intregity**|B0038.003| Checks for lenght to ensure a scection is correct. [[2]](#2)|

## Use in Malware

Name|Date|Method|Description|
|---|---|---|---|
|[**WannaCry**](../xample-malware/wannacry.md)|2023|B0023.002|The malware checks a string, keylen and a magic number before decrypting a dll. [[2]](#2)|
|[**WannaCry**](../xample-malware/wannacry.md)|2023|B0023.003|The malware checks the data lengh of a section before decypting a dll. [[2]](#2)|
## References

<a name="1">[1]</a> Method of creating a file that shows its own hash, https://github.com/Rogdham/gif-md5-hashquine
<a name="2">[2]</a> WannCry uses methods to check integreity before decyrpting an DLL, https://www.mandiant.com/resources/blog/wannacry-malware-profile
