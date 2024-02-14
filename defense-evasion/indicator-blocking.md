<table>
<tr>
<td><b>ID</b></td>
<td><b>F0006</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../defense-evasion">Defense Evasion</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Impair Defenses: Indicator Blocking (<a href="https://attack.mitre.org/techniques/T1562/006/">T1562.006</a>)</b></td>
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


# Indicator Blocking

Malware blocks indicators or events that would indicate malicious activity. This is achieved by blocking indicators or alerts that would typically notify users or security tools of a potential infection. This can be done in several ways, such as disabling security software, interfering with event logging, or altering system settings to suppress notifications. By blocking these indicators, the malware can continue its malicious activities without being detected. Methods relevant to the malware domain are below. 

See ATT&CK: **Impair Defenses: Indicator Blocking ([T1562.006](https://attack.mitre.org/techniques/T1562/006/))**.

## Methods

|Name|ID|Description|
|---|---|---|
|**Remove SMS Warning Messages**|F0006.001|Malware captures the message body of incoming SMS messages and aborts displaying messages that meets a certain criteria.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|--|The malware clears windows event logs and removes the watermark associated with enabling the TESTSIGNING boot configuration option by removing the relevent strings in the user32.dll.mui of the system. [[1]](#1)|
|[**Conficker**](../xample-malware/conficker.md)|2008|--|The malware terminates various services related to system security and Windows and prevents network access to various websites related to antivirus software. [[2]](#2)|
|[**DarkComet**](../xample-malware/dark-comet.md)|2008|--|The malware can disable security center functions like anti-virus and firewall. [[3]](#3)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|--|TrickBot terminates the following anti-malware services: Window Defender, MBamService (Malwarebytes), SAVService (Sophos AV). [[4]](#4)|

## Detection

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[tampers_powershell_logging](https://github.com/CAPESandbox/community/tree/master/modules/signatures/tampers_powershell_logging.py)|Indicator Blocking (F0006)|--|
|[stealth_hidden_extension](https://github.com/CAPESandbox/community/tree/master/modules/signatures/stealth_hidden_extension.py)|Indicator Blocking (F0006)|--|
|[stealth_hiddenreg](https://github.com/CAPESandbox/community/tree/master/modules/signatures/stealth_hiddenreg.py)|Indicator Blocking (F0006)|--|
|[stealth_hide_notifications](https://github.com/CAPESandbox/community/tree/master/modules/signatures/stealth_hide_notifications.py)|Indicator Blocking (F0006)|--|
|[creates_nullvalue](https://github.com/CAPESandbox/community/tree/master/modules/signatures/creates_nullvalue.py)|Indicator Blocking (F0006)|NtCreateKey, NtSetValueKey|
|[tampers_etw](https://github.com/CAPESandbox/community/tree/master/modules/signatures/tampers_etw.py)|Indicator Blocking (F0006)|--|
|[disables_wer](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_wer.py)|Indicator Blocking (F0006)|--|

## References

<a name="1">[1]</a> https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf

<a name="2">[2]</a> https://en.wikipedia.org/wiki/Conficker

<a name="3">[3]</a> https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/

<a name="4">[4]</a> https://www.trendmicro.com/en_us/research/18/k/trickbot-shows-off-new-trick-password-grabber-module.html

