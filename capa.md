# capa Rule Distribution #
15 August 2022

## Histograms ##

### ATT&CK Mapping Histogram ###

|  |  |  |
|-----|-----|-----|
|Reconnaissance |[0]| |
|Resource Development|[0]| |
|Initial Access |[0]| |
|**Execution**|[8]| **XXXXXXXX** |
|**Persistence**|[13]| **XXXXXXXXXXXXX** |
|**Privilege Escalation**|[1] | **X** |
|**Defense Evasion**|[32]| **XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX** |
|**Credential Access**|[4]| **XXXX** |
|**Discovery**|[17]| **XXXXXXXXXXXXXXXXX** |
|Lateral Movement|[0]| |
|**Collection**|[7]| **XXXXXXX** |
|**Command and Control**|[1]| **X** |
|Exfiltration|[0]| |
|**Impact**|[5]| **XXXXX** |

### MBC Mapping Histogram ###

|  |  |  |
|-----|-----|-----|
|**Anti-Behavioral Analysis** |[20]| **XXXXXXXXXXXXXXXXXXXX**|
|**Anti-Static Analysis**|[9]| **XXXXXXXXX** |
|**Collection**|[4]| **XXXX** |
|**Command and Control**|[3]| **XXX** |
|Credential Access|[0]| |
|**Defense Evasion**|[13]| **XXXXXXXXXXXXX** |
|**Discovery**|[6]| **XXXXXX** |
|**Execution**|[1]| **X** |
|Exfiltration|[0]| |
|**Impact**|[5]| **XXXXX** |
|Lateral Movement|[0]| |
|Persistence|[0]| |
|Privilege Escalation|[0] | |

### MBC Micro-behavior Mapping Histogram ###

|  |  |  |
|-----|-----|-----|
|**Communication** |[34]| **XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX**|
|**Cryptography**|[16]| **XXXXXXXXXXXXXXXX** |
|**Data**|[15]| **XXXXXXXXXXXXXXX** |
|**File System**|[11]| **XXXXXXXXXXX** |
|**Hardware**|[4]| **XXXX** |
|**Memory**|[2]| **XX** |
|**Operating System**|[11]| **XXXXXXXXXXX** |
|**Process**|[14]| **XXXXXXXXXXXXXX** |

## ATT&CK MAPPINGS ##

### Collection: ###
  num: 7
  - Archive Collected Data::Archive via Library [T1560.002]
  - Clipboard Data [T1115]
  - Video Capture [T1125]
  - Input Capture::Keylogging [T1056.001]
  - Data from Information Repositories [T1213]
  - Audio Capture [T1123]
  - Screen Capture [T1113]
  
### Command and Control: ###
  num: 1
  - Ingress Tool Transfer [T1105]
  
### Credential Access: ###
  num: 4
  - Credentials from Password Stores::Windows Credential Manager [T1555.004]
  - Credentials from Password Stores::Password Managers [T1555.005]
  - Credentials from Password Stores [T1555]
  - Credentials from Password Stores::Credentials from Web Browsers [T1555.003]
  
### Defense Evasion: ###
  num: 32
  - Obfuscated Files or Information::Software Packing [T1027.002]
  - Virtualization/Sandbox Evasion::System Checks [T1497.001]
  - Impair Defenses::Disable or Modify Tools [T1562.001]
  - Virtualization/Sandbox Evasion::User Activity Based Checks [T1497.002]
  - Virtualization/Sandbox Evasion [T1497]
  - Indicator Removal on Host [T1070]
  - Impair Defenses::Disable Windows Event Logging [T1562.002]
  - Process Injection [T1055]
  - Access Token Manipulation::Parent PID Spoofing [T1134.004]
  - Indicator Removal on Host::Clear Windows Event Logs [T1070.001]
  - Indicator Removal on Host::File Deletion [T1070.004]
  - Indicator Removal on Host::Timestomp [T1070.006]
  - Obfuscated Files or Information [T1027]
  - Obfuscated Files or Information::Indicator Removal from Tools [T1027.005]
  - Deobfuscate/Decode Files or Information [T1140]
  - Obfuscated Files or Information [T1027.002]
  - Subvert Trust Controls::Mark-of-the-Web Bypass [T1553.005]
  - File and Directory Permissions Modification [T1222]
  - Hide Artifacts::Hidden Window [T1564.003]
  - Hide Artifacts [T1564]
  - "Process Injection::Process Doppelg\xE4nging [T1055.013]"
  - Process Injection::Portable Executable Injection [T1055.002]
  - Process Injection::Dynamic-link Library Injection [T1055.001]
  - Process Injection::Thread Execution Hijacking [T1055.003]
  - Process Injection::Asynchronous Procedure Call [T1055.004]
  - Process Injection::Process Hollowing [T1055.012]
  - Modify Registry [T1112]
  - Impair Defenses::Safe Mode Boot [T1562.009]
  - Subvert Trust Controls::Code Signing Policy Modification [T1553.006]
  - Abuse Elevation Control Mechanism::Bypass User Account Control [T1548.002]
  - Hijack Execution Flow [T1574]
  - BITS Jobs [T1197]
  
### Discovery: ###
  num: 17
   
  - File and Directory Discovery [T1083]
  - System Information Discovery [T1082]
  - Process Discovery [T1057]
  - System Location Discovery::System Language Discovery [T1614.001]
  - System Service Discovery [T1007]
  - Application Window Discovery [T1010]
  - System Owner/User Discovery [T1033]
  - Account Discovery [T1087]
  - Query Registry [T1012]
  - Software Discovery::Security Software Discovery [T1518.001]
  - Software Discovery [T1518]
  - System Network Configuration Discovery::Internet Connection Discovery [T1016.001]
  - System Network Configuration Discovery [T1016]
  - Network Sniffing [T1040]
  - System Location Discovery [T1614]
  - Group Policy Discovery [T1615]
  - Domain Trust Discovery [T1482]
  
### Execution: ###
  num: 8
   
  - Command and Scripting Interpreter [T1059]
  - Windows Management Instrumentation [T1047]
  - System Services::Service Execution [T1569.002]
  - Command and Scripting Interpreter::PowerShell [T1059.001]
  - Shared Modules [T1129]
  - Command and Scripting Interpreter::Python [T1059.006]
  - Command and Scripting Interpreter::Unix Shell [T1059.004]
  - Command and Scripting Interpreter::Windows Command Shell [T1059.003]
  
### Exfiltration: ###
  num: 0
  
### Impact: ###
  num: 5
   
  - Endpoint Denial of Service [T1499]
  - System Shutdown/Reboot [T1529]
  - Data Manipulation::Transmitted Data Manipulation [T1565.002]
  - Inhibit System Recovery [T1490]
  - Disk Wipe::Disk Structure Wipe [T1561.002]
  
### Initial Access: ###
  num: 0
  
### Lateral Movement: ###
  num: 0
  
### Persistence: ###
  num: 13
   
  - Create or Modify System Process::Windows Service [T1543.003]
  - Event Triggered Execution::Unix Shell Configuration Modification [T1546.004]
  - Boot or Logon Autostart Execution::XDG Autostart Entries [T1547.013]
  - Server Software Component::IIS Components [T1505.004]
  - Modify Authentication Process [T1556]
  - Modify Authentication Process::Password Filter DLL [T1556.002]
  - Boot or Logon Initialization Scripts::RC Scripts [T1037.004]
  - Scheduled Task/Job::Scheduled Task [T1053.005]
  - Boot or Logon Autostart Execution::Active Setup [T1547.014]
  - Event Triggered Execution::AppInit DLLs [T1546.010]
  - Event Triggered Execution [T1546]
  - Boot or Logon Autostart Execution::Winlogon Helper DLL [T1547.004]
  - Boot or Logon Autostart Execution::Registry Run Keys / Startup Folder [T1547.001]
  
### Privilege Escalation: ###
  num: 1
   
  - Access Token Manipulation [T1134]
  
### Reconnaissance: ###
  num: 0
  
### Resource Development: ###
  num: 0
  


## MBC MAPPINGS ##

### Anti-Behavioral Analysis: ###
  num: 20
   
  - Emulator Detection [B0004]
  - Virtual Machine Detection [B0009]
  - Virtual Machine Detection::Human User Check [B0009.012]
  - Sandbox Detection::Product Key/ID Testing [B0007.005]
  - Debugger Detection [B0001]
  - Debugger Detection::Software Breakpoints [B0001.025]
  - Debugger Detection::Process Environment Block BeingDebugged [B0001.035]
  - Debugger Detection::Timing/Delay Check GetTickCount [B0001.032]
  - Debugger Detection::SetHandleInformation [B0001.024]
  - Debugger Detection::OutputDebugString [B0001.016]
  - Debugger Detection::Memory Write Watching [B0001.010]
  - Debugger Detection::Timing/Delay Check QueryPerformanceCounter [B0001.033]
  - Debugger Detection::Hardware Breakpoints [B0001.005]
  - Debugger Detection::NtQueryInformationProcess [B0001.012]
  - Debugger Detection::CheckRemoteDebuggerPresent [B0001.002]
  - Debugger Detection::Process Environment Block NtGlobalFlag [B0001.036]
  - Debugger Detection::Anti-debugging Instructions [B0001.034]
  - Conditional Execution::Runs as Service [B0025.007]
  - Debugger Detection::Process Environment Block [B0001.019]
  - Dynamic Analysis Evasion::Delayed Execution [B0003.003]
  
### Anti-Static Analysis: ###
  num: 9
   
  - Disassembler Evasion [B0012]
  - Software Packing [F0001]
  - Software Packing::Themida [F0001.011]
  - Software Packing::VMProtect [F0001.010]
  - Software Packing::Standard Compression [F0001.002]
  - Software Packing::Confuser [F0001.009]
  - Software Packing::UPX [F0001.008]
  - Executable Code Obfuscation [B0032]
  - Disassembler Evasion::Argument Obfuscation [B0012.001]
  
### Collection: ###
  num: 4
   
  - Keylogging::Polling [F0002.002]
  - Keylogging::Application Hook [F0002.001]
  - Screen Capture::WinAPI [E1113.m01]
  - Screen Capture [E1113]
  
### Command and Control: ###
  num: 3
   
  - C2 Communication::Send Data [B0030.001]
  - C2 Communication::Receive Data [B0030.002]
  - C2 Communication::Server to Client File Transfer [B0030.003]
  
### Credential Access: ###
  num: 0
  
### Defense Evasion: ###
  num: 13
   
  - Disable or Evade Security Tools::Heavens Gate [F0004.008]
  - Disable or Evade Security Tools::Modify Policy [F0004.005]
  - Process Injection::Patch Process Command Line [E1055.m04]
  - Self Deletion::COMSPEC Environment Variable [F0007.001]
  - Obfuscated Files or Information::Encryption [E1027.m04]
  - Obfuscated Files or Information::Encryption-Standard Algorithm [E1027.m05]
  - Obfuscated Files or Information::Encoding-Standard Algorithm [E1027.m02]
  - Disable or Evade Security Tools::Bypass Windows File Protection [F0004.007]
  - Process Injection [E1055]
  - Disable or Evade Security Tools::Disable Code Integrity [F0004.009]
  - Hijack Execution Flow::Abuse Windows Function Calls [F0015.006]
  - Process Injection::Injection via Windows Fibers [E1055.m05]
  - Hijack Execution Flow::Import Address Table (IAT) Hooking [F0015.003]
  
### Discovery: ###
  num: 6
   
  - Analysis Tool Discovery::Process detection [B0013.001]
  - Application Window Discovery::Window Text [E1010.m01]
  - Taskbar Discovery [B0043]
  - File and Directory Discovery::Log File [E1083.m01]
  - Code Discovery::Enumerate PE Sections [B0046.001]
  - Code Discovery::Inspect Section Memory Permissions [B0046.002]
  
### Execution: ###
  num: 1
   
  - Install Additional Program [B0023]
  
### Exfiltration: ###
  num: 0
  
### Impact: ###
  num: 5
   
  - Modify Hardware::Mouse [B0042.002]
  - Modify Hardware::CDROM [B0042.001]
  - Clipboard Modification [E1510]
  - Data Destruction::Delete Shadow Copies [E1485.m04]
  - Remote Access::Reverse Shell [B0022.001]
  
### Lateral Movement: ###
  num: 0
  
### Persistence: ###
  num: 0
  
### Privilege Escalation: ###
  num: 0
  


## MBC MICRO-BEHAVIOR MAPPING S##

### Communication: ###
  num: 34
   
  - DNS Communication::Resolve [C0011.001]
  - HTTP Communication::Read Header [C0002.014]
  - HTTP Communication::WinHTTP [C0002.008]
  - HTTP Communication::IWebBrowser [C0002.010]
  - HTTP Communication::Set Header [C0002.013]
  - HTTP Communication::Start Server [C0002.018]
  - HTTP Communication::Receive Request [C0002.015]
  - HTTP Communication::Send Response [C0002.016]
  - HTTP Communication::Get Response [C0002.017]
  - HTTP Communication::Send Request [C0002.003]
  - HTTP Communication::Download URL [C0002.006]
  - HTTP Communication::Create Request [C0002.012]
  - HTTP Communication::Send Data [C0002.005]
  - HTTP Communication::Open URL [C0002.004]
  - HTTP Communication::Connect to Server [C0002.009]
  - HTTP Communication::Extract Body [C0002.011]
  - Socket Communication::Start TCP Server [C0001.005]
  - Socket Communication::TCP Client [C0001.008]
  - Interprocess Communication::Create Pipe [C0003.001]
  - Interprocess Communication::Write Pipe [C0003.004]
  - Interprocess Communication::Connect Pipe [C0003.002]
  - Interprocess Communication::Read Pipe [C0003.003]
  - FTP Communication::Send File [C0004.001]
  - DNS Communication::Server Connect [C0011.002]
  - Socket Communication::Get Socket Status [C0001.012]
  - Socket Communication::Set Socket Config [C0001.001]
  - Socket Communication::Initialize Winsock Library [C0001.009]
  - Socket Communication::Connect Socket [C0001.004]
  - Socket Communication::Create TCP Socket [C0001.011]
  - Socket Communication::Send TCP Data [C0001.014]
  - Socket Communication::Create UDP Socket [C0001.010]
  - Socket Communication::Send Data [C0001.007]
  - Socket Communication::Receive Data [C0001.006]
  - ICMP Communication::Echo Request [C0014.002]

### Cryptography: ###
  num: 16
   
  - Encryption Key::Import Public Key [C0028.001]
  - Decrypt Data [C0031]
  - Encryption Key [C0028]
  - Decrypt Data::AES [C0031.001]
  - Encrypt Data [C0027]
  - Encrypt Data::RC4 [C0027.009]
  - Cryptographic Hash [C0029]
  - Cryptographic Hash::Tiger [C0029.005]
  - Cryptographic Hash::SHA1 [C0029.002]
  - Cryptographic Hash::SHA256 [C0029.003]
  - Cryptographic Hash::MD5 [C0029.001]
  - Cryptographic Hash::SHA224 [C0029.004]
  - Hashed Message Authentication Code [C0061]
  - Generate Pseudo-random Sequence::Use API [C0021.003]
  - Generate Pseudo-random Sequence::Mersenne Twister [C0021.005]
  - Crypto Library [C0059]

### Data: ###
  num: 15
   
  - Checksum::CRC32 [C0032.001]
  - Checksum::Luhn [C0032.002]
  - Checksum::Adler [C0032.005]
  - Non-Cryptographic Hash::MurmurHash [C0030.001]
  - Non-Cryptographic Hash::FNV [C0030.005]
  - Non-Cryptographic Hash [C0030]
  - Encode Data::Base64 [C0026.001]
  - Decompress Data::aPLib [C0025.003]
  - Decompress Data::IEncodingFilterFactory [C0025.002]
  - Compress Data [C0024]
  - Decompress Data::QuickLZ [C0025.001]
  - Decompress Data [C0025]
  - Check String [C0019]
  - Modulo [C0058]
  - Compression Library [C0060]
  
### File System: ###
  num: 11
   
  - Set File Attributes [C0050]
  - Create Directory [C0046]
  - Delete File [C0047]
  - Delete Directory [C0048]
  - Get File Attributes [C0049]
  - Move File [C0063]
  - Writes File [C0052]
  - Copy File [C0045]
  - Read File [C0051]
  - Read Virtual Disk [C0056]
  - Create File [C0016]

### Hardware: ###
  num: 4
   
  - Simulate Hardware::Ctrl-Alt-Del [C0057.001]
  - Install Driver [C0037]
  - Install Driver::Minifilter [C0037.001]
  - Load Driver::Minifilter [C0023.001]

### Memory: ###
  num: 2
   
  - Free Memory [C0044]
  - Allocate Memory [C0007]

### Operating System: ###
  num: 11
   
  - Environment Variable::Set Variable [C0034.001]
  - Environment Variable::Get Variable [C0034.002]
  - Wallpaper [C0035]
  - Console [C0033]
  - Registry::Set Registry Key [C0036.001]
  - Registry::Create Registry Key [C0036.004]
  - Registry::Open Registry Key [C0036.003]
  - Registry::Query Registry Key [C0036.005]
  - Registry::Query Registry Value [C0036.006]
  - Registry::Delete Registry Key [C0036.002]
  - Registry::Delete Registry Value [C0036.007]
  
### Process: ###
  num: 14
   
  - Create Thread [C0038]
  - Suspend Thread [C0055]
  - Terminate Thread [C0039]
  - Resume Thread [C0054]
  - Enumerate Threads [C0064]
  - Create Mutex [C0042]
  - Check Mutex [C0043]
  - Allocate Thread Local Storage [C0040]
  - Set Thread Local Storage Value [C0041]
  - Create Process [C0017]
  - Create Process::Create Suspended Process [C0017.003]
  - Terminate Process [C0018]
  - Open Process [C0065]
  - Open Thread [C0066]
  
