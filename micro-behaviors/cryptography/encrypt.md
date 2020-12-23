|||
|---|---|
|**ID**|**C0027**|
|**Objective(s)**|[Cryptography](../cryptography)|
|**Related ATT&CK Technique**|None|


Encrypt Data
============
Malware may encrypt data. 

Methods
-------
|Name|ID|Description|
|---|---|---|
|**AES**|C0027.001|Malware encrypts with the AES algorithm.|
|**Block Cipher**|C0027.014|Malware encrypts with a block cipher.|
|**Blowfish**|C0027.002|Malware encrypts with the Blowfish algorithm.|
|**Camellia**|C0027.003|Malware encrypts with the Camellia algorithm.|
|**3DES**|C0027.004|Malware encrypts with the 3DES algorithm.|
|**HC-128**|C0027.006|Malware encrypts with the HC-128 algorithm.|
|**HC-256**|C0027.007|Malware encrypts with the HC-256 algorithm.|
|**RC4**|C0027.009|Malware encrypts with the RC4 algorithm.|
|**RC6**|C0027.010|Malware encrypts with the RC6 algorithm.|
|**RSA**|C0027.011|Malware encrypts with the RSA algorithm.|
|**Skipjack**|C0027.013|Malware encrypts with the Skipjack block cipher algorithm.|
|**Sosemanuk**|C0027.008|Malware encrypts with the Sosemanuk stream cipher.|
|**Stream Cipher**|C0027.012|Malware encrypts with a stream cipher.|
|**Twofish**|C0027.005|Malware encrypts with the Twofish algorithm.|

Code Snippets
-------------
**Encrypt Data** (C0031) - the snippet encrypts and decrypts data.

Sample (SHA256): c86cbf5e78c9f05ecfc11e4f2c147781cef77842a457e19ba690477eb564c22b

```asm
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
```