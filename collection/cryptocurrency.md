<table>
<tr>
<td><b>ID</b></td>
<td><b>B0028</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../collection">Collection</a>, <a href="../credential-access">Credential Access</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.1</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>14 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>3 June 2023</b></td>
</tr>
</table>


# Cryptocurrency

Malware accesses files that contain sensitive data or credentials related to Bitcoin and other cryptocurrency wallets.

## Methods

|Name|ID|Description|
|---|---|---|
|**Bitcoin**|B0028.001|Access Bitcoin data.|
|**Ethereum**|B0028.002|Access Ethereum data.|
|**Zcash**|B0028.003|Access Zcash data.|

## Use in Malware
|Name|Date|Method|Description|
|---|---|---|---|
|[**ElectroRAT**](../xample-malware/electrorat.md)|2023|--|ElectroRAT compromises multiple currencies, including Monaro, Doegecoin, Ethereum, Litecoin, and Bitcoin. [[1]](#1)|

## References
<a name="1">[1]</a> https://www.intezer.com/blog/research/operation-electrorat-attacker-creates-fake-companies-to-drain-your-crypto-wallets/