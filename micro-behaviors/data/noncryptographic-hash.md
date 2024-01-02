<table>
<tr>
<td><b>ID</b></td>
<td><b>C0030</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../data">Data</a></b></td>
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
<td><b>13 October 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>5 December 2023</b></td>
</tr>
</table>


# Non-Cryptographic Hash

Malware may use a non-cryptographic hash. 

## Methods

|Name|ID|Description|
|---|---|---|
|**dhash**|C0030.004|Malware uses the dhash hash function.|
|**Fast-Hash**|C0030.003|Malware uses the Fast-Hash hash function.|
|**FNV**|C0030.005|Malware uses the FNV hash function.|
|**MurmurHash**|C0030.001|Malware uses the MurmurHash hash function.|
|**pHash**|C0030.002|Malware uses the pHash hash function.|
|**djb2**|C0030.006|Malware uses the djb2 hash function.|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[hash data using murmur3](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/hashing/murmur/hash-data-using-murmur3.yml)|Non-Cryptographic Hash::MurmurHash (C0030.001)|--|
|[hash data using fnv](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/hashing/fnv/hash-data-using-fnv.yml)|Non-Cryptographic Hash::FNV (C0030.005)|_allmul|
|[hash data using djb2](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/hashing/djb2/hash-data-using-djb2.yml)|Non-Cryptographic Hash::djb2 (C0030.006)|--|
