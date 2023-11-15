## Malware Objectives
| ID | Objective | Description |
|----|-----------|-------------|
|OB0001|**[Anti-Behavioral Analysis](https://github.com/MBCProject/mbc-markdown/blob/main/anti-behavioral-analysis/README.md)**|Behaviors that prevent, obstruct, or evade behavioral analysis of malware--for example, analysis done using a sandbox or debugger. Because the underlying methods differ, separate "detection" and "evasion" behaviors are defined for some anti-behavioral analysis areas.|
|OB0002|**[Anti-Static Analysis](https://github.com/MBCProject/mbc-markdown/blob/main/anti-static-analysis/README.md)**|Behaviors and code characteristics that prevent or hinder static analysis of the malware. Simple static analysis identifies features such as embedded strings, header information, or file metadata. More involved static analysis involves the disassembly of the binary code.|
|OB0003|**[Collection](https://github.com/MBCProject/mbc-markdown/blob/main/collection/README.md)**|Behaviors that enable malware to identify and gather information, such as sensitive files, from a machine or network. Sources often targeted include drives, browsers, audio/video, and email. Often the malware's next objective is to exfiltrate the information gathered.|
|OB0004|**[Command and Control](https://github.com/MBCProject/mbc-markdown/blob/main/command-and-control/README.md)**|Behaviors that enable malware to communicate with systems such as C2 servers or bots. Malware can establish command and control with various levels of covertness, depending on system configuration and network topology.|
|OB0005|**[Credential Access](https://github.com/MBCProject/mbc-markdown/blob/main/credential-access/README.md)**|Behaviors to obtain credential access, allowing it or its underlying threat actor to assume control of an account with the associated system and network permissions.|
|OB0006|**[Defense Evasion](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/README.md)**|Behaviors that enable malware to evade detection.|
|OB0007|**[Discovery](https://github.com/MBCProject/mbc-markdown/blob/main/discovery/README.md)**|Behaviors that enable malware to gain knowledge about the system and network.|
|OB0009|**[Execution](https://github.com/MBCProject/mbc-markdown/blob/main/execution/README.md)**|Behaviors that enable malware to execute code on a system to achieve a variety of goals.|
|OB0010|**[Exfiltration](https://github.com/MBCProject/mbc-markdown/blob/main/exfiltration/README.md)**|Behaviors that enable malware to steal data from a system. This includes stored data, such as files, as well as data input into applications, such as web browsers.|
|OB0008|**[Impact](https://github.com/MBCProject/mbc-markdown/blob/main/impact/README.md)**|Behaviors that enable malware to manipulate, interrupt, or destroy systems and data.|
|OB0011|**[Lateral Movement](https://github.com/MBCProject/mbc-markdown/blob/main/lateral-movement/README.md)**|Behaviors that enable malware to propagate or otherwise move through an environment. Lateral movement may be active, happening via direct machine access, or may be passive (for example, done via malicious email).|
|OB0012|**[Persistence](https://github.com/MBCProject/mbc-markdown/blob/main/persistence/README.md)**|Behaviors that enable malware to remain on a system regardless of system events, such as reboots.|
|OB0013|**[Privilege Escalation](https://github.com/MBCProject/mbc-markdown/blob/main/privilege-escalation/README.md)**|Behaviors that enable malware to obtain higher level permissions. These behaviors often overlap with Persistence behaviors.|

## Malware Micro-objectives
| ID | Micro-objective | Description |
|----|-----------------|-------------|
|OC0006|**[Communication](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/communication/README.md)**|Micro-behaviors that enable malware to communicate.|
|OC0005|**[Cryptography](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/cryptography/README.md)**|Micro-behaviors that enable malware to use crypto.|
|OC0004|**[Data](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/data/README.md)**|Micro-behaviors related to malware manipulating data.|
|OC0001|**[File System](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/README.md)**|Micro-behaviors related to file manipulation.|
|OC0007|**[Hardware](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/hardware/README.md)**|Micro-behaviors related to hardware.|
|OC0002|**[Memory](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/memory/README.md)**|Micro-behaviors related to malware manipulating machine memory.|
|OC0008|**[Operating System](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/operating-system/README.md)**|Micro-behaviors related to operating systems.|
|OC0003|**[Process](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/README.md)**|Micro-behaviors related to processes.|

## Malware Behaviors
| ID | Objective(s) | Behavior | Related ATT&CK Technique |
|----|--------------|----------|--------------------------|
|B0027|DEFENSE EVASION|**[Alternative Installation Location](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/alternative-installation-location.md)**|*none*|
|B0013|DISCOVERY|**[Analysis Tool Discovery](https://github.com/MBCProject/mbc-markdown/blob/main/discovery/analysis-tool-discovery.md)**|*none*|
|B0037|DEFENSE EVASION|**[Bypass Data Execution Prevention](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/bypass-data-execution-prevention.md)**|*none*|
|B0030|COMMAND AND CONTROL|**[C2 Communication](https://github.com/MBCProject/mbc-markdown/blob/main/command-and-control/c2-communication.md)**|*none*|
|B0010|ANTI-STATIC ANALYSIS|**[Call Graph Generation Evasion](https://github.com/MBCProject/mbc-markdown/blob/main/anti-static-analysis/call-graph-generation-evasion.md)**|*none*|
|B0036|ANTI-BEHAVIORAL ANALYSIS|**[Capture Evasion](https://github.com/MBCProject/mbc-markdown/blob/main/anti-behavioral-analysis/capture-evasion.md)**|*none*|
|B0046|DISCOVERY|**[Code Discovery](https://github.com/MBCProject/mbc-markdown/blob/main/discovery/code-discovery.md)**|*none*|
|B0016|IMPACT|**[Compromise Data Integrity](https://github.com/MBCProject/mbc-markdown/blob/main/impact/compromise-data-integrity.md)**|Data Manipulation: Stored Data Manipulation ([T1565.001](https://attack.mitre.org/techniques/T1565/001/))|
|B0025|EXECUTION, ANTI-BEHAVIORAL ANALYSIS, DEFENSE EVASION|**[Conditional Execution](https://github.com/MBCProject/mbc-markdown/blob/main/execution/conditional-execution.md)**|Execution Guardrails  ([T1480](https://attack.mitre.org/techniques/T1480))|
|B0040|DEFENSE EVASION|**[Covert Location](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/covert-location.md)**|*none*|
|B0028|COLLECTION, CREDENTIAL ACCESS|**[Cryptocurrency](https://github.com/MBCProject/mbc-markdown/blob/main/collection/cryptocurrency.md)**|*none*|
|B0045|ANTI-STATIC ANALYSIS|**[Data Flow Analysis Evasion](https://github.com/MBCProject/mbc-markdown/blob/main/anti-static-analysis/data-flow-analysis-evasion.md)**|*none*|
|B0001|ANTI-BEHAVIORAL ANALYSIS|**[Debugger Detection](https://github.com/MBCProject/mbc-markdown/blob/main/anti-behavioral-analysis/debugger-detection.md)**|*none*|
|B0002|ANTI-BEHAVIORAL ANALYSIS|**[Debugger Evasion](https://github.com/MBCProject/mbc-markdown/blob/main/anti-behavioral-analysis/debugger-evasion.md)**|Debugger Evasion ([T1622](https://attack.mitre.org/techniques/T1622/))|
|B0033|IMPACT|**[Denial of Service](https://github.com/MBCProject/mbc-markdown/blob/main/impact/denial-of-service.md)**|Network Denial of Service ([T1498](https://attack.mitre.org/techniques/T1498/))|
|B0017|IMPACT|**[Destroy Hardware](https://github.com/MBCProject/mbc-markdown/blob/main/impact/destroy-hardware.md)**|*none*|
|B0012|ANTI-STATIC ANALYSIS|**[Disassembler Evasion](https://github.com/MBCProject/mbc-markdown/blob/main/anti-static-analysis/disassembler-evasion.md)**|*none*|
|B0031|COMMAND AND CONTROL|**[Domain Name Generation](https://github.com/MBCProject/mbc-markdown/blob/main/command-and-control/domain-name-generation.md)**|Dynamic Resolution: Domain Generation Algorithms ([T1568.002](https://attack.mitre.org/techniques/T1568/002/))|
|B0003|ANTI-BEHAVIORAL ANALYSIS|**[Dynamic Analysis Evasion](https://github.com/MBCProject/mbc-markdown/blob/main/anti-behavioral-analysis/dynamic-analysis-evasion.md)**|Virtualization/Sandbox Evasion ([T1497](https://attack.mitre.org/techniques/T1497/),[T1633](https://attack.mitre.org/techniques/T1633/))|
|B0004|ANTI-BEHAVIORAL ANALYSIS|**[Emulator Detection](https://github.com/MBCProject/mbc-markdown/blob/main/anti-behavioral-analysis/emulator-detection.md)**|*none*|
|B0005|ANTI-BEHAVIORAL ANALYSIS|**[Emulator Evasion](https://github.com/MBCProject/mbc-markdown/blob/main/anti-behavioral-analysis/emulator-evasion.md)**|*none*|
|B0032|ANTI-STATIC ANALYSIS|**[Executable Code Obfuscation](https://github.com/MBCProject/mbc-markdown/blob/main/anti-static-analysis/executable-code-obfuscation.md)**|*none*|
|B0034|ANTI-STATIC ANALYSIS|**[Executable Code Optimization](https://github.com/MBCProject/mbc-markdown/blob/main/anti-static-analysis/executable-code-optimization.md)**|*none*|
|B0008|ANTI-BEHAVIORAL ANALYSIS, ANTI-STATIC ANALYSIS|**[Executable Code Virtualization](https://github.com/MBCProject/mbc-markdown/blob/main/anti-static-analysis/executable-code-virtualization.md)**|*none*|
|B0044|EXECUTION|**[Execution Dependency](https://github.com/MBCProject/mbc-markdown/blob/main/execution/execution-dependency.md)**|*none*|
|B0023|EXECUTION|**[Install Additional Program](https://github.com/MBCProject/mbc-markdown/blob/main/execution/install-additional-program.md)**|*none*|
|B0047|DEFENSE EVASION, PERSISTENCE|**[Install Insecure or Malicious Configuration](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/install-insecure-or-malicious-configuration.md)**|*none*|
|B0026|LATERAL MOVEMENT, PERSISTENCE|**[Malicious Network Driver](https://github.com/MBCProject/mbc-markdown/blob/main/persistence/malicious-network-driver.md)**|*none*|
|B0019|IMPACT|**[Manipulate Network Traffic](https://github.com/MBCProject/mbc-markdown/blob/main/impact/manipulate-network-traffic.md)**|Data Manipulation: Transmitted Data Manipulation ([T1565.002](https://attack.mitre.org/techniques/T1565/002/))|
|B0006|ANTI-BEHAVIORAL ANALYSIS|**[Memory Dump Evasion](https://github.com/MBCProject/mbc-markdown/blob/main/anti-behavioral-analysis/memory-dump-evasion.md)**|*none*|
|B0042|IMPACT|**[Modify Hardware](https://github.com/MBCProject/mbc-markdown/blob/main/impact/modify-hardware.md)**|*none*|
|B0029|DEFENSE EVASION|**[Polymorphic Code](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/polymorphic-code.md)**|*none*|
|B0024|EXECUTION|**[Prevent Concurrent Execution](https://github.com/MBCProject/mbc-markdown/blob/main/execution/prevent-concurrent-execution.md)**|*none*|
|B0022|IMPACT, PERSISTENCE|**[Remote Access](https://github.com/MBCProject/mbc-markdown/blob/main/impact/remote-access.md)**|*none*|
|B0011|EXECUTION|**[Remote Commands](https://github.com/MBCProject/mbc-markdown/blob/main/execution/remote-commands.md)**|*none*|
|B0018|IMPACT|**[Resource Hijacking](https://github.com/MBCProject/mbc-markdown/blob/main/impact/resource-hijacking.md)**|Resource Hijacking ([T1496](https://attack.mitre.org/techniques/T1496/))|
|B0014|DISCOVERY|**[SMTP Connection Discovery](https://github.com/MBCProject/mbc-markdown/blob/main/discovery/smtp-connection-discovery.md)**|*none*|
|B0007|ANTI-BEHAVIORAL ANALYSIS|**[Sandbox Detection](https://github.com/MBCProject/mbc-markdown/blob/main/anti-behavioral-analysis/sandbox-detection.md)**|Virtualization/Sandbox Evasion: System Checks ([T1497.001](https://attack.mitre.org/techniques/T1497/001/),[T1633.001](https://attack.mitre.org/techniques/T1633/001/)); Virtualization/Sandbox Evasion: User Activity Based Checks ([T1497.002](https://attack.mitre.org/techniques/T1497/002/))|
|B0038|DISCOVERY|**[Self Discovery](https://github.com/MBCProject/mbc-markdown/blob/main/discovery/self-discovery.md)**|*none*|
|B0020|EXECUTION, LATERAL MOVEMENT|**[Send Email](https://github.com/MBCProject/mbc-markdown/blob/main/execution/send-email.md)**|Phishing ([T1566](https://attack.mitre.org/techniques/T1566/))|
|B0021|EXECUTION, LATERAL MOVEMENT|**[Send Poisoned Text Message](https://github.com/MBCProject/mbc-markdown/blob/main/execution/send-poisoned-text-message.md)**|*none*|
|B0035|PERSISTENCE|**[Shutdown Event](https://github.com/MBCProject/mbc-markdown/blob/main/persistence/shutdown-event.md)**|*none*|
|B0039|IMPACT|**[Spamming](https://github.com/MBCProject/mbc-markdown/blob/main/impact/spamming.md)**|*none*|
|B0043|DISCOVERY|**[Taskbar Discovery](https://github.com/MBCProject/mbc-markdown/blob/main/discovery/taskbar-discovery.md)**|*none*|
|B0009|ANTI-BEHAVIORAL ANALYSIS|**[Virtual Machine Detection](https://github.com/MBCProject/mbc-markdown/blob/main/anti-behavioral-analysis/virtual-machine-detection.md)**|Virtualization/Sandbox Evasion ([T1497](https://attack.mitre.org/techniques/T1497/),[T1633](https://attack.mitre.org/techniques/T1633/))|

## Malware Micro-behaviors
| ID | Objective(s) | Micro-behavior |
|----|--------------|----------------|
|C0007|MEMORY|**[Allocate Memory](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/memory/allocate-memory.md)**|
|C0040|PROCESS|**[Allocate Thread Local Storage](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/allocate-thread-local-storage.md)**|
|C0015|FILE SYSTEM|**[Alter File Extension](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/alter-file-extension.md)**|
|C0008|MEMORY|**[Change Memory Protection](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/memory/change-memory-protection.md)**|
|C0043|PROCESS|**[Check Mutex](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/check-mutex.md)**|
|C0019|DATA|**[Check String](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/data/check-string.md)**|
|C0032|DATA|**[Checksum](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/data/checksum.md)**|
|C0024|DATA|**[Compress Data](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/data/compress-data.md)**|
|C0060|DATA|**[Compression Library](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/data/compression-library.md)**|
|C0033|OPERATING SYSTEM|**[Console](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/operating-system/console.md)**|
|C0045|FILE SYSTEM|**[Copy File](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/copy-file.md)**|
|C0046|FILE SYSTEM|**[Create Directory](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/create-directory.md)**|
|C0016|FILE SYSTEM|**[Create File](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/create-file.md)**|
|C0042|PROCESS|**[Create Mutex](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/create-mutex.md)**|
|C0017|PROCESS|**[Create Process](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/create-process.md)**|
|C0038|PROCESS|**[Create Thread](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/create-thread.md)**|
|C0068|CRYPTOGRAPHY|**[Crypto Algorithm](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/cryptography/crypto-algorithm.md)**|
|C0069|CRYPTOGRAPHY|**[Crypto Constant](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/cryptography/crypto-constant.md)**|
|C0059|CRYPTOGRAPHY|**[Crypto Library](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/cryptography/crypto-library.md)**|
|C0029|CRYPTOGRAPHY|**[Cryptographic Hash](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/cryptography/cryptographic-hash.md)**|
|C0011|COMMUNICATION|**[DNS Communication](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/communication/dns-communication.md)**|
|C0053|DATA|**[Decode Data](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/data/decode-data.md)**|
|C0025|DATA|**[Decompress Data](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/data/decompress-data.md)**|
|C0031|CRYPTOGRAPHY|**[Decrypt Data](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/cryptography/decrypt-data.md)**|
|C0048|FILE SYSTEM|**[Delete Directory](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/delete-directory.md)**|
|C0047|FILE SYSTEM|**[Delete File](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/delete-file.md)**|
|C0026|DATA|**[Encode Data](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/data/encode-data.md)**|
|C0027|CRYPTOGRAPHY|**[Encrypt Data](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/cryptography/encrypt-data.md)**|
|C0028|CRYPTOGRAPHY|**[Encryption Key](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/cryptography/encryption-key.md)**|
|C0064|PROCESS|**[Enumerate Threads](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/enumerate-threads.md)**|
|C0034|OPERATING SYSTEM|**[Environment Variable](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/operating-system/environment-variable.md)**|
|C0004|COMMUNICATION|**[FTP Communication](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/communication/ftp-communication.md)**|
|C0044|MEMORY|**[Free Memory](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/memory/free-memory.md)**|
|C0021|CRYPTOGRAPHY|**[Generate Pseudo-random Sequence](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/cryptography/generate-pseudorandom-sequence.md)**|
|C0049|FILE SYSTEM|**[Get File Attributes](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/get-file-attributes.md)**|
|C0002|COMMUNICATION|**[HTTP Communication](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/communication/http-communication.md)**|
|C0061|CRYPTOGRAPHY|**[Hashed Message Authentication Code](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/cryptography/hashed-message-authentication-code.md)**|
|C0006|MEMORY|**[Heap Spray](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/memory/heap-spray.md)**|
|C0014|COMMUNICATION|**[ICMP Communication](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/communication/icmp-communication.md)**|
|C0037|HARDWARE|**[Install Driver](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/hardware/install-driver.md)**|
|C0003|COMMUNICATION|**[Interprocess Communication](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/communication/interprocess-communication.md)**|
|C0023|HARDWARE|**[Load Driver](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/hardware/load-driver.md)**|
|C0058|DATA|**[Modulo](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/data/modulo.md)**|
|C0063|FILE SYSTEM|**[Move File](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/move-file.md)**|
|C0030|DATA|**[Non-Cryptographic Hash](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/data/noncryptographic-hash.md)**|
|C0065|PROCESS|**[Open Process](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/open-process.md)**|
|C0066|PROCESS|**[Open Thread](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/open-thread.md)**|
|C0010|MEMORY|**[Overflow Buffer](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/memory/overflow-buffer.md)**|
|C0051|FILE SYSTEM|**[Read File](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/read-file.md)**|
|C0056|FILE SYSTEM|**[Read Virtual Disk](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/read-virtual-disk.md)**|
|C0036|OPERATING SYSTEM|**[Registry](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/operating-system/registry.md)**|
|C0054|PROCESS|**[Resume Thread](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/resume-thread.md)**|
|C0012|COMMUNICATION|**[SMTP Communication](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/communication/smtp-communication.md)**|
|C0050|FILE SYSTEM|**[Set File Attributes](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/set-file-attributes.md)**|
|C0072|PROCESS|**[Set Thread Context](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/set-thread-context.md)**|
|C0041|PROCESS|**[Set Thread Local Storage Value](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/set-thread-local-storage-value.md)**|
|C0057|HARDWARE|**[Simulate Hardware](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/hardware/simulate-hardware.md)**|
|C0001|COMMUNICATION|**[Socket Communication](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/communication/socket-communication.md)**|
|C0009|MEMORY|**[Stack Pivot](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/memory/stack-pivot.md)**|
|C0055|PROCESS|**[Suspend Thread](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/suspend-thread.md)**|
|C0022|PROCESS|**[Synchronization](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/synchronization.md)**|
|C0018|PROCESS|**[Terminate Process](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/terminate-process.md)**|
|C0039|PROCESS|**[Terminate Thread](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/terminate-thread.md)**|
|C0070|PROCESS|**[Unmap Section View](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/unmap-section-view.md)**|
|C0020|DATA|**[Use Constant](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/data/use-constant.md)**|
|C0035|OPERATING SYSTEM|**[Wallpaper](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/operating-system/wallpaper.md)**|
|C0005|COMMUNICATION|**[WinINet](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/communication/wininet.md)**|
|C0071|PROCESS|**[Write Process Memory](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/write-process-memory.md)**|
|C0052|FILE SYSTEM|**[Writes File](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/writes-file.md)**|

## Enhanced Malware ATT&CK Techniques
| ID | Objective(s) | Technique |
|----|--------------|-----------|
|E1010|DISCOVERY|**[Application Window Discovery](https://github.com/MBCProject/mbc-markdown/blob/main/discovery/application-window-discovery.md)**|
|E1560|EXFILTRATION|**[Archive Collected Data](https://github.com/MBCProject/mbc-markdown/blob/main/exfiltration/archive-collected-data.md)**|
|E1020|EXFILTRATION|**[Automated Exfiltration](https://github.com/MBCProject/mbc-markdown/blob/main/exfiltration/automated-exfiltration.md)**|
|E1510|IMPACT|**[Clipboard Modification](https://github.com/MBCProject/mbc-markdown/blob/main/impact/clipboard-modification.md)**|
|E1059|EXECUTION|**[Command and Scripting Interpreter](https://github.com/MBCProject/mbc-markdown/blob/main/execution/command-and-scripting-interpreter.md)**|
|E1485|IMPACT|**[Data Destruction](https://github.com/MBCProject/mbc-markdown/blob/main/impact/data-destruction.md)**|
|E1486|IMPACT|**[Data Encrypted for Impact ](https://github.com/MBCProject/mbc-markdown/blob/main/impact/data-encrypted-for-impact-.md)**|
|E1190|IMPACT|**[Exploit Kit](https://github.com/MBCProject/mbc-markdown/blob/main/impact/exploit-kit.md)**|
|E1203|EXECUTION, IMPACT|**[Exploitation for Client Execution](https://github.com/MBCProject/mbc-markdown/blob/main/execution/exploitation-for-client-execution.md)**|
|E1083|DISCOVERY|**[File and Directory Discovery](https://github.com/MBCProject/mbc-markdown/blob/main/discovery/file-and-directory-discovery.md)**|
|E1643|IMPACT|**[Generate Traffic from Victim](https://github.com/MBCProject/mbc-markdown/blob/main/impact/generate-traffic-from-victim.md)**|
|E1564|DEFENSE EVASION, PERSISTENCE|**[Hide Artifacts](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/hide-artifacts.md)**|
|E1105|COMMAND AND CONTROL, LATERAL MOVEMENT, PERSISTENCE|**[Ingress Tool Transfer](https://github.com/MBCProject/mbc-markdown/blob/main/command-and-control/ingress-tool-transfer.md)**|
|E1056|COLLECTION, CREDENTIAL ACCESS|**[Input Capture](https://github.com/MBCProject/mbc-markdown/blob/main/collection/input-capture.md)**|
|E1608|PRIVILEGE ESCALATION|**[Install Certificate](https://github.com/MBCProject/mbc-markdown/blob/main/privilege-escalation/install-certificate.md)**|
|E1112|DEFENSE EVASION, PERSISTENCE|**[Modify Registry](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/modify-registry.md)**|
|E1027|ANTI-STATIC ANALYSIS, DEFENSE EVASION|**[Obfuscated Files or Information](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/obfuscated-files-or-information.md)**|
|E1055|DEFENSE EVASION, PRIVILEGE ESCALATION|**[Process Injection](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/process-injection.md)**|
|E1014|DEFENSE EVASION|**[Rootkit](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/rootkit.md)**|
|E1113|COLLECTION, CREDENTIAL ACCESS|**[Screen Capture](https://github.com/MBCProject/mbc-markdown/blob/main/collection/screen-capture.md)**|
|E1195|LATERAL MOVEMENT|**[Supply Chain Compromise](https://github.com/MBCProject/mbc-markdown/blob/main/lateral-movement/supply-chain-compromise.md)**|
|E1082|DISCOVERY|**[System Information Discovery](https://github.com/MBCProject/mbc-markdown/blob/main/discovery/system-information-discovery.md)**|
|E1569|EXECUTION|**[System Services](https://github.com/MBCProject/mbc-markdown/blob/main/execution/system-services.md)**|
|E1204|EXECUTION|**[User Execution](https://github.com/MBCProject/mbc-markdown/blob/main/execution/user-execution.md)**|

## Enhanced Malware ATT&CK Sub-techniques
| ID | Objective(s) | Sub-technique |
|----|--------------|---------------|
|F0013|DEFENSE EVASION, PERSISTENCE|**[Bootkit](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/bootkit.md)**|
|F0009|IMPACT, PERSISTENCE, DEFENSE EVASION|**[Component Firmware](https://github.com/MBCProject/mbc-markdown/blob/main/persistence/component-firmware.md)**|
|F0004|DEFENSE EVASION|**[Disable or Evade Security Tools](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/disable-or-evade-security-tools.md)**|
|F0014|IMPACT|**[Disk Wipe](https://github.com/MBCProject/mbc-markdown/blob/main/impact/disk-wipe.md)**|
|F0005|DEFENSE EVASION, PERSISTENCE|**[Hidden Files and Directories](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/hidden-files-and-directories.md)**|
|F0015|ANTI-BEHAVIORAL ANALYSIS, COLLECTION, CREDENTIAL ACCESS, DEFENSE EVASION, PERSISTENCE, PRIVILEGE ESCALATION|**[Hijack Execution Flow](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/hijack-execution-flow.md)**|
|F0006|DEFENSE EVASION|**[Indicator Blocking](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/indicator-blocking.md)**|
|F0010|PERSISTENCE, PRIVILEGE ESCALATION|**[Kernel Modules and Extensions](https://github.com/MBCProject/mbc-markdown/blob/main/persistence/kernel-modules-and-extensions.md)**|
|F0002|COLLECTION, CREDENTIAL ACCESS|**[Keylogging](https://github.com/MBCProject/mbc-markdown/blob/main/collection/keylogging.md)**|
|F0011|PERSISTENCE, PRIVILEGE ESCALATION|**[Modify Existing Service](https://github.com/MBCProject/mbc-markdown/blob/main/persistence/modify-existing-service.md)**|
|F0012|PERSISTENCE|**[Registry Run Keys / Startup Folder](https://github.com/MBCProject/mbc-markdown/blob/main/persistence/registry-run-keys-/-startup-folder.md)**|
|F0007|DEFENSE EVASION|**[Self Deletion](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/self-deletion.md)**|
|F0001|ANTI-BEHAVIORAL ANALYSIS, ANTI-STATIC ANALYSIS, DEFENSE EVASION|**[Software Packing](https://github.com/MBCProject/mbc-markdown/blob/main/anti-static-analysis/software-packing.md)**|

