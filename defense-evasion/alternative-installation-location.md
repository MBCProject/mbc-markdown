<table>
<tr>
<td><b>ID</b></td>
<td><b>B0027</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../defense-evasion">Defense Evasion</a></b></td>
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
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>01 May 2023</b></td>
</tr>
</table>


# Alternative Installation Location

Malware may install itself in areas other than the hard drive [[1]](#1). Other possible locations include the BIOS/Unified Extensible Firmware Interface (UEFI) firmware, which is embedded on a chip on the motherboard, and the graphics processor unit (GPU), where malware is stored in its memory buffer (also known as VRAM) [[2]](#2)[[3]](#3). Volatile memory is a third possibility and when installation occurs here, malware is known as “fileless.” 

While the definition of fileless malware can be ambiguous, here it represents malware that lives in memory only, not on disk, and it does not preclude fileless malware from using files on the system. Microsoft and Zeltser have addressed  this ambiguity by providing more context in [[4]](#4) and [[5]](#5), respectively.


## Methods
 
|Name|ID|Description|
|---|---|---|
|**Fileless Malware**|B0027.001|Stores itself in memory. This method is related to Unprotect technique U1205 and ATT&CK sub-technique Obfuscated Files or Information: Fileless Storage [T1027.011](https://attack.mitre.org/techniques/T1027/011/). |
|**Registry Install**|B0027.002|Stores itself in the Windows registry.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Kovter**](../xample-malware/kovter.md)|2016|B0027.002|Kovter stores malware files in the Registry instead of on the hard drive. [[1]](#1)|
|[**SYNful Knock**](../xample-malware/synful-knock.md)|2015|B0027.001|100 memory-resident modules can be installed. [[6]](#6)|


## References

<a name="1">[1]</a> "How to remove the Kovter Trojan (Removal Guide)," bleepingcomputer.com, 23 Mar. 2016. [Online]. Available: https://www.bleepingcomputer.com/virus-removal/remove-kovter-trojan.

<a name="2">[2]</a> J. Glazova,"CosmicStrand: A UEFI Rootkit," Kaspersky, blog, 26 Jul. 2022. [Online]. Available: https://usa.kaspersky.com/blog/cosmicstrand-uefi-rootkit/26807/.

<a name="3">[3]</a> I. Ilascu,"Cybercriminal sells tool to hide malware in AMD, NVIDIA GPUs," bleepingcomputer.com, 31 Aug. 2021. [Online]. Available: https://www.bleepingcomputer.com/news/security/cybercriminal-sells-tool-to-hide-malware-in-amd-nvidia-gpus/.

<a name="4">[4]</a> Contributors: D. Simpson, A. Lobo, A. Jupudi, D. Vangel, and C. Davis,"Fileless threats," learn.microsoft.com, 02 June 2023. [Online]. Available: https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/fileless-threats?view=o365-worldwide.

<a name="5">[5]</a> L. Zeltser,"The History of Fileless Malware – Looking Beyond the Buzzword," zeltser.com, blog, 12 Oct. 2018. [Online]. Available: https://zeltser.com/fileless-malware-beyond-buzzword/.

<a name="6">[6]</a> B. HAU, T. LEE, and J. HOMAN,"SYNful Knock - A Cisco router implant - Part I," Mandiant.com, 15 Sept. 2015. [Online]. Available: https://www.mandiant.com/resources/synful-knock-acis.

