<table>
<tr>
<td><b>ID</b></td>
<td><b>E1105</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../command-and-control">Command and Control</a>, <a href="../lateral-movement">Lateral Movement</a>, <a href="../persistence">Persistence</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Ingress Tool Transfer (<a href="https://attack.mitre.org/techniques/T1105/">T1105</a>)</b></td>
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


# Ingress Tool Transfer

Malware may copy files from an external system to a system on a compromised network. 

Note that this behavior is separate from possible execution (installation) of the file, which is covered by the **Install Additional Program ([B0023](../execution/install-additional-program.md))** behavior. 

See ATT&CK: **Ingress Tool Transfer ([T1105](https://attack.mitre.org/techniques/T1105/))**.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|E1105|Creates a folder on remote computers and then copies its executables (Shamoon and Filerase) into that directory  [[2]](#2)|
|[**CozyCar**](../xample-malware/cozycar.md)|2010|E1105|CozyCar requests a file using SSL to a C2 domain [[3]](#3)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|E1105|Can download files from remote repository upon instruction  [[1]](#1)|

## References

<a name="1">[1]</a> https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/

<a name="2">[2]</a> https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-attackers-employ-new-tool-kit-to-wipe-infected-systems/

<a name="3">[3]</a> https://unit42.paloaltonetworks.com/tracking-minidionis-cozycars-new-ride-is-related-to-seaduke

