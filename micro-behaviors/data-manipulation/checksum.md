|||
|---|---|
|**ID**|**C0023**|
|**Objective(s)**|[Data Manipulation](../data-manipulation)|
|**Related ATT&CK Technique**|None|


Checksum
========
Malware may derive a checksum from some block of data. The checksum is often used for data validation.

Methods
-------
|Name|ID|Description|
|---|---|---|
|**BSD**|C0023.003|Malware computes a BSD checksum.|
|**CRC32**|C0023.001|Malware computes a CRC32 checksum.|
|**Luhn**|C0023.002|Malware uses Luhn algorithm, often to validate identification numbers (e.g, credit card number).| 
|**Verhoeff**|C0023.004|Malware uses the Verhoeff algorithm, often for purposes of error detection.|