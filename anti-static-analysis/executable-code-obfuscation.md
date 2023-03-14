<table>
<tr>
<td><b>ID</b></td>
<td><b>B0032</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../anti-static-analysis">Anti-Static Analysis</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
<tr>
<td><b>Anti-Analysis Type</b></td>
<td><b>Evasion</b></td>
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
<td><b>21 November 2022</b></td>
</tr>
</table>

# Executable Code Obfuscation

Executable code is obfuscated to hinder static code analysis. This behavior is specific to a malware sample's executable code (data and text sections). While the Executable Code Obfuscation behavior makes the analysis process more difficult, it does not cause incorrect or incomplete disassembly, which is how this behavior differs from the Disassembler Evasion behavior.

For encryption and encoding characteristics of malware samples, as well as malware obfuscation behaviors related to non-malware sample files and information, see **Obfuscated Files or Information ([E1027](../defense-evasion/obfuscated-files-or-information.md))**.

## Methods

|Name|ID|Description|
|---|---|---|
|**Argument Obfuscation**|B0032.020|Simple number or string arguments to API calls are calculated at runtime, making analysis more difficult.|
|**API Hashing**|B0032.001|Instead of storing function names in the Import Address Table (IAT) and calling GetProcAddress, a DLL is loaded and the name of each of its exports is hashed until it matches a specific hash. Manual symbol resolution is then used to access and execute the exported function. This method is often used by shellcode because it reduces the size of each import from a human-readable string to a sequence of four bytes. The Method is also known as "Imports by Hash" and "GET_APIS_WITH_CRC." [[1]](#1)|
|**Code Insertion**|B0032.002|Insert code to impede disassembly and make analysis more difficult.|
|**Data Value Obfuscation**|B0032.008|Obfuscate data values through indirection of local or global variables. For example, the instruction *if (a == 0) do x* can be obfuscated by setting a global variable, *Z*, to zero and using it in the instruction: *if (a==Z) do x*.  [NEEDS REVIEW]|
|**Dead Code Insertion**|B0032.003|Include "dead" code with no real functionality. When executing, malware may skip over such code via an opaque predicate.|
|**Entry Point Obfuscation**|B0032.009|Obfuscate the entry point of the malware executable.|
|**Fake Code Insertion**|B0032.004|Add fake code similar to known packers or known goods to fool identification. Can confuse some automated unpackers.|
|**Guard Pages**|B0032.010|Encrypt blocks of code individually and decrypt temporarily only upon execution.|
|**Import Address Table Obfuscation**|B0032.011|Obfuscate the import address table.|
|**Import Compression**|B0032.012|Store and load imports with a compact import table format. Each DLL needed by the executable is mentioned in the IAT, but only one function from each/most is imported; the rest are imported via GetProcAddress calls.|
|**Instruction Overlap**|B0032.013|Jump after the first byte of an instruction to confuse disassembler.|
|**Interleaving Code**|B0032.014|Split code into sections that may be rearranged and may be connected by unconditional jumps. When instructions are out of order, writing a function signature is more difficult.|
|**Jump Insertion**|B0032.005|Insert jumps to make analysis visually harder.|
|**Junk Code Insertion**|B0032.007|Insert dummy code between relevant opcodes. Can make signature writing more complex.|
|**Merged Code Sections**|B0032.015|Merge all sections resulting in just one entry in the sections table to make readability more difficult. May affect some detection signatures if written to be section dependent.|
|**Opaque Predicate**|B0032.019|An opaque predicate either always jumps (jumping over dead or junk code) or never jumps (executing essential code), but determining the execution path can be difficult.|
|**Stack Strings**|[B0032.017](#b0032017-snippet)|Build and decrypt strings on the stack at each use, then discard to avoid obvious references.|
|**Structured Exception Handling (SEH)**|B0032.016|A portion of the code always generates an exception so that malicious code is executed with the exception handling. See [[3]](#3).|
|**Symbol Obfuscation**|B0032.018|Remove or rename symbolic information commonly inserted by compilers for debugging purposes.|
|**Thunk Code Insertion**|B0032.006|Variation on Jump Insertion. Used by some compilers for user-generated functions.|
|**Variable Recomposition**|B0032.021|Variables, often strings, are broken into multiple parts and stored out of order, in different memory ranges, or both. They must then be recomposed before use, making analysis difficult.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Heriplor**](../xample-malware/heriplor.md)|2012|B0032.001|The Heriplor Trojan uses API Hashing. [[1]](#1)|
|[**Emotet**](../xample-malware/emotet.md)|2018|B0032.007|Emotet macros are heavily obfuscated with junk functions and string substitutions. [[2]](#2)|
|[**Rombertik**](../anti-static-analysis/executable-code-obfuscation.md)|2015|B0032.002|Most of the malware file consists of unnecessary code or unnecessary data. [[4]](#4)|
|[**Poison Ivy**](../xample-malware/poison-ivy.md)|2005|B0032.017|Poison Ivy variant encrypts all its strings. [[6]](#6)|
|[**SamSam**](../xample-malware/samsam.md)|2015|--|SamSam obfuscates functions, class names and strings, including the list of targeted file extensions, the help file contents and environment variables using DES encryption with a fixed hard-coded key and the IV. [[7]](#7)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|E1027.m01|The configuration data block is encoded with a NOT XOR 0xFF operation. [[8]](#8)|
|[**Matanbuchus**](../xample-malware/matanbuchus.md)|2021|B0032.001|The function to import APIs uses a hash value and the DLL name of the target API. The API address returned from the function is stored into a global variance. API calls are obfuscated in the same manner as the stack strings and are resolved dynamically as the malware needs to use them. The malware encodes data in a stack string and copies that data into a global character buffer as a form of string obfuscation. [[9]](#9) [[10]](#10)|
|[**Matanbuchus**](../xample-malware/matanbuchus.md)|2021|B0032.017|The malware encodes data in a stack string and copies that data into a global character buffer as a form of string obfuscation. Different techniques are used to encrypt and obfuscate strings. Strings are dynamically decrypted when the malware needs to use them. [[9]](#9) [[10]](#10)|
|[**Matanbuchus**](../xample-malware/matanbuchus.md)|2021|B0032.009|The malware has 4 different export functions. [[9]](#9) [[10]](#10)|


## Code Snippets

### B0032.017 SNippet
<details>
<summary> Executable Code Obfuscation::Stack Strings </summary>
SHA256: 304f533ce9ea4a9ee5c19bc81c49838857c63469e26023f330823c3240ee4e03
<pre>
asm
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
</pre>
</details>

## References

<a name="1">[1]</a> https://blogs.cisco.com/security/talos/rombertik

<a name="2">[2]</a> https://cofense.com/blog/recent-geodo-malware-campaigns-feature-heavily-obfuscated-macros/

<a name="3">[3]</a> Rob Simmons, "Comparing Malicious Files," BSides, 2019. http://www.irongeek.com/i.php?page=videos/bsidescharm2019/2-04-comparing-malicious-files-robert-simmons

<a name="4">[4]</a> https://blogs.cisco.com/security/talos/rombertik

<a name="5">[5]</a> https://www.proofpoint.com/us/threat-insight/post/ursnif-variant-dreambot-adds-tor-functionality

<a name="6">[6]</a> https://www.mandiant.com/sites/default/files/2021-09/rpt-poison-ivy.pdf

<a name="7">[7]</a> https://blog.talosintelligence.com/2018/01/samsam-evolution-continues-netting-over.html

<a name="8">[8]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en

<a name="9">[9]</a> https://www.0ffset.net/reverse-engineering/matanbuchus-loader-analysis/

<a name="10">[10]</a> https://www.cyberark.com/resources/threat-research-blog/inside-matanbuchus-a-quirky-loader
