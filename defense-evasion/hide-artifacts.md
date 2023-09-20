<table>
<tr>
<td><b>ID</b></td>
<td><b>E1564</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../defense-evasion">Defense Evasion</a>, <a href="../persistence">Persistence</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Hide Artifacts (<a href="https://attack.mitre.org/techniques/T1564/">T1564</a>, <a href="https://attack.mitre.org/techniques/T1628/">T1628</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>8 November 2021</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>4 March 2023</b></td>
</tr>
</table>


# Hide Artifacts

Malware may hide artifacts to evade detection and/or to persist on the system. See potential methods related to malware below. 

See ATT&CK: **Hide Artifacts ([T1564](https://attack.mitre.org/techniques/T1564/), [T1628](https://attack.mitre.org/techniques/T1628/))**.

## Methods

|Name|ID|Description|
|---|---|---|
|**Hidden Userspace Libraries**|E1564.m01|Hides userspace libraries used by the malware instance. Technique refers to hiding libraries loaded in memory (not disk). For example, a userspace library may be injected into a system process such that memory scanning tools may be prevented from finding them. This technique is different than DLL injection, in which the DLL will continue to show up in process metadata that tracks what is stored in memory. This technique involves clearing that metadata or making it inaccessible to security and inspection tools.|
|**Direct Kernel Object Manipulation**|E1564.m02|Direct Kernel Object Manipulation (DKOM) can be used instead of loading a new driver. It leverages an undocumented function exported by ntdll.dll (NtSystemDebugControl()) that provides debugging functionalities at the kernel level.|
|**Hidden Kernel Modules**|E1564.m05|Hides the use of kernel modules by the malware instance (e.g. rootkit). Techniques include kernel module list unlinking.|
|**Hidden Processes**|E1564.m03|Hides processes used by the adversary or malware instance. This can involve techniques such as process list unlinking.|
|**Hidden Services**|E1564.m04|Hides any system services that the malware instance creates or injects itself into. Services can be hidden by hiding associated registry keys.|


## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**YiSpecter**](../xample-malware/yispecter.md)|2015|--|The malware hides icons from iOS's SpringBoard as well as use the same name and logos of system apps to trick iOS power users. [[1]](#1)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|--|Stuxnet intercepts IRP requests (reads, writes) to devices (NFTS, FAT, CD-ROM). It monitors directory control IRPs, in particular directory query notifications, such that when an application requests the list of files, it returns a Stuxnet-specified subset of the true items. These filters hide the files used by Stuxnet to spread through removable drives.  [[2]](#2)|

## References

<a name="1">[1]</a> https://unit42.paloaltonetworks.com/yispecter-first-ios-malware-attacks-non-jailbroken-ios-devices-by-abusing-private-apis/

<a name="2">[2]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en

