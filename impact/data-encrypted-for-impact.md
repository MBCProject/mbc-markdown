|||
|---|---|
|**ID**|**E1486**|
|**Objective(s)**|[Impact](../impact)|
|**Related ATT&CK Techniques**|[Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486/), [Data Encrypted for Impact (Mobile)](https://attack.mitre.org/techniques/T1471/)|


Data Encrypted for Impact 
=========================
Malware may encrypt files stored on the system to prevent user access until a ransom is paid and/or to interrupt system availability. The encryption process usually iterates over all letter drives in the system (except for CD drives) and then recursively encrypts all files with specific suffixes.

See ATT&CK: [**Data Encrypted for Impact**](https://attack.mitre.org/techniques/T1486/) and [**Data Encrypted for Impact (Mobile)**](https://attack.mitre.org/techniques/T1471/). 

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Ransom Note**|E1486.001|Ransomware displays a ransom note. Ransom notes are sometimes used to link instances of ransomware, even when the code or anti-analysis techniques change.|

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**CryptoWall**](../xample-malware/cryptowall.md)|2014|[[1]](#1)|
|[**CryptoLocker**](../xample-malware/cryptolocker.md)|2013|[[2]](#2)|
|[**Locky Bart**](../xample-malware/locky-bart.md)|2017|Encrypts files for ransom without any connection to the Internet.|
|[**SamSam**](../xample-malware/samsam.md)|2015|Ransomware.|

References
----------
<a name="1">[1]</a> http://www.secureworks.com/cyber-threat-intelligence/threats/cryptowall-ransomware/

<a name="2">[2]</a> http://www.secureworks.com/cyber-threat-intelligence/threats/cryptolocker-ransomware/
