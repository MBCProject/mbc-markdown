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
<td><b>2.1</b></td>
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


# Create Mutex

Malware creates a mutex. 

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Poison Ivy**](../xample-malware/poison-ivy.md)|2005|--|Poison Ivy has a default process mutex, but can be altered at build time. [[1]](#1)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|--|Malware creates global mutexes that signal rootkit installation has occurred successfully. [[2]](#2)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Hupigon creates a mutex. [[3]](#3)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|Kovter creates a mutex. [[3]](#3)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|--|Redhip creates a mutex. [[3]](#3)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|--|Rombertik creates a mutex. [[3]](#3)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[create mutex](https://github.com/mandiant/capa-rules/blob/master/host-interaction/mutex/create-mutex.yml)|Create Mutex (C0042)|kernel32.CreateMutex, kernel32.CreateMutexEx, System.Threading.Mutex::ctor|
|[lock file](https://github.com/mandiant/capa-rules/blob/master/host-interaction/mutex/lock-file.yml)|Create Mutex (C0042)|fcntl|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[banker_zeus_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/banker_zeus_mutex.py)|Create Mutex (C0042)|--|
|[parallax_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/parallax_mutexes.py)|Create Mutex (C0042)|--|
|[gandcrab_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/gandcrab_mutexes.py)|Create Mutex (C0042)|--|
|[packer_armadillo_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/packer_armadillo_mutex.py)|Create Mutex (C0042)|--|
|[fleercivet_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/fleercivet_mutex.py)|Create Mutex (C0042)|--|
|[renamer_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/renamer_mutexes.py)|Create Mutex (C0042)|--|
|[revil_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/revil_mutexes.py)|Create Mutex (C0042)|--|
|[trickbot_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/trickbot_mutex.py)|Create Mutex (C0042)|--|
|[rat_fynloski_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/rat_fynloski_mutexes.py)|Create Mutex (C0042)|--|
|[rat_beebus_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/rat_beebus_mutexes.py)|Create Mutex (C0042)|--|
|[xpertrat_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/xpertrat_mutexes.py)|Create Mutex (C0042)|--|
|[nemty_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/nemty_mutexes.py)|Create Mutex (C0042)|--|
|[stop_ransom_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/stop_ransom_mutexes.py)|Create Mutex (C0042)|--|
|[okrum_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/okrum_mutexes.py)|Create Mutex (C0042)|--|
|[pysa_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/pysa_mutexes.py)|Create Mutex (C0042)|--|
|[banker_cridex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/banker_cridex.py)|Create Mutex (C0042)|--|
|[fonix_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/fonix_mutexes.py)|Create Mutex (C0042)|--|
|[germanwiper_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/germanwiper_mutexes.py)|Create Mutex (C0042)|--|
|[ratsnif_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/ratsnif_mutexes.py)|Create Mutex (C0042)|--|
|[crat_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/crat_mutexes.py)|Create Mutex (C0042)|--|
|[neshta_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/neshta_mutexes.py)|Create Mutex (C0042)|--|
|[banker_spyeye_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/banker_spyeye_mutexes.py)|Create Mutex (C0042)|--|
|[powerpool_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/powerpool_mutexes.py)|Create Mutex (C0042)|--|
|[geodo_banking_trojan](https://github.com/CAPESandbox/community/tree/master/modules/signatures/geodo_banking_trojan.py)|Create Mutex (C0042)|--|
|[deepfreeze_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/deepfreeze_mutex.py)|Create Mutex (C0042)|--|
|[rat_xtreme_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/rat_xtreme_mutexes.py)|Create Mutex (C0042)|--|
|[lokibot_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/lokibot_mutexes.py)|Create Mutex (C0042)|--|
|[blackrat_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/blackrat_mutexes.py)|Create Mutex (C0042)|--|
|[rat_plugx_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/rat_plugx_mutexes.py)|Create Mutex (C0042)|--|
|[obliquerat_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/obliquerat_mutexes.py)|Create Mutex (C0042)|--|
|[cypherit_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/cypherit_mutexes.py)|Create Mutex (C0042)|--|
|[protonbot_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/protonbot_mutexes.py)|Create Mutex (C0042)|--|
|[cryptomix_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/cryptomix_mutexes.py)|Create Mutex (C0042)|--|
|[phorpiex_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/phorpiex_mutexes.py)|Create Mutex (C0042)|--|
|[venomrat_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/venomrat_mutexes.py)|Create Mutex (C0042)|--|
|[dcrat_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/dcrat_mutexes.py)|Create Mutex (C0042)|--|
|[andromut_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/andromut_mutexes.py)|Create Mutex (C0042)|--|
|[azorult_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/azorult_mutexes.py)|Create Mutex (C0042)|--|
|[dharma_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/dharma_mutexes.py)|Create Mutex (C0042)|--|
|[rat_quasar_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/rat_quasar_mutexes.py)|Create Mutex (C0042)|--|
|[bot_russkill](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bot_russkill.py)|Create Mutex (C0042)|--|
|[snake_ransom_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/snake_ransom_mutexes.py)|Create Mutex (C0042)|--|
|[limerat_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/limerat_mutexes.py)|Create Mutex (C0042)|--|
|[qulab_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/qulab_mutexes.py)|Create Mutex (C0042)|--|
|[allaple_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/allaple_mutexes.py)|Create Mutex (C0042)|--|
|[banker_zeus_p2p](https://github.com/CAPESandbox/community/tree/master/modules/signatures/banker_zeus_p2p.py)|Create Mutex (C0042)|--|
|[carberp_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/carberp_mutex.py)|Create Mutex (C0042)|--|
|[rat_poisonivy_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/rat_poisonivy_mutexes.py)|Create Mutex (C0042)|--|
|[satan_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/satan_mutexes.py)|Create Mutex (C0042)|--|
|[medusalocker_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/medusalocker_mutexes.py)|Create Mutex (C0042)|--|
|[remcos_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/remcos_mutexes.py)|Create Mutex (C0042)|--|

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
