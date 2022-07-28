|||
|---|---|
|**ID**|**E1105**|
|**Objective(s)**|[Command and Control](../command-and-control), [Lateral Movement](../lateral-movement), [Persistence](../persistence)|
|**Related ATT&CK Technique**|[Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105/)|


Ingress Tool Transfer
================
Malware may copy files from an external system to a system on a compromised network. 

Note that this behavior is separate from possible execution (installation) of the file, which is covered by the [Install Additional Program](../execution/install-prog.md) behavior. 

**See ATT&CK:** [**Ingress Tool Transfer**](https://attack.mitre.org/techniques/T1105/).

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|Trojan spyware program that has mainly been used for targeting banking sites.|
|[**Poison-Ivy**](../xample-malware/poison-ivy.md)|2005|After the Poison-Ivy implant is running on the target machine, the attacker can use a Windows GUI controller to control the target computer. [[1]](#1)|
|[**CryptoLocker**](../command-and-control/remote-file-copy.md)|2013|The malware receives a public key from the C2 [[2]](#2)|
|[**Gamut**](../command-and-control/remote-file-copy.md)|2014|The malware receives data from C2 [[3]](#3)|
|[**DarkComet**](../command-and-control/remote-file-copy.md)|2008|Can download files from remote repository upon instruction  [[4]](#4)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|Creates a folder on remote computers and then copies its executables (Shamoon and Filerase) into that directory  [[5]](#5)|

References
----------
<a name="1">[1]</a> https://www.cyber.nj.gov/threat-profiles/trojan-variants/poison-ivy

<a name="2">[2]</a> https://www.secureworks.com/research/cryptolocker-ransomware

<a name="3">[3]</a> https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/gamut-spambot-analysis/

<a name="4">[4]</a> https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/

<a name="5">[5]</a> https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-attackers-employ-new-tool-kit-to-wipe-infected-systems/
