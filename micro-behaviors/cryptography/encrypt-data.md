<table>
<tr>
<td><b>ID</b></td>
<td><b>C0027</b></td>
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
<td><b>21 November 2022</b></td>
</tr>
</table>


# Encrypt Data

Malware may encrypt data. 

## Methods

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


## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**TrickBot**](../../xample-malware/trickbot.md)|2016|C0027.001|The malware uses an AES CBC (256 bits) encryption algorithm for its loader and configuration files. [[1]](#1)|
|[**Emotet**](../xample-malware/emotet.md)|2018|C0027.009|Emotet encrypts data using RC4 PRGA. [[8]](#8)|
|[**Emotet**](../../xample-malware/emotet.md)|2018|C0027.011|Emotet uses RSA to encrypt network traffic to its C2. [[2]](#2)|
|[**GravityRAT**](../../xample-malware/gravity-rat.md)|2018|C0027.001|GravityRat v3 supports file AES file encryption. [[3]](#3)|
|[**Poison-Ivy**](../../xample-malware/poison-ivy.md)|2005|C0027.003|Poison Ivy's custom network protocol over TCP is encrypted using Camellia cipher with a 256-bit key. [[4]](#4)|
|[**CHOPSTICK**](../xample-malware/chopstick.md)|2015|C0027.009|CHOPSTICK encrypts the configuration block using RC4 encryption. [[5]](#5)|
|[**Matanbuchus**](../xample-malware/matanbuchus.md)|2021|C0027.009|The malware decrypts inner configurations stored in the binary. The malware also encrypts the value of each JSON key with RC4 and encodes the value with Base64. [[6]](#6) [[7]](#7)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|C0027.009|BlackEnergy encrypts data using RC4 via WinAPI. [[8]](#8)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|C0027.009|Dark Comet encrypts data using RC4 PRGA. [[8]](#8)|
|[**DNSChanger**](../xample-malware/dnschanger.md)|2011|C0027.009|DNSChanger encrypts data using RC4 PRGA. [[8]](#8)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|C0027.004|Hupigon encrypts data using DES. [[8]](#8)|
|[**Kraken**](../xample-malware/kraken.md)|2008|C0027.009|Kraken encrypts data using RC4 PRGA. [[8]](#8)|
|[**Locky Bart**](../xample-malware/locky-bart.md)|2017|C0027.009|Locky Bart encrypts data using RC4 PRGA. [[8]](#8)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|--|Redhip encrypts data using DPAPI. [[8]](#8)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|C0027.009|Rombertik encrypts data using RC4 PRGA. [[8]](#8)|


## Code Snippets

### C0031
<details>
<summary> Encrypt Data </summary>
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
</details>


## References

<a name="1">[1]</a> https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf

<a name="2">[2]</a> https://documents.trendmicro.com/assets/white_papers/ExploringEmotetsActivities_Final.pdf

<a name="3">[3]</a> https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html

<a name="4">[4]</a> https://www.cyber.nj.gov/threat-center/threat-profiles/trojan-variants/poison-ivy

<a name="5">[5]</a> https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf

<a name="6">[6]</a> https://www.0ffset.net/reverse-engineering/matanbuchus-loader-analysis/

<a name="7">[7]</a> https://www.cyberark.com/resources/threat-research-blog/inside-matanbuchus-a-quirky-loader

<a name="8">[8]</a> capa v4.0, analyzed at MITRE on 10/12/2022
