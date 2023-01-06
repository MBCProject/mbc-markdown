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


# Ingress Tool Transfer

Malware may copy files from an external system to a system on a compromised network. 

Note that this behavior is separate from possible execution (installation) of the file, which is covered by the **Install Additional Program ([B0023](../execution/install-additional-program.md))** behavior. 

See ATT&CK: **Ingress Tool Transfer ([T1105](https://attack.mitre.org/techniques/T1105/))**.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|--|Trojan spyware program that has mainly been used for targeting banking sites.|
|[**Poison-Ivy**](../xample-malware/poison-ivy.md)|2005|--|After the Poison-Ivy implant is running on the target machine, the attacker can use a Windows GUI controller to control the target computer. [[1]](#1)|
|[**CryptoLocker**](../xample-malware/cryptolocker.md)|2013|--|The malware receives a public key from the C2. [[2]](#2)|
|[**Gamut**](../xample-malware/gamut.md)|2014|--|The malware receives data from C2. [[3]](#3)|
|[**DarkComet**](../xample-malware/dark-comet.md)|2008|--|Can download files from remote repository upon instruction.  [[4]](#4)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|--|Creates a folder on remote computers and then copies its executables (Shamoon and Filerase) into that directory.  [[5]](#5)|
|[**CozyCar**](../xample-malware/cozycar.md)|2010|--|CozyCar requests a file using SSL to a C2 domain. [[6]](#6)|
|[**Vobfus**](../xample-malware/vobfus.md)|2016|--|Vobfus downloads its latest version from a remote server. [[7]](#7)|
|[**TEARDROP**](../xample-malware/teardrop.md)|2018|--|TEARDROP decrypts embedded code buffer which is a Cobalt Strike RAT. [[8]](#8)|


## References

<a name="1">[1]</a> https://www.cyber.nj.gov/threat-profiles/trojan-variants/poison-ivy

<a name="2">[2]</a> https://www.secureworks.com/research/cryptolocker-ransomware

<a name="3">[3]</a> https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/gamut-spambot-analysis/

<a name="4">[4]</a> https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/

<a name="5">[5]</a> https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-attackers-employ-new-tool-kit-to-wipe-infected-systems/

<a name="6">[6]</a> https://unit42.paloaltonetworks.com/tracking-minidionis-cozycars-new-ride-is-related-to-seaduke

<a name="7">[7]</a> https://securitynews.sonicwall.com/xmlpost/revisiting-vobfus-worm-mar-8-2013/

<a name="8">[8]</a> https://www.cisa.gov/uscert/ncas/analysis-reports/ar21-039b