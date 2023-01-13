<table>
<tr>
<td><b>ID</b></td>
<td><b>E1204</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../execution">Execution</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>User Execution (<a href="https://attack.mitre.org/techniques/T1204">T1204</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>28 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>21 November 2022</b></td>
</tr>
</table>


# User Execution

Malware may include code that relies on specific actions by a user to execute. Note that this MBC behavior differs from [User Execution](https://attack.mitre.org/techniques/T1204) in that it does do not include direct code execution (user action for *initial* execution) - MBC does not encompass ATT&CK's Initial Access Tactic.  

See ATT&CK Technique: **User Execution ([T1204](https://attack.mitre.org/techniques/T1204/))**.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|E1204| GoBotKR makes their malware look like the torrent content that the user intended to download, in order to entice a user to click on it. [[1]](#1)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|E1204|The malware relies on a victim to execute itself [[2]](#2)|
|[**Terminator**](../xample-malware/terminator.md)|2013|E1204|The malware relies on user interaction to execute [[3]](#3)|
|[**CryptoLocker**](../xample-malware/cryptolocker.md)|2013|E1204|The malware relies on victims to execute [[5]](#5)|
|[**SearchAwesome**](../xample-malware/searchawesome.md)|2018|E1204|A user must execute the malicious program. [[4]](#4)|

## References

<a name="1">[1]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="2">[2]</a> https://blogs.cisco.com/security/talos/rombertik

<a name="3">[3]</a> https://www.mandiant.com/resources/hot-knives-through-butter-evading-file-based-sandboxes

<a name="4">[4]</a> https://blog.malwarebytes.com/threat-analysis/2018/10/mac-malware-intercepts-encrypted-web-traffic-for-ad-injection/

<a name="5">[5]</a> https://www.secureworks.com/research/cryptolocker-ransomware

