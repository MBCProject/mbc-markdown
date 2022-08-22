
<table>
<tr>
<td><b>ID</b></td>
<td><b>E1112</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../defense-evasion">Defense Evasion</a>, <a href="../persistence">Persistence</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Modify Registry<a href="https://attack.mitre.org/techniques/T1112">T1112</a>)</b></td>
</tr>
</table>


Modify Registry
===============
Malware may make changes to the Windows Registry to hide execution or to persist on the system (note that ATT&CK does not extend this behavior to the Persistence objective). 


See ATT&CK: **Modify Registry ([T1112](https://attack.mitre.org/techniques/T1112/))**.

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|Trojan spyware program that has mainly been used for targeting banking sites.|
|[**Poison-Ivy**](../xample-malware/poison-ivy.md)|2005|After the Poison-Ivy server is running on the target machine, the attacker can use a Windows GUI client to control the target computer. [[1]](#1)|
|[**GotBotKR**](../xample-malware/gotbotkr.md)|2019|GoBotKR can modify registry keys to disable Task Manager, Registry Editor and Command Prompt. [[2]](#2)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|The malware adds many entries to the registry [[3]](#3)|
|[**Gamut**](../xample-malware/gamut.md)|2014|The malware adds a registry key [[4]](#4)|
|[**Kovter**](../xample-malware/kovter.md)|2016|The malware modifies the registry during execution [[5]](#5)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|Disables remote user account control by enabling the registry key LocalAccountTokenFilterPolicy  [[6]](#6)|

References
----------
<a name="1">[1]</a> https://www.cyber.nj.gov/threat-profiles/trojan-variants/poison-ivy

<a name="2">[2]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="3">[3]</a> https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/HUPIGON

<a name="4">[4]</a> https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/gamut-spambot-analysis/

<a name="5">[5]</a> https://blog.malwarebytes.com/threat-analysis/2016/07/untangling-kovter/

<a name="6">[6]</a> https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-returns-to-wipe-systems-in-middle-east-europe/
