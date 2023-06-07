<table>
<tr>
<td><b>ID</b></td>
<td><b>B0014</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../discovery">Discovery</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.1</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>3 June 2023</b></td>
</tr>
</table>


# SMTP Connection Discovery

Malware may test whether an outgoing SMTP connection can be made from the system on which the malware instance is executing to some SMTP server, by sending a test SMTP transaction. 

## Use in Malware

Name|Date|Method|Description|
|---|---|---|---|
|[**Snake**](../xample-malware/snake.md)|2004|--|Snake attempts to login to an attacker controlled SMTP server before sending information. [[1]](#1)|

## References

<a name="1">[1]</a> https://www.cybereason.com/blog/research/threat-analysis-report-snake-infostealer-malware