|||
|---------|------------------------|
|**ID**|**E1027**|
|**Objective(s)**| [Anti-Static Analysis](https://github.com/MBCProject/mbc-markdown/tree/master/anti-static-analysis), [Defense Evasion](https://github.com/MBCProject/mbc-markdown/tree/master/defense-evasion)|
|**Related ATT&CK Technique(s)**|[Obfuscated Files or Information](https://attack.mitre.org/techniques/T1027)|


Obfuscated Files or Information
===============================
Malware may make files or information difficult to discover or analyze by encoding, encrypting, or otherwise obfuscating the content. In addition, a malware sample itself can be encoded or encrypted (i.e., encoding/encryption is a code characteristic).

A related MBC behavior, associated explicitly with executable code and making its analysis more difficult, is [Executable Code Obfuscation](https://github.com/MBCProject/mbc-markdown/tree/master/anti-static-analysis/exe-code-obfuscate.md).

See ATT&CK: [**Obfuscated Files or Information**](https://attack.mitre.org/techniques/T1027/).

Methods
-------
* **Encoding**:
   * *Standard Encoding*: A standard algorithm, such as base64 encoding, is used to encode the malware sample, a file, or other information.
   * *Custom Encoding*: A custom algorithm is used to encode the malware sample, a file, or other information.
* **Encryption**: 
   * *Standard Encryption*: A standard algorithm, such as Rijndael/AES, DES, RC4, is used to encrypt an executable file. Encryption hinders static analysis of malware code. Also known as **Code Encryption in File**.
   * *Standard Encryption of Code*: A standard encryption algorithm is used to encrypt a file's executable code, but not necessarily the file's data. 
   * *Standard Encryption of Data*: A standard encryption algorithm is used to encrypt a file's data, but not necessarily the file's code. 
   * *Custom Encryption*: A custom algorithm is used to encrypt an executable file. Encryption hinders static analysis of malware code. Also known as **Code Encryption in File**.
   * *Custom Encryption of Code*: A custom encryption algorithm is used to encrypt a file's executable code, but not necessarily the file's data.
   * *Custom Encryption of Data*: A custom encryption algorithm is used to encrypt a file's data, but not necessarily the file's code.


Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|-----------|-----------------------------|
|[**TrickBot**](https://github.com/MBCProject/mbc-markdown/tree/master/xample-malware/trickbot.md)|2016|Trojan spyware program that has mainly been used for targeting banking sites.|
