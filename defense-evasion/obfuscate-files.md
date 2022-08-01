|||
|---|---|
|**ID**|**E1027**|
|**Objective(s)**|[Anti-Static Analysis](../anti-static-analysis), [Defense Evasion](../defense-evasion)|
|**Related ATT&CK Technique**|Obfuscated Files or Information ([T1027](https://attack.mitre.org/techniques/T1027/)), Obfuscated Files or Information: Steganography ([T1406.001](https://attack.mitre.org/techniques/T1406/001/))|


Obfuscated Files or Information
===============================
Malware may make files or information difficult to discover or analyze by encoding, encrypting, or otherwise obfuscating the content. In addition, a malware sample itself can be encoded or encrypted (i.e., encoding/encryption is a code characteristic).

A related MBC behavior (code characteristic), associated explicitly with executable code and making its analysis more difficult, is [Executable Code Obfuscation](../anti-static-analysis/exe-code-obfuscate.md).

Another related MBC behavior (code characteristic), is [Software Packing](../anti-static-analysis/software-packing.md) which has methods capturing specific packers and types of compression.

See ATT&CK: **Obfuscated Files or Information ([T1027](https://attack.mitre.org/techniques/T1027/)), Obfuscated Files or Information: Steganography ([T1406.001](https://attack.mitre.org/techniques/T1406/001/))**.

Instead of being listed alphabetically, methods have been grouped to better faciliate labeling and mapping.

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Encoding**|E1027.m01|A malware sample, file, or other information is encoded.|
|**Encoding-Custom Algorithm**|E1027.m03|A custom algorithm is used to encode a malware sample, file or other information.|
|**Encoding-Standard Algorithm**|E1027.m02|A standard algorithm (e.g., base64) is used to encode a malware sample, file, or other information.|
|**Encryption**|E1027.m04|A malware sample, file, or other information is encrypted.|
|**Encryption-Custom Algorithm**|E1027.m08|A custom algorithm is used to encrypt a malware sample, file, or other information.|
|**Encryption-Standard Algorithm**|E1027.m05|A standard algorithm (e.g., Rijndael/AES, DES, RC4) is used to encrypt a malware sample, file, or other information.|
|**Encryption of Code**|E1027.m06|A file's executable code is encrypted, but not necessarily the file's data.|
|**Encryption of Data**|E1027.m07|A file's data is encrypted, but not necessarily the file's code.|


Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|Trojan spyware program that has mainly been used for targeting banking sites.|
|[**Poison Ivy**](../xample-malware/poison-ivy.md)|2005|Obfuscates files.|
|[**WebCobra**](../xample-malware/webcobra.md)|2018|Obfuscates files.|
