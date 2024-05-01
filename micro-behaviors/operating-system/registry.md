<table>
<tr>
<td><b>ID</b></td>
<td><b>C0036</b></td>
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
<td><b>2.3</b></td>
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


# Registry

Malware modifies the registry. 

## Methods

|Name|ID|Description|
|---|---|---|
|**Create Registry Key**|C0036.004|Malware creates a registry key.|
|**Delete Registry Key**|C0036.002|Malware deletes a registry key.|
|**Delete Registry Value**|C0036.007|Malware deletes a registry value.|
|**Open Registry Key**|C0036.003|Malware opens a registry key.|
|**Query Registry Key**|C0036.005|Malware queries a registry key.|
|**Query Registry Value**|C0036.006|Malware queries a registry value.|
|**Set Registry Value**|C0036.001|Malware sets a registry value.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**BlackEnergy**](../../xample-malware/blackenergy.md)|2007|C0036.005|BlackEnergy queries or enumerates a registry key. [[1]](#1)|
|[**BlackEnergy**](../../xample-malware/blackenergy.md)|2007|C0036.006|BlackEnergy queries or enumerates a registry value. [[1]](#1)|
|[**Dark Comet**](../../xample-malware/dark-comet.md)|2008|C0036.001|Dark Comet sets registry values. [[1]](#1)|
|[**Dark Comet**](../../xample-malware/dark-comet.md)|2008|C0036.002|Dark Comet deletes registry keys. [[1]](#1)|
|[**Dark Comet**](../../xample-malware/dark-comet.md)|2008|C0036.005|Dark Comet queries or enumerates registry keys. [[1]](#1)|
|[**Dark Comet**](../../xample-malware/dark-comet.md)|2008|C0036.006|Dark Comet queries or enumerates registry values. [[1]](#1)|
|[**Dark Comet**](../../xample-malware/dark-comet.md)|2008|C0036.007|Dark Comet deletes registry values. [[1]](#1)|
|[**DNSChanger**](../../xample-malware/dnschanger.md)|2011|C0036.001|DNSChanger sets registry keys. [[1]](#1)|
|[**DNSChanger**](../../xample-malware/dnschanger.md)|2011|C0036.006|DNSChanger queries or enumerates registry values. [[1]](#1)|
|[**Gamut**](../../xample-malware/gamut.md)|2014|C0036.001|Gamut sets registry values. [[1]](#1)|
|[**Gamut**](../../xample-malware/gamut.md)|2014|C0036.002|Gamut deletes registry keys. [[1]](#1)|
|[**Gamut**](../../xample-malware/gamut.md)|2014|C0036.005|Gamut queries or enumerates registry keys. [[1]](#1)|
|[**Gamut**](../../xample-malware/gamut.md)|2014|C0036.006|Gamut queries or enumerates registry values. [[1]](#1)|
|[**Gamut**](../../xample-malware/gamut.md)|2014|C0036.007|Gamut deletes registry values. [[1]](#1)|
|[**GoBotKR**](../../xample-malware/gobotkr.md)|2019|C0036.006|GoBotKR queries or enumerates registry values. [[1]](#1)|
|[**Hupigon**](../../xample-malware/hupigon.md)|2013|C0036.001|Hupigon sets registry values. [[1]](#1)|
|[**Hupigon**](../../xample-malware/hupigon.md)|2013|C0036.002|Hupigon deletes registry keys. [[1]](#1)|
|[**Hupigon**](../../xample-malware/hupigon.md)|2013|C0036.005|Hupigon queries or enumerates registry keys. [[1]](#1)|
|[**Hupigon**](../../xample-malware/hupigon.md)|2013|C0036.006|Hupigon queries or enumerates registry values. [[1]](#1)|
|[**Hupigon**](../../xample-malware/hupigon.md)|2013|C0036.007|Hupigon deletes registry values. [[1]](#1)|
|[**Kovter**](../../xample-malware/kovter.md)|2016|C0036.004|Kovter creates or opens registry keys. [[1]](#1)|
|[**Kovter**](../../xample-malware/kovter.md)|2016|C0036.006|Kovter queries or enumerates registry values. [[1]](#1)|
|[**Locky Bart**](../../xample-malware/locky-bart.md)|2017|C0036.001|Locky Bart sets registry values. [[1]](#1)|
|[**Poison Ivy**](../../xample-malware/poison-ivy.md)|2005|C0036.006|Poison Ivy queries or enumerates registry values. [[1]](#1)|
|[**Redhip**](../../xample-malware/redhip.md)|2011|C0036.001|Redhip set registry values. [[1]](#1)|
|[**Redhip**](../../xample-malware/redhip.md)|2011|C0036.002|Redhip deletes registry keys. [[1]](#1)|
|[**Redhip**](../../xample-malware/redhip.md)|2011|C0036.006|Redhip queries or enumerates registry values. [[1]](#1)|
|[**Rombertik**](../../xample-malware/rombertik.md)|2015|C0036.001|Rombertik sets registry values. [[1]](#1)|
|[**Rombertik**](../../xample-malware/rombertik.md)|2015|C0036.002|Rombertik deletes registry keys. [[1]](#1)|
|[**Rombertik**](../../xample-malware/rombertik.md)|2015|C0036.006|Rombertik queries or enumerates registry values. [[1]](#1)|
|[**Shamoon**](../../xample-malware/shamoon.md)|2012|C0036.006|Shamoon queries or enumerates registry values. [[1]](#1)|
|[**Shamoon**](../../xample-malware/shamoon.md)|2012|C0036.007|Shamoon deletes registry values. [[1]](#1)|
|[**UP007**](../../xample-malware/up007.md)|2016|C0036.001|UP007 sets registry values. [[1]](#1)|
|[**UP007**](../../xample-malware/up007.md)|2016|C0036.006|UP007 queries or enumerates registry values. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[set registry key via offline registry library](https://github.com/mandiant/capa-rules/blob/master/host-interaction/registry/set-registry-key-via-offline-registry-library.yml)|Registry::Set Registry Key (C0036.001)|ORSetValue, ORSaveHive|
|[open registry key via offline registry library](https://github.com/mandiant/capa-rules/blob/master/host-interaction/registry/open-registry-key-via-offline-registry-library.yml)|Registry::Open Registry Key (C0036.003)|OROpenHive, OROpenKey|
|[query or enumerate registry key](https://github.com/mandiant/capa-rules/blob/master/host-interaction/registry/query-or-enumerate-registry-key.yml)|Registry::Query Registry Key (C0036.005)|advapi32.RegEnumKey, advapi32.RegEnumKeyEx, advapi32.RegQueryInfoKeyA, ZwQueryKey, ZwEnumerateKey, NtQueryKey, NtEnumerateKey, RtlCheckRegistryKey, SHEnumKeyEx, SHQueryInfoKey, SHRegEnumUSKey, SHRegQueryInfoUSKey, Microsoft.Win32.RegistryKey::GetSubKeyNames, Microsoft.Win32.RegistryKey::OpenBaseKey, Microsoft.Win32.RegistryKey::OpenRemoteBaseKey, Microsoft.Win32.RegistryKey::OpenSubKey|
|[query or enumerate registry value](https://github.com/mandiant/capa-rules/blob/master/host-interaction/registry/query-or-enumerate-registry-value.yml)|Registry::Query Registry Value (C0036.006)|advapi32.RegGetValue, advapi32.RegEnumValue, advapi32.RegQueryValue, advapi32.RegQueryValueEx, advapi32.RegQueryMultipleValues, ZwQueryValueKey, ZwEnumerateValueKey, NtQueryValueKey, NtEnumerateValueKey, RtlQueryRegistryValues, SHGetValue, SHEnumValue, SHRegGetInt, SHRegGetPath, SHRegGetValue, SHQueryValueEx, SHRegGetUSValue, SHOpenRegStream, SHRegEnumUSValue, SHOpenRegStream2, SHRegQueryUSValue, SHRegGetBoolUSValue, SHRegGetValueFromHKCUHKLM, SHRegGetBoolValueFromHKCUHKLM, Microsoft.Win32.RegistryKey::GetValue, Microsoft.Win32.RegistryKey::GetValueKind, Microsoft.Win32.RegistryKey::GetValueNames, Microsoft.Win32.Registry::GetValue|
|[query registry key via offline registry library](https://github.com/mandiant/capa-rules/blob/master/host-interaction/registry/query-registry-key-via-offline-registry-library.yml)|Registry::Query Registry Value (C0036.006)|ORGetValue|
|[create registry key via offline registry library](https://github.com/mandiant/capa-rules/blob/master/host-interaction/registry/create-registry-key-via-offline-registry-library.yml)|Registry::Create Registry Key (C0036.004)|ORCreateHive, ORCreateKey|
|[set registry value](https://github.com/mandiant/capa-rules/blob/master/host-interaction/registry/create/set-registry-value.yml)|Registry::Set Registry Key (C0036.001)|advapi32.RegSetValue, advapi32.RegSetValueEx, advapi32.RegSetKeyValue, ZwSetValueKey, NtSetValueKey, RtlWriteRegistryValue, SHSetValue, SHRegSetPath, SHRegSetValue, SHRegSetUSValue, SHRegWriteUSValue, Microsoft.Win32.RegistryKey::SetValue, Microsoft.Win32.Registry::SetValue|
|[delete registry key](https://github.com/mandiant/capa-rules/blob/master/host-interaction/registry/delete/delete-registry-key.yml)|Registry::Delete Registry Key (C0036.002)|advapi32.RegDeleteKey, advapi32.RegDeleteTree, advapi32.RegDeleteKeyEx, advapi32.RegDeleteKeyTransacted, ZwDeleteKey, NtDeleteKey, SHDeleteKey, SHDeleteEmptyKey, SHRegDeleteEmptyUSKey, Microsoft.Win32.RegistryKey::DeleteSubKey, Microsoft.Win32.RegistryKey::DeleteSubKeyTree|
|[delete registry value](https://github.com/mandiant/capa-rules/blob/master/host-interaction/registry/delete/delete-registry-value.yml)|Registry::Delete Registry Value (C0036.007)|advapi32.RegDeleteValue, advapi32.RegDeleteKeyValue, ZwDeleteValueKey, NtDeleteValueKey, RtlDeleteRegistryValue, SHDeleteValue, SHRegDeleteUSValue, Microsoft.Win32.RegistryKey::DeleteValue|
|[create or open registry key](https://github.com/mandiant/capa-rules/blob/master/lib/create-or-open-registry-key.yml)|Registry::Create Registry Key (C0036.004)|advapi32.RegOpenKey, advapi32.RegOpenKeyEx, advapi32.RegCreateKey, advapi32.RegCreateKeyEx, advapi32.RegOpenCurrentUser, advapi32.RegOpenKeyTransacted, advapi32.RegOpenUserClassesRoot, advapi32.RegCreateKeyTransacted, ZwOpenKey, ZwOpenKeyEx, ZwCreateKey, ZwOpenKeyTransacted, ZwOpenKeyTransactedEx, ZwCreateKeyTransacted, NtOpenKey, NtCreateKey, SHRegOpenUSKey, SHRegCreateUSKey, RtlCreateRegistryKey, Microsoft.Win32.RegistryKey::OpenSubKey, Microsoft.Win32.RegistryKey::OpenBaseKey, Microsoft.Win32.RegistryKey::OpenRemoteBaseKey, Microsoft.Win32.RegistryKey::CreateSubKey|
|[create or open registry key](https://github.com/mandiant/capa-rules/blob/master/lib/create-or-open-registry-key.yml)|Registry::Open Registry Key (C0036.003)|advapi32.RegOpenKey, advapi32.RegOpenKeyEx, advapi32.RegCreateKey, advapi32.RegCreateKeyEx, advapi32.RegOpenCurrentUser, advapi32.RegOpenKeyTransacted, advapi32.RegOpenUserClassesRoot, advapi32.RegCreateKeyTransacted, ZwOpenKey, ZwOpenKeyEx, ZwCreateKey, ZwOpenKeyTransacted, ZwOpenKeyTransactedEx, ZwCreateKeyTransacted, NtOpenKey, NtCreateKey, SHRegOpenUSKey, SHRegCreateUSKey, RtlCreateRegistryKey, Microsoft.Win32.RegistryKey::OpenSubKey, Microsoft.Win32.RegistryKey::OpenBaseKey, Microsoft.Win32.RegistryKey::OpenRemoteBaseKey, Microsoft.Win32.RegistryKey::CreateSubKey|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[persistence_rdp_registry](https://github.com/CAPESandbox/community/tree/master/modules/signatures/persistence_rdp_registry.py)|Registry (C0036)|--|
|[browser_helper_object](https://github.com/CAPESandbox/community/tree/master/modules/signatures/browser_helper_object.py)|Registry (C0036)|--|
|[browser_helper_object](https://github.com/CAPESandbox/community/tree/master/modules/signatures/browser_helper_object.py)|Registry::Set Registry Value (C0036.001)|--|
|[modirat_behavior](https://github.com/CAPESandbox/community/tree/master/modules/signatures/modirat_behavior.py)|Registry (C0036)|--|
|[darkcomet_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/darkcomet_regkeys.py)|Registry (C0036)|--|
|[ransomware_revil_regkey](https://github.com/CAPESandbox/community/tree/master/modules/signatures/ransomware_revil_regkey.py)|Registry (C0036)|--|
|[browser_security](https://github.com/CAPESandbox/community/tree/master/modules/signatures/browser_security.py)|Registry (C0036)|--|
|[browser_security](https://github.com/CAPESandbox/community/tree/master/modules/signatures/browser_security.py)|Registry::Set Registry Value (C0036.001)|--|
|[disables_notificationcenter](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_notificationcenter.py)|Registry (C0036)|--|
|[mapped_drives_uac](https://github.com/CAPESandbox/community/tree/master/modules/signatures/mapped_drives_uac.py)|Registry (C0036)|--|
|[removes_networking_icon](https://github.com/CAPESandbox/community/tree/master/modules/signatures/removes_networking_icon.py)|Registry (C0036)|--|
|[tampers_powershell_logging](https://github.com/CAPESandbox/community/tree/master/modules/signatures/tampers_powershell_logging.py)|Registry (C0036)|--|
|[disables_power_options](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_power_options.py)|Registry (C0036)|--|
|[disables_cpl_disable](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_cpl_disable.py)|Registry (C0036)|--|
|[browser_startpage](https://github.com/CAPESandbox/community/tree/master/modules/signatures/browser_startpage.py)|Registry (C0036)|--|
|[browser_startpage](https://github.com/CAPESandbox/community/tree/master/modules/signatures/browser_startpage.py)|Registry::Set Registry Value (C0036.001)|--|
|[hides_recycle_bin_icon](https://github.com/CAPESandbox/community/tree/master/modules/signatures/hides_recycle_bin_icon.py)|Registry (C0036)|--|
|[disables_restore_default_state](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_restore_default_state.py)|Registry (C0036)|--|
|[disables_auto_app_termination](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_auto_app_termination.py)|Registry (C0036)|--|
|[nemty_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/nemty_regkeys.py)|Registry (C0036)|--|
|[warzonerat_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/warzonerat_regkeys.py)|Registry (C0036)|--|
|[antivm_generic_cpu](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_generic_cpu.py)|Registry (C0036)|--|
|[antivm_generic_cpu](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_generic_cpu.py)|Registry::Query Registry Key (C0036.005)|--|
|[prevents_safeboot](https://github.com/CAPESandbox/community/tree/master/modules/signatures/prevents_safeboot.py)|Registry (C0036)|--|
|[accesses_mailslot](https://github.com/CAPESandbox/community/tree/master/modules/signatures/accesses_mailslot.py)|Registry (C0036)|--|
|[accesses_mailslot](https://github.com/CAPESandbox/community/tree/master/modules/signatures/accesses_mailslot.py)|Registry::Open Registry Key (C0036.003)|--|
|[accesses_netlogon_regkey](https://github.com/CAPESandbox/community/tree/master/modules/signatures/accesses_netlogon_regkey.py)|Registry (C0036)|--|
|[accesses_netlogon_regkey](https://github.com/CAPESandbox/community/tree/master/modules/signatures/accesses_netlogon_regkey.py)|Registry::Open Registry Key (C0036.003)|--|
|[disables_smartscreen](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_smartscreen.py)|Registry (C0036)|--|
|[disables_context_menus](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_context_menus.py)|Registry (C0036)|--|
|[ketrican_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/ketrican_regkeys.py)|Registry (C0036)|--|
|[ketrican_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/ketrican_regkeys.py)|Registry::Query Registry Key (C0036.005)|--|
|[antivm_generic_bios](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_generic_bios.py)|Registry (C0036)|--|
|[antivm_generic_bios](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_generic_bios.py)|Registry::Query Registry Key (C0036.005)|--|
|[evil_grab](https://github.com/kevoreilly/CAPEv2/blob/master/modules/signatures/CAPE.py)|Registry (C0036)|RegCreateKeyExA, RegSetValueExA, RegCreateKeyExW, RegSetValueExW|
|[PlugX](https://github.com/kevoreilly/CAPEv2/blob/master/modules/signatures/CAPE.py)|Registry (C0036)|memcpy, RtlDecompressBuffer|
|[reg_binary](https://github.com/kevoreilly/CAPEv2/blob/master/modules/signatures/CAPE.py)|Registry (C0036)|RegCreateKeyExA, RegSetValueExA, RegCreateKeyExW, RegSetValueExW|
|[stealth_hidden_extension](https://github.com/CAPESandbox/community/tree/master/modules/signatures/stealth_hidden_extension.py)|Registry (C0036)|--|
|[disables_run_command](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_run_command.py)|Registry (C0036)|--|
|[persistence_ifeo](https://github.com/CAPESandbox/community/tree/master/modules/signatures/persistence_ifeo.py)|Registry (C0036)|--|
|[persistence_slient_process_exit](https://github.com/CAPESandbox/community/tree/master/modules/signatures/persistence_slient_process_exit.py)|Registry (C0036)|--|
|[antivm_vbox_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_vbox_keys.py)|Registry (C0036)|--|
|[antivm_vbox_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_vbox_keys.py)|Registry::Query Registry Key (C0036.005)|--|
|[packer_armadillo_regkey](https://github.com/CAPESandbox/community/tree/master/modules/signatures/packer_armadillo_regkey.py)|Registry (C0036)|--|
|[disables_backups](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_backups.py)|Registry (C0036)|--|
|[antianalysis_detectreg](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antianalysis_detectreg.py)|Registry (C0036)|--|
|[antianalysis_detectreg](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antianalysis_detectreg.py)|Registry::Open Registry Key (C0036.003)|--|
|[creates_largekey](https://github.com/CAPESandbox/community/tree/master/modules/signatures/creates_largekey.py)|Registry (C0036)|RegSetValueExA, RegSetValueExW, NtSetValueKey|
|[removes_username_startmenu](https://github.com/CAPESandbox/community/tree/master/modules/signatures/removes_username_startmenu.py)|Registry (C0036)|--|
|[stealth_hiddenreg](https://github.com/CAPESandbox/community/tree/master/modules/signatures/stealth_hiddenreg.py)|Registry (C0036)|--|
|[disables_startmenu_search](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_startmenu_search.py)|Registry (C0036)|--|
|[stealth_hide_notifications](https://github.com/CAPESandbox/community/tree/master/modules/signatures/stealth_hide_notifications.py)|Registry (C0036)|--|
|[antivm_hyperv_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_hyperv_keys.py)|Registry (C0036)|--|
|[antivm_hyperv_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_hyperv_keys.py)|Registry::Query Registry Key (C0036.005)|--|
|[disables_app_launch](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_app_launch.py)|Registry (C0036)|--|
|[neshta_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/neshta_regkeys.py)|Registry (C0036)|RegSetValueExA, RegSetValueExW|
|[creates_nullvalue](https://github.com/CAPESandbox/community/tree/master/modules/signatures/creates_nullvalue.py)|Registry (C0036)|NtCreateKey, NtSetValueKey|
|[geodo_banking_trojan](https://github.com/CAPESandbox/community/tree/master/modules/signatures/geodo_banking_trojan.py)|Registry (C0036)|--|
|[geodo_banking_trojan](https://github.com/CAPESandbox/community/tree/master/modules/signatures/geodo_banking_trojan.py)|Registry::Set Registry Value (C0036.001)|--|
|[modify_attachment_manager](https://github.com/CAPESandbox/community/tree/master/modules/signatures/modify_attachment_manager.py)|Registry (C0036)|--|
|[modify_attachment_manager](https://github.com/CAPESandbox/community/tree/master/modules/signatures/modify_attachment_manager.py)|Registry::Set Registry Value (C0036.001)|--|
|[modify_certs](https://github.com/CAPESandbox/community/tree/master/modules/signatures/modify_certs.py)|Registry (C0036)|--|
|[modify_proxy](https://github.com/CAPESandbox/community/tree/master/modules/signatures/modify_proxy.py)|Registry (C0036)|--|
|[modify_proxy](https://github.com/CAPESandbox/community/tree/master/modules/signatures/modify_proxy.py)|Registry::Set Registry Value (C0036.001)|--|
|[antivm_generic_scsi](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_generic_scsi.py)|Registry (C0036)|RegOpenKeyExW, RegQueryValueExA, RegQueryValueExW, RegOpenKeyExA|
|[antivm_generic_scsi](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_generic_scsi.py)|Registry::Query Registry Key (C0036.005)|RegOpenKeyExW, RegQueryValueExA, RegQueryValueExW, RegOpenKeyExA|
|[disables_appv_virtualization](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_appv_virtualization.py)|Registry (C0036)|--|
|[antivm_xen_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_xen_keys.py)|Registry (C0036)|--|
|[antivm_xen_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_xen_keys.py)|Registry::Query Registry Key (C0036.005)|--|
|[njrat_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/njrat_regkeys.py)|Registry (C0036)|--|
|[antivm_parallels_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_parallels_keys.py)|Registry (C0036)|--|
|[antivm_parallels_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_parallels_keys.py)|Registry::Query Registry Key (C0036.005)|--|
|[blackrat_registry_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/blackrat_registry_keys.py)|Registry (C0036)|RegQueryValueExW, RegSetValueExW|
|[antivm_generic_diskreg](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_generic_diskreg.py)|Registry (C0036)|--|
|[antivm_generic_diskreg](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_generic_diskreg.py)|Registry::Query Registry Key (C0036.005)|--|
|[dotnet_clr_usagelog_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/dotnet_clr_usagelog_regkeys.py)|Registry (C0036)|--|
|[rdptcp_key](https://github.com/CAPESandbox/community/tree/master/modules/signatures/rdptcp_key.py)|Registry (C0036)|--|
|[antivm_vpc_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_vpc_keys.py)|Registry (C0036)|--|
|[antivm_vpc_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_vpc_keys.py)|Registry::Query Registry Key (C0036.005)|--|
|[disables_system_restore](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_system_restore.py)|Registry (C0036)|--|
|[disables_folder_options](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_folder_options.py)|Registry (C0036)|--|
|[office_security](https://github.com/CAPESandbox/community/tree/master/modules/signatures/office_security.py)|Registry (C0036)|--|
|[antivm_bochs_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_bochs_keys.py)|Registry::Query Registry Key (C0036.005)|--|
|[removes_security_maintenance_icon](https://github.com/CAPESandbox/community/tree/master/modules/signatures/removes_security_maintenance_icon.py)|Registry (C0036)|--|
|[tampers_etw](https://github.com/CAPESandbox/community/tree/master/modules/signatures/tampers_etw.py)|Registry (C0036)|--|
|[disables_event_logging](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_event_logging.py)|Registry (C0036)|--|
|[antivm_generic_system](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_generic_system.py)|Registry (C0036)|--|
|[antivm_generic_system](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_generic_system.py)|Registry::Query Registry Key (C0036.005)|--|
|[browser_addon](https://github.com/CAPESandbox/community/tree/master/modules/signatures/browser_addon.py)|Registry (C0036)|--|
|[browser_addon](https://github.com/CAPESandbox/community/tree/master/modules/signatures/browser_addon.py)|Registry::Set Registry Value (C0036.001)|--|
|[enables_wdigest](https://github.com/CAPESandbox/community/tree/master/modules/signatures/enables_wdigest.py)|Registry (C0036)|--|
|[removes_startmenu_defaults](https://github.com/CAPESandbox/community/tree/master/modules/signatures/removes_startmenu_defaults.py)|Registry (C0036)|--|
|[disables_uac](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_uac.py)|Registry (C0036)|--|
|[disables_wer](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_wer.py)|Registry (C0036)|--|
|[antivm_generic_services](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_generic_services.py)|Registry (C0036)|RegOpenKeyExW, RegEnumKeyExW, RegEnumKeyExA, RegOpenKeyExA|
|[antivm_generic_services](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_generic_services.py)|Registry::Query Registry Key (C0036.005)|RegOpenKeyExW, RegEnumKeyExW, RegEnumKeyExA, RegOpenKeyExA|
|[antivm_generic_services](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_generic_services.py)|Registry::Query Registry Value (C0036.006)|RegOpenKeyExW, RegEnumKeyExW, RegEnumKeyExA, RegOpenKeyExA|
|[office_perfkey](https://github.com/CAPESandbox/community/tree/master/modules/signatures/office_perfkey.py)|Registry (C0036)|--|
|[modify_oem_information](https://github.com/CAPESandbox/community/tree/master/modules/signatures/modify_oem_information.py)|Registry (C0036)|--|
|[limerat_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/limerat_regkeys.py)|Registry (C0036)|--|
|[disables_windows_defender_dism](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_windows_defender_dism.py)|Registry (C0036)|--|
|[disables_windows_defender_logging](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_windows_defender_logging.py)|Registry (C0036)|--|
|[removes_windows_defender_contextmenu](https://github.com/CAPESandbox/community/tree/master/modules/signatures/removes_windows_defender_contextmenu.py)|Registry (C0036)|--|
|[disables_browser_warn](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_browser_warn.py)|Registry (C0036)|--|
|[antiemu_wine_reg](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antiemu_wine_reg.py)|Registry (C0036)|--|
|[antiemu_wine_reg](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antiemu_wine_reg.py)|Registry::Query Registry Key (C0036.005)|--|
|[antiav_detectreg](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antiav_detectreg.py)|Registry (C0036)|--|
|[antiav_detectreg](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antiav_detectreg.py)|Registry::Query Registry Key (C0036.005)|--|
|[antivm_vmware_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_vmware_keys.py)|Registry (C0036)|--|
|[antivm_vmware_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antivm_vmware_keys.py)|Registry::Query Registry Key (C0036.005)|--|
|[disables_windowsupdate](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_windowsupdate.py)|Registry (C0036)|--|
|[recon_programs](https://github.com/CAPESandbox/community/tree/master/modules/signatures/recon_programs.py)|Registry (C0036)|RegQueryValueExA, RegQueryValueExW|
|[antiav_srp](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antiav_srp.py)|Registry (C0036)|--|
|[antiav_srp](https://github.com/CAPESandbox/community/tree/master/modules/signatures/antiav_srp.py)|Registry::Set Registry Value (C0036.001)|--|
|[recon_fingerprint](https://github.com/CAPESandbox/community/tree/master/modules/signatures/recon_fingerprint.py)|Registry (C0036)|--|
|[removes_pinned_programs](https://github.com/CAPESandbox/community/tree/master/modules/signatures/removes_pinned_programs.py)|Registry (C0036)|--|
|[medusalocker_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/medusalocker_regkeys.py)|Registry (C0036)|--|
|[bypass_firewall](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bypass_firewall.py)|Registry (C0036)|--|
|[bypass_firewall](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bypass_firewall.py)|Registry::Set Registry Value (C0036.001)|--|
|[remcos_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/remcos_regkeys.py)|Registry (C0036)|--|

### C0036.005 Snippet
<details>
<summary> Registry::Query Registry Key </summary>
SHA256: 1e0215f67fb7b02bc44f33bf6a5b884c3061cbeb38e0150b559635458951fa53
Location: 0x408723
<pre>
push    eax     ; phkResult: stores pointer to handle containing open registry key
push    0x1     ; samDesired: Desired access rights for opened key.  0x1 is KEY_QUERY_VALUE, which is required to query the value of the sought registry key
push    0x0     ; ulOptions: Optional key set to 0, so no options passed to registry key
push    ecx     ; lpSubKey: Optional parameter indicating a subkey to read from
push    edx     ; handle to open registry key or name of registry key to open
call    dword ptr [->ADVAPI32.DLL::RegOpenKeyExA] ; Windows API call which opens registry key for the query
</pre>
</details>

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

