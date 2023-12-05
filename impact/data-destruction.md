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
<td><b>Data Destruction (<a href="https://attack.mitre.org/techniques/T1485/">T1485</a>)</b></td>
</tr>
<tr>
<td><b>Impact Type</b></td>
<td><b>Availability</b></td>
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
<td><b>13 September 2023</b></td>
</tr>
</table>


# Data Destruction

Data, system files, or other files are destroyed. Individual files are selected, as opposed to wiping an entire sector.

See ATT&CK: **Data Destruction ([T1485](https://attack.mitre.org/techniques/T1485/))**.

## Methods

|Name|ID|Description|
|---|---|---|
|**Delete Application/Software**|E1485.m03|An application or software is deleted.|
|**Delete Shadow Copies**|E1485.m04|Deletes shadow drive data, which is related to ransomware.|
|**Empty Recycle Bin**|E1485.m02|Empties the recycle bin, which can be related to ransomware.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|--|A 2018 variant includes a component that erases files and then wipes the Master Boot Record (MBR), preventing file recovery. [[1]](#1)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|--|If a specific anti-analysis check fails, the malware will overwrite the Master Boot Record or the user's home folder. [[2]](#2)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|--|BlackEnergy 2 variant contains a Destroy plugin that destroys data stored on victim hard drives by overwriting file contents.  [[3]](#3)|
|[**Conficker**](../xample-malware/conficker.md)|2008|--|Conficker resets system restore points and deletes backup files. [[4]](#4)|
|[**MazarBot**](../xample-malware/mazarbot.md)|2016|--|MazarBot can erase phone data. [[5]](#5)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[delete volume shadow copies](https://github.com/mandiant/capa-rules/blob/master/impact/inhibit-system-recovery/delete-volume-shadow-copies.yml)|Data Destruction::Delete Shadow Copies (E1485.m04)|--|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[clears_logs](https://github.com/CAPESandbox/community/tree/master/modules/signatures/clears_logs.py)|Data Destruction (E1485)|--|
|[ransomware_recyclebin](https://github.com/CAPESandbox/community/tree/master/modules/signatures/ransomware_recyclebin.py)|Data Destruction (E1485)|--|
|[uses_windows_utilities_cipher](https://github.com/CAPESandbox/community/tree/master/modules/signatures/uses_windows_utilities_cipher.py)|Data Destruction (E1485)|--|
|[anomalous_deletefile](https://github.com/CAPESandbox/community/tree/master/modules/signatures/anomalous_deletefile.py)|Data Destruction (E1485)|NtDeleteFile, DeleteFileW, DeleteFileA|

## References

<a name="1">[1]</a> https://www.darkreading.com/attacks-breaches/disk-wiping-shamoon-malware-resurfaces-with-file-erasing-malware-in-tow/d/d-id/1333509

<a name="2">[2]</a> https://blogs.cisco.com/security/talos/rombertik

<a name="3">[3]</a> https://securelist.com/be2-extraordinary-plugins-siemens-targeting-dev-fails/68838/

<a name="4">[4]</a> https://en.wikipedia.org/wiki/Conficker

<a name="5">[5]</a> https://heimdalsecurity.com/blog/security-alert-mazar-bot-active-attacks-android-malware/

<a name="6">[6]</a> https://www.darkreading.com/attacks-breaches/disk-wiping-shamoon-malware-resurfaces-with-file-erasing-malware-in-tow

