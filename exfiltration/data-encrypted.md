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
|ID|Name|Description|
|---|---|---|
|E1560.m01|**Encoding**|Data is encoded.|
|E1560.m02|**Encryption**|Data is encrypted.|
|E1560.m03|**Standard Encoding**|A standard algorithm, such as base64 encoding, is used to encode the exfiltrated data.|
|E1560.m04|**Custom Encoding**|A custom algorithm is used to encode the exfiltrated data.|
|E1560.m05|**Standard Encryption**|A standard algorithm, such as Rijndael/AES, DES, RC4, is used to encrypt the exfiltrated data.|
|E1560.m06|**Custom Encryption**|A custom algorithm is used to encrypt the exfiltrated data.|
