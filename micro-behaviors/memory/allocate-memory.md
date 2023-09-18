<table>
<tr>
<td><b>ID</b></td>
<td><b>C0007</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../memory">Memory</a></b></td>
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
<td><b>1 March 2023</b></td>
</tr>
</table>


# Allocate Memory

Malware allocates memory, often to unpack itself. 

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**CryptoLocker**](../xample-malware/cryptolocker.md)|2013|--|CryptoLocker allocates RWX memory. [[1]](#1)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|--|Dark Comet allocates RWX memory. [[1]](#1)|
|[**DNSChanger**](../xample-malware/dnschanger.md)|2011|--|DNSChanger allocates RWX memory. [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Hupigon allocates RWX memory. [[1]](#1)|
|[**Mebromi**](../xample-malware/mebromi.md)|2011|--|Mebromi allocates RWX memory. [[1]](#1)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|--|Redhip spawns threads to RWX shellcode. [[1]](#1)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|--|Rombertik allocates RWX memory. [[1]](#1)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|--|Stuxnet allocates RWX memory. [[1]](#1)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|--|TrickBot allocates RWX memory. [[1]](#1)|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

