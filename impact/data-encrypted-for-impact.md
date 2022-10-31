<table>
<tr>
<td><b>ID</b></td>
<td><b>E1486</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../impact">Impact</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Data Encrypted for Impact (<a href="https://attack.mitre.org/techniques/T1486/">T1486</a>), Data Encrypted for Impact (Mobile) (<a href="https://attack.mitre.org/techniques/T1471/">T1471</a>) </b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>31 October 2022</b></td>
</tr>
</table>


Data Encrypted for Impact 
=========================
Malware may encrypt files stored on the system to prevent user access until a ransom is paid and/or to interrupt system availability. The encryption process usually iterates over all letter drives in the system (except for CD drives) and then recursively encrypts all files with specific suffixes.

See ATT&CK: **Data Encrypted for Impact ([T1486](https://attack.mitre.org/techniques/T1486/))** and **Data Encrypted for Impact (Mobile) ([T1471](https://attack.mitre.org/techniques/T1471/))**

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
