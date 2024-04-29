<table>
<tr>
<td><b>ID</b></td>
<td><b>C0026</b></td>
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


# Encode Data

Malware may encode data.

## Methods

|Name|ID|Description|
|---|---|---|
|**Base64**|C0026.001|Malware may encode data using Base64.|
|**XOR**|C0026.002|Malware may use XOR to encode data.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**CryptoLocker**](../../xample-malware/cryptolocker.md)|2013|C0026.002|CryptoLocker encodes data using XOR. [[1]](#1)|
|[**Dark Comet**](../../xample-malware/dark-comet.md)|2008|C0026.002|Dark Comet encodes data using XOR. [[1]](#1)|
|[**DNSChanger**](../../xample-malware/dnschanger.md)|2011|C0026.002|DNSChanger encodes data using XOR. [[1]](#1)|
|[**Gamut**](../../xample-malware/gamut.md)|2014|C0026.002|Gamut encodes data using XOR. [[1]](#1)|
|[**Hupigon**](../../xample-malware/hupigon.md)|2013|C0026.002|Hupigon encodes data using XOR. [[1]](#1)|
|[**Kraken**](../../xample-malware/kraken.md)|2008|C0026.002|Kraken encodes data using XOR. [[1]](#1)|
|[**Locky Bart**](../../xample-malware/locky-bart.md)|2017|C0026.002|Locky Bart encodes data using XOR. [[1]](#1)|
|[**Mebromi**](../../xample-malware/mebromi.md)|2011|C0026.002|Mebromi encodes data using XOR. [[1]](#1)|
|[**Redhip**](../../xample-malware/redhip.md)|2011|C0026.002|Redhip encodes data using XOR. [[1]](#1)|
|[**Rombertik**](../../xample-malware/rombertik.md)|2015|C0026.002|Rombertik encodes data using XOR. [[1]](#1)|
|[**Shamoon**](../../xample-malware/shamoon.md)|2012|C0026.002|Shamoon encodes data using XOR. [[1]](#1)|
|[**Stuxnet**](../../xample-malware/stuxnet.md)|2010|C0026.002|Stuxnet encodes data using XOR. [[1]](#1)|
|[**TrickBot**](../../xample-malware/trickbot.md)|2016|C0026.002|TrickBot encodes data using XOR. [[1]](#1)|
|[**UP007**](../../xample-malware/up007.md)|2016|C0026.002|The malware encodes data using XOR. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[encode data using XOR](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/encoding/xor/encode-data-using-xor.yml)|Encode Data::XOR (C0026.002)|--|
|[encode data using Base64](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/encoding/base64/encode-data-using-base64.yml)|Encode Data::Base64 (C0026.001)|System.Convert::ToBase64String, System.Convert::ToBase64CharArray, System.Convert::TryToBase64Chars|
|[decode data using Base64 via dword translation table](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/encoding/base64/decode-data-using-base64-via-dword-translation-table.yml)|Encode Data::Base64 (C0026.001)|--|
|[reference Base64 string](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/encoding/base64/reference-base64-string.yml)|Encode Data::Base64 (C0026.001)|--|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022
