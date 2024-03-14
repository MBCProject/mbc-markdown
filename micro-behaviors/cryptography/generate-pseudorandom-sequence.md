<table>
<tr>
<td><b>ID</b></td>
<td><b>C0021</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../cryptography">Cryptography</a></b></td>
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
<td><b>14 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>5 December 2023</b></td>
</tr>
</table>


# Generate Pseudo-random Sequence

The Generate Pseudo-random Sequence micro-behavior can be used for a number of purposes. The methods below include specific functions, as well as pseudo-random number generators (PRNG).

## Methods

|Name|ID|Description|
|---|---|---|
|**GetTickCount**|C0021.001|Malware generates a pseudo-random sequence using GetTickCount.|
|**Use API**|C0021.003|Malware generates a pseudo-random sequence using a Windows API.|
|**rand**|C0021.002|Malware generates a pseudo-random sequence using rand.|
|**RC4 PRGA**|C0021.004|Malware generates a pseudo-random sequence using the RC4 Pseudo Random (Byte) Generation Algorithm (PRGA).|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|C0021.003|BlackEnergy generates random numbers via WinAPI. [[1]](#1)|
|[**Locky Bart**](../xample-malware/locky-bart.md)|2017|C0021.003|Generate random numbers via WinAPI (This capa rule had 1 match) [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[encrypt data using RC4 PRGA](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/encryption/rc4/encrypt-data-using-rc4-prga.yml)|Generate Pseudo-random Sequence::RC4 PRGA (C0021.004)|--|
|[generate random numbers via WinAPI](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/prng/generate-random-numbers-via-winapi.yml)|Generate Pseudo-random Sequence::Use API (C0021.003)|BCryptGenRandom, CryptGenRandom, BCryptOpenAlgorithmProvider, BCryptCloseAlgorithmProvider, CryptAquireContext|
|[generate random numbers via RtlGenRandom](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/prng/generate-random-numbers-via-rtlgenrandom.yml)|Generate Pseudo-random Sequence::Use API (C0021.003)|SystemFunction036|
|[generate random numbers using a Mersenne Twister](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/prng/mersenne/generate-random-numbers-using-a-mersenne-twister.yml)|Generate Pseudo-random Sequence (C0021)|--|

### C0021 Snippet
<details>
<summary> Cryptography::Generate Pseudo-random Sequence </summary>
SHA256: 192cdcbdec8bdebb7cae89037d6004b4aff2b8264c35a3875fa2d6db104437ca
Location: 0x40B120
<pre>
mov     eax, [DAT_00423174]     ; set up the array of values used for the twister
mov     ecx, dword ptr [eax*0x4 + DAT_004227b0]
mov     dword ptr [EBP + local_8], ecx
mov     edx, dword ptr [DAT_00423174]
add     edx, 0x1
mov     dword ptr [DAT_OO423174], edx
mov     eax, dword ptr [ebp + local_8]  ; set up by taking x (value in series to start the transform, stored at the memory address [ebp + local_8] in this case
shr     eax, 0xb        ; shift x right by 11
xor     eax, dword ptr [ebp + local_8]  ; xor the result of the previous operation with the old value of x.  The eax register now contains intermediate value y
mov     dword ptr [ebp + local_8], eax  ; store the value of y
mov     ecx, dword ptr [ebp + local_8]  ; ecx now contains y
shl     ecx, 0x7        ; shift y left by 7
and     ecx, 0x9d2c5680 ; perform a bitwise and against a known constant bitmask (this value is specified in the transform equation)
xor     ecx, dword ptr [ebp + local_8]  ; xor the output of the previous two instructions with the old value of y to produce y1 (still an intermediate value)
mov     dword ptr [ebp + local_8], ecx  ; store y1
mov     edx, dword ptr [ebp + local_8]  ; load  y1 into edx to start the third part of the transform
shl     edx, 0xf        ; shift y1 left by 15
and     edx, 0xefc60000 ; take y1 and perform a bitwise and operation with another constant
xor     edx, dword ptr [ebp + local_8]  ; xor the output from the previous two instructions with the value of y1 stored earlier
mov     dword ptr [ebp + local_8], edx  ; save this new intermediate y-value (y2)
mov     eax, dword ptr [ebp + local_8]  ; load y2 into eax to start the final portion of the transform and produce the output
shr     eax, 0x12       ; shift y2 right by 18
xor     eax, dword ptr [ebp + local_8]  ; xor the output from the previous instruction with the value of y2 stored earlier
mov     dword ptr [ebp + local_8], eax  ; store the z-value (final output)
mov     eax, dword ptr [ebp + local_8]  ; load the z-value into eax to return it
mov     esp, ebp        ; move the stack pointer to the frame pointer
pop     ebp     ; pop the current frame off the stack
ret     ; return from the function
</pre>
</details>

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

