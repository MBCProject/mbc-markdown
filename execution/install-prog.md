|||
|---------|------------------------|
|**ID**|**B0023**|
|**Objective(s)**| [Execution](https://github.com/MBCProject/mbc-markdown/tree/master/execution)|
|**Related ATT&CK Technique**|None|


Install Additional Program
==========================
Installs another, different program on the system. The additional program can be any secondary module; examples include backdoors, malicious drivers, kernel modules, and OS X Apps. 

Malware that installs another component is called a "dropper." If the code is contained in the malware, it's a "single stage" dropper; "two stage" droppers download the code from a remote location (the associated download behavior is covered by the [Remote File Copy](https://github.com/MBCProject/mbc-markdown/blob/master/command-and-control/remote-file-copy.md) behavior).

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|
|[**WebCobra**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/webcobra.md)|November 2018|Drops software to mine for cryptocurrency. [[1]](#1)|
|[**Geneio**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/geneio.md)|August 2015|Tricks OS X keychain to create application files.|
|[**GotBotKR**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/gotbotkr.md)|July 2019 |GotBotKR reinstalls its running instance if it is removed. [[3]](#3)|
|[**MazarBot**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/mazarbot.md)|2016|Installs a backdoor.|
|[**Mebromi**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/mebromi.md)|2011|A Trojan downloader.|
|[**YiSpecter**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/yispecter.md)|2015|Can download and install arbitrary iOS apps.|

References
----------
<a name="1">[1]</a> https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/

<a name="2">[2]</a> https://www.fortinet.com/blog/threat-research/deep-analysis-of-driver-based-mitm-malware-itranslator.html

<a name="3">[3]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/
