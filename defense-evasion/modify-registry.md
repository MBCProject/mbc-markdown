<table>
<tr>
<td><b>ID</b></td>
<td><b>E1112</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../defense-evasion">Defense Evasion</a>, <a href="../persistence">Persistence</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Modify Registry (<a href="https://attack.mitre.org/techniques/T1112">T1112</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.3</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>2 August 2022</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>28 April 2024</b></td>
</tr>
</table>


# Modify Registry

Malware may make changes to the Windows Registry to hide execution or to persist on the system (note that ATT&CK does not extend this behavior to the Persistence objective). The Windows registry is a database that stores low-level settings for the operating system and for applications that opt to use the registry. Malware may create, delete, or modify registry keys and values to change the behavior of the system or certain applications. For instance, malware may modify registry keys to enable remote desktop connections, disable security features, or to automatically start the malware whenever the system boots. This technique is commonly used by various types of malware, including ransomware, trojans, and worms.


See ATT&CK: **Modify Registry ([T1112](https://attack.mitre.org/techniques/T1112/))**.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|--|GoBotKR can modify registry keys to disable Task Manager, Registry Editor and Command Prompt. [[2]](#2)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|The malware adds many entries to the registry. [[3]](#3)|
|[**Gamut**](../xample-malware/gamut.md)|2014|--|The malware adds a registry key. [[4]](#4)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|The malware modifies the registry during execution. [[5]](#5)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|--|Shamoon disables remote user account control by enabling the registry key LocalAccountTokenFilterPolicy. [[6]](#6)|
|[**CHOPSTICK**](../xample-malware/chopstick.md)|2015|--|CHOPSTICK may encrypt and store configuration data inside a registry key. [[7]](#7)|
|[**Clipminer**](../xample-malware/clipminer.md)|2011|--|Clipminer edits the registry. [[8]](#8)|

## Detection

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[persistence_remotedesktop](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/persistence_remotedesktop.py)|Modify Registry (E1112)|--|
|[browser_helper_object](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/browser_bho.py)|Modify Registry (E1112)|--|
|[browser_security](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/browser_security.py)|Modify Registry (E1112)|--|
|[disables_notificationcenter](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_notificationcenter.py)|Modify Registry (E1112)|--|
|[removes_networking_icon](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/removes_networking_icon.py)|Modify Registry (E1112)|--|
|[tampers_powershell_logging](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/tampers_powershell_logging.py)|Modify Registry (E1112)|--|
|[disables_power_options](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_power_options.py)|Modify Registry (E1112)|--|
|[disables_cpl_disable](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_cpl_disable.py)|Modify Registry (E1112)|--|
|[browser_startpage](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/browser_startpage.py)|Modify Registry (E1112)|--|
|[persistence_registry_script](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/persistence_registry_script.py)|Modify Registry (E1112)|RegSetValueExA, RegSetValueExW, NtSetValueKey|
|[hides_recycle_bin_icon](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/hides_recycle_bin_icon.py)|Modify Registry (E1112)|--|
|[disables_restore_default_state](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_restore_default_state.py)|Modify Registry (E1112)|--|
|[disables_auto_app_termination](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_auto_app_termination.py)|Modify Registry (E1112)|--|
|[nemty_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/nemty_regkeys.py)|Modify Registry (E1112)|--|
|[warzonerat_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/warzonerat_regkeys.py)|Modify Registry (E1112)|--|
|[prevents_safeboot](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/prevents_safeboot.py)|Modify Registry (E1112)|--|
|[disables_smartscreen](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_smartscreen.py)|Modify Registry (E1112)|--|
|[disables_context_menus](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_context_menus.py)|Modify Registry (E1112)|--|
|[reg_binary](https://github.com/kevoreilly/CAPEv2/blob/master/modules/signatures/windows/CAPE.py)|Modify Registry (E1112)|RegCreateKeyExA, RegSetValueExA, RegCreateKeyExW, RegSetValueExW|
|[stealth_hidden_extension](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/stealth_hidden_extension.py)|Modify Registry (E1112)|--|
|[disables_run_command](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_run_command.py)|Modify Registry (E1112)|--|
|[persistence_ifeo](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/persistence_ifeo.py)|Modify Registry (E1112)|--|
|[persistence_slient_process_exit](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/persistence_slient_process_exit.py)|Modify Registry (E1112)|--|
|[disables_backups](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_backups.py)|Modify Registry (E1112)|--|
|[creates_largekey](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/creates_largekey.py)|Modify Registry (E1112)|RegSetValueExA, RegSetValueExW, NtSetValueKey|
|[removes_username_startmenu](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/removes_username_startmenu.py)|Modify Registry (E1112)|--|
|[stealth_hiddenreg](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/stealth_hiddenreg.py)|Modify Registry (E1112)|--|
|[disables_startmenu_search](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_startmenu_search.py)|Modify Registry (E1112)|--|
|[stealth_hide_notifications](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/stealth_hide_notifications.py)|Modify Registry (E1112)|--|
|[disables_app_launch](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_app_launch.py)|Modify Registry (E1112)|--|
|[neshta_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/neshta_regkeys.py)|Modify Registry (E1112)|RegSetValueExA, RegSetValueExW|
|[creates_nullvalue](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/creates_nullvalue.py)|Modify Registry (E1112)|NtCreateKey, NtSetValueKey|
|[geodo_banking_trojan](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/geodo_banking_trojan.py)|Modify Registry (E1112)|--|
|[persistence_autorun](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/persistence_autorun.py)|Modify Registry (E1112)|NtSetValueKey, RegSetValueExA, RegSetValueExW, CreateServiceW, CreateServiceA|
|[persistence_autorun_tasks](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/persistence_autorun_tasks.py)|Modify Registry (E1112)|NtSetValueKey, RegSetValueExA, RegSetValueExW, CreateServiceW, CreateServiceA|
|[persistence_safeboot](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/persistence_safeboot.py)|Modify Registry (E1112)|--|
|[modify_attachment_manager](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/modify_attachment_manager.py)|Modify Registry (E1112)|--|
|[modify_certs](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/modify_certs.py)|Modify Registry (E1112)|--|
|[modify_proxy](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/modify_proxy.py)|Modify Registry (E1112)|--|
|[disables_appv_virtualization](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_appv_virtualization.py)|Modify Registry (E1112)|--|
|[njrat_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/njrat_regkeys.py)|Modify Registry (E1112)|--|
|[modify_uac_prompt](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/modify_uac_prompt.py)|Modify Registry (E1112)|--|
|[blackrat_registry_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/blackrat_registry_keys.py)|Modify Registry (E1112)|RegQueryValueExW, RegSetValueExW|
|[rdptcp_key](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rdptcp_key.py)|Modify Registry (E1112)|--|
|[disables_system_restore](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_system_restore.py)|Modify Registry (E1112)|--|
|[disables_folder_options](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_folder_options.py)|Modify Registry (E1112)|--|
|[office_security](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/office_security.py)|Modify Registry (E1112)|--|
|[removes_security_maintenance_icon](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/removes_security_maintenance_icon.py)|Modify Registry (E1112)|--|
|[tampers_etw](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/tampers_etw.py)|Modify Registry (E1112)|--|
|[disables_event_logging](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_event_logging.py)|Modify Registry (E1112)|--|
|[browser_addon](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/browser_addon.py)|Modify Registry (E1112)|--|
|[removes_startmenu_defaults](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/removes_startmenu_defaults.py)|Modify Registry (E1112)|--|
|[disables_uac](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_uac.py)|Modify Registry (E1112)|--|
|[modify_security_center_warnings](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/modify_security_center_warnings.py)|Modify Registry (E1112)|--|
|[disables_wer](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_wer.py)|Modify Registry (E1112)|--|
|[office_perfkey](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/office_perfkey.py)|Modify Registry (E1112)|--|
|[modify_oem_information](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/modify_oem_information.py)|Modify Registry (E1112)|--|
|[limerat_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/limerat_regkeys.py)|Modify Registry (E1112)|--|
|[disables_windows_defender_dism](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_windows_defender_dism.py)|Modify Registry (E1112)|--|
|[disables_windows_defender_logging](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_windows_defender_logging.py)|Modify Registry (E1112)|--|
|[removes_windows_defender_contextmenu](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/removes_windows_defender_contextmenu.py)|Modify Registry (E1112)|--|
|[disables_browser_warn](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_browser_warn.py)|Modify Registry (E1112)|--|
|[disables_windowsupdate](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_windowsupdate.py)|Modify Registry (E1112)|--|
|[removes_pinned_programs](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/removes_pinned_programs.py)|Modify Registry (E1112)|--|
|[medusalocker_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/medusalocker_regkeys.py)|Modify Registry (E1112)|--|
|[bypass_firewall](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/bypass_firewall.py)|Modify Registry (E1112)|--|
|[remcos_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/remcos_regkeys.py)|Modify Registry (E1112)|--|

## References

<a name="1">[1]</a> https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/clipminer-bitcoin-mining-hijacking

<a name="2">[2]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="3">[3]</a> https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/HUPIGON

<a name="4">[4]</a> https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/gamut-spambot-analysis/

<a name="5">[5]</a> https://labs.vipre.com/analysis-of-kovter-a-very-clever-piece-of-malware/#:~:text=Kovter%20copies%20the%20fileless%20persistence,written%20on%20to%20the%20filesystem.

<a name="6">[6]</a> https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-returns-to-wipe-systems-in-middle-east-europe/

<a name="7">[7]</a> https://web.archive.org/web/20210307034415/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf

<a name="8">[8]</a> https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/clipminer-bitcoin-mining-hijacking

