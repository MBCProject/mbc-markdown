<table>
<tr>
<td><b>ID</b></td>
<td><b>B0020</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../execution">Execution</a>, <a href="../lateral-movement">Lateral Movement</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Phishing (<a href="https://attack.mitre.org/techniques/T1566/">T1566</a>)</b></td>
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


# Send Email

Sends an email message from the system on which the malware is executing to one or more recipients, mostly commonly for the purpose of spamming or for distributing a malicious attachment or URL (malspamming).

This behavior is related to the **Phishing ([T1566](https://attack.mitre.org/techniques/T1566/))** ATT&CK technique defined under ATT&CK's Initial Access tactic.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Gamut**](../xample-malware/gamut.md)|2014|--|Gamut probes the infected system's SMTP port 25 by sending a test SMTP transaction to mail.ru and hotmail.com. If port 25 is open, the bot requests the spam template and email list, which it uses to send spam. [[1]](#1)|
|[**Bagle**](../xample-malware/bagle.md)|2004|--|Bagle uses its own SMTP engine to mass-mail itself as an attachment from an infected computer. [[2]](#2)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|--|Trojan spyware program that has mainly been used for targeting banking sites.|
|[**Emotet**](../xample-malware/emotet.md)|2018|--|Spam email with the Emotet loader is sent automatically. [[3]](#3)|

## References

<a name="1">[1]</a> https://www.trustwave.com/Resources/SpiderLabs-Blog/Gamut-Spambot-Analysis/

<a name="2">[2]</a> https://en.wikipedia.org/wiki/Bagle_(computer_worm)

<a name="3">[3]</a> https://securelist.com/the-banking-trojan-emotet-detailed-analysis/69560/
