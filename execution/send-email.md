|||
|---------|------------------------|
|**ID**|**M0020**|
|**Objective(s)**|[Execution](https://github.com/MAECProject/malware-behaviors/tree/master/execution), [Lateral Movement](https://github.com/MAECProject/malware-behaviors/tree/master/lateral-movement)|
|**Related ATT&CK Technique(s)**|[Spearphishing Attachment](https://attack.mitre.org/techniques/T1193), [Spearphishing Link](https://attack.mitre.org/techniques/T1192)|

Send Email
==========
Sends an email message from the system on which the malware is executing to one or more recipients, mostly commonly for the purpose of spamming or for distributing a malicious attachment or URL (malspamming).

**See related ATT&CK Techniques:** [**Spearphishing Attachment**](https://attack.mitre.org/techniques/T1193), [**Spearphishing Link**](https://attack.mitre.org/techniques/T1192).

Malware Examples
----------------
|Name|Date|Description|
|--------------|--------------------------|-----------------------------|
|Gamut|2014|Gamut probes the infected system's SMTP port 25 by sending a test SMTP transaction to mail.ru and hotmail.com. If port 25 is open, the bot requests the spam template and email list, which it uses to send spam. [[1]](#1)|
|Bagle|2004|Bagle uses its own SMTP engine to mass-mail itself as an attachment from an infected computer. [[2]](#2)|

References
----------
<a name="1">[1]</a> https://www.trustwave.com/Resources/SpiderLabs-Blog/Gamut-Spambot-Analysis/

<a name="2">[2]</a> https://en.wikipedia.org/wiki/Bagle_(computer_worm)