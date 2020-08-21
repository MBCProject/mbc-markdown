|||
|---|---|
|**ID**|**B0005**|
|**Objective(s)**|[Anti-Behavioral Analysis](https://github.com/MBCProject/mbc-markdown/tree/master/anti-behavioral-analysis)|
|**Related ATT&CK Technique**|None|


Emulator Evasion
================
Behaviors that obstruct analysis in an emulator.

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Different Opcode Sets**|B0005.001|Use different opcodes sets (ex: FPU, MMX, SSE) to block emulators.|
|**Extra Loops/Time Locks**|B0005.004|Add extra loops to make time-constraint emulators give up.|
|**Undocumented Opcodes**|B0005.002|Use rare or undocumented opcodes to block non-exhaustive emulators.|
|**Unusual/Undocumented API Calls**|B0005.003|Call unusual APIs to block non-exhaustive emulators (particularly anti-virus).|

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**WebCobra**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/webcobra.md)|2018|Evades emulator-based analysis.)|
