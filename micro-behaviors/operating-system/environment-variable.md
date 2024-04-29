<table>
<tr>
<td><b>ID</b></td>
<td><b>C0034</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../operating-system">Operating System</a></b></td>
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
<td><b>5 December 2023</b></td>
</tr>
</table>


# Environment Variable

Malware modifies environment variables. 

## Methods

|Name|ID|Description|
|---|---|---|
|**Set Variable**|C0034.001|Malware sets an environment variable.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Kovter**](../../xample-malware/kovter.md)|2016|C0034.001|Kovter sets environment variables. [[1]](#1)|
|[**UP007**](../../xample-malware/up007.md)|2016|C0034.001|UP007 sets environment variables. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[set environment variable](https://github.com/mandiant/capa-rules/blob/master/host-interaction/environment-variable/set-environment-variable.yml)|Environment Variable::Set Variable (C0034.001)|kernel32.SetEnvironmentStrings, kernel32.SetEnvironmentVariable, System.Environment::SetEnvironmentVariable|
|[get COMSPEC environment variable](https://github.com/mandiant/capa-rules/blob/master/host-interaction/environment-variable/get-comspec-environment-variable.yml)|Environment Variable (C0034)|--|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

