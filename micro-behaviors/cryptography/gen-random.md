|||
|---|---|
|**ID**|**C0021**|
|**Objective(s)**|[Cryptography](../cryptography)|
|**Related ATT&CK Technique**|None|


Generate Pseudo-random Sequence
===============================
The Generate Pseudo-random Sequence microbehavior can be used for a number of purposes. The methods below include specific functions, as well as pseudorandom number generators (PRNG).

Methods
-------
|Name|ID|Description|
|---|---|---|
|**GetTickCount**|C0021.001|Malware generates a pseudo-random sequence using GetTickCount.|
|**Use API**|C0021.003|Malware generates a pseudo-random sequence using a Windows API.|
|**rand**|C0021.002|Malware generates a pseudo-random sequence using rand.|
|**RC4 PRGA**|C0021.004|Malware generates a pseudo-random sequence using the RC4 Pseudo Random (Byte) Generation Algorithm (PRGA).|
|**Mersenne Twister**|C0021.005|Malware generates a pseudo-random sequence using the Mersenne Twister PRNG.|