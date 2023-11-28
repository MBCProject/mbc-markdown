<table>
<tr>
<td><b>ID</b></td>
<td><b>C0011</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../communication">Communication</a></b></td>
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
<td><b>14 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>13 September 2023</b></td>
</tr>
</table>


# DNS Communication

The DNS Communication micro-behavior focuses on DNS communication. 

## Methods

|Name|ID|Description|
|---|---|---|
|**DDNS Domain Connect**|C0011.003|Connects to dynamic DNS domain.|
|**Resolve**|C0011.001|Resolves a domain.|
|**Resolve Free Hosting Domain**|C0011.005|Resolves a free hosting domain (e.g., freeiz.com).|
|**Resolve TLD**|C0011.004|Resolves top level domain.|
|**Server Connect**|C0011.002|Connects to DNS server.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|C0011.001|Hupigon resolves DNS. [[1]](#1)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|C0011.001|Shamoon resolves DNS. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[reference DNS over HTTPS endpoints](https://github.com/mandiant/capa-rules/blob/master/communication/dns/reference-dns-over-https-endpoints.yml)|DNS Communication::Server Connect (C0011.002)|--|
|[resolve DNS](https://github.com/mandiant/capa-rules/blob/master/communication/dns/resolve-dns.yml)|DNS Communication::Resolve (C0011.001)|ws2_32.gethostbyname, DnsQuery_A, DnsQuery_W, DnsQuery_UTF8, DnsQueryEx, getaddrinfo, GetAddrInfo, GetAddrInfoEx, gethostbyname, getaddrinfo, getnameinfo, gethostent, System.Net.Dns::GetHostAddresses|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[network_dns_blockchain](https://github.com/CAPESandbox/community/tree/master/modules/signatures/network_dns_blockchain.py)|DNS Communication (C0011)|--|
|[network_dns_idn](https://github.com/CAPESandbox/community/tree/master/modules/signatures/network_dns_idn.py)|DNS Communication (C0011)|DnsQueryA|
|[network_dns_opennic](https://github.com/CAPESandbox/community/tree/master/modules/signatures/network_dns_opennic.py)|DNS Communication (C0011)|--|
|[network_dns_reverse_proxy](https://github.com/CAPESandbox/community/tree/master/modules/signatures/network_dns_reverse_proxy.py)|DNS Communication (C0011)|--|
|[network_dns_suspicious_querytype](https://github.com/CAPESandbox/community/tree/master/modules/signatures/network_dns_suspicious_querytype.py)|DNS Communication (C0011)|DnsQueryA|
|[network_dns_tunneling_request](https://github.com/CAPESandbox/community/tree/master/modules/signatures/network_dns_tunneling_request.py)|DNS Communication (C0011)|DnsQuery_A, DnsQuery_W|
|[network_dns_doh_tls](https://github.com/CAPESandbox/community/tree/master/modules/signatures/network_dns_doh_tls.py)|DNS Communication (C0011)|--|
|[network_dga](https://github.com/CAPESandbox/community/tree/master/modules/signatures/network_dga.py)|DNS Communication (C0011)|--|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

