# capa Rule Distribution #
19 September 2023

## Histograms ##
The histograms below show the number of capa rules mapped into ATT&CK techniques (organized by tactic), MBC behaviors (organized by objective), and MBC micro-behaviors (organized by micro-objective). The count tracks ATT&CK techniques and sub-techniques and MBC behaviors and methods individually. For example, both B0009 and B0009.012 are counted under the Anti-Behavioral Analysis objective. The explicit techniques/sub-techiques, behaviors/methods, and micro-behaviors/micro-methods follow the histograms.

### ATT&CK Mapping Histogram ###

| **TACTIC** | **Number of Techniques**  |  |
|-----|-----|-----|
|Reconnaissance|0| |
|Resource Development|0| |
|Initial Access|0| |
|**Execution**|8| **XXXXXXXX** |
|**Persistence**|22| **XXXXXXXXXXXXXXXXXXXXXX** |
|**Privilege Escalation**|1| **X** |
|**Defense Evasion**|37| **XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX** |
|**Credential Access**|4| **XXXX** |
|**Discovery**|17| **XXXXXXXXXXXXXXXXX** |
|Lateral Movement|0| |
|**Collection**|7| **XXXXXXX** |
|**Command and Control**|1| **X** |
|Exfiltration|0| |
|**Impact**|5| **XXXXX** |

### MBC Mapping Histogram (Objectives) ###

| **OBJECTIVE** | **Number of Behaviors** |  |
|-----|-----|-----|
|**Anti-Behavioral Analysis**|24| **XXXXXXXXXXXXXXXXXXXXXXXX** |
|**Anti-Static Analysis**|10| **XXXXXXXXXX** |
|**Collection**|5| **XXXXX** |
|**Command and Control**|3| **XXX** |
|Credential Access|0| |
|**Defense Evasion**|15| **XXXXXXXXXXXXXXX** |
|**Discovery**|8| **XXXXXXXX** |
|**Execution**|2| **XX** |
|Exfiltration|0| |
|**Impact**|6| **XXXXXX** |
|Lateral Movement|0| |
|**Persistence**|2| **XX** |
|Privilege Escalation|0| |

### MBC Mapping Histogram (Micro-Objectives) ###

| **MICRO-OBJECTIVE** | **Number of Micro-Behaviors**  |  |
|-----|-----|-----|
|**Communication**|38| **XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX** |
|**Cryptography**|27| **XXXXXXXXXXXXXXXXXXXXXXXXXXX** |
|**Data**|16| **XXXXXXXXXXXXXXXX** |
|**File System**|11| **XXXXXXXXXXX** |
|**Hardware**|4| **XXXX** |
|**Memory**|2| **XX** |
|**Operating System**|11| **XXXXXXXXXXX** |
|**Process**|14| **XXXXXXXXXXXXXX** |

## ATT&CK MAPPINGS ##

### Reconnaissance ###
  num: 0

### Resource Development ###
  num: 0

### Initial Access ###
  num: 0

### Execution ###
  num: 8
  - Command and Scripting Interpreter [T1059] Count-3
  - Windows Management Instrumentation [T1047] Count-1
  - System Services::Service Execution [T1569.002] Count-1
  - Shared Modules [T1129] Count-8
  - Command and Scripting Interpreter::PowerShell [T1059.001] Count-1
  - Command and Scripting Interpreter::Unix Shell [T1059.004] Count-2
  - Command and Scripting Interpreter::Windows Command Shell [T1059.003] Count-2
  - Command and Scripting Interpreter::Python [T1059.006] Count-2

### Persistence ###
  num: 22
  - Hijack Execution Flow [T1574] Count-1
  - Create or Modify System Process::Windows Service [T1543.003] Count-9
  - Pre-OS Boot::System Firmware [T1542.001] Count-2
  - Boot or Logon Autostart Execution::Shortcut Modification [T1547.009] Count-1
  - Server Software Component [T1505] Count-2
  - Event Triggered Execution::Unix Shell Configuration Modification [T1546.004] Count-1
  - Boot or Logon Autostart Execution::XDG Autostart Entries [T1547.013] Count-1
  - Server Software Component::IIS Components [T1505.004] Count-2
  - Office Application Startup::Add-ins [T1137.006] Count-3
  - Modify Authentication Process::Network Provider DLL [T1556.008] Count-1
  - Boot or Logon Autostart Execution::Security Support Provider [T1547.005] Count-1
  - Boot or Logon Autostart Execution::Authentication Package [T1547.002] Count-1
  - Modify Authentication Process::Password Filter DLL [T1556.002] Count-1
  - Boot or Logon Initialization Scripts::RC Scripts [T1037.004] Count-1
  - Server Software Component::Transport Agent [T1505.002] Count-1
  - Scheduled Task/Job::Scheduled Task [T1053.005] Count-2
  - Scheduled Task/Job::At [T1053.002] Count-1
  - Boot or Logon Autostart Execution::Active Setup [T1547.014] Count-1
  - Event Triggered Execution::AppInit DLLs [T1546.010] Count-2
  - Event Triggered Execution [T1546] Count-1
  - Boot or Logon Autostart Execution::Winlogon Helper DLL [T1547.004] Count-1
  - Boot or Logon Autostart Execution::Registry Run Keys / Startup Folder [T1547.001] Count-3

### Privilege Escalation ###
  num: 1
  - Access Token Manipulation [T1134] Count-2

### Defense Evasion ###
  num: 37
  - Obfuscated Files or Information::Software Packing [T1027.002] Count-20
  - Virtualization/Sandbox Evasion::System Checks [T1497.001] Count-16
  - Impair Defenses::Indicator Blocking [T1562.006] Count-1
  - Impair Defenses::Disable or Modify Tools [T1562.001] Count-3
  - Virtualization/Sandbox Evasion::User Activity Based Checks [T1497.002] Count-2
  - Virtualization/Sandbox Evasion [T1497] Count-1
  - Debugger Evasion [T1622] Count-2
  - Indicator Removal [T1070] Count-2
  - Impair Defenses::Disable Windows Event Logging [T1562.002] Count-1
  - Process Injection [T1055] Count-7
  - Access Token Manipulation::Parent PID Spoofing [T1134.004] Count-1
  - Indicator Removal::Clear Windows Event Logs [T1070.001] Count-1
  - Indicator Removal::File Deletion [T1070.004] Count-1
  - Indicator Removal::Timestomp [T1070.006] Count-1
  - Obfuscated Files or Information [T1027] Count-44
  - Obfuscated Files or Information::Indicator Removal from Tools [T1027.005] Count-1
  - Deobfuscate/Decode Files or Information [T1140] Count-2
  - Subvert Trust Controls::Mark-of-the-Web Bypass [T1553.005] Count-1
  - Hide Artifacts::Hidden File System [T1564.005] Count-1
  - File and Directory Permissions Modification [T1222] Count-1
  - Hide Artifacts::Hidden Window [T1564.003] Count-1
  - Hide Artifacts [T1564] Count-1
  - Process Injection::Process Doppelgänging [T1055.013] Count-1
  - Process Injection::Portable Executable Injection [T1055.002] Count-1
  - Process Injection::Dynamic-link Library Injection [T1055.001] Count-2
  - Process Injection::Thread Execution Hijacking [T1055.003] Count-2
  - Process Injection::Extra Window Memory Injection [T1055.011] Count-1
  - Process Injection::Asynchronous Procedure Call [T1055.004] Count-1
  - Process Injection::Process Hollowing [T1055.012] Count-1
  - Modify Registry [T1112] Count-4
  - Impair Defenses::Safe Mode Boot [T1562.009] Count-1
  - Subvert Trust Controls::Code Signing Policy Modification [T1553.006] Count-1
  - Abuse Elevation Control Mechanism::Bypass User Account Control [T1548.002] Count-4
  - Reflective Code Loading [T1620] Count-1
  - Obfuscated Files or Information::Dynamic API Resolution [T1027.007] Count-1
  - Hijack Execution Flow [T1574] Count-1
  - BITS Jobs [T1197] Count-1

### Credential Access ###
  num: 4
  - Credentials from Password Stores::Windows Credential Manager [T1555.004] Count-1
  - Credentials from Password Stores::Password Managers [T1555.005] Count-1
  - Credentials from Password Stores [T1555] Count-48
  - Credentials from Password Stores::Credentials from Web Browsers [T1555.003] Count-2

### Discovery ###
  num: 17
  - File and Directory Discovery [T1083] Count-10
  - System Information Discovery [T1082] Count-16
  - Process Discovery [T1057] Count-9
  - System Location Discovery::System Language Discovery [T1614.001] Count-2
  - System Service Discovery [T1007] Count-3
  - Application Window Discovery [T1010] Count-2
  - System Owner/User Discovery [T1033] Count-4
  - Account Discovery [T1087] Count-2
  - Query Registry [T1012] Count-3
  - Software Discovery::Security Software Discovery [T1518.001] Count-1
  - Software Discovery [T1518] Count-1
  - System Network Configuration Discovery::Internet Connection Discovery [T1016.001] Count-1
  - System Network Configuration Discovery [T1016] Count-8
  - Network Sniffing [T1040] Count-1
  - System Location Discovery [T1614] Count-1
  - Group Policy Discovery [T1615] Count-1
  - Domain Trust Discovery [T1482] Count-1

### Lateral Movement ###
  num: 0

### Collection ###
  num: 7
  - Archive Collected Data::Archive via Library [T1560.002] Count-1
  - Clipboard Data [T1115] Count-3
  - Video Capture [T1125] Count-1
  - Input Capture::Keylogging [T1056.001] Count-3
  - Data from Information Repositories [T1213] Count-2
  - Audio Capture [T1123] Count-1
  - Screen Capture [T1113] Count-2

### Command and Control ###
  num: 1
  - Ingress Tool Transfer [T1105] Count-1

### Exfiltration ###
  num: 0

### Impact ###
  num: 5
  - Endpoint Denial of Service [T1499] Count-1
  - System Shutdown/Reboot [T1529] Count-1
  - Data Manipulation::Transmitted Data Manipulation [T1565.002] Count-1
  - Inhibit System Recovery [T1490] Count-1
  - Disk Wipe::Disk Structure Wipe [T1561.002] Count-1

## MBC MAPPINGS ##

### Anti-Behavioral Analysis ###
  num: 24
  - Emulator Detection [B0004] Count-1
  - Virtual Machine Detection [B0009] Count-14
  - Sandbox Detection [B0007] Count-1
  - Virtual Machine Detection::Human User Check [B0009.012] Count-2
  - Virtual Machine Detection::Unique Hardware/Firmware Check [B0009.023] Count-1
  - Sandbox Detection::Product Key/ID Testing [B0007.005] Count-1
  - Debugger Evasion [B0002] Count-2
  - Debugger Detection [B0001] Count-3
  - Debugger Detection::Software Breakpoints [B0001.025] Count-1
  - Debugger Detection::Process Environment Block BeingDebugged [B0001.035] Count-1
  - Debugger Detection::Timing/Delay Check GetTickCount [B0001.032] Count-1
  - Debugger Detection::SetHandleInformation [B0001.024] Count-1
  - Debugger Detection::OutputDebugString [B0001.016] Count-1
  - Debugger Detection::Memory Write Watching [B0001.010] Count-1
  - Debugger Detection::Timing/Delay Check QueryPerformanceCounter [B0001.033] Count-1
  - Debugger Detection::Hardware Breakpoints [B0001.005] Count-1
  - Debugger Detection::NtQueryInformationProcess [B0001.012] Count-1
  - Debugger Detection::CheckRemoteDebuggerPresent [B0001.002] Count-1
  - Debugger Detection::WudfIsAnyDebuggerPresent [B0001.031] Count-1
  - Debugger Detection::Process Environment Block NtGlobalFlag [B0001.036] Count-1
  - Debugger Detection::Anti-debugging Instructions [B0001.034] Count-1
  - Conditional Execution::Runs as Service [B0025.007] Count-1
  - Debugger Detection::Process Environment Block [B0001.019] Count-1
  - Dynamic Analysis Evasion::Delayed Execution [B0003.003] Count-1

### Anti-Static Analysis ###
  num: 10
  - Disassembler Evasion [B0012] Count-1
  - Software Packing [F0001] Count-14
  - Software Packing::Themida [F0001.011] Count-1
  - Software Packing::VMProtect [F0001.010] Count-1
  - Software Packing::Standard Compression [F0001.002] Count-2
  - Software Packing::Confuser [F0001.009] Count-1
  - Software Packing::UPX [F0001.008] Count-1
  - Executable Code Obfuscation [B0032] Count-10
  - Executable Code Obfuscation::Argument Obfuscation [B0032.020] Count-1
  - Executable Code Obfuscation::Stack Strings [B0032.017] Count-1

### Collection ###
  num: 5
  - Input Capture [E1056] Count-1
  - Keylogging::Polling [F0002.002] Count-1
  - Keylogging::Application Hook [F0002.001] Count-1
  - Screen Capture::WinAPI [E1113.m01] Count-1
  - Screen Capture [E1113] Count-1

### Command and Control ###
  num: 3
  - C2 Communication::Send Data [B0030.001] Count-1
  - C2 Communication::Receive Data [B0030.002] Count-1
  - C2 Communication::Server to Client File Transfer [B0030.003] Count-1

### Credential Access ###
  num: 0

### Defense Evasion ###
  num: 15
  - Disable or Evade Security Tools::Heavens Gate [F0004.008] Count-1
  - Disable or Evade Security Tools [F0004] Count-1
  - Disable or Evade Security Tools::Modify Policy [F0004.005] Count-2
  - Process Injection::Patch Process Command Line [E1055.m04] Count-1
  - Self Deletion::COMSPEC Environment Variable [F0007.001] Count-1
  - Obfuscated Files or Information::Encryption [E1027.m04] Count-1
  - Obfuscated Files or Information::Encryption-Standard Algorithm [E1027.m05] Count-21
  - Obfuscated Files or Information::Encoding-Standard Algorithm [E1027.m02] Count-3
  - Disable or Evade Security Tools::Bypass Windows File Protection [F0004.007] Count-1
  - Process Injection [E1055] Count-4
  - Disable or Evade Security Tools::Disable Code Integrity [F0004.009] Count-1
  - Process Injection::Injection via Windows Fibers [E1055.m05] Count-1
  - Hijack Execution Flow::Abuse Windows Function Calls [F0015.006] Count-1
  - Hijack Execution Flow::Import Address Table Hooking [F0015.003] Count-1
  - Obfuscated Files or Information [E1027] Count-1

### Discovery ###
  num: 8
  - Analysis Tool Discovery::Process detection [B0013.001] Count-1
  - System Information Discovery [E1082] Count-5
  - File and Directory Discovery [E1083] Count-7
  - Application Window Discovery [E1010] Count-1
  - Taskbar Discovery [B0043] Count-1
  - File and Directory Discovery::Log File [E1083.m01] Count-2
  - Code Discovery::Enumerate PE Sections [B0046.001] Count-1
  - Code Discovery::Inspect Section Memory Permissions [B0046.002] Count-1

### Execution ###
  num: 2
  - Command and Scripting Interpreter [E1059] Count-2
  - Install Additional Program [B0023] Count-2

### Exfiltration ###
  num: 0

### Impact ###
  num: 6
  - Modify Hardware::Mouse [B0042.002] Count-1
  - Modify Hardware::CDROM [B0042.001] Count-1
  - Clipboard Modification [E1510] Count-1
  - Remote Access::Reverse Shell [B0022.001] Count-2
  - Data Destruction::Delete Shadow Copies [E1485.m04] Count-1
  - Disk Wipe [F0014] Count-1

### Lateral Movement ###
  num: 0

### Persistence ###
  num: 2
  - Hijack Execution Flow [F0015] Count-1
  - Registry Run Keys / Startup Folder [F0012] Count-1

### Privilege Escalation ###
  num: 0

## MBC MICRO-BEHAVIOR MAPPINGS ##

### Communication ###
  num: 38
  - Interprocess Communication [C0003] Count-2
  - HTTP Communication::Read Header [C0002.014] Count-2
  - HTTP Communication::WinHTTP [C0002.008] Count-1
  - HTTP Communication::IWebBrowser [C0002.010] Count-2
  - HTTP Communication [C0002] Count-2
  - HTTP Communication::Set Header [C0002.013] Count-1
  - HTTP Communication::Start Server [C0002.018] Count-1
  - HTTP Communication::Receive Request [C0002.015] Count-1
  - HTTP Communication::Send Response [C0002.016] Count-1
  - HTTP Communication::Get Response [C0002.017] Count-5
  - HTTP Communication::Send Request [C0002.003] Count-1
  - HTTP Communication::Download URL [C0002.006] Count-1
  - HTTP Communication::Create Request [C0002.012] Count-2
  - HTTP Communication::Send Data [C0002.005] Count-1
  - HTTP Communication::Open URL [C0002.004] Count-1
  - HTTP Communication::Connect to Server [C0002.009] Count-1
  - HTTP Communication::Extract Body [C0002.011] Count-1
  - Socket Communication::Start TCP Server [C0001.005] Count-1
  - Socket Communication::TCP Client [C0001.008] Count-1
  - Interprocess Communication::Create Pipe [C0003.001] Count-2
  - Interprocess Communication::Write Pipe [C0003.004] Count-1
  - Interprocess Communication::Connect Pipe [C0003.002] Count-1
  - Interprocess Communication::Read Pipe [C0003.003] Count-1
  - FTP Communication::Send File [C0004.001] Count-1
  - FTP Communication::WinINet [C0004.002] Count-1
  - DNS Communication::Server Connect [C0011.002] Count-1
  - DNS Communication::Resolve [C0011.001] Count-1
  - Socket Communication::Get Socket Status [C0001.012] Count-1
  - Socket Communication::Create Socket [C0001.003] Count-2
  - Socket Communication::Set Socket Config [C0001.001] Count-1
  - Socket Communication::Initialize Winsock Library [C0001.009] Count-1
  - Socket Communication::Connect Socket [C0001.004] Count-1
  - Socket Communication::Create TCP Socket [C0001.011] Count-2
  - Socket Communication::Send TCP Data [C0001.014] Count-2
  - Socket Communication::Create UDP Socket [C0001.010] Count-1
  - Socket Communication::Send Data [C0001.007] Count-1
  - Socket Communication::Receive Data [C0001.006] Count-1
  - ICMP Communication::Echo Request [C0014.002] Count-1

### Cryptography ###
  num: 27
  - Encryption Key::Import Public Key [C0028.001] Count-1
  - Decrypt Data [C0031] Count-1
  - Encrypt Data [C0027] Count-4
  - Encryption Key [C0028] Count-2
  - Encrypt Data::HC-128 [C0027.006] Count-2
  - Encrypt Data::RC6 [C0027.010] Count-1
  - Encrypt Data::Twofish [C0027.005] Count-1
  - Encrypt Data::AES [C0027.001] Count-4
  - Decrypt Data::AES [C0031.001] Count-1
  - Encrypt Data::Sosemanuk [C0027.008] Count-1
  - Encrypt Data::Camellia [C0027.003] Count-1
  - Encrypt Data::3DES [C0027.004] Count-2
  - Encrypt Data::RC4 [C0027.009] Count-4
  - Generate Pseudo-random Sequence::RC4 PRGA [C0021.004] Count-1
  - Encryption Key::RC4 KSA [C0028.002] Count-1
  - Encrypt Data::Skipjack [C0027.013] Count-1
  - Encrypt Data::Blowfish [C0027.002] Count-1
  - Cryptographic Hash [C0029] Count-2
  - Cryptographic Hash::Tiger [C0029.005] Count-1
  - Cryptographic Hash::SHA1 [C0029.002] Count-1
  - Cryptographic Hash::SHA256 [C0029.003] Count-1
  - Cryptographic Hash::MD5 [C0029.001] Count-1
  - Cryptographic Hash::SHA224 [C0029.004] Count-1
  - Hashed Message Authentication Code [C0061] Count-1
  - Generate Pseudo-random Sequence::Use API [C0021.003] Count-2
  - Generate Pseudo-random Sequence [C0021] Count-1
  - Crypto Library [C0059] Count-5

### Data ###
  num: 16
  - Checksum::Luhn [C0032.002] Count-3
  - Checksum::Adler [C0032.005] Count-1
  - Checksum::CRC32 [C0032.001] Count-1
  - Non-Cryptographic Hash::MurmurHash [C0030.001] Count-1
  - Non-Cryptographic Hash::FNV [C0030.005] Count-1
  - Non-Cryptographic Hash::djb2 [C0030.006] Count-1
  - Encode Data::XOR [C0026.002] Count-1
  - Encode Data::Base64 [C0026.001] Count-3
  - Check String [C0019] Count-2
  - Decompress Data::aPLib [C0025.003] Count-1
  - Decompress Data::IEncodingFilterFactory [C0025.002] Count-1
  - Compress Data [C0024] Count-3
  - Decompress Data [C0025] Count-2
  - Decompress Data::QuickLZ [C0025.001] Count-1
  - Modulo [C0058] Count-1
  - Compression Library [C0060] Count-2

### File System ###
  num: 11
  - Set File Attributes [C0050] Count-2
  - Create Directory [C0046] Count-1
  - Delete File [C0047] Count-1
  - Delete Directory [C0048] Count-1
  - Get File Attributes [C0049] Count-1
  - Move File [C0063] Count-1
  - Writes File [C0052] Count-3
  - Copy File [C0045] Count-1
  - Read File [C0051] Count-4
  - Read Virtual Disk [C0056] Count-1
  - Create File [C0016] Count-1

### Hardware ###
  num: 4
  - Simulate Hardware::Ctrl-Alt-Del [C0057.001] Count-1
  - Install Driver [C0037] Count-1
  - Install Driver::Minifilter [C0037.001] Count-1
  - Load Driver::Minifilter [C0023.001] Count-1

### Memory ###
  num: 2
  - Free Memory [C0044] Count-1
  - Allocate Memory [C0007] Count-4

### Operating System ###
  num: 11
  - Environment Variable::Set Variable [C0034.001] Count-1
  - Environment Variable [C0034] Count-1
  - Wallpaper [C0035] Count-1
  - Console [C0033] Count-2
  - Registry::Set Registry Key [C0036.001] Count-2
  - Registry::Open Registry Key [C0036.003] Count-2
  - Registry::Query Registry Key [C0036.005] Count-1
  - Registry::Query Registry Value [C0036.006] Count-2
  - Registry::Create Registry Key [C0036.004] Count-2
  - Registry::Delete Registry Key [C0036.002] Count-1
  - Registry::Delete Registry Value [C0036.007] Count-1

### Process ###
  num: 14
  - Create Thread [C0038] Count-2
  - Suspend Thread [C0055] Count-1
  - Terminate Thread [C0039] Count-1
  - Resume Thread [C0054] Count-1
  - Enumerate Threads [C0064] Count-1
  - Create Mutex [C0042] Count-2
  - Check Mutex [C0043] Count-2
  - Terminate Process [C0018] Count-3
  - Allocate Thread Local Storage [C0040] Count-1
  - Set Thread Local Storage Value [C0041] Count-1
  - Create Process [C0017] Count-4
  - Create Process::Create Suspended Process [C0017.003] Count-1
  - Open Process [C0065] Count-1
  - Open Thread [C0066] Count-1
