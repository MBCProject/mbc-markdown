|||
|---|---|
|**ID**|**B0032**|
|**Objective(s)**|[Anti-Static Analysis](https://github.com/MBCProject/mbc-markdown/tree/master/anti-static-analysis)|
|**Related ATT&CK Technique**|None|


Executable Code Obfuscation
===========================
Executable code can be obfuscated to hinder disassembly and static code analysis. This behavior is specific to a malware sample's executable code (data and text sections).

For encryption and encoding characteristics of malware samples, as well as malware obfuscation behaviors related to non-malware-sample files and information, see [**Obfuscated Files or Information**](https://github.com/MBCProject/mbc-markdown/blob/master/defense-evasion/obfuscate-files.md).

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
|[**Heriplor**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/heriplor.md)|March 2019|The Heriplor Trojan uses API Hashing. [[1]](#1)|
|[**Emotet**](https://github.com/MBCProject/mbc-markdown/blob/master/xample-malware/emotet.md)|2018|Emotet macros are heavily obfuscated with junk functions and string substitutions. [[2]](#2)|
|[**TrickBot**](https://github.com/MBCProject/mbc-markdown/tree/master/xample-malware/trickbot.md)|2016|Trojan spyware program that has mainly been used for targeting banking sites.|

References
----------
<a name="1">[1]</a> https://insights.sei.cmu.edu/cert/2019/03/api-hashing-tool-imagine-that.html

<a name="2">[2]</a> https://cofense.com/recent-geodo-malware-campaigns-feature-heavily-obfuscated-macros/

<a name="3">[3]</a> Rob Simmons, "Comparing Malicious Files," BSides, 2019. http://www.irongeek.com/i.php?page=videos/bsidescharm2019/2-04-comparing-malicious-files-robert-simmons
