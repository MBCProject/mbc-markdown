|||
|---|---|
|**ID**|**B0032**|
|**Objective(s)**|[Anti-Static Analysis](../anti-static-analysis)|
|**Related ATT&CK Technique**|None|


Executable Code Obfuscation
===========================
Executable code can be obfuscated to hinder disassembly and static code analysis. This behavior is specific to a malware sample's executable code (data and text sections).

For encryption and encoding characteristics of malware samples, as well as malware obfuscation behaviors related to non-malware-sample files and information, see [**Obfuscated Files or Information**](../defense-evasion/obfuscate-files.md).

Methods
-------
|Name|ID|Description|
|---|---|---|
|**API Hashing**|B0032.001|Instead of storing function names in the Import Address Table (IAT) and calling GetProcAddress, a DLL is loaded and the name of each of its exports is hashed until it matches a specific hash. Manual symbol resolution is then used to access and execute the exported function. This method is often used by shellcode because it reduces the size of each import from a human-readable string to a sequence of four bytes. The Method is also known as "Imports by Hash" and "GET_APIS_WITH_CRC." [[1]](#1)|
|**Code Insertion**|B0032.002|Insert code to impede disassembly.|
|**Data Value Obfuscation**|B0032.008|Obfuscate data values through indirection of local or global variables. For example, the instruction *if (a == 0) do x* can be obfuscated by setting a global variable, *Z*, to zero and using it in the instruction: *if (a==Z) do x*.  [NEEDS REVIEW]|
|**Dead Code Insertion**|B0032.003|Include "dead" code with no real functionality.|
|**Entry Point Obfuscation**|B0032.009|Obfuscate the entry point of the malware executable.|
|**Fake Code Insertion**|B0032.004|Add fake code similar to known packers or known goods to fool identification. Can confuse some automated unpackers.|
|**Guard Pages**|B0032.010|Encrypt blocks of code individually and decrypt temporarily only upon execution.|
|**Import Address Table Obfuscation**|B0032.011|Obfuscate the import address table.|
|**Import Compression**|B0032.012|Store and load imports with a compact import table format. Each DLL needed by the executable is mentioned in the IAT, but only one function from each/most is imported; the rest are imported via GetProcAddress calls.|
|**Instruction Overlap**|B0032.013|Jump after the first byte of an instruction to confuse disassembler.|
|**Interleaving Code**|B0032.014|Split code into sections that may be rearranged and are connected by unconditional jumps.|
|**Jump Insertion**|B0032.005|Insert jumps to make analysis visually harder.|
|**Junk Code Insertion**|B0032.007|Insert dummy code between relevant opcodes. Can make signature writing more complex.|
|**Merged Code Sections**|B0032.015|Merge all sections resulting in just one entry in the sections table to make readability more difficult. May affect some detection signatures if written to be section dependent.|
|**Stack Strings**|B0032.017|Build and decrypt strings on the stack at each use, then discard to avoid obvious references.|
|**Structured Exception Handling (SEH)**|B0032.016|A portion of the code always generates an exception so that malicious code is executed with the exception handling. See  [[3]](#3).|
|**Symbol Obfuscation**|B0032.018|Remove or rename symbolic information commonly inserted by compilers for debugging purposes.|
|**Thunk Code Insertion**|B0032.006|Variation on Jump Insertion. Used by some compilers for user-generated functions.|
   

Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**Heriplor**](../xample-malware/heriplor.md)|March 2019|The Heriplor Trojan uses API Hashing. [[1]](#1)|
|[**Emotet**](../xample-malware/emotet.md)|2018|Emotet macros are heavily obfuscated with junk functions and string substitutions. [[2]](#2)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|Trojan spyware program that has mainly been used for targeting banking sites.|

Code Snippets
-------------
**Obfuscated Files or Information::Encoding-Standard Algorithm** (E1027.m02)
 <br/>MD5: b6e1a2048ea6bd6a941a72300b2d41ce
```asm
jle short_40182F
mov dl, byte ptr [ebp+eax+var_7CA8]
xor dl, cl
mov byte ptr [ebp+eax+var_7CA8], dl
inc eax
cmp eax, edi
jl short loc_40181A
```
**Executable Code Obfuscation::Stack Strings** (B0032.017)
 <br/>MD5: b6e1a2048ea6bd6a941a72300b2d41ce
```asm
mov cl, 65h ; 'e'
mov al, 70h ; 'p'
mov [ebp+var_23], cl
mov [ebp_var_1f], cl
mov [ebp_Str], bl
mov [ebp+var_12], bl
mov [ebp+var_2E], al
mov [ebp+var_2D], al
lea ecx, [ebp+Str]
mov al, 74h ; 't'
mov bl, 2Eh ; '.'
mov dl. 6Eh ; 'n'
push ecx ; STR
mov [ebp+var_13], 30h ; '0'
mov [ebp+var_11], 30h ; '0'
mov [ebp+var_10], 0
mov [ebp+cp], 73h ; 's'
mov [ebp+var_2F], 75h ; u'
mov [ebp+var_2C], 6Fh ; 'o'
mov [ebp+var_2B], 72h ; 'r'
mov [ebp+var_2A], al
mov [ebp+var_29], bl
mov [ebp+var_28], 62h ; 'b'
mov [ebp+var_27], 79h ; 'y'
mov [ebp+var_26], 69h ; 'i'
mov [ebp+var_25], dl
mov [ebp+var_24], al
mov [ebp+var_22], 72h ; 'r'
mov [ebp+var_21], bl
mov [ebp+var_20], dl
mov [ebp+var_1E], al
mov [ebp+var_1D], h
call ds:atoi
add esp, 4
mov dword ptr [ebp+hostshort], eax
jmp short loc_401326
```
|[**Rombertik**](../anti-static-analysis/exe-code-obfuscate.md)|2015|Most of the malware file consists of unnecessary code or unnecessary data [[4]](#4)|
|[**Ursnif**](../anti-static-analysis/exe-code-obfuscate.md)|2016|Creates an encrypted Registry key called TorClient to store its data [[5]](#5)|
|[**Poison-Ivy**](../xample-malware/poison-ivy.md)|2005|Poison Ivy variant encrypts all its strings [[6]](#6)|
|[**SamSam**](../xample-malware/samsam.md)|2015|SamSam obfuscates functions, class names and strings, including the list of targeted file extensions, the help file contents and environment variables using DES encryption with a fixed hard-coded key and the IV  [[7]](#7)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|The configuration data block is encoded with a NOT XOR 0xFF operation  [[8]](#8)|

References
----------
<a name="1">[1]</a> https://insights.sei.cmu.edu/cert/2019/03/api-hashing-tool-imagine-that.html

<a name="2">[2]</a> https://cofense.com/recent-geodo-malware-campaigns-feature-heavily-obfuscated-macros/

<a name="3">[3]</a> Rob Simmons, "Comparing Malicious Files," BSides, 2019. http://www.irongeek.com/i.php?page=videos/bsidescharm2019/2-04-comparing-malicious-files-robert-simmons

<a name="4">[4]</a> https://blogs.cisco.com/security/talos/rombertik

<a name="5">[5]</a> https://www.proofpoint.com/us/threat-insight/post/ursnif-variant-dreambot-adds-tor-functionality

<a name="6">[6]</a> https://www.mandiant.com/sites/default/files/2021-09/rpt-poison-ivy.pdf

<a name="7">[7]</a> https://blog.talosintelligence.com/2018/01/samsam-evolution-continues-netting-over.html

<a name="8">[8]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en
