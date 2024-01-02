<table>
<tr>
<td><b>ID</b></td>
<td><b>C0059</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../cryptography">Cryptography</a></b></td>
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
<td><b>17 January 2021</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>5 December 2023</b></td>
</tr>
</table>


# Crypto Library

Malware uses a crypto library.

## Methods

|Name|ID|Description|
|---|---|---|
|**API Call**|C0059.001|Malware uses crypto API calls.|
|**Static Public Library**|C0059.002|A public crypto library is embedded in the code.|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[linked against Crypto++](https://github.com/mandiant/capa-rules/blob/master/linking/static/cryptopp/linked-against-crypto.yml)|Crypto Library (C0059)|--|
|[linked against wolfCrypt](https://github.com/mandiant/capa-rules/blob/master/linking/static/wolfcrypt/linked-against-wolfcrypt.yml)|Crypto Library (C0059)|--|
|[linked against OpenSSL](https://github.com/mandiant/capa-rules/blob/master/linking/static/openssl/linked-against-openssl.yml)|Crypto Library (C0059)|--|
|[linked against PolarSSL/mbed TLS](https://github.com/mandiant/capa-rules/blob/master/linking/static/polarssl/linked-against-polarsslmbed-tls.yml)|Crypto Library (C0059)|--|
|[linked against wolfSSL](https://github.com/mandiant/capa-rules/blob/master/linking/static/wolfssl/linked-against-wolfssl.yml)|Crypto Library (C0059)|--|
