
<table>
<tr>
<td><b>ID</b></td>
<td><b>E1485</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../impact">Impact</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b><a href="https://attack.mitre.org/techniques/T1485/">Data Destruction</a></b></td>
</tr>
</table>


Data Destruction
================
Data, system files, or other files are destroyed. Individual files are selected, as opposed to wiping an entire sector.

see ATT&CK: [**Data Destruction**](https://attack.mitre.org/techniques/T1485/).

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Delete Application/Software**|E1485.m03|An application or software is deleted.|
|**Delete Shadow Copies**|E1485.m04|Deletes shadow drive data, which is related to ransomware.|
|**Empty Recycle Bin**|E1485.m02|Empties the recycle bin, which can be related to ransomware.|

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|A 2018 variant includes a component that erases files and then wipes the master boot record, preventing file recovery.[[1]](#1)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|If a specific anti-analysis check fails, the malware will overwrite the Master Boot Record or the User's home folder [[2]](#2)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|BlackEnergy 2 variant contains a Destroy plugin that destroys data stored on victim hard drives by overwriting file contents  [[3]](#3)|
|[**Conficker**](../xample-malware/conficker.md)|2008|resets system restore points and deletes backup files [[4]](#4)|
|[**MazarBot**](../xample-malware/mazarbot.md)|2016|Can erase phone data  [[5]](#5)|

References
----------
<a name="1">[1]</a> http://www.darkreading.com/attacks-breaches/disk-wiping-shamoon-malware-resurfaces-with-file-erasing-malware-in-tow/d/d-id/1333509

<a name="2">[2]</a> https://blogs.cisco.com/security/talos/rombertik

<a name="3">[3]</a> https://securelist.com/be2-extraordinary-plugins-siemens-targeting-dev-fails/68838/

<a name="4">[4]</a> https://en.wikipedia.org/wiki/Conficker

<a name="5">[5]</a> https://heimdalsecurity.com/blog/security-alert-mazar-bot-active-attacks-android-malware/
