<table>
<tr>
<td><b>ID</b></td>
<td><b>C0032</b></td>
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
<td><b>13 September 2023</b></td>
</tr>
</table>


# Checksum

Malware may derive a checksum from some block of data. The checksum is often used for data validation.


## Methods

|Name|ID|Description|
|---|---|---|
|**Adler**|C0032.005|Malware computes an Adler checksum.|
|**BSD**|C0032.003|Malware computes a BSD checksum.|
|**CRC32**|C0032.001|Malware computes a CRC32 checksum.|
|**Luhn**|C0032.002|Malware uses Luhn algorithm, often to validate identification numbers (e.g, credit card number).| 


## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|C0032.001|Dark Comet hashes data with CRC32. [[1]](#1)|
|[**Gamut**](../xample-malware/gamut.md)|2014|C0032.001|Gamut hashes data with CRC32. [[1]](#1)|
|[**Locky Bart**](../xample-malware/locky-bart.md)|2017|C0032.001|Locky Bart hashes data with CRC32. [[1]](#1)|
|[**UP007**](../xample-malware/up007.md)|2016|C0032.001|UP007 hashes data with CRC32. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[validate payment card number using luhn algorithm](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/checksum/luhn/validate-payment-card-number-using-luhn-algorithm.yml)|Checksum::Luhn (C0032.002)| |
|[compute adler32 checksum](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/checksum/adler32/compute-adler32-checksum.yml)|Checksum::Adler (C0032.005)| |
|[hash data with CRC32](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/checksum/crc32/hash-data-with-crc32.yml)|Checksum::CRC32 (C0032.001)|RtlComputeCrc32|
|[validate payment card number using luhn algorithm with lookup table](https://github.com/mandiant/capa-rules/blob/master/lib/validate-payment-card-number-using-luhn-algorithm-with-lookup-table.yml)|Checksum::Luhn (C0032.002)| |
|[validate payment card number using luhn algorithm with no lookup table](https://github.com/mandiant/capa-rules/blob/master/lib/validate-payment-card-number-using-luhn-algorithm-with-no-lookup-table.yml)|Checksum::Luhn (C0032.002)| |

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

