|||
|---|---|
|**ID**|**E1485**|
|**Objective(s)**|[Impact](../impact)|
|**Related ATT&CK Technique**|[Data Destruction](https://attack.mitre.org/techniques/T1485/), [Delete Device Data](https://attack.mitre.org/techniques/T1447/)|


Data Destruction
================
Data, system files, or other files are destroyed. Individual files are selected, as opposed to wiping an entire sector.

see ATT&CK: [**Data Destruction**](https://attack.mitre.org/techniques/T1485/).

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Delete Application/Software**|E1485.m03|An application or software is deleted.|
|**Delete Shadow Drive**|E1485.m01|Deletes shadow drive data, which is related to ransomware.|
|**Empty Recycle Bin**|E1485.m02|Empties the recycle bin, which can be related to ransomware.|

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|A 2018 variant includes a component that erases files and then wipes the master boot record, preventing file recovery.[[1]](#1)|

References
----------
<a name="1">[1]</a> http://www.darkreading.com/attacks-breaches/disk-wiping-shamoon-malware-resurfaces-with-file-erasing-malware-in-tow/d/d-id/1333509
