<table>
<tr>
<td><b>ID</b></td>
<td><b>C0030</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../data">Data</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.1</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>13 October 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>30 April 2024</b></td>
</tr>
</table>


# Non-Cryptographic Hash

Malware may use a non-cryptographic hash. 

## Methods

|Name|ID|Description|
|---|---|---|
|**dhash**|C0030.004|Malware uses the dhash hash function.|
|**Fast-Hash**|C0030.003|Malware uses the Fast-Hash hash function.|
|**FNV**|C0030.005|Malware uses the FNV hash function.|
|**MurmurHash**|C0030.001|Malware uses the MurmurHash hash function.|
|**pHash**|C0030.002|Malware uses the pHash hash function.|
|**djb2**|C0030.006|Malware uses the djb2 hash function.|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[hash data using murmur3](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/hashing/murmur/hash-data-using-murmur3.yml)|Non-Cryptographic Hash::MurmurHash (C0030.001)|--|
|[hash data using fnv](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/hashing/fnv/hash-data-using-fnv.yml)|Non-Cryptographic Hash::FNV (C0030.005)|_allmul|
|[hash data using djb2](https://github.com/mandiant/capa-rules/blob/master/data-manipulation/hashing/djb2/hash-data-using-djb2.yml)|Non-Cryptographic Hash::djb2 (C0030.006)|--|


### C0030.005 Snippet
<details>
<summary> Data::Non-Cryptographic Hash::FNV </summary>
SHA256: 0b8e662e7e595ef56396a298c367b74721d66591d856e8a8241fcdd60d08373c
Location: 0x403454
<pre>
mov     esi, dword ptr [ebp + param_2]  ; set number of bytes to hash
mov     edx, 0x811c9dc5 ; store FNV offset constant.  The constants used in this snippet are the constants used for a 32-bit/4 byte message.
push    edi     ; save the value of edi on the stack
mov     edi, dword ptr [ebp + param_1]  ; first byte to hash
mov     ecx, 0x0        ; initialize counter
sub     esi, edi        ; obtain the offset between first and last bytes to hash
jz      LAB_00403481    ; if the first and last bytes of the hash are the same, execute elsewhere and don't perform the hashing operation.
nop     dword ptr [eax]
movzx   eax, byte ptr [ecx + edi*0x1]   ; move the byte to hash into the accumulator
inc     ecx     ; increment the counter
xor     eax, edx        ; xor the new value in the accumulator with the rest of the hash (for first xor, this will be the offset constant set earlier) and store the result in the accumulator.  The xor occurring before the multiplication indicates that this is the FNV-1a variant of the algorithm
imul    edx, eax, 0x1000193     ; multiply the accumulator by the prime constant and store in edx for xor operation in next iteration
cmp     ecx, esi        ; check if counter has reached offset (hashed last byte)
jc      LAB_00403470    ; if the counter has not yet reached the offset, jump back to the movzx instruction above
</pre>
</details>
