
<table>
<tr>
<td><b>ID</b></td>
<td><b>B0023</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../execution">Execution</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
</table>


Install Additional Program
==========================
Installs another, different program on the system. The additional program can be any secondary module; examples include backdoors, malicious drivers, kernel modules, and OS X Apps. 

Malware that installs another component is called a "dropper." If the code is contained in the malware, it's a "single stage" dropper; "two stage" droppers download the code from a remote location (the associated download behavior is covered by the [Remote File Copy](../command-and-control/ingress-tool-transfer.md) behavior).

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**WebCobra**](../xample-malware/webcobra.md)|November 2018|Drops software to mine for cryptocurrency. [[1]](#1)|
|[**Geneio**](../xample-malware/geneio.md)|August 2015|Tricks OS X keychain to create application files.|
|[**GotBotKR**](../xample-malware/gotbotkr.md)|July 2019|GotBotKR reinstalls its running instance if it is removed. [[3]](#3)|
|[**MazarBot**](../xample-malware/mazarbot.md)|2016|Installs a backdoor.|
|[**Mebromi**](../xample-malware/mebromi.md)|2011|A Trojan downloader.|
|[**YiSpecter**](../xample-malware/yispecter.md)|2015|Can download and install arbitrary iOS apps.|
|[**UP007**](../xample-malware/up007.md)|2016|The malware is a dropper that creates multiple files [[4]](#4)|

References
----------
<a name="1">[1]</a> https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/

<a name="2">[2]</a> https://www.fortinet.com/blog/threat-research/deep-analysis-of-driver-based-mitm-malware-itranslator.html

<a name="3">[3]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="4">[4]</a> https://citizenlab.ca/2016/04/between-hong-kong-and-burma/
