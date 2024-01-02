<table>
<tr>
<td><b>ID</b></td>
<td><b>B0022</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../impact">Impact</a>, <a href="../persistence">Persistence</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
<tr>
<td><b>Impact Type</b></td>
<td><b>Breach</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.1</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>5 December 2023</b></td>
</tr>
</table>


# Remote Access

Malware may provide an attacker with potentially full access to a system via a remote network connection, which may also provide persistence.

A RAT (Remote Access Trojan) is an example of malware that provides a degree of remote access. If the malware provides an "execute" command, the attacker may choose to delete files or corrupt data, power-off the machine, or upload and execute other applications. The malware may also provide specific commands to the attacker (e.g., Delete File). Explicit commands provided by the malware can be captured with Methods associated with the **Execution::Remote Commands ([B0011](../execution/remote-commands.md))** behavior; examples include *Execution:Remote Commands:Execute* and *Execution:Remote Commands:Delete File*.

Note that the **Ingress Tool Transfer ([T1105](https://attack.mitre.org/techniques/T1105/))** technique defined under the Command and Control tactic is no longer specific to "legitimate desktop support and remote access software” as it was under a previous version of ATT&CK. However, *Ingress Tool Transfer* relates only to files copied; this MBC behavior is broader, allowing for remote access behaviors beyond file transfers (i.e., *Impact:Remote Access* and *Command and Control: Ingress Tool Transfer* are not equivalent).

## Methods

|Name|ID|Description|
|---|---|---|
|**Reverse Shell**|B0022.001|Malware may create a reverse shell. For example, malware can invoke cmd.exe and create three pipes (stdin, stdout, stderr) to forward data between cmd.exe and an adversary.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Poison Ivy**](../xample-malware/poison-ivy.md)|2005|--|After the Poison Ivy server is running on the target machine, the attacker can use a Windows GUI client to control the target computer. [[2]](#2)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|--|Dark Comet allows an attacker to control the system via a GUI. [[3]](#3)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|The malware acts as a backdoor. [[4]](#4)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[create reverse shell on Linux](https://github.com/mandiant/capa-rules/blob/master/communication/c2/shell/create-reverse-shell-on-linux.yml)|Remote Access::Reverse Shell (B0022.001)|--|
|[create reverse shell](https://github.com/mandiant/capa-rules/blob/master/communication/c2/shell/create-reverse-shell.yml)|Remote Access::Reverse Shell (B0022.001)|kernel32.PeekNamedPipe, kernel32.CreateProcess, kernel32.ReadFile, kernel32.WriteFile|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[persistence_rdp_registry](https://github.com/CAPESandbox/community/tree/master/modules/signatures/persistence_rdp_registry.py)|Remote Access (B0022)|--|
|[rat_spynet](https://github.com/CAPESandbox/community/tree/master/modules/signatures/rat_spynet.py)|Remote Access (B0022)|--|
|[parallax_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/parallax_mutexes.py)|Remote Access (B0022)|--|
|[rat_pcclient](https://github.com/CAPESandbox/community/tree/master/modules/signatures/rat_pcclient.py)|Remote Access (B0022)|--|
|[rat_fynloski_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/rat_fynloski_mutexes.py)|Remote Access (B0022)|--|
|[rat_beebus_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/rat_beebus_mutexes.py)|Remote Access (B0022)|--|
|[xpertrat_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/xpertrat_files.py)|Remote Access (B0022)|--|
|[xpertrat_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/xpertrat_mutexes.py)|Remote Access (B0022)|--|
|[warzonerat_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/warzonerat_files.py)|Remote Access (B0022)|--|
|[warzonerat_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/warzonerat_regkeys.py)|Remote Access (B0022)|--|
|[evil_grab](https://github.com/kevoreilly/CAPEv2/blob/master/modules/signatures/CAPE.py)|Remote Access (B0022)|RegCreateKeyExA, RegSetValueExA, RegCreateKeyExW, RegSetValueExW|
|[PlugX](https://github.com/kevoreilly/CAPEv2/blob/master/modules/signatures/CAPE.py)|Remote Access (B0022)|memcpy, RtlDecompressBuffer|
|[ratsnif_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/ratsnif_mutexes.py)|Remote Access (B0022)|--|
|[netwire_behavior](https://github.com/CAPESandbox/community/tree/master/modules/signatures/netwire_behavior.py)|Remote Access (B0022)|RegSetValueExA|
|[njrat_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/njrat_regkeys.py)|Remote Access (B0022)|--|
|[rat_xtreme_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/rat_xtreme_mutexes.py)|Remote Access (B0022)|--|
|[blackrat_apis](https://github.com/CAPESandbox/community/tree/master/modules/signatures/blackrat_apis.py)|Remote Access (B0022)|CryptHashData, RtlDecompressBuffer, CreateProcessInternalW|
|[blackrat_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/blackrat_mutexes.py)|Remote Access (B0022)|--|
|[blackrat_network_activity](https://github.com/CAPESandbox/community/tree/master/modules/signatures/blackrat_network_activity.py)|Remote Access (B0022)|send|
|[blackrat_registry_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/blackrat_registry_keys.py)|Remote Access (B0022)|RegQueryValueExW, RegSetValueExW|
|[uses_rdp_clip](https://github.com/CAPESandbox/community/tree/master/modules/signatures/uses_rdp_clip.py)|Remote Access (B0022)|--|
|[uses_remote_desktop_session](https://github.com/CAPESandbox/community/tree/master/modules/signatures/uses_remote_desktop_session.py)|Remote Access (B0022)|--|
|[rat_plugx_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/rat_plugx_mutexes.py)|Remote Access (B0022)|--|
|[obliquerat_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/obliquerat_files.py)|Remote Access (B0022)|--|
|[obliquerat_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/obliquerat_mutexes.py)|Remote Access (B0022)|--|
|[obliquerat_network_activity](https://github.com/CAPESandbox/community/tree/master/modules/signatures/obliquerat_network_activity.py)|Remote Access (B0022)|send|
|[venomrat_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/venomrat_mutexes.py)|Remote Access (B0022)|--|
|[trochilusrat_apis](https://github.com/CAPESandbox/community/tree/master/modules/signatures/trochilusrat_apis.py)|Remote Access (B0022)|OutputDebugStringW, NtCreateUserProcess, RegSetValueExW, CreateProcessInternalW|
|[dcrat_behavior](https://github.com/CAPESandbox/community/tree/master/modules/signatures/dcrat_behavior.py)|Remote Access (B0022)|GetAddrInfo, GetAddrInfoW, CryptHashData|
|[dcrat_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/dcrat_files.py)|Remote Access (B0022)|--|
|[dcrat_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/dcrat_mutexes.py)|Remote Access (B0022)|--|
|[karagany_system_event_objects](https://github.com/CAPESandbox/community/tree/master/modules/signatures/karagany_system_event_objects.py)|Remote Access (B0022)|NtCreateEventEx, NtCreateEvent|
|[karagany_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/karagany_files.py)|Remote Access (B0022)|--|
|[orcusrat_behavior](https://github.com/CAPESandbox/community/tree/master/modules/signatures/orcusrat_behavior.py)|Remote Access (B0022)|RegOpenKeyExW|
|[limerat_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/limerat_mutexes.py)|Remote Access (B0022)|--|
|[limerat_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/limerat_regkeys.py)|Remote Access (B0022)|--|
|[rat_luminosity](https://github.com/CAPESandbox/community/tree/master/modules/signatures/rat_luminosity.py)|Remote Access (B0022)|CryptHashData, NtCreateMutant, NtCreateFile|
|[rat_nanocore](https://github.com/CAPESandbox/community/tree/master/modules/signatures/rat_nanocore.py)|Remote Access (B0022)|CryptHashData|
|[static_rat_config](https://github.com/CAPESandbox/community/tree/master/modules/signatures/static_rat_config.py)|Remote Access (B0022)|--|
|[remcos_files](https://github.com/CAPESandbox/community/tree/master/modules/signatures/remcos_files.py)|Remote Access (B0022)|--|
|[remcos_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/remcos_mutexes.py)|Remote Access (B0022)|--|
|[remcos_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/remcos_regkeys.py)|Remote Access (B0022)|--|

## References

<a name="1">[1]</a> https://en.wikipedia.org/wiki/Remote_access_trojan

<a name="2">[2]</a> https://www.cyber.nj.gov/threat-center/threat-profiles/trojan-variants/poison-ivy

<a name="3">[3]</a> https://en.wikipedia.org/wiki/DarkComet

<a name="4">[4]</a> https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/HUPIGON

