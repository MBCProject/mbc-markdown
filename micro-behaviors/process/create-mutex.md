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
<td><b>16 September 2024</b></td>
</tr>
</table>


# Create Mutex

Malware creates a mutex. Mutexes may be created for synchronization purposes (two or more processes/threads to share a resource).

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

|Tool: CAPE|Class|Mapping|APIs|
|---|---|---|---|
|[allaple_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/worm_allaple_mutex.py)|AllapleMutexes|Create Mutex (C0042)|--|
|[andromut_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/downloader_andromut_mutex.py)|AndromutMutexes|Create Mutex (C0042)|--|
|[asyncrat_mutex_raccoon](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/infostealer_raccoon.py)|RaccoonInfoStealerMutex|Create Mutex (C0042)|--|
|[asyncrat_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/asyncrat_mutex.py)|AsyncRatMutex|Create Mutex (C0042)|--|
|[azorult_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/infostealer_azorult_mutex.py)|AzorultMutexes|Create Mutex (C0042)|--|
|[banker_cridex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/banker_cridex.py)|Cridex|Create Mutex (C0042)|--|
|[banker_spyeye_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/banker_spyeye_mutex.py)|SpyEyeMutexes|Create Mutex (C0042)|--|
|[banker_zeus_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/banker_zeus_mutex.py)|ZeusMutexes|Create Mutex (C0042)|--|
|[banker_zeus_p2p](https://github.com/CAPESandbox/community/blob/master/modules/signatures/all/banker_zeus_p2p.py)|ZeusP2P|Create Mutex (C0042)|--|
|[blackrat_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_blackremote.py)|BlackRATMutexes|Create Mutex (C0042)|--|
|[bot_russkill](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/bot_russkill.py)|Ruskill|Create Mutex (C0042)|--|
|[carberp_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/carberp_mutex.py)|CarberpMutexes|Create Mutex (C0042)|--|
|[crat_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_crat.py)|CRATMutexes|Create Mutex (C0042)|--|
|[cryptomix_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_cryptomix.py)|CryptoMixMutexes|Create Mutex (C0042)|--|
|[cypherit_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/cypherit_mutex.py)|CypherITMutexes|Create Mutex (C0042)|--|
|[dcrat_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_dcrat.py)|DCRatMutex|Create Mutex (C0042)|--|
|[deepfreeze_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/deepfreeze_mutex.py)|DeepFreezeMutex|Create Mutex (C0042)|--|
|[dharma_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_dharma.py)|DharmaMutexes|Create Mutex (C0042)|--|
|[fleercivet_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/trojan_fleercivet_mutex.py)|FleerCivetMutexes|Create Mutex (C0042)|--|
|[fonix_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_fonix_mutex.py)|FonixMutexes|Create Mutex (C0042)|--|
|[gandcrab_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_gandcrab.py)|GandCrabMutexes|Create Mutex (C0042)|--|
|[geodo_banking_trojan](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/banker_geodo.py)|Geodo|Create Mutex (C0042)|--|
|[germanwiper_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_germanwiper.py)|GermanWiperMutexes|Create Mutex (C0042)|--|
|[limerat_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_limerat.py)|LimeRATMutexes|Create Mutex (C0042)|--|
|[lokibot_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/trojan_lokibot_mutex.py)|LokibotMutexes|Create Mutex (C0042)|--|
|[medusalocker_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_medusalocker.py)|MedusaLockerMutexes|Create Mutex (C0042)|--|
|[nemty_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_nemty.py)|NemtyMutexes|Create Mutex (C0042)|--|
|[neshta_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/virus_neshta.py)|NeshtaMutexes|Create Mutex (C0042)|--|
|[obliquerat_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_oblique.py)|ObliquekRATMutexes|Create Mutex (C0042)|--|
|[okrum_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/backdoor_okrum_mutex.py)|OkrumMutexes|Create Mutex (C0042)|--|
|[packer_armadillo_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/packer_armadillo_mutex.py)|ArmadilloMutex|Create Mutex (C0042)|--|
|[parallax_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_parallax_mutex.py)|ParallaxMutexes|Create Mutex (C0042)|--|
|[phorpiex_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/downloader_phorpiex_mutex.py)|PhorpiexMutexes|Create Mutex (C0042)|--|
|[powerpool_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/powerpool_mutex.py)|PowerpoolMutexes|Create Mutex (C0042)|--|
|[protonbot_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/downloader_protonbot_mutex.py)|ProtonBotMutexes|Create Mutex (C0042)|--|
|[pysa_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_pysa_mutex.py)|PYSAMutexes|Create Mutex (C0042)|--|
|[qulab_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/infostealer_qulab.py)|QulabMutexes|Create Mutex (C0042)|--|
|[ransomware_radamant](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_radamant.py)|RansomwareRadamant|Create Mutex (C0042)|--|
|[rat_beebus_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_beebus_mutex.py)|BeebusMutexes|Create Mutex (C0042)|--|
|[rat_fynloski_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_fynloski_mutex.py)|FynloskiMutexes|Create Mutex (C0042)|--|
|[rat_luminosity](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_luminosity.py)|LuminosityRAT|Create Mutex (C0042)| CryptHashData, NtCreateMutant|
|[rat_nanocore](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_nanocore.py)|NanocoreRAT|Create Mutex (C0042)|--|
|[rat_pcclient](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_pcclient.py)|PcClientMutexes|Create Mutex (C0042)|--|
|[rat_plugx_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_plugx_mutex.py)|PlugxMutexes|Create Mutex (C0042)|--|
|[rat_poisonivy_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_poisonivy.py)|PoisonIvyMutexes|Create Mutex (C0042)|--|
|[rat_quasar_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_quasar.py)|QuasarMutexes|Create Mutex (C0042)|--|
|[rat_spynet](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_spynet.py)|SpynetRat|Create Mutex (C0042)|--|
|[rat_xtreme_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_xtreme_mutex.py)|XtremeMutexes|Create Mutex (C0042)|--|
|[ratsnif_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_ratsnif_mutex.py)|RatsnifMutexes|Create Mutex (C0042)|--|
|[remcos_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/remcos.py)|RemcosMutexes|Create Mutex (C0042)|--|
|[renamer_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/virus_renamer_mutex.py)|RenamerMutexes|Create Mutex (C0042)|--|
|[revil_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_revil_mutex.py)|RevilMutexes|Create Mutex (C0042)|--|
|[satan_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_satan_mutex.py)|SatanMutexes|Create Mutex (C0042)|--|
|[snake_ransom_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_snake_mutex.py)|SnakeRansomMutexes|Create Mutex (C0042)|--|
|[stop_ransom_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_stop.py)|StopRansomMutexes|Create Mutex (C0042)|--|
|[targeted_flame](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/targeted_flame.py)|Flame|Create Mutex (C0042)|--|
|[trickbot_mutex](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/trickbot_mutex.py)|TrickBotMutexes|Create Mutex (C0042)|--|
|[ursnif_behavior](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/trojan_ursnif.py)|UrsnifBehavior|Create Mutex (C0042)|--|
|[venomrat_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_venom.py)|VenomRAT|Create Mutex (C0042)|--|
|[xpertrat_mutexes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_xpert.py)|XpertRATMutexes|Create Mutex (C0042)|--|![image](https://github.com/user-attachments/assets/c0dc90a3-80a1-4ce2-9ba9-5eae9c7852b7)

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
