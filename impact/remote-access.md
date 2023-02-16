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
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>21 November 2022</b></td>
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
|[**Poison-Ivy**](../xample-malware/poison-ivy.md)|2005|--|After the Poison-Ivy server is running on the target machine, the attacker can use a Windows GUI client to control the target computer. [[2]](#2)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|--|Dark Comet allows an attacker to control the system via a GUI. [[3]](#3)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|The malware acts as a backdoor. [[4]](#4)|


## References

<a name="1">[1]</a> https://en.wikipedia.org/wiki/Remote_access_trojan

<a name="2">[2]</a> https://www.cyber.nj.gov/threat-profiles/trojan-variants/poison-ivy

<a name="3">[3]</a> https://en.wikipedia.org/wiki/DarkComet

<a name="4">[4]</a> https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/HUPIGON

