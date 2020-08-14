|||
|---------|------------------------|
|**ID**|**B0005**|
|**Objective(s)**|[Anti-Behavioral Analysis](https://github.com/MBCProject/mbc-beta/tree/master/anti-behavioral-analysis)|
|**Related ATT&CK Technique**|None|

Emulator Evasion
================
Behaviors that obstruct analysis in an emulator.

Methods
-------
|ID|Name|Description|
|-----------------------------|--------|-----------------------------|
|B0005.001|**Different Opcode Sets**|Use different opcodes sets (ex: FPU, MMX, SSE) to block emulators.|
|B0005.002|**Undocumented Opcodes**|Use rare or undocumented opcodes to block non-exhaustive emulators.|
|B0005.003|**Unusual/Undocumented API Calls**|Call unusual APIs to block non-exhaustive emulators (particularly anti-virus).|
|B0005.004|**Extra Loops/Time Locks**|Add extra loops to make time-constraint emulators give up.|

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|-----------|-----------------------------|
|[**WebCobra**](https://github.com/MBCProject/mbc-beta/blob/master/xample-malware/webcobra.md)|2018|Evades emulator-based analysis.)|