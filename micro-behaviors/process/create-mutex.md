<table>
<tr>
<td><b>ID</b></td>
<td><b>C0042</b></td>
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
<td><b>2.2</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>4 December 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>30 April 2024</b></td>
</tr>
</table>


# Create Mutex

Malware creates a mutex. 

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Poison Ivy**](../../xample-malware/poison-ivy.md)|2005|--|Poison Ivy has a default process mutex, but can be altered at build time. [[1]](#1)|
|[**Stuxnet**](../../xample-malware/stuxnet.md)|2010|--|Malware creates global mutexes that signal rootkit installation has occurred successfully. [[2]](#2)|
|[**Hupigon**](../../xample-malware/hupigon.md)|2013|--|Hupigon creates a mutex. [[3]](#3)|
|[**Kovter**](../../xample-malware/kovter.md)|2016|--|Kovter creates a mutex. [[3]](#3)|
|[**Redhip**](../../xample-malware/redhip.md)|2011|--|Redhip creates a mutex. [[3]](#3)|
|[**Rombertik**](../../xample-malware/rombertik.md)|2015|--|Rombertik creates a mutex. [[3]](#3)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[create mutex](https://github.com/mandiant/capa-rules/blob/master/host-interaction/mutex/create-mutex.yml)|Create Mutex (C0042)|kernel32.CreateMutex, kernel32.CreateMutexEx, System.Threading.Mutex::ctor|
|[lock file](https://github.com/mandiant/capa-rules/blob/master/host-interaction/mutex/lock-file.yml)|Create Mutex (C0042)|fcntl|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[banker_zeus_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/banker_zeus_mutex.py)|Create Mutex (C0042)|--|
|[parallax_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/parallax_mutexes.py)|Create Mutex (C0042)|--|
|[packer_armadillo_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/packer_armadillo_mutex.py)|Create Mutex (C0042)|--|
|[trickbot_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/trickbot_mutex.py)|Create Mutex (C0042)|--|
|[banker_cridex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/banker_cridex.py)|Create Mutex (C0042)|--|
|[deepfreeze_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/deepfreeze_mutex.py)|Create Mutex (C0042)|--|
|[bot_russkill](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bot_russkill.py)|Create Mutex (C0042)|--|
|[banker_zeus_p2p](https://github.com/CAPESandbox/community/tree/master/modules/signatures/banker_zeus_p2p.py)|Create Mutex (C0042)|--|
|[carberp_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/carberp_mutex.py)|Create Mutex (C0042)|--|

### C0042 Snippet
<details>
<summary> Process::Create Mutex </summary>
SHA256: 0b8e662e7e595ef56396a298c367b74721d66591d856e8a8241fcdd60d08373c
Location: 0x402A1E
<pre>
push    eax     ; name of mutex
push    0x0     ; if the thread that creates the mutex owns it (false, in this case)
push    0x0     ; optional security descriptor set to NULL, so default security descriptor will be used
call    dword ptr [->KERNEL32.DLL::CreateMutexW]        ; call function to create mutex
</pre>
</details>

## References

<a name="1">[1]</a> https://www.fortinet.com/blog/threat-research/deep-analysis-of-new-poison-ivy-variant

<a name="2">[2]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en

<a name="3">[3]</a> capa v4.0, analyzed at MITRE on 10/12/2022
