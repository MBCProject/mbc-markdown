<table>
<tr>
<td><b>ID</b></td>
<td><b>C0003</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../communication">Communication</a></b></td>
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
<td><b>14 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>5 December 2023</b></td>
</tr>
</table>


# Interprocess Communication

The Interprocess Communication micro-behavior focuses on interprocess communication. 

## Methods

|Name|ID|Description|
|---|---|---|
|**Connect Pipe**|C0003.002|--|
|**Create Pipe**|C0003.001|--|
|**Read Pipe**|C0003.003|--|
|**Write Pipe**|C0003.004|--|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|C0003.001|Hupigon creates two anonymous pipes. [[1]](#1)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|C0003.004|Hupigon writes pipes. [[1]](#1)|
|[**Poison Ivy**](../xample-malware/poison-ivy.md)|2005|C0003.004|Poison Ivy writes pipes. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[create mailslot](https://github.com/mandiant/capa-rules/blob/master/communication/mailslot/create-mailslot.yml)|Interprocess Communication (C0003)|kernel32.CreateMailslot, kernel32.GetMailslotInfo, kernel32.SetMailslotInfo|
|[read from mailslot](https://github.com/mandiant/capa-rules/blob/master/communication/mailslot/read-from-mailslot.yml)|Interprocess Communication (C0003)|kernel32.GetMailslotInfo, kernel32.ReadFile, kernel32.ReadFileEx|
|[create pipe](https://github.com/mandiant/capa-rules/blob/master/communication/named-pipe/create/create-pipe.yml)|Interprocess Communication::Create Pipe (C0003.001)|kernel32.CreatePipe, kernel32.CreateNamedPipe, System.IO.Pipes.AnonymousPipeClientStream::ctor, System.IO.Pipes.NamedPipeClientStream::ctor, System.IO.Pipes.AnonymousPipeServerStream::ctor, System.IO.Pipes.AnonymousPipeServerStreamAcl::Create, System.IO.Pipes.NamedPipeServerStream::ctor, System.IO.Pipes.NamedPipeServerStreamAcl::Create|
|[create two anonymous pipes](https://github.com/mandiant/capa-rules/blob/master/communication/named-pipe/create/create-two-anonymous-pipes.yml)|Interprocess Communication::Create Pipe (C0003.001)|--|
|[write pipe](https://github.com/mandiant/capa-rules/blob/master/communication/named-pipe/write/write-pipe.yml)|Interprocess Communication::Write Pipe (C0003.004)|kernel32.WriteFile, kernel32.TransactNamedPipe, kernel32.CallNamedPipe|
|[connect pipe](https://github.com/mandiant/capa-rules/blob/master/communication/named-pipe/connect/connect-pipe.yml)|Interprocess Communication::Connect Pipe (C0003.002)|kernel32.ConnectNamedPipe, kernel32.CallNamedPipe, System.IO.Pipes.NamedPipeClientStream::Connect, System.IO.Pipes.NamedPipeClientStream::ConnectAsync|
|[read pipe](https://github.com/mandiant/capa-rules/blob/master/communication/named-pipe/read/read-pipe.yml)|Interprocess Communication::Read Pipe (C0003.003)|kernel32.PeekNamedPipe, kernel32.ReadFile, kernel32.TransactNamedPipe, kernel32.CallNamedPipe|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[ipc_namedpipe](https://github.com/CAPESandbox/community/tree/master/modules/signatures/ipc_namedpipe.py)|Interprocess Communication (C0003)|NtReadFile, NtCreateNamedPipeFile, NtWriteFile|
|[ipc_namedpipe](https://github.com/CAPESandbox/community/tree/master/modules/signatures/ipc_namedpipe.py)|Interprocess Communication::Create Pipe (C0003.001)|NtReadFile, NtCreateNamedPipeFile, NtWriteFile|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

