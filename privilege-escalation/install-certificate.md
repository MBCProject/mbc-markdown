<table>
<tr>
<td><b>ID</b></td>
<td><b>F0016</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../privilege-escalation">Privilege Escalation</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Stage Capabilities: Install Digital Certificate (<a href="https://attack.mitre.org/techniques/T1608/003/">T1608.003</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.1</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>2 August 2022</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>10 February 2024</b></td>
</tr>
</table>


# Install Certificate

Malware may install a malicious or fraudulent certificate onto a victim's system. This can be used to facilitate a variety of attacks, such as man-in-the-middle attacks, where the attacker intercepts and potentially alters communication between two parties without their knowledge. By installing a certificate, the malware can trick the system into trusting it, allowing the attacker to bypass security measures, intercept sensitive data, or deliver additional malicious payloads. This technique can also be used to impersonate websites or services, tricking the user into revealing sensitive information.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**SearchAwesome**](../xample-malware/searchawesome.md)|2018|--|The malware installs a certificate. [[1]](#1)|

## References

<a name="1">[1]</a> https://www.malwarebytes.com/blog/news/2018/10/mac-malware-intercepts-encrypted-web-traffic-for-ad-injection

