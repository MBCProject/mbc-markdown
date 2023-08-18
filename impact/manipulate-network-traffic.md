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
<td><b>01 May 2023</b></td>
</tr>
</table>


# Manipulate Network Traffic

Malware intercepts and manipulates network traffic, typically accessing or modifying data, going to or originating from the system on which the malware instance is executing. This is also known as a Man-in-the-Middle(MIM) attack. This manipulation is reflected by activities such as data theft (e.g., credential harvesting) and injection of unwanted ads into websites. The former can be accomplished through installation of a fraudulent certificate, enabling interception of encrypted or unencrypted data. Malicious code executed in a MIM attack has also been credited with strategic redirection of web traffic, manipulation of a victim’s browsing experience, and code injection [[1]] (#1). 

The related **Data Manipulation: Transmitted Data Manipulation ([T1565.002](https://attack.mitre.org/techniques/T1565/002/))** ATT&CK sub-technique was defined subsequent to this MBC behavior.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**SearchAwesome**](../xample-malware/searchawesome.md)|2018|--|SearchAwesome adware intercepts encrypted web traffic to inject ads. [[2]](#2)|
|[**MazarBot**](../xample-malware/mazarbot.md)|2016|--|MazarBot intercepts data coming into and going out of the device. [[3]](#3)|


## References
<a name="1">[1]</a> B. Feeley and B. Stone-Gross,"New Evidence Proves Ongoing WIZARD SPIDER / LUNAR SPIDER Collaboration," CrowdStrike, blog, 20 Mar. 2019. [Online]. Available: https://www.crowdstrike.com/blog/wizard-spider-lunar-spider-shared-proxy-module. 

<a name="2">[2]</a> https://blog.malwarebytes.com/threat-analysis/2018/10/mac-malware-intercepts-encrypted-web-traffic-for-ad-injection/

<a name="3">[3]</a> https://us.norton.com/internetsecurity-emerging-threats-mazar-bot-malware-invades-and-erases-android-devices.html
