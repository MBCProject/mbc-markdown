<table>
<tr>
<td><b>ID</b></td>
<td><b>C0021</b></td>
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
<td><b>14 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>1 MArch 2023</b></td>
</tr>
</table>


# Generate Pseudo-random Sequence

The Generate Pseudo-random Sequence micro-behavior can be used for a number of purposes. The methods below include specific functions, as well as pseudo-random number generators (PRNG).

## Methods

|Name|ID|Description|
|---|---|---|
|**GetTickCount**|C0021.001|Malware generates a pseudo-random sequence using GetTickCount.|
|**Use API**|C0021.003|Malware generates a pseudo-random sequence using a Windows API.|
|**rand**|C0021.002|Malware generates a pseudo-random sequence using rand.|
|**RC4 PRGA**|C0021.004|Malware generates a pseudo-random sequence using the RC4 Pseudo Random (Byte) Generation Algorithm (PRGA).|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|C0021.003|BlackEnergy generates random numbers via WinAPI. [[1]](#1)|
|[**Locky Bart**](../xample-malware/locky-bart.md)|2017|C0021.003|Generate random numbers via WinAPI (This capa rule had 1 match) [[1]](#1)|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

