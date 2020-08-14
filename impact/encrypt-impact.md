|||
|---------|------------------------|
|**ID**|**E1486**|
|**Objective(s)**|[Impact](https://github.com/MBCProject/mbc-markdown/tree/master/impact)|
|**Related ATT&CK Techniques**|[Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486/), [Data Encrypted for Impact (Mobile)](https://attack.mitre.org/techniques/T1471/)|


Data Encrypted for Impact 
=========================
Malware may encrypt files stored on the system to prevent user access until a ransom is paid and/or to interrupt system availability. The encryption process usually iterates over all letter drives in the system (except for CD drives) and then recursively encrypts all files with specific suffixes.

See ATT&CK: [**Data Encrypted for Impact**](https://attack.mitre.org/techniques/T1486/) and [**Data Encrypted for Impact (Mobile)**](https://attack.mitre.org/techniques/T1471/). 

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|-----------|-----------------------------|
|[**CryptoWall**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/cryptowall.md)| 2014 | [[1]](#1)| 
|[**CryptoLocker**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/cryptolocker.md)| 2013| [[2]](#2)| 
|[**Locky Bart**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/locky-bart.md)|2017|Encrypts files for ransom without any connection to the Internet.|
|[**SamSam**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/samsam.md)|2015|Ransomware.|

References
----------
<a name="1">[1]</a> http://www.secureworks.com/cyber-threat-intelligence/threats/cryptowall-ransomware/

<a name="2">[2]</a> http://www.secureworks.com/cyber-threat-intelligence/threats/cryptolocker-ransomware/


 
