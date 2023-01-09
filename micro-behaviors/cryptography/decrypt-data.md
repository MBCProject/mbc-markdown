<table>
<tr>
<td><b>ID</b></td>
<td><b>C0031</b></td>
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
<td><b>13 October 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>31 October 2022</b></td>
</tr>
</table>


# Decrypt Data

Malware may decrypt data. 

## Methods

|Name|ID|Description|
|---|---|---|
|**AES**|C0031.001|Malware decrypts data encrypted with the AES algorithm.|
|**Block Cipher**|C0031.002|Malware decrypts data encrypted with a block cipher.|
|**Blowfish**|C0031.003|Malware decrypts data encrypted with the Blowfish algorithm.|
|**Camellia**|C0031.004|Malware decrypts data encrypted with the Camellia algorithm.|
|**3DES**|C0031.005|Malware decrypts data encrypted with the 3DES algorithm.|
|**HC-128**|C0031.006|Malware decrypts data encrypted with the HC-128 algorithm.|
|**HC-256**|C0031.007|Malware decrypts data encrypted with the HC-256 algorithm.|
|**RC4**|C0031.008|Malware decrypts data encrypted with the RC4 algorithm.|
|**RC6**|C0031.009|Malware decrypts data encrypted with the RC6 algorithm.|
|**RSA**|C0031.010|Malware decrypts data encrypted with the RSA algorithm.|
|**Skipjack**|C0031.011|Malware decrypts data encrypted with the Skipjack block cipher algorithm.|
|**Sosemanuk**|C0031.012|Malware decrypts data encrypted with the Sosemanuk stream cipher.|
|**Stream Cipher**|C0031.013|Malware decrypts data encrypted with a stream cipher.|
|**Twofish**|C0031.014|Malware decrypts data encrypted with the Twofish algorithm.|


## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|C0031|Encrypt or decrypt via WinCrypt (This capa rule had 1 match) [[1]](#1)|
|[**Kovter**](../xample-malware/kovter.md)|2016|C0031|Encrypt or decrypt via WinCrypt (This capa rule had 1 match) [[1]](#1)|

## Code Snippets

### C0031
<details>
<summary> Decrypt Data </summary>
SHA256: c86cbf5e78c9f05ecfc11e4f2c147781cef77842a457e19ba690477eb564c22b
<pre>
asm
push    ebx
mov     ebx, [esp+4+arg_4]
push    esi
lea     eax, [ebx+20h]
push    eax             ; unsigned int
call    ??2@YAPAXI@Z    ; operator new(uint)
mov     ecx, [esp+0Ch+arg_C]
mov     edx, eax
add     esp, 4
mov     esi, [ecx]
mov     [edx], esi
mov     esi, [ecx+4]
mov     [edx+4], esi
mov     ecx, [ecx+8]
mov     [edx+8], ecx
mov     edx, [esp+8+arg_8]
test    ebx, ebx
mov     [eax+0Ch], edx
jle     short loc_B
mov     esi, [esp+8+arg_0]
push    edi
mov     edi, 0FFFFFFFDh
lea     edx, [eax+3]
sub     edi, eax

loc_A:
mov     cl, [edx-3]
xor     cl, [edx+2]
xor     cl, [edx-1]
xor     cl, [edx]
mov     [edx+0Dh], cl
xor     [esi], cl
inc     edx
inc     esi
lea     ecx, [edi+edx]
cmp     ecx, ebx
jl      short loc_A
pop     edi

loc_B:
push    eax             ; void *
call    ??3@YAXPAX@Z    ; operator delete(void *)
add     esp, 4
mov     eax, 1
pop     esi
pop     ebx
retn

</pre>

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

