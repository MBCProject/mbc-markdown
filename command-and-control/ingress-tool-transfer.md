<table>
<tr>
<td><b>ID</b></td>
<td><b>E1105</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../command-and-control">Command and Control</a>, <a href="../lateral-movement">Lateral Movement</a>, <a href="../persistence">Persistence</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Ingress Tool Transfer (<a href="https://attack.mitre.org/techniques/T1105/">T1105</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.1</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>5 December 2023</b></td>
</tr>
</table>


# Ingress Tool Transfer

Malware may copy files from an external system to a system on a compromised network. 

Note that this behavior is separate from possible execution (installation) of the file, which is covered by the **Install Additional Program ([B0023](../execution/install-additional-program.md))** behavior. 

See ATT&CK: **Ingress Tool Transfer ([T1105](https://attack.mitre.org/techniques/T1105/))**.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Poison Ivy**](../xample-malware/poison-ivy.md)|2005|--|After the Poison Ivy implant is running on the target machine, the attacker can use a Windows GUI controller to control the target computer. [[1]](#1)|
|[**DarkComet**](../xample-malware/dark-comet.md)|2008|--|DarkComet can download files from a remote repository upon instruction. [[2]](#2)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|--|Shamoon creates a folder on remote computers and then copies its executables (Shamoon and Filerase) into that directory. [[3]](#3)|
|[**CozyCar**](../xample-malware/cozycar.md)|2010|--|CozyCar requests a file using SSL to a C2 domain. [[4]](#4)|
|[**Vobfus**](../xample-malware/vobfus.md)|2016|--|Vobfus downloads its latest version from a remote server. [[5]](#5)|
|[**TEARDROP**](../xample-malware/teardrop.md)|2018|--|TEARDROP executes the decrypted, embedded code buffer, which is a Cobalt Strike RAT. [[6]](#6)|
|[**Matanbuchus**](../xample-malware/matanbuchus.md)|2021|--|Malware downloads DLLs from the hardcoded URL/remote server. [[7]](#7) [[8]](#8)|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|--|GoBotKR can download additional files and update itself. [[9]](#9)|
|[**Gamut**](../xample-malware/gamut.md)|2014|--|Gamut receives files from the C2. [[10]](#10)|
|[**UP007**](../xample-malware/up007.md)|2016|--|UP007 downloads files from the C2. [[11]](#11)|

## Detection

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[suspicious_mpcmdrun_use](https://github.com/CAPESandbox/community/tree/master/modules/signatures/suspicious_mpcmdrun_use.py)|Ingress Tool Transfer (E1105)|--|
|[network_document_file](https://github.com/CAPESandbox/community/tree/master/modules/signatures/network_document_file.py)|Ingress Tool Transfer (E1105)|URLDownloadToFileW, HttpOpenRequestW, send, InternetCrackUrlW, InternetCrackUrlA, WSASend, URLDownloadToCacheFileW|

## References

<a name="1">[1]</a> https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/

<a name="2">[2]</a> https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-attackers-employ-new-tool-kit-to-wipe-infected-systems/

<a name="3">[3]</a> https://unit42.paloaltonetworks.com/tracking-minidionis-cozycars-new-ride-is-related-to-seaduke

<a name="2">[2]</a> https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/

<a name="3">[3]</a> https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-attackers-employ-new-tool-kit-to-wipe-infected-systems/

<a name="4">[4]</a> https://unit42.paloaltonetworks.com/tracking-minidionis-cozycars-new-ride-is-related-to-seaduke

<a name="5">[5]</a> https://securitynews.sonicwall.com/xmlpost/revisiting-vobfus-worm-mar-8-2013/

<a name="6">[6]</a> https://www.cisa.gov/uscert/ncas/analysis-reports/ar21-039b

<a name="7">[7]</a> https://www.0ffset.net/reverse-engineering/matanbuchus-loader-analysis/

<a name="8">[8]</a> https://www.cyberark.com/resources/threat-research-blog/inside-matanbuchus-a-quirky-loader

<a name="9">[9]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="10">[10]</a> https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/gamut-spambot-analysis/

<a name="11">[11]</a> https://citizenlab.ca/2016/04/between-hong-kong-and-burma/
