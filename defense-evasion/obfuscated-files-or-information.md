<table>
<tr>
<td><b>ID</b></td>
<td><b>E1027</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../anti-static-analysis">Anti-Static Analysis</a>, <a href="../defense-evasion">Defense Evasion</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Obfuscated Files or Information (<a href="https://attack.mitre.org/techniques/T1027/">T1027</a>, <a href="https://attack.mitre.org/techniques/T1406/">T1406</a>)</b></td>
</tr>
<tr>
<td><b>Anti-Analysis Type</b></td>
<td><b>Evasion</b></td>
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
<td><b>21 November 2022</b></td>
</tr>
</table>


# Obfuscated Files or Information

Malware may make files or information difficult to discover or analyze by encoding, encrypting, or otherwise obfuscating the content. In addition, a malware sample itself can be encoded or encrypted (i.e., encoding/encryption is a code characteristic).

A related MBC behavior (code characteristic), associated explicitly with executable code and making its analysis more difficult, is **Executable Code Obfuscation ([B0032](../anti-static-analysis/executable-code-obfuscation.md))**.

Another related MBC behavior (code characteristic), is **Software Packing ([F0001](../anti-static-analysis/software-packing.md))** which has methods capturing specific packers and types of compression.

See ATT&CK: **Obfuscated Files or Information ([T1027](https://attack.mitre.org/techniques/T1027/), [T1406](https://attack.mitre.org/techniques/T1406/))**.

Instead of being listed alphabetically, methods have been grouped to better faciliate labeling and mapping.

## Methods

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


## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|E1027.m02|Trojan spyware program that has mainly been used for targeting banking sites. [[4]](#4)|
|[**WebCobra**](../xample-malware/webcobra.md)|2018|--|Obfuscates files. [[5]](#5)|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|--|GoBotKR uses base64 to obfuscate strings, commands and files. [[1]](#1)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|The malware will use a key to decrypt text from a URL to create more malicious code [[2]](#2)|
|[**Netwalker**](../xample-malware/netwalker.md)|2020|--|Netwalker is obfuscated with several layers of encoding, obfuscation, and encryption techniques such as base64, hexademcimal, and XOR [[3]](#3)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|E1027.m05|Encrypt data using RC4 via WinAPI (This capa rule had 1 match) [[7]](#7)|
|[**CryptoLocker**](../xample-malware/cryptolocker.md)|2013|E1027.m02|Encode data using XOR (This capa rule had 1 match) [[7]](#7)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|E1027.m02|Encode data using XOR (This capa rule had 13 matches) [[7]](#7)|
|[**DNSChanger**](../xample-malware/dnschanger.md)|2011|E1027.m02|Encode data using XOR (This capa rule had 1 match) [[7]](#7)|
|[**Gamut**](../xample-malware/gamut.md)|2014|E1027.m02|Encode data using XOR (This capa rule had 1 match) [[7]](#7)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|E1027.m02, E1027.m05|Please see the Hupigon malware page for details. [[7]](#7)|
|[**Kraken**](../xample-malware/kraken.md)|2008|E1027.m02|Encode data using XOR (This capa rule had 2 matches) [[7]](#7)|
|[**Locky Bart**](../xample-malware/locky-bart.md)|2017|E1027.m02|Encode data using XOR (This capa rule had 4 matches) [[7]](#7)|
|[**Mebromi**](../xample-malware/mebromi.md)|2011|E1027.m02|Encode data using XOR (This capa rule had 2 matches) [[7]](#7)|
|[**Poison-Ivy**](../xample-malware/poison-ivy.md)|2005|E1027.m07|Poison Ivy variant encrypts all its strings [[6]](#6)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|E1027.m02|Encode data using XOR (This capa rule had 1 match) [[7]](#7)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|E1027.m02|Encode data using XOR (This capa rule had 5 matches) [[7]](#7)|
|[**SamSam**](../xample-malware/samsam.md)|2015|E1027.m07|SamSam obfuscates functions, class names and strings, including the list of targeted file extensions, the help file contents and environment variables using DES encryption with a fixed hard-coded key and the IV  [[8]](#8)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|E1027.m02|Encode data using XOR (This capa rule had 1 match) [[7]](#7)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|E1027.m01, E1027.m02|Please see the Stuxnet malware page for details. [[9]](#9)|
|[**UP007 Malware Family**](../xample-malware/up007.md)|2016|E1027.m02|Encode data using XOR (This capa rule had 13 matches) [[7]](#7)|
|[**Ursnif**](../xample-malware/ursnif.md)|2016|--|Creates an encrypted Registry key called TorClient to store its data [[10]](#10)|

## References

<a name="1">[1]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="2">[2]</a> https://www.bleepingcomputer.com/virus-removal/remove-kovter-trojan

<a name="3">[3]</a> https://www.trendmicro.com/en_us/research/20/e/netwalker-fileless-ransomware-injected-via-reflective-loading.html

<a name="4">[4]</a> https://www.trendmicro.com/en_us/research/18/k/trickbot-shows-off-new-trick-password-grabber-module.html

<a name="5">[5]</a> https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/

<a name="6">[6]</a> https://www.fortinet.com/blog/threat-research/deep-analysis-of-new-poison-ivy-variant

<a name="7">[7]</a> capa v4.0, analyzed at MITRE on 10/12/2022

<a name="8">[8]</a> https://blog.talosintelligence.com/2018/01/samsam-evolution-continues-netting-over.html

<a name="9">[9]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en

<a name="10">[10]</a> https://www.proofpoint.com/us/threat-insight/post/ursnif-variant-dreambot-adds-tor-functionality

<a name="11">[11]</a> https://blog.malwarebytes.com/threat-analysis/2016/07/untangling-kovter/

