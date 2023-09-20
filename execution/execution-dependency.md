<table>
<tr>
<td><b>ID</b></td>
<td><b>B0044</b></td>
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
<td><b>2.1</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>20 April 2021</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>12 June 2023</b></td>
</tr>
</table>


# Execution Dependency

Software may require certain run-time or library dependencies consistent with normal software development and deployment. For example, software may require the presence of a .NET or Java runtime or to be run by a webserver that supports PHP. Unlike in **Conditional Execution ([B0025](../execution/conditional-execution.md))**, this dependency is not because of an explicit check coded into the malware by the author.


## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Adwind jRAT**](../xample-malware/adwindjrat.md)|2019|--|Adwind jRAT uses standard Java commands to mask its behavior. [[1]](#1)|


## References

<a name="1">[1]</a> https://www.menlosecurity.com/blog/hiding-in-plain-sight-new-adwind-jrat-variant-uses-normal-java-commands-to-mask-its-behavior/