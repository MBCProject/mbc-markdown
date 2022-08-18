
<table>
<tr>
<td><b>ID</b></td>
<td><b>E1560</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../exfiltration">Exfiltration</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b><a href="https://attack.mitre.org/techniques/T1560/">Archive Collected Data</a></b></td>
</tr>
</table>


Archive Collected Data
======================
Malware may obfuscate data via encryption or encoding before exfiltration.

**See ATT&CK Technique:** [**Archive Collected Data**](https://attack.mitre.org/techniques/T1560/).

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Encoding**|E1560.m01|Data is encoded.|
|**Encoding - Custom Encoding**|E1560.m04|Data is encoded. A custom algorithm is used to encode the exfiltrated data.|
|**Encoding - Standard Encoding**|E1560.m03|Data is encoded. A standard algorithm, such as base64 encoding, is used to encode the exfiltrated data.|
|**Encryption**|E1560.m02|Data is encrypted.|
|**Encryption - Custom Encryption**|E1560.m06|Data is encrypted. A custom algorithm is used to encrypt the exfiltrated data.|
|**Encryption - Standard Encryption**|E1560.m05|Data is encrypted. A standard algorithm, such as Rijndael/AES, DES, RC4, is used to encrypt the exfiltrated data.|


Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|Uses a custom crypter leveraging Microsoft's CryptoAPI to encrypt C2 traffic. C2 update responses seem to have been digitally signed using bcrypt  [[1]](#1)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|Exfiltrated payloads are XORed with a static 31-byte long byte string found inside Stuxnet and hexified in order to be passed on as an ASCII data parameter in an HTTP request to the C2 servers  [[2]](#2)|


References
----------
<a name="1">[1]</a> https://www.bitdefender.com/blog/labs/trickbot-is-dead-long-live-trickbot/

<a name="2">[2]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en
