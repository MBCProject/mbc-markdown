<table>
<tr>
<td><b>ID</b></td>
<td><b>C0043</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../process">Process</a></b></td>
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
<td><b>4 December 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>21 November 2022</b></td>
</tr>
</table>


# Check Mutex

Malware checks a mutex. 

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Poison Ivy**](../xample-malware/poison-ivy.md)|2005|--|Poison Ivy variant checks if the wireshark-is-running{} named mutex object exists. [[1]](#1)|
|[**Matanbuchus**](../xample-malware/matanbuchus.md)|2021|--|Malware checks if multiple instances of the same mutex is running. If multiple instances are running, the malware exits. [[2]](#2) [[3]](#3)|

## References

<a name="1">[1]</a> https://www.fortinet.com/blog/threat-research/deep-analysis-of-new-poison-ivy-variant

<a name="2">[2]</a> https://www.0ffset.net/reverse-engineering/matanbuchus-loader-analysis/

<a name="3">[3]</a> https://www.cyberark.com/resources/threat-research-blog/inside-matanbuchus-a-quirky-loader
