# CAPE Rule Distribution #
February 2023

## Histograms ##
The histograms below show the number of CAPE rules mapped to ATT&CK techniques (organized by tactic), MBC behaviors (organized by objective), and MBC micro-behaviors (organized by micro-objective). The explicit techniques, behaviors, and micro-behaviors follow. 

The data below reflects [community repository signatures](https://github.com/kevoreilly/community/tree/master/modules/signatures) (not including deprecated signatures), as well as [CAPEv2 signatures](https://github.com/kevoreilly/CAPEv2/blob/master/modules/signatures/CAPE.py). 

Information on CAPE signatures can be found [here](https://github.com/kevoreilly/CAPEv2/blob/master/docs/book/src/customization/signatures.rst).

### ATT&CK Mapping Histogram ###

| **TACTIC** | **Number of Techniques**  |  |
|-----|-----|-----|
|**Reconnaissance**|5| **XXXXX** |
|**Resource Development**|2| **XX** |
|**Initial Access**|4| **XXXX** |
|**Execution**|18| **XXXXXXXXXXXXXXXXXX** |
|**Persistence**|34| **XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX** |
|**Privilege Escalation**|27| **XXXXXXXXXXXXXXXXXXXXXXXXXXX** |
|**Defense Evasion**|70| **XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX** |
|**Credential Access**|15| **XXXXXXXXXXXXXXX** |
|**Discovery**|19| **XXXXXXXXXXXXXXXXXXX** |
|**Lateral Movement**|3| **XXX** |
|**Collection**|10| **XXXXXXXXXX** |
|**Command And Control**|18| **XXXXXXXXXXXXXXXXXX** |
|**Exfiltration**|4| **XXXX** |
|**Impact**|11| **XXXXXXXXXXX** |

### MBC Mapping Histogram (Objectives) ###

| **OBJECTIVE** | **Number of Behaviors** |  |
|-----|-----|-----|
|**Anti-behavioral Analysis**|36| **XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX** |
|**Anti-static Analysis**|7| **XXXXXXX** |
|**Collection**|6| **XXXXXX** |
|**Command And Control**|4| **XXXX** |
|**Credential Access**|6| **XXXXXX** |
|**Defense Evasion**|22| **XXXXXXXXXXXXXXXXXXXXXX** |
|**Discovery**|7| **XXXXXXX** |
|**Execution**|3| **XXX** |
|**Exfiltration**|1| **X** |
|**Impact**|9| **XXXXXXXXX** |
|**Lateral Movement**|1| **X** |
|**Persistence**|11| **XXXXXXXXXXX** |
|**Privilege Escalation**|4| **XXXX** |

### MBC Mapping Histogram (Micro-Objectives) ###

| **MICRO-OBJECTIVE** | **Number of Micro-Behaviors**  |  |
|-----|-----|-----|
|**Communication**|13| **XXXXXXXXXXXXX** |
|**Cryptography**|3| **XXX** |
|**Data**|1| **X** |
|**File System**|9| **XXXXXXXXX** |
|**Hardware**|1| **X** |
|**Memory**|3| **XXX** |
|**Process**|5| **XXXXX** |
|**Operating System**|7| **XXXXXXX** |

### Objective-only Mapping Counts ###
This histogram indicates the number of CAPE signatures that map to an MBC objective.

| **OBJECTIVE** | **Number of CAPE signatures** |  |
|-----|-----|-----|
|**Anti-behavioral Analysis**|84| **XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX** |
|**Anti-static Analysis**|23| **XXXXXXXXXXXXXXXXXXXXXXX** |
|**Collection**|10| **XXXXXXXXXX** |
|**Command And Control**|15| **XXXXXXXXXXXXXXX** |
|**Credential Access**|16| **XXXXXXXXXXXXXXXX** |
|**Defense Evasion**|98| **XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX** |
|**Discovery**|68| **XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX** |
|**Execution**|72| **XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX** |
|**Exfiltration**|3| **XXX** |
|**Impact**|22| **XXXXXXXXXXXXXXXXXXXXXX** |
|Lateral Movement|0| |
|**Persistence**|22| **XXXXXXXXXXXXXXXXXXXXXX** |
|**Privilege Escalation**|4| **XXXX** |

This histogram indicates the number of CAPE signatures that map to an MBC micro-objective.

| **MICRO-OBJECTIVE** | **Number of CAPE signatures**  |  |
|-----|-----|-----|
|**Communication**|45| **XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX** |
|**Cryptography**|12| **XXXXXXXXXXXX** |
|**Data**|1| **X** |
|**File System**|51| **XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX** |
|**Hardware**|1| **X** |
|**Memory**|3| **XXX** |
|**Process**|72| **XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX** |
|**Operating System**|94| **XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX** |


## ATT&CK MAPPINGS ##

### Reconnaissance ###
  num: 5
  - Gather Victim Host Information [T1592] Count-2
  - Client Configurations [T1592.004] Count-2
  - Gather Victim Identity Information [T1589] Count-1
  - Credentials [T1589.001] Count-1
  - Software [T1592.002] Count-1

### Resource Development ###
  num: 2
  - Develop Capabilities [T1587] Count-1
  - Digital Certificates [T1587.003] Count-1

### Initial Access ###
  num: 4
  - Replication Through Removable Media [T1091] Count-1
  - Spearphishing Link [T1192] Count-1
  - Phishing [T1566] Count-1
  - Spearphishing Link [T1566.002] Count-1

### Execution ###
  num: 18
  - Exploitation for Client Execution [T1203] Count-19
  - Command and Scripting Interpreter [T1059] Count-52
  - Native API [T1106] Count-13
  - Scripting [T1064] Count-20
  - JavaScript [T1059.007] Count-5
  - PowerShell [T1086] Count-12
  - Regsvr32 [T1117] Count-4
  - PowerShell [T1059.001] Count-14
  - Visual Basic [T1059.005] Count-5
  - Windows Command Shell [T1059.003] Count-2
  - InstallUtil [T1118] Count-2
  - User Execution [T1204] Count-6
  - Scheduled Task/Job [T1053] Count-2
  - Scheduled Task [T1053.005] Count-2
  - At [T1053.002] Count-1
  - Windows Management Instrumentation [T1047] Count-5
  - Malicious File [T1204.002] Count-4
  - Shared Modules [T1129] Count-2

### Persistence ###
  num: 34
  - Office Application Startup [T1137] Count-20
  - Browser Extensions [T1176] Count-2
  - Modify Existing Service [T1031] Count-6
  - New Service [T1050] Count-5
  - Create or Modify System Process [T1543] Count-6
  - Windows Service [T1543.003] Count-6
  - Bootkit [T1067] Count-6
  - Pre-OS Boot [T1542] Count-5
  - Bootkit [T1542.003] Count-5
  - Office Template Macros [T1137.001] Count-6
  - Hidden Files and Directories [T1158] Count-3
  - Image File Execution Options Injection [T1183] Count-2
  - Event Triggered Execution [T1546] Count-4
  - Image File Execution Options Injection [T1546.012] Count-2
  - Server Software Component [T1505] Count-3
  - Web Shell [T1505.003] Count-3
  - Registry Run Keys / Startup Folder [T1060] Count-4
  - Boot or Logon Autostart Execution [T1547] Count-5
  - Registry Run Keys / Startup Folder [T1547.001] Count-4
  - Scheduled Task/Job [T1053] Count-2
  - Scheduled Task [T1053.005] Count-2
  - At [T1053.002] Count-1
  - Accessibility Features [T1015] Count-1
  - Accessibility Features [T1546.008] Count-1
  - Hijack Execution Flow [T1574] Count-2
  - Kernel Modules and Extensions [T1215] Count-1
  - Kernel Modules and Extensions [T1547.006] Count-1
  - DLL Side-Loading [T1574.002] Count-1
  - Add-ins [T1137.006] Count-1
  - Create Account [T1136] Count-2
  - Local Account [T1136.001] Count-2
  - Account Manipulation [T1098] Count-1
  - Application Shimming [T1138] Count-1
  - Application Shimming [T1546.011] Count-1

### Privilege Escalation ###
  num: 27
  - Process Injection [T1055] Count-20
  - New Service [T1050] Count-5
  - Create or Modify System Process [T1543] Count-6
  - Windows Service [T1543.003] Count-6
  - Extra Window Memory Injection [T1055.011] Count-2
  - Image File Execution Options Injection [T1183] Count-2
  - Event Triggered Execution [T1546] Count-4
  - Image File Execution Options Injection [T1546.012] Count-2
  - Boot or Logon Autostart Execution [T1547] Count-5
  - Registry Run Keys / Startup Folder [T1547.001] Count-4
  - Scheduled Task/Job [T1053] Count-2
  - Scheduled Task [T1053.005] Count-2
  - At [T1053.002] Count-1
  - Accessibility Features [T1015] Count-1
  - Accessibility Features [T1546.008] Count-1
  - Hijack Execution Flow [T1574] Count-2
  - Kernel Modules and Extensions [T1547.006] Count-1
  - Bypass User Account Control [T1088] Count-5
  - Abuse Elevation Control Mechanism [T1548] Count-6
  - Bypass User Account Control [T1548.002] Count-5
  - DLL Side-Loading [T1574.002] Count-1
  - Application Shimming [T1138] Count-1
  - Application Shimming [T1546.011] Count-1
  - Portable Executable Injection [T1055.002] Count-1
  - Process Hollowing [T1055.012] Count-2
  - Extra Window Memory Injection [T1181] Count-1
  - Process Doppelgänging [T1055.013] Count-1

### Defense Evasion ###
  num: 70
  - Virtualization/Sandbox Evasion [T1497] Count-39
  - Time Based Evasion [T1497.003] Count-4
  - Modify Registry [T1112] Count-75
  - Masquerading [T1036] Count-11
  - Masquerade Task or Service [T1036.004] Count-1
  - Match Legitimate Name or Location [T1036.005] Count-3
  - Disabling Security Tools [T1089] Count-22
  - Impair Defenses [T1562] Count-30
  - Disable or Modify Tools [T1562.001] Count-17
  - Hidden Window [T1143] Count-1
  - Hide Artifacts [T1564] Count-6
  - Hidden Window [T1564.003] Count-1
  - System Checks [T1497.001] Count-12
  - Scripting [T1064] Count-20
  - Software Packing [T1045] Count-21
  - Obfuscated Files or Information [T1027] Count-30
  - Software Packing [T1027.002] Count-22
  - Indicator Blocking [T1054] Count-7
  - Impair Command History Logging [T1562.003] Count-1
  - Indicator Blocking [T1562.006] Count-7
  - Regsvr32 [T1117] Count-4
  - System Binary Proxy Execution [T1218] Count-8
  - Regsvr32 [T1218.010] Count-4
  - Rootkit [T1014] Count-4
  - Process Injection [T1055] Count-20
  - Disable or Modify System Firewall [T1562.004] Count-3
  - Timestomp [T1099] Count-4
  - Indicator Removal [T1070] Count-11
  - Timestomp [T1070.006] Count-4
  - Pre-OS Boot [T1542] Count-5
  - Bootkit [T1542.003] Count-5
  - Extra Window Memory Injection [T1055.011] Count-2
  - Code Signing [T1116] Count-2
  - Subvert Trust Controls [T1553] Count-5
  - Code Signing [T1553.002] Count-3
  - Invalid Code Signature [T1036.001] Count-2
  - Hidden Files and Directories [T1158] Count-3
  - Hidden Files and Directories [T1564.001] Count-3
  - InstallUtil [T1118] Count-2
  - Trusted Developer Utilities Proxy Execution [T1127] Count-3
  - InstallUtil [T1218.004] Count-2
  - Image File Execution Options Injection [T1183] Count-2
  - Clear Windows Event Logs [T1070.001] Count-1
  - NTFS File Attributes [T1096] Count-3
  - NTFS File Attributes [T1564.004] Count-2
  - Indirect Command Execution [T1202] Count-4
  - Rename System Utilities [T1036.003] Count-1
  - Install Root Certificate [T1130] Count-1
  - Deobfuscate/Decode Files or Information [T1140] Count-4
  - Install Root Certificate [T1553.004] Count-2
  - Compile After Delivery [T1500] Count-3
  - Compile After Delivery [T1027.004] Count-3
  - File Deletion [T1107] Count-2
  - File Deletion [T1070.004] Count-2
  - User Activity Based Checks [T1497.002] Count-1
  - Hijack Execution Flow [T1574] Count-2
  - Bypass User Account Control [T1088] Count-5
  - Abuse Elevation Control Mechanism [T1548] Count-6
  - Bypass User Account Control [T1548.002] Count-5
  - DLL Side-Loading [T1073] Count-1
  - DLL Side-Loading [T1574.002] Count-1
  - Disable Windows Event Logging [T1562.002] Count-1
  - CMSTP [T1218.003] Count-1
  - Template Injection [T1221] Count-1
  - Portable Executable Injection [T1055.002] Count-1
  - Process Hollowing [T1093] Count-2
  - Process Hollowing [T1055.012] Count-2
  - Extra Window Memory Injection [T1181] Count-1
  - Process Doppelgänging [T1186] Count-1
  - Process Doppelgänging [T1055.013] Count-1

### Credential Access ###
  num: 15
  - Credentials in Files [T1081] Count-7
  - OS Credential Dumping [T1003] Count-18
  - Unsecured Credentials [T1552] Count-8
  - Credentials In Files [T1552.001] Count-7
  - Input Capture [T1056] Count-3
  - Keylogging [T1056.001] Count-2
  - Credentials from Password Stores [T1555] Count-6
  - Credentials from Web Browsers [T1503] Count-5
  - Credentials from Web Browsers [T1555.003] Count-5
  - Group Policy Preferences [T1552.006] Count-1
  - Steal Web Session Cookie [T1539] Count-1
  - LSASS Memory [T1003.001] Count-1
  - Security Account Manager [T1003.002] Count-4
  - LSA Secrets [T1003.004] Count-1
  - Network Sniffing [T1040] Count-1

### Discovery ###
  num: 19
  - Process Discovery [T1057] Count-35
  - File and Directory Discovery [T1083] Count-31
  - Virtualization/Sandbox Evasion [T1497] Count-39
  - Time Based Evasion [T1497.003] Count-4
  - System Information Discovery [T1082] Count-24
  - System Checks [T1497.001] Count-12
  - Security Software Discovery [T1063] Count-18
  - Software Discovery [T1518] Count-21
  - Security Software Discovery [T1518.001] Count-18
  - Application Window Discovery [T1010] Count-3
  - Permission Groups Discovery [T1069] Count-2
  - Query Registry [T1012] Count-21
  - System Owner/User Discovery [T1033] Count-3
  - System Network Configuration Discovery [T1016] Count-4
  - Domain Trust Discovery [T1482] Count-2
  - Account Discovery [T1087] Count-3
  - User Activity Based Checks [T1497.002] Count-1
  - System Service Discovery [T1007] Count-1
  - Network Sniffing [T1040] Count-1

### Lateral Movement ###
  num: 3
  - Remote Services [T1021] Count-4
  - Remote Desktop Protocol [T1021.001] Count-3
  - Replication Through Removable Media [T1091] Count-1

### Collection ###
  num: 10
  - Data from Local System [T1005] Count-7
  - Email Collection [T1114] Count-2
  - Input Capture [T1056] Count-3
  - Keylogging [T1056.001] Count-2
  - Data Staged [T1074] Count-1
  - Screen Capture [T1113] Count-2
  - Clipboard Data [T1115] Count-3
  - Archive Collected Data [T1560] Count-4
  - Browser Session Hijacking [T1185] Count-3
  - Automated Collection [T1119] Count-1

### Command And Control ###
  num: 18
  - Application Layer Protocol [T1071] Count-35
  - Remote Access Software [T1219] Count-39
  - Proxy [T1090] Count-5
  - Web Protocols [T1071.001] Count-19
  - Multi-hop Proxy [T1188] Count-3
  - Multi-hop Proxy [T1090.003] Count-3
  - Standard Cryptographic Protocol [T1032] Count-15
  - Encrypted Channel [T1573] Count-14
  - File Transfer Protocols [T1071.002] Count-1
  - Non-Application Layer Protocol [T1095] Count-4
  - Custom Command and Control Protocol [T1094] Count-2
  - DNS [T1071.004] Count-7
  - Ingress Tool Transfer [T1105] Count-2
  - Data Encoding [T1132] Count-1
  - Standard Encoding [T1132.001] Count-1
  - Domain Generation Algorithms [T1483] Count-2
  - Dynamic Resolution [T1568] Count-3
  - Domain Generation Algorithms [T1568.002] Count-2

### Exfiltration ###
  num: 4
  - Exfiltration Over C2 Channel [T1041] Count-2
  - Automated Exfiltration [T1020] Count-1
  - Data Encrypted [T1022] Count-4
  - Exfiltration Over Alternative Protocol [T1048] Count-2

### Impact ###
  num: 11
  - Data Encrypted for Impact [T1486] Count-22
  - Endpoint Denial of Service [T1499] Count-3
  - Application or System Exploitation [T1499.004] Count-3
  - Service Stop [T1489] Count-1
  - Defacement [T1491] Count-1
  - Internal Defacement [T1491.001] Count-1
  - System Shutdown/Reboot [T1529] Count-1
  - Inhibit System Recovery [T1490] Count-8
  - Data Destruction [T1485] Count-4
  - Disk Wipe [T1561] Count-1
  - Resource Hijacking [T1496] Count-2

## MBC MAPPINGS ##

### Anti-behavioral Analysis ###
  num: 36
  - Sandbox Detection [B0007] Count-10
  - Sandbox Detection [B0007.002] Count-5
  - Dynamic Analysis Evasion [B0003] Count-5
  - Dynamic Analysis Evasion [B0003.002] Count-1
  - Dynamic Analysis Evasion [B0003.003] Count-1
  - Virtual Machine Detection [B0009] Count-29
  - Virtual Machine Detection [B0009.015] Count-1
  - Software Packing [F0001] Count-19
  - Software Packing [F0001.010] Count-1
  - Virtual Machine Detection [B0009.001] Count-6
  - Debugger Detection [B0001] Count-9
  - Debugger Detection [B0001.002] Count-1
  - Debugger Detection [B0001.012] Count-1
  - Debugger Detection [B0001.001] Count-1
  - Software Packing [F0001.009] Count-1
  - Dynamic Analysis Evasion [B0003.010] Count-1
  - Emulator Detection [B0004] Count-4
  - Virtual Machine Detection [B0009.005] Count-13
  - Virtual Machine Detection [B0009.024] Count-2
  - Debugger Detection [B0001.030] Count-1
  - Virtual Machine Detection [B0009.008] Count-3
  - Debugger Detection [B0001.016] Count-1
  - Sandbox Detection [B0007.003] Count-1
  - Virtual Machine Detection [B0009.012] Count-1
  - Debugger Detection [B0001.032] Count-1
  - Emulator Detection [B0004.003] Count-2
  - Software Packing [F0001.008] Count-1
  - Debugger Detection [B0001.009] Count-1
  - Debugger Evasion [B0002] Count-3
  - Debugger Evasion [B0002.008] Count-1
  - Software Packing [F0001.013] Count-1
  - Virtual Machine Detection [B0009.006] Count-1
  - Software Packing [F0001.011] Count-2
  - Debugger Evasion [B0002.024] Count-1
  - Debugger Detection [B0001.014] Count-1
  - Virtual Machine Detection [B0009.009] Count-1

### Anti-static Analysis ###
  num: 7
  - Software Packing [F0001] Count-19
  - Software Packing [F0001.010] Count-1
  - Software Packing [F0001.009] Count-1
  - Obfuscated Files or Information [E1027] Count-6
  - Software Packing [F0001.008] Count-1
  - Software Packing [F0001.013] Count-1
  - Software Packing [F0001.011] Count-2

### Collection ###
  num: 6
  - Keylogging [F0002] Count-2
  - Keylogging [F0002.001] Count-1
  - Screen Capture [E1113] Count-2
  - Cryptocurrency [B0028] Count-1
  - Cryptocurrency [B0028.001] Count-1
  - Input Capture [E1056] Count-3

### Command And Control ###
  num: 4
  - C2 Communication [B0030] Count-14
  - C2 Communication [B0030.005] Count-1
  - Ingress Tool Transfer [E1105] Count-1
  - Domain Name Generation [B0031] Count-2

### Credential Access ###
  num: 6
  - Keylogging [F0002] Count-2
  - Keylogging [F0002.001] Count-1
  - Screen Capture [E1113] Count-2
  - Cryptocurrency [B0028] Count-1
  - Cryptocurrency [B0028.001] Count-1
  - Input Capture [E1056] Count-3

### Defense Evasion ###
  num: 22
  - Modify Registry [E1112] Count-71
  - Disable or Evade Security Tools [F0004] Count-23
  - Hidden Files and Directories [F0005] Count-7
  - Hidden Files and Directories [F0005.002] Count-1
  - Indicator Blocking [F0006] Count-7
  - Software Packing [F0001] Count-19
  - Software Packing [F0001.010] Count-1
  - Rootkit [E1014] Count-4
  - Process Injection [E1055] Count-23
  - Software Packing [F0001.009] Count-1
  - Hidden Files and Directories [F0005.004] Count-3
  - Bypass Data Execution Prevention [B0037] Count-1
  - Bootkit [F0013] Count-5
  - Obfuscated Files or Information [E1027] Count-6
  - Disable or Evade Security Tools [F0004.005] Count-3
  - Polymorphic Code [B0029] Count-1
  - Self Deletion [F0007] Count-2
  - Disable or Evade Security Tools [F0004.007] Count-1
  - Software Packing [F0001.008] Count-1
  - Disable or Evade Security Tools [F0004.003] Count-1
  - Software Packing [F0001.013] Count-1
  - Software Packing [F0001.011] Count-2

### Discovery ###
  num: 7
  - File and Directory Discovery [E1083] Count-17
  - System Information Discovery [E1082] Count-24
  - Application Window Discovery [E1010] Count-1
  - Analysis Tool Discovery [B0013] Count-5
  - Analysis Tool Discovery [B0013.001] Count-1
  - Analysis Tool Discovery [B0013.009] Count-1
  - Analysis Tool Discovery [B0013.008] Count-1

### Execution ###
  num: 3
  - Exploitation for Client Execution [E1203] Count-26
  - Command and Scripting Interpreter [E1059] Count-47
  - Install Additional Program [B0023] Count-5

### Exfiltration ###
  num: 1
  - Archive Collected Data [E1560] Count-6

### Impact ###
  num: 9
  - Exploitation for Client Execution [E1203] Count-26
  - Data Encrypted for Impact [E1486] Count-8
  - Remote Access [B0022] Count-43
  - Denial of Service [B0033] Count-4
  - Disk Wipe [F0014] Count-2
  - Disk Wipe [F0014.001] Count-1
  - Data Destruction [E1485] Count-4
  - Resource Hijacking [B0018] Count-2
  - Resource Hijacking [B0018.002] Count-1

### Lateral Movement ###
  num: 1
  - Ingress Tool Transfer [E1105] Count-1

### Persistence ###
  num: 11
  - Remote Access [B0022] Count-43
  - Modify Registry [E1112] Count-71
  - Hidden Files and Directories [F0005] Count-7
  - Hidden Files and Directories [F0005.002] Count-1
  - Kernel Modules and Extensions [F0010] Count-2
  - Kernel Modules and Extensions [F0010.001] Count-1
  - Modify Existing Service [F0011] Count-6
  - Hidden Files and Directories [F0005.004] Count-3
  - Bootkit [F0013] Count-5
  - Registry Run Keys / Startup Folder [F0012] Count-3
  - Ingress Tool Transfer [E1105] Count-1

### Privilege Escalation ###
  num: 4
  - Process Injection [E1055] Count-23
  - Kernel Modules and Extensions [F0010] Count-2
  - Kernel Modules and Extensions [F0010.001] Count-1
  - Modify Existing Service [F0011] Count-6

## MBC MICRO-BEHAVIOR MAPPINGS ##

### Communication ###
  num: 13
  - HTTP Communication [C0002] Count-23
  - HTTP Communication [C0002.003] Count-1
  - HTTP Communication [C0002.005] Count-3
  - WinINet [C0005] Count-5
  - WinINet [C0005.002] Count-1
  - WinINet [C0005.003] Count-1
  - SMTP Communication [C0012] Count-1
  - Socket Communication [C0001] Count-6
  - WinINet [C0005.001] Count-1
  - DNS Communication [C0011] Count-8
  - ICMP Communication [C0014] Count-2
  - Interprocess Communication [C0003] Count-1
  - Interprocess Communication [C0003.001] Count-1

### Cryptography ###
  num: 3
  - Encrypt Data [C0027] Count-10
  - Encryption Key [C0028] Count-1
  - Decrypt Data [C0031] Count-1

### Data ###
  num: 1
  - Decompress Data [C0025] Count-1

### File System ###
  num: 9
  - Create File [C0016] Count-24
  - Writes File [C0052] Count-8
  - Create Directory [C0046] Count-1
  - Alter File Extension [C0015] Count-4
  - Delete File [C0047] Count-7
  - Read File [C0051] Count-6
  - Create File [C0016.002] Count-1
  - Copy File [C0045] Count-1
  - Create File [C0016.001] Count-1

### Hardware ###
  num: 1
  - Load Driver [C0023] Count-1

### Memory ###
  num: 3
  - Change Memory Protection [C0008] Count-1
  - Heap Spray [C0006] Count-1
  - Allocate Memory [C0007] Count-1

### Process ###
  num: 5
  - Create Mutex [C0042] Count-59
  - Check Mutex [C0043] Count-4
  - Create Process [C0017] Count-3
  - Create Process [C0017.002] Count-1
  - Create Thread [C0038] Count-4

### Operating System ###
  num: 7
  - Registry [C0036] Count-89
  - Registry [C0036.001] Count-9
  - Wallpaper [C0035] Count-1
  - Console [C0033] Count-1
  - Registry [C0036.005] Count-16
  - Registry [C0036.003] Count-3
  - Registry [C0036.006] Count-1
