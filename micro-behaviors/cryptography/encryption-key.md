<table>
<tr>
<td><b>ID</b></td>
<td><b>C0028</b></td>
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
<td><b>13 October 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>31 October 2022</b></td>
</tr>
</table>


# Encryption Key

Malware may import, generate, or otherwise use an encryption key. 

## Methods

|Name|ID|Description|
|---|---|---|
|**Import Public Key**|C0028.001|Malware imports a public key.|
|**RC4 KSA**|C0028.002|Malware uses the RC4 Key Scheduling Algorithm (KSA).|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|--|Create new key via CryptAcquireContext (This capa rule had 1 match) [[1]](#1)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|Create new key via CryptAcquireContext (This capa rule had 1 match) [[1]](#1)|
|[**Locky Bart**](../xample-malware/locky-bart.md)|2017|--|Create new key via CryptAcquireContext (This capa rule had 1 match) [[1]](#1)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|C0028.002|Encrypt data using RC4 KSA (This capa rule had 1 match) [[1]](#1)|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

