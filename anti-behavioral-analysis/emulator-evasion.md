<table>
<tr>
<td><b>ID</b></td>
<td><b>B0005</b></td>
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
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>4 March 2023</b></td>
</tr>
</table>


# Emulator Evasion

Behaviors that obstruct analysis in an emulator.

## Methods

|Name|ID|Description|
|---|---|---|
|**Different Opcode Sets**|B0005.001|Use different opcodes sets (ex: FPU, MMX, SSE) to block emulators.|
|**Extra Loops/Time Locks**|B0005.004|Add extra loops to make time-constraint emulators give up.|
|**Undocumented/Unimplemented Opcodes**|B0005.002|Use rare, undocumented, or unimplemented opcodes to block non-exhaustive emulators.|
|**Unusual/Undocumented API Calls**|B0005.003|Call unusual APIs to block non-exhaustive emulators (particularly anti-virus).|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**WebCobra**](../xample-malware/webcobra.md)|2018|B0005.004|The malware evades emulator-based analysis by using an infinite loop to check all open windows and compare each window's title bar to a list of strings. [[1]](#1)|

## References

<a name="1">[1]</a> https://www.mcafee.com/blogs/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/

