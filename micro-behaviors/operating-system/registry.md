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

|Tool: CAPE|Class|Mapping|APIs|
|---|---|---|---|
|[darkcomet_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/darkcomet_regkeys.py)|DarkCometRegkeys|Registry (C0036)|--|
|[ransomware_revil_regkey](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_revil_regkey.py)|RevilRegkey|Registry (C0036)|--|
|[browser_security](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/browser_security.py)|BrowserSecurity| Registry (C0036), Registry::Set Registry Value (C0036.001)|--|
|[disables_notificationcenter](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_notificationcenter.py)|DisablesNotificationCenter|Registry (C0036)|--|
|[removes_networking_icon](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/removes_networking_icon.py)|RemovesNetworkingIcon|Registry (C0036)|--|
|[tampers_powershell_logging](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/tampers_powershell_logging.py)|TampersPowerShellLogging|Registry (C0036)|--|
|[disables_power_options](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_power_options.py)|DisablesPowerOptions|Registry (C0036)|--|
|[browser_startpage](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/browser_startpage.py)|browser_startpage|Registry (C0036), Registry::Set Registry Value (C0036.001)|--|
|[disables_restore_default_state](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_restore_default_state.py)|DisablesRestoreDefaultState|Registry (C0036)|--|
|[antivm_generic_cpu](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_generic_cpu.py)|AntiVMCPU|Registry (C0036), Registry::Query Registry Key (C0036.005)| RegQueryValueExW, RegQueryValueExA, NtQueryValueKey|
|[prevents_safeboot](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/prevents_safeboot.py)|prevents_safeboot|Registry (C0036)|--|
|[disables_smartscreen](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_smartscreen.py)|DisablesSmartScreen|Registry (C0036)|--|
|[disables_context_menus](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_context_menus.py)|DisablesContextMenus|Registry (C0036)|--|
|[antivm_generic_bios](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_generic_bios.py)|AntiVMBios|Registry (C0036), Registry::Query Registry Key (C0036.005)|--|
|[disables_run_command](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_run_command.py)|DisableRunCommand|Registry (C0036)|--|
|[persistence_ifeo](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/persistence_ifeo.py)|Registry (C0036)|--|
|[antivm_vbox_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_vbox_keys.py)|VBoxDetectKeys|Registry (C0036), Registry::Query Registry Key (C0036.005)|--|
|[packer_armadillo_regkey](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/packer_armadillo_regkey.py)|ArmadilloRegKey|Registry (C0036)|--|
|[disables_backups](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_backups.py)|DisablesBackups|Registry (C0036)|--|
|[antianalysis_detectreg](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antianalysis_detectreg.py)|AntiAnalysisDetectReg|Registry (C0036), Registry::Open Registry Key (C0036.003)|--|
|[creates_largekey](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/creates_largekey.py)|CreatesLargeKey|Registry (C0036)|RegSetValueExA, RegSetValueExW, NtSetValueKey|
|[removes_username_startmenu](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/removes_username_startmenu.py)|RemovesUsernameStartMenu|Registry (C0036)|--|
|[stealth_hiddenreg](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/stealth_hiddenreg.py)|StealthHiddenReg|Registry (C0036)|--|
|[disables_startmenu_search](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_startmenu_search.py)|DisablesStartMenuSearch|Registry (C0036)|--|
|[antivm_hyperv_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_hyperv_keys.py)|HyperVDetectKeys|Registry (C0036), Registry::Query Registry Key (C0036.005)|--|
|[creates_nullvalue](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/creates_nullvalue.py)|CreatesNullValue|Registry (C0036)|NtCreateKey, NtSetValueKey|
|[antivm_generic_scsi](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_generic_scsi.py)|AntiVMSCSI|Registry (C0036), Registry::Query Registry Key (C0036.005)|RegOpenKeyExW, RegQueryValueExA, RegQueryValueExW, RegOpenKeyExA|
|[disables_appv_virtualization](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_appv_virtualization.py)|DisablesAppVirtualiztion|Registry (C0036)|--|
|[antivm_xen_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_xen_keys.py)|XenDetectKeys|Registry (C0036), Registry::Query Registry Key (C0036.005)|--|
|[antivm_parallels_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_parallels_keys.py)|ParallelsDetectKeys|Registry (C0036), Registry::Query Registry Key (C0036.005)|--|
|[antivm_generic_diskreg](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_generic_diskreg.py)|AntiVMDiskReg|Registry (C0036), Registry::Query Registry Key (C0036.005)|--|
|[antivm_vpc_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_vpc_keys.py)|AntiVMDiskReg|Registry (C0036), Registry::Query Registry Key (C0036.005)|--|
|[disables_folder_options](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_folder_options.py)|DisableFolderOptions|Registry (C0036)|--|
|[office_security](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/office_security.py)|OfficeSecurity|Registry (C0036)|--|
|[antivm_bochs_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_bochs_keys.py)|BochsDetectKeys|Registry::Query Registry Key (C0036.005)|--|
|[tampers_etw](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/tampers_etw.py)|TampersETW|Registry (C0036)|--|
|[disables_event_logging](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_event_logging.py)|DisablesEventLogging|Registry (C0036)|--|
|[antivm_generic_system](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_generic_system.py)|AntiVMSystem|Registry (C0036), Registry::Query Registry Key (C0036.005)|--
|[browser_addon](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/browser_addon.py)|BrowserAddon|Registry (C0036),Registry::Set Registry Value (C0036.001)|--|
|[removes_startmenu_defaults](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/removes_startmenu_defaults.py)|RemovesStartMenuDefaults|Registry (C0036)|--|
|[disables_uac](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_uac.py)|DisablesUAC|Registry (C0036)|--|
|[disables_wer](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_wer.py)|DisablesWER|Registry (C0036)|--|
|[antivm_generic_services](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_generic_services.py)|AntiVMServices|Registry (C0036), Registry::Query Registry Key (C0036.005), Registry::Query Registry Value (C0036.006)|RegOpenKeyExW, RegEnumKeyExW, RegEnumKeyExA, RegOpenKeyExA|
|[antiav_detectreg](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antiav_detectreg.py)|AntiAVDetectReg|Registry (C0036), Registry::Query Registry Key (C0036.005)|--|
|[antivm_vmware_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_vmware_keys.py)|VMwareDetectKeys|Registry (C0036), Registry::Query Registry Key (C0036.005)|--|
|[disables_windowsupdate](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_windowsupdate.py)|DisablesWindowsUpdate|Registry (C0036)|--|
|[recon_programs](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/recon_programs.py)|InstalledApps|Registry (C0036)|RegQueryValueExA, RegQueryValueExW|
|[antiav_srp](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antiav_srp.py)|AntiAVSRP|Registry (C0036), Registry::Set Registry Value (C0036.001)|--|
|[recon_fingerprint](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/recon_fingerprint.py)|Fingerprint|Registry (C0036)|--|
|[removes_pinned_programs](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/removes_pinned_programs.py)|RemovesPinnedPrograms|Registry (C0036)|--|
|[bypass_firewall](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/bypass_firewall.py)|BypassFirewall|Registry (C0036), Registry::Set Registry Value (C0036.001)|--|
|[antivm_vmware_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_vmware_keys.py)|VMwareDetectKeys|Registry (C0036), Registry::Query Registry Key (C0036.005)|--|
|[antivm_vbox_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_vbox_keys.py)|VBoxDetectKeys|Registry (C0036), Registry::Query Registry Key (C0036.005)|--|
|[disables_smartscreen](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_smartscreen.py)|DisablesSmartScreen|Registry (C0036)|--|
|[recon_fingerprint](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/recon_fingerprint.py)|Fingerprint|Registry (C0036)|--|
|[browser_proxy](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/browser_proxy.py)|ModifyProxy|Registry (C0036), Registry::Set Registry Value (C0036.001)|--|
|[stealth_hiddenextension](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/stealth_hiddenextension.py)|StealthHiddenExtension|Registry (C0036)|--|
|[rat_blackremote](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_blackremote.py)|BlackRATRegistryKeys|Registry (C0036)| RegSetValueExW, RegQueryValueExW|
|[disables_event_logging](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_event_logging.py)|DisablesEventLogging|Registry (C0036)|--|
|[disables_sysrestore](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_sysrestore.py)|DisablesSystemRestore|Registry (C0036)|--|
|[removes_pinned_programs](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/removes_pinned_programs.py)|RemovesPinnedPrograms|Registry (C0036)|--|
|[removes_startmenu_defaults](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/removes_startmenu_defaults.py)|RemovesStartMenuDefaults|Registry (C0036)|--|
|[rat_warzone](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_warzone.py)|WarzoneRATRegkeys|Registry (C0036)|--|
|[bypass_firewall](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/bypass_firewall.py)|BypassFirewall|Registry (C0036), Registry::Set Registry Value (C0036.001)|--|
|[stealth_hidenotifications](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/stealth_hidenotifications.py)|StealthHideNotifications|Registry (C0036)|--|
|[stealth_hiddenreg](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/stealth_hiddenreg.py)|StealthHiddenReg|Registry (C0036)|--|
|[ransomware_revil_regkey](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_revil_regkey.py)|RevilRegkey|Registry (C0036)|--|
|[accesses_netlogon](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/accesses_netlogon.py)|AccessesMailslot|Registry (C0036), Registry::Open Registry Key (C0036.003)]|--|
|[accesses_netlogon](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/accesses_netlogon.py)|AccessesNetlogonRegkey|Registry (C0036), Registry::Open Registry Key (C0036.003)]|--|
|[browser_addon](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/browser_addon.py)|BrowserAddon|Registry (C0036), Registry::Set Registry Value (C0036.001)|--|
|[antivm_generic_scsi](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_generic_scsi.py)|AntiVMSCSI|Registry (C0036), Registry::Query Registry Key (C0036.005)| RegOpenKeyExA, RegOpenKeyExW, RegQueryValueExA, RegQueryValueExW|
|[recon_programs](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/recon_programs.py)|InstalledApps|Registry (C0036)| RegQueryValueExA, RegQueryValueExW|
|[disables_windefender](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_windefender.py)|DisablesWindowsDefender|Registry (C0036)|--|
|[disables_windefender](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_windefender.py)|RemovesWindowsDefenderContextMenu|Registry (C0036)|--|
|[disables_windefender](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_windefender.py)|DisablesWindowsDefenderLogging|Registry (C0036)|--|
|[disables_windefender](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_windefender.py)|DisablesWindowsDefenderDISM|Registry (C0036)|--|
|[office_dll_loading](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/office_dll_loading.py)|OfficePerfKey|Registry (C0036)|--|
|[disables_folder_options](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_folder_options.py)|DisableFolderOptions|Registry (C0036)|--|
|[ransomware_radamant](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_radamant.py)|RansomwareRadamant|Registry (C0036)|--|
|[antiav_bypass](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antiav_bypass.py)|ModifiesAttachmentManager|Registry (C0036), Registry::Set Registry Value (C0036.001)|--|
|[rat_spynet](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_spynet.py)|SpynetRat|Registry (C0036)|--|
|[rat_njrat_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_njrat_regkeys.py)|NjratRegkeys|Registry (C0036)|--|
|[disables_uac](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_uac.py)|DisablesUAC|Registry (C0036)|--|
|[remcos](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/remcos.py)|RemcosRegkeys|Registry (C0036)|--|
|[disables_power_options](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_power_options.py)|DisablesPowerOptions|Registry (C0036)|--|
|[browser_bho](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/browser_bho.py)|BrowserHelperObject|Registry (C0036), Registry::Set Registry Value (C0036.001)|--|
|[disables_windowsupdate](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_windowsupdate.py)|DisablesWindowsUpdate|Registry (C0036)|--|
|[antivm_vpc_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_vpc_keys.py)|VPCDetectKeys|Registry (C0036), Registry::Query Registry Key (C0036.005)|--|
|[antivm_hyperv_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_hyperv_keys.py)|HyperVDetectKeys|Registry (C0036), Registry::Query Registry Key (C0036.005)|--|
|[antivm_xen_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_xen_keys.py)|XenDetectKeys|Registry (C0036), Registry::Query Registry Key (C0036.005)|--|
|[antivm_generic_system](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_generic_system.py)|AntiVMSystem|Registry (C0036), Registry::Query Registry Key (C0036.005)|--|
|[antiemu_wine](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antiemu_wine.py)|WineDetectReg|Registry (C0036), Registry::Query Registry Key (C0036.005)|--|
|[virus_neshta](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/virus_neshta.py)|NeshtaRegKeys|Registry (C0036)| RegSetValueExA, RegSetValueExW|
|[antivm_generic_bios](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_generic_bios.py)|AntiVMBios|Registry (C0036), Registry::Query Registry Key (C0036.005)|--|
|[hides_recyclebin_icon](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/hides_recyclebin_icon.py)|HidesRecycleBinIcon|Registry (C0036)|--|
|[antiav_detectreg](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antiav_detectreg.py)|AntiAVDetectReg|Registry (C0036), Registry::Query Registry Key (C0036.005)|--|
|[browser_security](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/browser_security.py)|BrowserSecurity|Registry (C0036), Registry::Set Registry Value (C0036.001)|--|
|[banker_geodo](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/banker_geodo.py)|Geodo|Registry (C0036), Registry::Set Registry Value (C0036.001)|--|
|[antivm_generic_services](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_generic_services.py)|AntiVMServices|Registry (C0036), Registry::Query Registry Key (C0036.005) Registry::Query Registry Value (C0036.006)| RegOpenKeyExA, RegEnumKeyExA, RegOpenKeyExW, RegEnumKeyExW|
|[antiav_srp](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antiav_srp.py)|AntiAVSRP|Registry (C0036), Registry::Set Registry Value (C0036.001)|--|
|[antivm_parallels_keys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_parallels_keys.py)|ParallelsDetectKeys|Registry (C0036), Registry::Query Registry Key (C0036.005)|--|
|[disables_startmenu_search](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_startmenu_search.py)|DisablesStartMenuSearch|Registry (C0036)|--|
|[office_security](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/office_security.py)|OfficeSecurity|Registry (C0036)|--|
|[tampers_etw](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/tampers_etw.py)|TampersETW|Registry (C0036)|--|
|[persistence_ifeo](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/persistence_ifeo.py)|PersistenceIFEO|Registry (C0036)|--|
|[persistence_ifeo](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/persistence_ifeo.py)|PersistenceSilentProcessExit|Registry (C0036)|--|
|[persistence_shim](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/persistence_shim.py)|PersistenceShimDatabase|Registry (C0036)|--|
|[disables_app](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_app.py)|DisablesAppLaunch|Registry (C0036)|--|
|[disables_backups](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_backups.py)|DisablesBackups|Registry (C0036)|--|
|[disables_appv_virtualization](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_appv_virtualization.py)|DisablesAppVirtualiztion|Registry (C0036)|--|
|[disables_browserwarn](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_browserwarn.py)|DisablesBrowserWarn|Registry (C0036)|--|
|[creates_largekey](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/creates_largekey.py)|CreatesLargeKey|Registry (C0036)| NtSetValueKey, RegSetValueExA RegSetValueExW])|
|[remote_desktop](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/remote_desktop.py)|RDPTCPKey|Registry (C0036)|--|
|[ransomware_medusalocker](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_medusalocker.py)|MedusaLockerRegkeys|Registry (C0036)|--|
|[antivm_generic_cpu](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_generic_cpu.py)|AntiVMCPU|Registry (C0036), Registry::Query Registry Key (C0036.005)| filter_apinames = set(|
|[disables_app_autotermination](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_app_autotermination.py)|DisablesAutomaticAppTermination|Registry (C0036)|--|
|[disables_restore_default_state](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_restore_default_state.py)|DisablesRestoreDefaultState|Registry (C0036)|--|
|[disables_context_menus](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_context_menus.py)|DisablesContextMenus|Registry (C0036)|--|
|[ransomware_nemty](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_nemty.py)|NemtyRegkeys|Registry (C0036)|--|
|[ransomware_nemty](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_nemty.py)|NemtyNote|--| NtWriteFile|
|[ransomware_nemty](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/ransomware_nemty.py)|NemtyNetworkActivity|--| InternetOpenA, InternetOpenUrlA|
|[disables_cpl_display](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_cpl_display.py)|DisablesCPLDisplay|Registry (C0036)|--|
|[antivm_generic_diskreg](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antivm_generic_diskreg.py)|AntiVMDiskReg|Registry (C0036), Registry::Query Registry Key (C0036.005)|--|
|[modifies_oem](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/modifies_oem.py)|ModifiesOEMInformation|Registry (C0036)|--|
|[forces_mappeddrives_uac](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/forces_mappeddrives_uac.py)|MappedDrivesUAC| Registry (C0036)|--|
|[rat_limerat](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/rat_limerat.py)|LimeRATRegkeys|Registry (C0036)|--|
|[persistence_remotedesktop](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/persistence_remotedesktop.py)|PersistenceRDPRegistry|Registry (C0036)|--|
|[prevents_safeboot](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/prevents_safeboot.py)|PreventsSafeboot|Registry (C0036)|--|
|[removes_sec_maintain_icon](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/removes_sec_maintain_icon.py)|RemovesSecurityAndMaintenanceIcon|Registry (C0036)|--|
|[creates_nullvalue](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/creates_nullvalue.py)|CreatesNullValue|Registry (C0036)| NtSetValueKey, NtCreateKey|
|[antianalysis_detectreg](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/antianalysis_detectreg.py)|AntiAnalysisDetectReg|Registry (C0036), Registry::Open Registry Key (C0036.003)]|--|
|[disables_notificationcenter](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_notificationcenter.py)|DisablesNotificationCenter|Registry (C0036)|--|
|[trojan_ursnif](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/trojan_ursnif.py)|UrsnifBehavior|Registry (C0036)|--|
|[packer_armadillo_regkey](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/packer_armadillo_regkey.py)|ArmadilloRegKey| Registry (C0036)|--|
|[browser_startpage](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/browser_startpage.py)|browser_startpage|Registry (C0036), Registry::Set Registry Value (C0036.001)|--|
|[tampers_powershell_logging](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/tampers_powershell_logging.py)|TampersPowerShellLogging|Registry (C0036)|--|
|[credential_access](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/credential_access.py)|EnablesWDigest|Registry (C0036)|--|
|[disables_run_command](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_run_command.py)|DisableRunCommand|Registry (C0036)|--|
|[backdoor_ketrican_regkeys](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/backdoor_ketrican_regkeys.py)|KetricanRegkeys| Registry (C0036), Registry::Query Registry Key (C0036.005)|--|
|[removes_networking_icon](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/removes_networking_icon.py)|RemovesNetworkingIcon|Registry (C0036)|--|
|[modifies_certs](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/modifies_certs.py)|ModifiesCerts| Registry (C0036)|--|
|[removes_username_startmenu](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/removes_username_startmenu.py)|RemovesUsernameStartMenu|Registry (C0036)|--|
|[disables_wer](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/disables_wer.py)|DisablesWER|Registry (C0036)|--|

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

