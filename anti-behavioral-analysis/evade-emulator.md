|||
|---------|------------------------|
|**ID**|**M0005**|
|**Objective(s)**|[Anti-Behavioral Analysis](https://github.com/MAECProject/malware-behaviors/tree/master/anti-behavioral-analysis)|
|**Related ATT&CK Technique(s)**|None|

Emulator Evasion
================
Behaviors that obstruct analysis in an emulator.

Methods
-------
* **Different Opcode Sets**: Use different opcodes sets (ex: FPU, MMX, SSE) to block emulators.
* **Undocumented Opcodes**: Use rare or undocumented opcodes to block non-exhaustive emulators.
* **Unusual/Undocumented API Calls**: Call unusual APIs to block non-exhaustive emulators (particularly anti-virus).
* **Extra Loops/Time Locks**: Add extra loops to make time-constraint emulators give up.


