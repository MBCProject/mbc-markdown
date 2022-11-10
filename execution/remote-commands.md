<table>
<tr>
<td><b>ID</b></td>
<td><b>B0011</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../execution">Execution</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
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
<td><b>31 October 2022</b></td>
</tr>
</table>


Remote Commands
===============
Malware may provide an attacker with explicit commands. This behavior differs from the **Remote Access ([B0022](../impact/remote-access.md))** behavior under the [Impact](../impact) objective in that *Impact: Remote Access* is potentially much broader and may include full remote access.

Given an "execute" command, the attacker may choose to delete files or corrupt data, power-off the machine, or upload and execute other applications. The malware may also provide specific commands to the attacker (e.g., "delete file"). 

Commands provided by the malware can be captured with the methods defined below. For example, malware that enables an attacker to delete a file could be tagged with *Execution:Remote Commands:Delete File*.

It may be useful to capture remote commands along with related behaviors because the associated descriptions could provide details of how the malware implements the command. For example, *Defense Evasion:File Deletion* could be used to provide details and context to *Execution:Remote Commands:Delete File*.

Autonomous behaviors - those done by the malware without an active attacker - should not be captured with *Execution:Remote Commands*. For example, malware that *automatically* destroys data would be tagged with the **Impact: Data Destruction ([E1485](../impact/data-destruction.md))** behavior.

## Methods

|Name|ID|Description|
|---|---|---|
|**Delete File**|B0011.001||
|**Download File**|B0011.002||
|**Execute**|B0011.003||
|**Shutdown**|B0011.004||
|**Sleep**|B0011.005||
|**Uninstall**|B0011.006||
|**Upload File**|B0011.007||


## Use in Malware

|Name|Date|Description|
|---|---|---|
|[**Ursnif**](../xample-malware/ursnif.md)|2016|Commands sent by a remote user can archive/upload files, capture screenshots, clear cookies, download execute other files, list running processes, reboot the affected system, steal certificates and cookies, update/download a configuration file, upload a log file which contains stolen information  [[1]](#1)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|infected bots receive commands from botmaster to load plugins associated with botmaster's goals [[2]](#2)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|Receives various commands from c2 server.  [[3]](#3)|

## References

<a name="1">[1]</a> https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/BKDR_URSNIF.SM?_ga=2.129468940.1462021705.1559742358-1202584019.1549394279

<a name="2">[2]</a> https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf

<a name="3">[3]</a> https://www.cybereason.com/blog/research/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware
