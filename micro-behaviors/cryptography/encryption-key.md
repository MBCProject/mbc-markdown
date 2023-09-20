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
<td><b>13 September 2023</b></td>
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
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|--|BlackEnergy creates new key via CryptAcquireContext. [[1]](#1)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|Kovter creates a new key via CryptAcquireContext. [[1]](#1)|
|[**Locky Bart**](../xample-malware/locky-bart.md)|2017|--|Locky Bart creates a new key via CryptAcquireContext. [[1]](#1)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|C0028.002|Rombertik encrypts data using RC4 KSA. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[import public key](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/encryption/import-public-key.yml)|Encryption Key::Import Public Key (C0028.001)|advapi32.CryptAcquireContext, crypt32.CryptImportPublicKeyInfo, crypt32.CryptStringToBinary, crypt32.CryptDecodeObjectEx|
|[create new key via CryptAcquireContext](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/encryption/create-new-key-via-cryptacquirecontext.yml)|Encryption Key (C0028)|advapi32.CryptAcquireContext|
|[encrypt data using RC4 KSA](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/encryption/rc4/encrypt-data-using-rc4-ksa.yml)|Encryption Key::RC4 KSA (C0028.002)| |
|[reference public RSA key](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/encryption/rsa/reference-public-rsa-key.yml)|Encryption Key (C0028)| |

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

