|||
|---|---|
|**ID**|**E1027**|
|**Objective(s)**|[Anti-Static Analysis](https://github.com/MBCProject/mbc-markdown/tree/master/anti-static-analysis), [Defense Evasion](https://github.com/MBCProject/mbc-markdown/tree/master/defense-evasion)|
|**Related ATT&CK Technique**|[Obfuscated Files or Information](https://attack.mitre.org/techniques/T1027)|


Obfuscated Files or Information
===============================
Malware may make files or information difficult to discover or analyze by encoding, encrypting, or otherwise obfuscating the content. In addition, a malware sample itself can be encoded or encrypted (i.e., encoding/encryption is a code characteristic).

A related MBC behavior, associated explicitly with executable code and making its analysis more difficult, is [Executable Code Obfuscation](https://github.com/MBCProject/mbc-markdown/tree/master/anti-static-analysis/exe-code-obfuscate.md).

See ATT&CK: [**Obfuscated Files or Information**](https://attack.mitre.org/techniques/T1027/).

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Encoding**|E1027.m01|The malware sample, file, or other information is encoded.|
|**Encoding - Custom Encoding**|E1027.m03|The malware sample, file, or other information is encoded. A custom algorithm is used to encode the malware sample, a file, or other information.|
|**Encoding - Standard Encoding**|E1027.m02|The malware sample, file, or other information is encoded. A standard algorithm, such as base64 encoding, is used to encode the malware sample, a file, or other information.|
|**Encryption**|E1027.m04|The malware sample, file, or other information is encrypted.|
|**Encryption - Custom Encryption**|E1027.m08|The malware sample, file, or other information is encrypted. A custom algorithm is used to encrypt an executable file. Encryption hinders static analysis of malware code. Also known as *Code Encryption in File*.|
|**Encryption - Custom Encryption of Code**|E1027.m09|The malware sample, file, or other information is encrypted. A custom encryption algorithm is used to encrypt a file's executable code, but not necessarily the file's data.|
|**Encryption - Custom Encryption of Data**|E1027.m10|The malware sample, file, or other information is encrypted. A custom encryption algorithm is used to encrypt a file's data, but not necessarily the file's code.|
|**Encryption - Standard Encryption**|E1027.m05|The malware sample, file, or other information is encrypted. A standard algorithm, such as Rijndael/AES, DES, RC4, is used to encrypt an executable file. Encryption hinders static analysis of malware code. Also known as *Code Encryption in File*.|
|**Encryption - Standard Encryption of Code**|E1027.m06|The malware sample, file, or other information is encrypted. A standard encryption algorithm is used to encrypt a file's executable code, but not necessarily the file's data.|
|**Encryption - Standard Encryption of Data**|E1027.m07|The malware sample, file, or other information is encrypted. A standard encryption algorithm is used to encrypt a file's data, but not necessarily the file's code.|

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**TrickBot**](https://github.com/MBCProject/mbc-markdown/tree/master/xample-malware/trickbot.md)|2016|Trojan spyware program that has mainly been used for targeting banking sites.|
|[**Poison Ivy**](https://github.com/MBCProject/mbc-markdown/tree/master/xample-malware/poison-ivy.md)|2005|Obfuscates files.|
|[**WebCobra**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/webcobra.md)|2018|Obfuscates files.|
