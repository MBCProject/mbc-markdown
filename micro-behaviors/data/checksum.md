|||
|---|---|
|**ID**|**C0032**|
|**Objective(s)**|[Data](../data)|
|**Related ATT&CK Technique**|None|


Checksum
========
Malware may derive a checksum from some block of data. The checksum is often used for data validation.

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Adler**|C0032.005|Malware computes an Adler checksum.|
|**BSD**|C0032.003|Malware computes a BSD checksum.|
|**CRC32**|C0032.001|Malware computes a CRC32 checksum.|
|**Luhn**|C0032.002|Malware uses Luhn algorithm, often to validate identification numbers (e.g, credit card number).| 
|**Verhoeff**|C0032.004|Malware uses the Verhoeff algorithm, often for purposes of error detection.|