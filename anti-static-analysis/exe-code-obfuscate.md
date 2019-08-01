|||
|---------|------------------------|
|**ID**|**M0032**|
|**Objective(s)**| [Anti-Static Analysis](https://github.com/MAECProject/malware-behaviors/tree/master/anti-static-analysis)|
|**Related ATT&CK Technique(s)**|None|


Executable Code Obfuscation
===========================
Executable code uses obfuscation to hinder disassembly and static code analysis. Methods related to *anti-static analysis* are below. The Executable Code Obfuscation behavior is specific to a malware sample's executable code (data and text sections).

For obfuscation behaviors related to non-malware-sample files and information, see ATT&CK: [**Obfuscated Files or Information**](https://attack.mitre.org/techniques/T1027/), under the [Defense Evasion](https://github.com/MAECProject/malware-behaviors/tree/master/defense-evasion) objective.

Methods
-------
* **API Hashing**: Instead of storing function names in the Import Address Table (IAT) and calling GetProcAddress, a DLL is loaded and the name of each of its exports is hashed until it matches a specific hash. Manual symbol resolution is then used to access and execute the exported function. This method is often used by shellcode because it reduces the size of each import from a human-readable string to a sequence of four bytes. The Method is also known as "Imports by Hash" and "GET_APIS_WITH_CRC." [[1]](#1) 
* **Code Insertion**: Insert code to impede disassembly.
   * *Dead Code Insertion*: Include "dead" code with no real functionality.
   * *Fake Code Insertion*: Add fake code similar to known packers or known goods to fool identification. Can confuse some automated unpackers.
   * *Jump Insertion*: Insert jumps to make analysis visually harder.
   * *Thunk Code Insertion*: Variation on Jump Insertion. Used by some compilers for user-generated functions.
   * *Junk Code Insertion*: Insert dummy code between relevant opcodes. Can make signature writing more complex.
* **Data Value Obfuscation**: Obfuscate data values through indirection of local or global variables. For example, the instruction *if (a == 0) do x* can be obfuscated by setting a global variable, *Z*, to zero and using it in the instruction: *if (a==Z) do x*.  [NEEDS REVIEW]
* **Encryption**: 
   * *Standard Encryption*: A standard algorithm, such as Rijndael/AES, DES, RC4, is used to encrypt an executable file. Encryption hinders static analysis of malware code. Also known as **Code Encryption in File**.
   * *Standard Encryption of Code*: A standard encryption algorithm is used to encrypt a file's executable code, but not necessarily the file's data. 
   * *Standard Encryption of Data*: A standard encryption algorithm is used to encrypt a file's data, but not necessarily the file's code. 
   * *Custom Encryption*: A custom algorithm is used to encrypt an executable file. Encryption hinders static analysis of malware code. Also known as **Code Encryption in File**.
   * *Custom Encryption of Code*: A custom encryption algorithm is used to encrypt a file's executable code, but not necessarily the file's data.
   * *Custom Encryption of Data*: A custom encryption algorithm is used to encrypt a file's data, but not necessarily the file's code.
* **Entry Point Obfuscation**: Obfuscate the entry point of the malware executable.
* **Guard Pages**: Encrypt blocks of code individually and decrypt temporarily only upon execution.
* **Import Address Table Obfuscation**: Obfuscate the import address table.
* **Import Compression**: Store and load imports with a compact import table format. Each DLL needed by the executable is mentioned in the IAT, but only one function from each/most is imported; the rest are imported via GetProcAddress calls.
* **Instruction Overlap**: Jump after the first byte of an instruction to confuse disassembler.
* **Interleaving Code**: Split code into sections that may be rearranged and are connected by unconditional jumps.
* **Merged Code Sections**: Merge all sections resulting in just one entry in the sections table to make readability more difficult. May affect some detection signatures if written to be section dependent.
* **Structured Exception Handling (SEH)**: A portion of the code always generates an exception so that malicious code is executed with the exception handling. See  [[3]](#3).
* **Stack Strings**: Build and decrypt strings on the stack at each use, then discard to avoid obvious references.
* **Symbol Obfuscation**: Remove or rename symbolic information commonly inserted by compilers for debugging purposes.
   
Malware Examples
----------------
|Name|Date|Description|
|-----------------------------------------------|--------|-----------------------------|
|[**Heriplor Trojan**](https://github.com/MAECProject/malware-behaviors/blob/master/xample-malware/heriplor.md) | March 2019 | The Heriplor Trojan uses API Hashing. [[1]](#1)|
|[**Geodo**](https://github.com/MAECProject/malware-behaviors/blob/master/xample-malware/geodo.md) |August 2018| Geodo macros are heavily obfuscated with junk functions and string substitutions. [[2]](#2)|

References
----------
<a name="1">[1]</a> https://insights.sei.cmu.edu/cert/2019/03/api-hashing-tool-imagine-that.html 

<a name="2">[2]</a> https://cofense.com/recent-geodo-malware-campaigns-feature-heavily-obfuscated-macros/ 

<a name="3">[3]</a> Rob Simmons, "Comparing Malicious Files," BSides, 2019. http://www.irongeek.com/i.php?page=videos/bsidescharm2019/2-04-comparing-malicious-files-robert-simmons 