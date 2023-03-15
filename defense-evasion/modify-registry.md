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
<td><b>Modify Registry (<a href="https://attack.mitre.org/techniques/T1112">T1112</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>2 August 2022</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>21 November 2022</b></td>
</tr>
</table>


# Modify Registry

Malware may make changes to the Windows Registry to hide execution or to persist on the system (note that ATT&CK does not extend this behavior to the Persistence objective). 


See ATT&CK: **Modify Registry ([T1112](https://attack.mitre.org/techniques/T1112/))**.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|--|GoBotKR can modify registry keys to disable Task Manager, Registry Editor and Command Prompt. [[2]](#2)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|The malware adds many entries to the registry. [[3]](#3)|
|[**Gamut**](../xample-malware/gamut.md)|2014|--|The malware adds a registry key. [[4]](#4)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|The malware modifies the registry during execution. [[5]](#5)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|--|Shamoon disables remote user account control by enabling the registry key LocalAccountTokenFilterPolicy. [[6]](#6)|
|[**CHOPSTICK**](../xample-malware/chopstick.md)|2015|--|CHOPSTICK may encrypt and store configuration data inside a registry key. [[7]](#7)|
|[**Clipminer**](../xample-malware/clipminer.md)|2011|--|Clipminer edits the registry. [[8]](#8)|


## References

<a name="1">[1]</a> https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/clipminer-bitcoin-mining-hijacking

<a name="2">[2]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="3">[3]</a> https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/HUPIGON

<a name="4">[4]</a> https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/gamut-spambot-analysis/

<a name="5">[5]</a> https://blog.malwarebytes.com/threat-analysis/2016/07/untangling-kovter/

<a name="6">[6]</a> https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-returns-to-wipe-systems-in-middle-east-europe/

<a name="7">[7]</a> https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf

<a name="8">[8]</a> https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/clipminer-bitcoin-mining-hijacking

