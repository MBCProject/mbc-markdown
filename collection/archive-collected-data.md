<table>
<tr>
<td><b>ID</b></td>
<td><b>E1560</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../collection">Collection</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Archive Collected Data (<a href="https://attack.mitre.org/techniques/T1560/">T1560</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>4.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>27 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>18 December 2023</b></td>
</tr>
</table>


# Archive Collected Data

Malware may collect and package (or archive) the information they have gathered from a compromised system. Once collected, the data is often compressed and encrypted into an archive file using various tools or utilities. Common formats for archive files include .zip, .tar, .rar, or .7z. This helps the attack by reducing the size of the data, making it easier and quicker to exfiltrate, and helps avoid detection, since many security tools may not inspect the contents of compressed or encrypted files. 

See ATT&CK Technique: **Archive Collected Data ([T1560](https://attack.mitre.org/techniques/T1560/))**.

## Methods

|Name|ID|Description|
|---|---|---|
|**Encoding**|E1560.m01|Data is encoded.|
|**Encoding - Custom Encoding**|E1560.m04|Data is encoded. A custom algorithm is used to encode the exfiltrated data.|
|**Encoding - Standard Encoding**|E1560.m03|Data is encoded. A standard algorithm, such as base64 encoding, is used to encode the exfiltrated data.|
|**Encryption**|E1560.m02|Data is encrypted.|
|**Encryption - Custom Encryption**|E1560.m06|Data is encrypted. A custom algorithm is used to encrypt the exfiltrated data.|
|**Encryption - Standard Encryption**|E1560.m05|Data is encrypted. A standard algorithm, such as Rijndael/AES, DES, RC4, is used to encrypt the exfiltrated data.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|E1560.m02|The malware uses a custom crypter leveraging Microsoft's CryptoAPI to encrypt C2 traffic. C2 update responses seem to have been digitally signed using bcrypt. [[1]](#1)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|E1560.m04|Exfiltrated payloads are XORed with a static 31-byte long byte string found inside Stuxnet and hexified in order to be passed on as an ASCII data parameter in an HTTP request to the C2 servers. [[2]](#2)|
|[**Matanbuchus**](../xample-malware/matanbuchus.md)|2021|E1560.m03|Malware sends data as a Base64 string of JSON. [[3]](#3) [[4]](#4)|

## Detection

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[encrypt_data_agenttesla_http](https://github.com/CAPESandbox/community/tree/master/modules/signatures/encrypt_data_agenttesla_http.py)|Archive Collected Data (E1560)|CryptEncrypt|
|[encrypt_data_agenttesla_http](https://github.com/CAPESandbox/community/tree/master/modules/signatures/encrypt_data_agenttesla_http.py)|Archive Collected Data::Encryption (E1560.m02)|CryptEncrypt|
|[encrypt_data_agentteslat2_http](https://github.com/CAPESandbox/community/tree/master/modules/signatures/encrypt_data_agentteslat2_http.py)|Archive Collected Data (E1560)|CryptEncrypt, GetUserNameW, GetComputerNameW|
|[encrypt_data_agentteslat2_http](https://github.com/CAPESandbox/community/tree/master/modules/signatures/encrypt_data_agentteslat2_http.py)|Archive Collected Data::Encryption (E1560.m02)|CryptEncrypt, GetUserNameW, GetComputerNameW|
|[encrypt_data_nanocore](https://github.com/CAPESandbox/community/tree/master/modules/signatures/encrypt_data_nanocore.py)|Archive Collected Data (E1560)|CryptEncrypt, GetUserNameW, GetComputerNameW|
|[encrypt_data_nanocore](https://github.com/CAPESandbox/community/tree/master/modules/signatures/encrypt_data_nanocore.py)|Archive Collected Data::Encryption (E1560.m02)|CryptEncrypt, GetUserNameW, GetComputerNameW|

## References

<a name="1">[1]</a> https://www.bitdefender.com/blog/labs/trickbot-is-dead-long-live-trickbot/

<a name="2">[2]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en

<a name="3">[3]</a> https://www.0ffset.net/reverse-engineering/matanbuchus-loader-analysis/

<a name="4">[4]</a> https://www.cyberark.com/resources/threat-research-blog/inside-matanbuchus-a-quirky-loader
