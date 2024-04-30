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
<td><b>Impact Type</b></td>
<td><b>Availability</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.3</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>30 April 2024</b></td>
</tr>
</table>


# Data Encrypted for Impact 

Malware may encrypt files stored on the system to prevent user access until a ransom is paid and/or to interrupt system availability. The encryption process usually iterates over all letter drives in the system (except for CD drives) and then recursively encrypts all files with specific suffixes.

See ATT&CK: **Data Encrypted for Impact ([T1486](https://attack.mitre.org/techniques/T1486/))** and **Data Encrypted for Impact (Mobile) ([T1471](https://attack.mitre.org/techniques/T1471/))**

## Methods

|Name|ID|Description|
|---|---|---|
|**Ransom Note**|E1486.001|Ransomware displays a ransom note. Ransom notes are sometimes used to link instances of ransomware, even when the code or anti-analysis techniques change.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**CryptoWall**](../xample-malware/cryptowall.md)|2014|E1486.001|The malware launches Internet Explorer to show ransom notes. [[1]](#1)|
|[**CryptoLocker**](../xample-malware/cryptolocker.md)|2013|E1486.001|The malware launches Internet Explorer to show ransom notes. [[2]](#2)|
|[**Locky Bart**](../xample-malware/locky-bart.md)|2017|--|Locky Bart encrypts files for ransom without any connection to the Internet. [[3]](#3)|
|[**SamSam**](../xample-malware/samsam.md)|2015|--|SamSam encrypts data to hold for ransom. [[4]](#4)|
|[**Netwalker**](../xample-malware/netwalker.md)|2020|--|Netwalker encrypts files for ransom. [[5]](#5)|
|[**WannaCry**](../xample-malware/wannacry.md)|2017|--|WannaCry encrypts files for ransom. [[6]](#6)|

## Detection

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[mass_data_encryption](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_crypto.py)|Data Encrypted for Impact  (E1486)|CryptEncrypt|
|[ransomware_dmalocker](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_dmalocker.py)|Data Encrypted for Impact  (E1486)|RegSetValueExA|
|[ransomware_revil_regkey](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_revil_regkey.py)|Data Encrypted for Impact  (E1486)|--|
|[ransomware_radamant](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_radamant.py)|Data Encrypted for Impact  (E1486)|--|
|[ransomware_extensions](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_fileextensions.py)|Data Encrypted for Impact  (E1486)|--|
|[sodinokibi_behavior](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_sodinokibi.py)|Data Encrypted for Impact  (E1486)|bind, RegSetValueExW, WinHttpOpen, NtCreateUserProcess, CreateProcessInternalW|
|[ransomware_message](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_message.py)|Data Encrypted for Impact  (E1486)|NtWriteFile|
|[ransomware_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_files.py)|Data Encrypted for Impact  (E1486)|--|
|[ransomware_file_modifications](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_filemodifications.py)|Data Encrypted for Impact  (E1486)|NtWriteFile, MoveFileWithProgressW, NtCreateFile, MoveFileWithProgressTransactedW|

## References

<a name="1">[1]</a> https://news.sophos.com/en-us/2015/12/17/the-current-state-of-ransomware-cryptowall/

<a name="2">[2]</a> https://www.secureworks.com/research/cryptolocker-ransomware

<a name="3">[3]</a> https://blog.malwarebytes.com/threat-analysis/2017/01/locky-bart-ransomware-and-backend-server-analysis/

<a name="4">[4]</a> https://www.cisa.gov/uscert/ncas/alerts/AA18-337A

<a name="5">[5]</a> https://www.trendmicro.com/en_us/research/20/e/netwalker-fileless-ransomware-injected-via-reflective-loading.html

<a name="6">[6]</a> https://www.mandiant.com/resources/blog/wannacry-malware-profile

