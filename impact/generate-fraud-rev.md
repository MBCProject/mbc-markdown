|||
|---------|------------------------|
|**ID**|**E1472**|
|**Objective(s)**|[Impact](https://github.com/MAECProject/malware-behaviors/tree/master/impact)|
|**Related ATT&CK Technique(s)**|[Generate Fraudulent Advertising Revenue](https://attack.mitre.org/techniques/T1472/)|


Generate Fraudulent Advertising Revenue
=======================================
Malware may generate advertising revenue by generating clicks of advertising links. The ATT&CK technique, [Generate Fraudulent Advertising Revenue](https://attack.mitre.org/techniques/T1472/), pertains only to mobile platform, but the behavior is applicable to other platforms as well. 

See ATT&CK: [**Generate Fraudulent Advertising Revenue**](https://attack.mitre.org/techniques/T1472/).

Methods
-------
* **Click Hijacking**: Malware alters DNS server settings to route to a rogue DNS server: when the user clicks on a search result link displayed through a search engine query, malware re-routes the user to different website. Instead of going to the requested site, the user is taken to an alternate website such that the click triggers payment to the threat actor. [[1]](#1)

* **Advertisement Replacement Fraud**:  Malware injects ad windows onto websites the user is views. [[2]](#2) 

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|-----------|-----------------------------|
|DNSChanger| November 2011| Alters DNS server settings to route to a rogue DNS server for the purpose of click hijacking. [[1]](#1)|
|Kovter|2016|Performs click-fraud. [[4]](#4)|

References
----------
<a name="1">[1]</a> https://www.itworld.com/article/2734253/security/behind-the--massive--malware-ad-revenue-fraud-case.html

<a name="2">[2]</a> https://www.fipp.com/news/insightnews/what-are-the-nine-types-of-digital-ad-fraud

<a name="3">[3]</a> https://www.huffingtonpost.com/2011/11/09/click-hijack-hackers-online-ad-scam_n_1084497.html

<a name="4">[4]</a> https://www.bleepingcomputer.com/virus-removal/remove-kovter-trojan

 