<table>
<tr>
<td><b>ID</b></td>
<td><b>E1059</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../execution">Execution</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>Command and Scripting Interpreter (<a href="https://attack.mitre.org/techniques/T1059">T1059</a>, <a href="https://attack.mitre.org/techniques/T1623">T1623</a>)</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>2 August 2022</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>13 September 2023</b></td>
</tr>
</table>


# Command and Scripting Interpreter

Malware may abuse command and script interpreters to execute commands, scripts, or binaries.

See ATT&CK: **Command and Scripting Interpreter ([T1059](https://attack.mitre.org/techniques/T1059), [T1623](https://attack.mitre.org/techniques/T1623))**.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**Poison Ivy**](../xample-malware/poison-ivy.md)|2005|--|After the Poison Ivy server is running on the target machine, the attacker can use a Windows GUI client to control the target computer. [[1]](#1)|
|[**WebCobra**](../xample-malware/webcobra.md)|2018|--|From the command line, the malware drops and unzips a password-protected Cabinet archive file. [[1]](#1)|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|--|GoBotKR uses cmd.exe to execute commands. [[2]](#2)|
|[**Kovter**](../xample-malware/kovter.md)|2016|--|The malware executes malicious javascript and powershell. [[3]](#3)|
|[**SamSam**](../xample-malware/samsam.md)|2015|--|SamSam uses a batch file for executing the malware and deleting certain components. [[4]](#4)|
|[**Shamoon**](../xample-malware/shamoon.md)|2012|--|The wiper component of Shamoon creates a service to run the driver with the command: sc create hdv_725x type= kernel start= demand binpath= WINDOWS\hdv_725x.sys 2>&1 >nul and sends an additional reboot command after completion. Shamoon also accepts command line arguments.[[5]](#5)|
|[**Stuxnet**](../xample-malware/stuxnet.md)|2010|--|Stuxnet will store and execute SQL code that will extract and execute Stuxnet from the saved CAB file using xp_cmdshell. [[6]](#6)|
|[**EvilBunny**](../xample-malware/evilbunny.md)|2011|--|EvilBunny executes Lua scripts. [[7]](#7)|
|[**Netwalker**](../xample-malware/netwalker.md)|2020|--|Netwalker is written and executed in Powershell. [[8]](#8)|
|[**CryptoLocker**](../xample-malware/cryptolocker.md)|2013|--|The malware accepts command line arguments. [[9]](#9)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|--|The malware accepts command line arguments. [[9]](#9)|
|[**Gamut**](../xample-malware/gamut.md)|2014|--|Gamut accepts command line arguments. [[9]](#9)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|--|Hupigon accepts command line arguments. [[9]](#9)|
|[**Mebromi**](../xample-malware/mebromi.md)|2011|--|Mebromi accepts command line arguments. [[9]](#9)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|--|Redhip accepts command line arguments. [[9]](#9)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|--|The malware accepts command line arguments. [[9]](#9)|
|[**SearchAwesome**](../xample-malware/searchawesome.md)|2018|--|The malware installs a script to inject a JavaScript script and modify web traffic. [[10]](#10)|
|[**TrickBot**](../xample-malware/trickbot.md)|2016|--|TrickBot accepts command line arguments. [[9]](#9)|
|[**UP007**](../xample-malware/up007.md)|2016|--|The malware accepts command line arguments. [[9]](#9)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[accept command line arguments](https://github.com/mandiant/capa-rules/blob/master/host-interaction/cli/accept-command-line-arguments.yml)|Command and Scripting Interpreter (E1059)|GetCommandLine, CommandLineToArgv, System.Environment::GetCommandLineArgs|
|[run PowerShell expression](https://github.com/mandiant/capa-rules/blob/master/load-code/powershell/run-powershell-expression.yml)|Command and Scripting Interpreter (E1059)|System.Management.Automation.PowerShell::Create, System.Management.Automation.PowerShell::AddScript, System.Management.Automation.PowerShell::Invoke|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[office_postscript](https://github.com/CAPESandbox/community/tree/master/modules/signatures/office_postscript.py)|Command and Scripting Interpreter (E1059)|NtWriteFile|
|[js_suspicious_redirect](https://github.com/CAPESandbox/community/tree/master/modules/signatures/js_suspicious_redirect.py)|Command and Scripting Interpreter (E1059)|CDocument_write, JsEval, COleScript_ParseScriptText, COleScript_Compile|
|[odbcconf_bypass](https://github.com/CAPESandbox/community/tree/master/modules/signatures/odbcconf_bypass.py)|Command and Scripting Interpreter (E1059)|--|
|[regsvr32_squiblydoo_dll_load](https://github.com/CAPESandbox/community/tree/master/modules/signatures/regsvr32_squiblydoo_dll_load.py)|Command and Scripting Interpreter (E1059)|LdrLoadDll|
|[squiblydoo_bypass](https://github.com/CAPESandbox/community/tree/master/modules/signatures/squiblydoo_bypass.py)|Command and Scripting Interpreter (E1059)|--|
|[squiblytwo_bypass](https://github.com/CAPESandbox/community/tree/master/modules/signatures/squiblytwo_bypass.py)|Command and Scripting Interpreter (E1059)|--|
|[exe_dropper_js](https://github.com/CAPESandbox/community/tree/master/modules/signatures/exe_dropper_js.py)|Command and Scripting Interpreter (E1059)|JsEval|
|[persistence_registry_script](https://github.com/CAPESandbox/community/tree/master/modules/signatures/persistence_registry_script.py)|Command and Scripting Interpreter (E1059)|RegSetValueExA, RegSetValueExW, NtSetValueKey|
|[ie_martian_children](https://github.com/CAPESandbox/community/tree/master/modules/signatures/ie_martian_children.py)|Command and Scripting Interpreter (E1059)|--|
|[bcdedit_command](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bcdedit_command.py)|Command and Scripting Interpreter (E1059)|ShellExecuteExW, NtCreateUserProcess, CreateProcessInternalW|
|[office_martian_children](https://github.com/CAPESandbox/community/tree/master/modules/signatures/office_martian_children.py)|Command and Scripting Interpreter (E1059)|--|
|[js_phish](https://github.com/CAPESandbox/community/tree/master/modules/signatures/js_phish.py)|Command and Scripting Interpreter (E1059)|JsEval, COleScript_ParseScriptText, COleScript_Compile|
|[disables_winfirewall](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_winfirewall.py)|Command and Scripting Interpreter (E1059)|--|
|[script_tool_executed](https://github.com/CAPESandbox/community/tree/master/modules/signatures/script_tool_executed.py)|Command and Scripting Interpreter (E1059)|--|
|[cmdline_obfuscation](https://github.com/CAPESandbox/community/tree/master/modules/signatures/cmdline_obfuscation.py)|Command and Scripting Interpreter (E1059)|--|
|[cmdline_switches](https://github.com/CAPESandbox/community/tree/master/modules/signatures/cmdline_switches.py)|Command and Scripting Interpreter (E1059)|--|
|[cmdline_terminate](https://github.com/CAPESandbox/community/tree/master/modules/signatures/cmdline_terminate.py)|Command and Scripting Interpreter (E1059)|--|
|[cmdline_forfiles_wildcard](https://github.com/CAPESandbox/community/tree/master/modules/signatures/cmdline_forfiles_wildcard.py)|Command and Scripting Interpreter (E1059)|--|
|[cmdline_http_link](https://github.com/CAPESandbox/community/tree/master/modules/signatures/cmdline_http_link.py)|Command and Scripting Interpreter (E1059)|--|
|[cmdline_long_string](https://github.com/CAPESandbox/community/tree/master/modules/signatures/cmdline_long_string.py)|Command and Scripting Interpreter (E1059)|--|
|[cmdline_reversed_http_link](https://github.com/CAPESandbox/community/tree/master/modules/signatures/cmdline_reversed_http_link.py)|Command and Scripting Interpreter (E1059)|--|
|[long_commandline](https://github.com/CAPESandbox/community/tree/master/modules/signatures/long_commandline.py)|Command and Scripting Interpreter (E1059)|--|
|[powershell_renamed_commandline](https://github.com/CAPESandbox/community/tree/master/modules/signatures/powershell_renamed_commandline.py)|Command and Scripting Interpreter (E1059)|--|
|[wmi_script_process](https://github.com/CAPESandbox/community/tree/master/modules/signatures/wmi_script_process.py)|Command and Scripting Interpreter (E1059)|NtCreateUserProcess, CreateProcessInternalW|
|[disables_mappeddrives_autodisconnect](https://github.com/CAPESandbox/community/tree/master/modules/signatures/disables_mappeddrives_autodisconnect.py)|Command and Scripting Interpreter (E1059)|ShellExecuteExW, NtCreateUserProcess, CreateProcessInternalW|
|[system_account_discovery_cmd](https://github.com/CAPESandbox/community/tree/master/modules/signatures/system_account_discovery_cmd.py)|Command and Scripting Interpreter (E1059)|--|
|[system_currently_loggedin_user_cmd](https://github.com/CAPESandbox/community/tree/master/modules/signatures/system_currently_loggedin_user_cmd.py)|Command and Scripting Interpreter (E1059)|--|
|[system_info_discovery_cmd](https://github.com/CAPESandbox/community/tree/master/modules/signatures/system_info_discovery_cmd.py)|Command and Scripting Interpreter (E1059)|--|
|[system_info_discovery_pwsh](https://github.com/CAPESandbox/community/tree/master/modules/signatures/system_info_discovery_pwsh.py)|Command and Scripting Interpreter (E1059)|--|
|[system_network_discovery_cmd](https://github.com/CAPESandbox/community/tree/master/modules/signatures/system_network_discovery_cmd.py)|Command and Scripting Interpreter (E1059)|--|
|[system_network_discovery_pwsh](https://github.com/CAPESandbox/community/tree/master/modules/signatures/system_network_discovery_pwsh.py)|Command and Scripting Interpreter (E1059)|--|
|[system_user_discovery_cmd](https://github.com/CAPESandbox/community/tree/master/modules/signatures/system_user_discovery_cmd.py)|Command and Scripting Interpreter (E1059)|--|
|[powershell_network_connection](https://github.com/CAPESandbox/community/tree/master/modules/signatures/powershell_network_connection.py)|Command and Scripting Interpreter (E1059)|URLDownloadToFileW, HttpOpenRequestW, send, WSAConnect, InternetCrackUrlW, InternetCrackUrlA, InternetReadFile|
|[powershell_scriptblock_logging](https://github.com/CAPESandbox/community/tree/master/modules/signatures/powershell_scriptblock_logging.py)|Command and Scripting Interpreter (E1059)|--|
|[powershell_command_suspicious](https://github.com/CAPESandbox/community/tree/master/modules/signatures/powershell_command_suspicious.py)|Command and Scripting Interpreter (E1059)|--|
|[powershell_renamed](https://github.com/CAPESandbox/community/tree/master/modules/signatures/powershell_renamed.py)|Command and Scripting Interpreter (E1059)|--|
|[powershell_reversed](https://github.com/CAPESandbox/community/tree/master/modules/signatures/powershell_reversed.py)|Command and Scripting Interpreter (E1059)|--|
|[powershell_variable_obfuscation](https://github.com/CAPESandbox/community/tree/master/modules/signatures/powershell_variable_obfuscation.py)|Command and Scripting Interpreter (E1059)|--|
|[office_com_load](https://github.com/CAPESandbox/community/tree/master/modules/signatures/office_com_load.py)|Command and Scripting Interpreter (E1059)|LdrGetDllHandle, LdrLoadDll|
|[office_vb_load](https://github.com/CAPESandbox/community/tree/master/modules/signatures/office_vb_load.py)|Command and Scripting Interpreter (E1059)|LdrGetDllHandle, LdrLoadDll|
|[office_wmi_load](https://github.com/CAPESandbox/community/tree/master/modules/signatures/office_wmi_load.py)|Command and Scripting Interpreter (E1059)|LdrGetDllHandle, LdrLoadDll|
|[document_script_exe_drop](https://github.com/CAPESandbox/community/tree/master/modules/signatures/document_script_exe_drop.py)|Command and Scripting Interpreter (E1059)|NtWriteFile|
|[windows_defender_powershell](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows_defender_powershell.py)|Command and Scripting Interpreter (E1059)|--|
|[office_suspicious_processes](https://github.com/CAPESandbox/community/tree/master/modules/signatures/office_suspicious_processes.py)|Command and Scripting Interpreter (E1059)|NtCreateUserProcess, CreateProcessInternalW|
|[script_created_process](https://github.com/CAPESandbox/community/tree/master/modules/signatures/script_created_process.py)|Command and Scripting Interpreter (E1059)|NtCreateUserProcess, CreateProcessInternalW|
|[script_network_activity](https://github.com/CAPESandbox/community/tree/master/modules/signatures/script_network_activity.py)|Command and Scripting Interpreter (E1059)|URLDownloadToFileW, HttpOpenRequestW, send, WSAConnect, InternetCrackUrlW, InternetCrackUrlA, SslEncryptPacket, InternetReadFile|
|[suspicious_js_script](https://github.com/CAPESandbox/community/tree/master/modules/signatures/suspicious_js_script.py)|Command and Scripting Interpreter (E1059)|JsEval, COleScript_ParseScriptText|

## References

<a name="1">[1]</a> https://www.cyber.nj.gov/threat-center/threat-profiles/trojan-variants/poison-ivy

<a name="2">[2]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="3">[3]</a> https://www.bleepingcomputer.com/virus-removal/remove-kovter-trojan

<a name="4">[4]</a> https://www.sophos.com/en-us/medialibrary/PDFs/technical-papers/SamSam-ransomware-chooses-Its-targets-carefully-wpna.pdf

<a name="5">[5]</a> https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-returns-to-wipe-systems-in-middle-east-europe/

<a name="6">[6]</a> https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en

<a name="7">[7]</a> https://web.archive.org/web/20150311013500/http://www.cyphort.com/evilbunny-malware-instrumented-lua/

<a name="8">[8]</a> https://www.trendmicro.com/en_us/research/20/e/netwalker-fileless-ransomware-injected-via-reflective-loading.html

<a name="9">[9]</a> capa v4.0, analyzed at MITRE on 10/12/2022

<a name="10">[10]</a> https://www.malwarebytes.com/blog/news/2018/10/mac-malware-intercepts-encrypted-web-traffic-for-ad-injection

<a name="11">[11]</a> https://www.mcafee.com/blogs/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/

<a name="12">[12]</a> https://blog.malwarebytes.com/threat-analysis/2016/07/untangling-kovter/

<a name="13">[13]</a> https://www.cyber.nj.gov/threat-center/threat-profiles/trojan-variants/poison-ivy

