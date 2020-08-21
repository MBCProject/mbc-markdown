|||
|---|---|
|**ID**|**E1560**|
|**Objective(s)**|[Exfiltration](https://github.com/MBCProject/mbc-markdown/tree/master/exfiltration)|
|**Related ATT&CK Technique**|[Archive Collected Data](https://attack.mitre.org/techniques/T1560/)|


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
