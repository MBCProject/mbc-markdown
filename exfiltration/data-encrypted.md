|||
|---------|------------------------|
|**ID**|**E1022**|
|**Objective(s)**| [Exfiltration](https://github.com/MBCProject/mbc-markdown/tree/master/exfiltration)|
|**Related ATT&CK Technique**|[Data Encrypted](https://attack.mitre.org/techniques/T1022/)|


Data Encrypted
==============
Malware may obfuscate data via encryption or encoding before exfiltration.

**See ATT&CK Technique:** [**Data Encrypted**](https://attack.mitre.org/techniques/T1022/).

Methods
-------
* **Encoding**:
   * *Standard Encoding*: A standard algorithm, such as base64 encoding, is used to encode the exfiltrated data.
   * *Custom Encoding*: A custom algorithm is used to encode the exfiltrated data.
* **Encryption**: 
   * *Standard Encryption*: A standard algorithm, such as Rijndael/AES, DES, RC4, is used to encrypt the exfiltrated data.
   * *Custom Encryption*: A custom algorithm is used to encrypt the exfiltrated data.