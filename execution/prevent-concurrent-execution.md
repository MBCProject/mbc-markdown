<table>
<tr>
<td><b>ID</b></td>
<td><b>B0024</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../execution">Execution</a></b></td>
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
<td><b>8 May 2023</b></td>
</tr>
</table>


# Prevent Concurrent Execution

To avoid running multiple instances of itself, malicious code may check a system to see if it is already running. To accomplish this, malware authors use a mutex (mutual exclusion), also known as a mutant, to evaluate whether a system has been infected. If the mutex is running, the system is likely already compromised and there is no need to re-infect the host [[1]](#1). A mutex also serializes access to a resource so that multiple parties do not attempt simultaneous access [[2]](#2).

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Bagle**](../xample-malware/bagle.md)|2004|--|Some variants look for an unnamed mutex to ensure only one copy of itself is running on a system. [[3]](#3)|

## References

<a name="1">[1]</a> M. Elias,"Prime Minister’s Office Compromised: Details of Recent Espionage Campaign," Trellix.com, 25 Jan. 2022. [Online]. Available: https://www.trellix.com/en-us/about/newsroom/stories/research/prime-ministers-office-compromised.html.
<a name="2">[2]</a> Contributors: S. White, K. Sharkey, D. Coulter, D. Batchelor, and M. Satran, "Mutex Objects," learn.microsoft.com, 07 Jan. 2021. [Online]. Available: https://learn.microsoft.com/en-us/windows/win32/sync/mutex-objects.
<a name="3">[3]</a> https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/WORM_BAGLE.U/

