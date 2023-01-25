<table>
<tr>
<td><b>ID</b></td>
<td><b>B0004</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../anti-behavioral-analysis">Anti-Behavioral Analysis</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
<tr>
<td><b>Anti-Analysis Type</b></td>
<td><b>Detection</b></td>
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


# Emulator Detection

Detects whether the malware instance is being executed inside an emulator. If so, conditional execution selects a benign execution path.

## Methods

|Name|ID|Description|
|---|---|---|
|**Check Emulator-related Registry Keys**|B0004.003|Emulators register artifacts in the registry, which can be detected by malware. For example, installation of QEMU results in the registry key: *HARDWARE\DEVICEMAP\Scsi\Scsi Port 0\Scsi Bus 0\Target Id 0\Logical Unit Id 0* with value=*Identifier* and data=*QEMU*, or registry key: *HARDWARE\Description\System* with value=*SystemBiosVersion* and data=*QEMU*. [[1]](#1)|
|**Check for Emulator-related Files**|B0004.001|Checks whether particular files (e.g., QEMU files) exist.|
|**Check for WINE Version**|B0004.002|Checks for WINE via the `get_wine_version` function from WINE's `ntdll.dll`.|
|**Failed Network Connections**|B0004.004|Some emulated systems fail to handle some network communications; such failures will indicate the emulated environment.|

## Detection
|Tool: capa|Mapping|APIs|
|---|---|---|
|[check if process is running under wine](https://github.com/mandiant/capa-rules/blob/master/anti-analysis/anti-emulation/wine/check-if-process-is-running-under-wine.yml)|Emulator Detection (B0007)|GetModuleHandle, GetProcAddress|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|--|Stuxnet checks for specific operating systems on 32-bit machines, registry keys, and dates to profile a potential target machine before execution. If the conditions are not met to be considered a viable target, it will exit execution. [[2]](#2)|

## References

<a name="1">[1]</a> https://search.unprotect.it/map/sandbox-evasion/

<a name="2">[2]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en
