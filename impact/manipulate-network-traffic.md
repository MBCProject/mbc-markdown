<table>
<tr>
<td><b>ID</b></td>
<td><b>B0019</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../impact">Impact</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Data Manipulation: Transmitted Data Manipulation (<a href="https://attack.mitre.org/techniques/T1565/002/">T1565.002</a>)</b></td>
</tr>
<tr>
<td><b>Impact Type</b></td>
<td><b>Integrity</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>31 October 2022</b></td>
</tr>
</table>


Manipulate Network Traffic
==========================
Malware intercepts and manipulates network traffic, typically accessing or modifying data, going to or originating from the system on which the malware instance is executing. Also known as a Man-in-the-Middle attack.

The related **Data Manipulation: Transmitted Data Manipulation ([T1565.002](https://attack.mitre.org/techniques/T1565/002/))** ATT&CK sub-technique was defined subsequent to this MBC behavior.

## Use in Malware

|Name|Date|Description|
|---|---|---|
|[**SearchAwesome**](../xample-malware/searchawesome.md)|2018|Intercepts encrypted web traffic to inject adds. [[1]](#1)|
|[**MazarBot**](../xample-malware/mazarbot.md)|2016|Intercepts data coming into and going out of device.|

## References

<a name="1">[1]</a> https://blog.malwarebytes.com/threat-analysis/2018/10/mac-malware-intercepts-encrypted-web-traffic-for-ad-injection/
