<table>
<tr>
<td><b>ID</b></td>
<td><b>B0006</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../anti-behavioral-analysis">Anti-Behavioral Analysis</a></b></td>
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
<td><b>8 May 2023</b></td>
</tr>
</table>

# Memory Dump Evasion

Memory dump evasion is an anti-forensic technique in which malware hinders retrieval and/or discovery of the contents of the physical memory of the system on which the malware instance is executing [[1]](#1). Tools enabling capture of malware code from memory can be software-based or hardware-based. Malicious code thwarts software-based tools by relying on such methods as resolving API addresses before each use (on-the-fly APIs method) and erasing or corrupting specific file parts to prevent rebuilding (tampering method) [[2]](#2),[[3]](#3). 

## Methods

|Name|ID|Description|
|---|---|---|
|**Code Encryption in Memory**|B0006.001|Encrypt the executing malware instance code in memory.|
|**Erase the PE header**|B0006.002|Erase PE header from memory.|
|**Feed Misinformation**|B0006.008|API behavior can be altered to prevent memory dumps. For example, inaccurate data can be reported when the contents of the physical memory of the system on which the malware instance is executing is retrieved. See [Hijack Execution Flow](../defense-evasion/hijack-execution-flow.md).|
|**Flow Opcode Obstruction**|B0006.009|Flow opcodes (e.g., jumps, loops) are removed and emulated (or decrypted) by the packer during execution, resulting in incorrect dumps. [[6]](#6).|
|**Guard Pages**|B0006.006|Encrypt blocks of code individually and decrypt temporarily only upon execution. This method is related to Unprotect technique U0102.|
|**Hide virtual memory**|B0006.003|Hide arbitrary segments of virtual memory.|
|**On-the-Fly APIs**|B0006.007|Resolve API addresses before each use to prevent complete dumping.|
|**SizeOfImage**|B0006.004|Set the SizeOfImage field of PEB.LoaderData to be huge.|
|**Tampering**|B0006.005|Erase or corrupt specific file parts to prevent rebuilding (header, packer stub, etc.).|
|**Hook memory mapping APIs**|B0006.010|Hooking prevents memory dumps by preventing mapping of memory into the kernel's virtual address space. [[1]](#1)|
|**Patch MmGetPhysicalMemoryRanges**|[B0006.011](#b0006011-snippet)|Patching this function to always return NULL prevents drivers from getting information about the physical address space layout, preventing memory dumps. [[1]](#1)|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Kraken**](../xample-malware/kraken.md)|2008|--|Dumping Kraken's c.dll module from the heap of its own process is tricky because its PE-header is erased in memory. [[4]](#4)|

## Code Snippets

### B0006.011 Snippet
<details>
<summary> Memory Dump::Code Encryption in Memory </summary>
SHA256: 304f533ce9ea4a9ee5c19bc81c49838857c63469e26023f330823c3240ee4e03
<pre>
asm
mov cl, 65h ; 'e'
mov al, 70h ; 'p'
mov [ebp+var_23], cl
mov [ebp+var_1F], cl
mov [ebp+String], bl
mov [ebp+var_12], bl
mov [ebp+var_2E], al
mov [ebp+var_2D], al
lea ecx, [ebp+String]
mov al, 74h ; 't'
mov bl, 2Eh ; '.'
push ecx
mov [ebp+var_13], 30h
mov [ebp+var_11], 30h
mov [ebp+var_10], 0
mov [ebp+cp]
mov [ebp+var_2F], 75h
mov [ebp+var_2C], 6Fh
mov [ebp+var_2B], 72h
mov [ebp+var_2A], al
mov [ebp+var_29], bl
mov [ebp+var_28], 62h
mov [ebp+var_27], 79h
mov [ebp+var_26], 69h
mov [ebp+var_25], dl
mov [ebp+var_24], al
mov [ebp+var_22], 72h
mov [ebp+var_21], bl
mov [ebp+var_20], dl
mov [ebp+var_1E], al
mov [ebp+var_1D], 0
call ds:atoi
add esp, 4
mov dword ptr [ebp+hostshort], eax
jmp short loc_401326
</pre>
</details>

## References

<a name="1">[1]</a> J. Stüttgen and M. Cohen,"Anti-Forensic Resilient Memory Acquisition," in DFRWS USA 2013 Conference, 2013. [Online]. Available: https://dfrws.org/presentation/anti-forensic-resilient-memory-acquisition/. 

<a name="2">[2]</a> L. Maffia, D. Nisi, P. Kotzias, G. Lagorio, S. Aonzo, and D. Balzarotti, "Longitudinal Study of the Prevalence of Malware Evasive Techniques," arXiv:2112.11289 , 21 Dec 2021. [Online]. Available: https://arxiv.org/pdf/2112.11289.pdf.

<a name="3">[3]</a> "PlugX: Memory Forensics Lifecycle with Volatility," Volatility Labs, blog, 6 Nov. 2015. [Online]. Available: https://volatility-labs.blogspot.com/2015/11/plugx-memory-forensics-lifecycle-with.html.

<a name="4">[4]</a> http://blog.threatexpert.com/2008/04/kraken-changes-tactics.html

<a name="5">[5]</a> https://waleedassar.blogspot.com/search/label/anti-dump

<a name="6">[6]</a> https://www.gironsec.com/code/packers.pdf

