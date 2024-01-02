<table>
<tr>
<td><b>ID</b></td>
<td><b>B0047</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../defense-evasion">Defense Evasion</a>, <a href="../persistence">Persistence</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>3.1</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>13 December 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>5 December 2023</b></td>
</tr>
</table>


# Install Insecure or Malicious Configuration

Malware may install malicious configuration settings or may modify existing configuration settings. For example, malware may change configuration settings associated with security mechanisms to make it difficult to detect or change configuration settings to maintain a foothold on the network.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Black Energy**](../xample-malware/blackenergy.md)|2007|--|Malware configures the system to the TESTSIGNING boot configuration option to load its unsigned driver component. [[1]](#1)|
|[**YiSpecter**](../xample-malware/yispecter.md)|2015|--|The malware changes iOS Safari's default configuration. [[2]](#2)|

## Detection

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[bcdedit_command](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bcdedit_command.py)|Install Insecure or Malicious Configuration (B0047)|ShellExecuteExW, NtCreateUserProcess, CreateProcessInternalW|
|[stealth_hidden_extension](https://github.com/CAPESandbox/community/tree/master/modules/signatures/stealth_hidden_extension.py)|Install Insecure or Malicious Configuration (B0047)|--|
|[stealth_hiddenreg](https://github.com/CAPESandbox/community/tree/master/modules/signatures/stealth_hiddenreg.py)|Install Insecure or Malicious Configuration (B0047)|--|
|[stealth_hide_notifications](https://github.com/CAPESandbox/community/tree/master/modules/signatures/stealth_hide_notifications.py)|Install Insecure or Malicious Configuration (B0047)|--|
|[disables_app_launch](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_app_launch.py)|Install Insecure or Malicious Configuration (B0047)|--|
|[modify_hostfile](https://github.com/CAPESandbox/community/tree/master/modules/signatures/modify_hostfile.py)|Install Insecure or Malicious Configuration (B0047)|--|
|[antiav_srp](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antiav_srp.py)|Install Insecure or Malicious Configuration (B0047)|--|
|[bypass_firewall](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bypass_firewall.py)|Install Insecure or Malicious Configuration (B0047)|--|

## References

<a name="1">[1]</a> https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf

<a name="2">[2]</a> https://unit42.paloaltonetworks.com/yispecter-first-ios-malware-attacks-non-jailbroken-ios-devices-by-abusing-private-apis/
