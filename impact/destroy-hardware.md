<table>
<tr>
<td><b>ID</b></td>
<td><b>B0017</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../impact">Impact</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
<tr>
<td><b>Impact Type</b></td>
<td><b>Availability</b></td>
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


# Destroy Hardware

Malicious code accomplishes hardware destruction. For example, malicious code may cause hardware to overheat through manipulation of power management software that controls the CPU’s voltage and frequency. Destruction of hardware is also associated with cyber attacks against industrial control systems, exemplified in the 2007 Aurora test at the Department of Energy’s Idaho National Laboratory that successfully used 149 kilobytes of code to physically damage a generator connected to the electric grid [[1]](#1). A more recent example is PIPEDREAM, a modular ICS attack framework that reportedly has “capabilities to disrupt, degrade, and potentially destroy physical processes in industrial environments” [[2]](#2). 

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|--|Stuxnet made centrifuges at Iran's nuclear plant spin dangerously fast for a few minutes, before returning to normal speed. A month later, it slowed the centrifuges down for nearly an hour. This was repeated for several months, and over time the strain destroyed the machines. [[3]](#3)|

## References

<a name="1">[1]</a> A. Greenberg,"How 30 Lines of Code Blew Up a 27-Ton Generator," Wired, 23 Oct. 2020. [Online]. Available: https://www.wired.com/story/how-30-lines-of-code-blew-up-27-ton-generator/.

<a name="2">[2]</a> "ICS/OT CYBERSECURITY YEAR IN REVIEW 2022," Dragos, 25 Feb. 2023. [Online]. Available: https://hub.dragos.com/hubfs/312-Year-in-Review/2022/Dragos_Year-In-Review-Report-2022.pdf?hsLang=en.

<a name="3">[3]</a> https://www.langner.com/wp-content/uploads/2017/03/to-kill-a-centrifuge.pdf

<a name="4">[4]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en

