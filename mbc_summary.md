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
| ID | Behavior | Objective(s) | Related ATT&CK Technique |
|----|----------|--------------|--------------------------|
|B0010|**[Call Graph Generation Evasion](https://github.com/MBCProject/mbc-markdown/blob/main/anti-static-analysis/call-graph-generation-evasion.md)**|ANTI-STATIC ANALYSIS|*none*|
|B0032|**[Executable Code Obfuscation](https://github.com/MBCProject/mbc-markdown/blob/main/anti-static-analysis/executable-code-obfuscation.md)**|ANTI-STATIC ANALYSIS|*none*|
|B0034|**[Executable Code Optimization](https://github.com/MBCProject/mbc-markdown/blob/main/anti-static-analysis/executable-code-optimization.md)**|ANTI-STATIC ANALYSIS|*none*|
|B0008|**[Executable Code Virtualization](https://github.com/MBCProject/mbc-markdown/blob/main/anti-static-analysis/executable-code-virtualization.md)**|ANTI-BEHAVIORAL ANALYSIS, ANTI-STATIC ANALYSIS|*none*|
|B0045|**[Data Flow Analysis Evasion](https://github.com/MBCProject/mbc-markdown/blob/main/anti-static-analysis/data-flow-analysis-evasion.md)**|ANTI-STATIC ANALYSIS|*none*|
|B0012|**[Disassembler Evasion](https://github.com/MBCProject/mbc-markdown/blob/main/anti-static-analysis/disassembler-evasion.md)**|ANTI-STATIC ANALYSIS|*none*|
|B0014|**[SMTP Connection Discovery](https://github.com/MBCProject/mbc-markdown/blob/main/discovery/smtp-connection-discovery.md)**|DISCOVERY|*none*|
|B0046|**[Code Discovery](https://github.com/MBCProject/mbc-markdown/blob/main/discovery/code-discovery.md)**|DISCOVERY|*none*|
|B0038|**[Self Discovery](https://github.com/MBCProject/mbc-markdown/blob/main/discovery/self-discovery.md)**|DISCOVERY|*none*|
|B0013|**[Analysis Tool Discovery](https://github.com/MBCProject/mbc-markdown/blob/main/discovery/analysis-tool-discovery.md)**|DISCOVERY|*none*|
|B0043|**[Taskbar Discovery](https://github.com/MBCProject/mbc-markdown/blob/main/discovery/taskbar-discovery.md)**|DISCOVERY|*none*|
|B0028|**[Cryptocurrency](https://github.com/MBCProject/mbc-markdown/blob/main/collection/cryptocurrency.md)**|COLLECTION, CREDENTIAL ACCESS|*none*|
|B0030|**[C2 Communication](https://github.com/MBCProject/mbc-markdown/blob/main/command-and-control/c2-communication.md)**|COMMAND AND CONTROL|*none*|
|B0031|**[Domain Name Generation](https://github.com/MBCProject/mbc-markdown/blob/main/command-and-control/domain-name-generation.md)**|COMMAND AND CONTROL|Dynamic Resolution: Domain Generation Algorithms ([T1568.002](https://attack.mitre.org/techniques/T1568/002/))|
|B0024|**[Prevent Concurrent Execution](https://github.com/MBCProject/mbc-markdown/blob/main/execution/prevent-concurrent-execution.md)**|EXECUTION|*none*|
|B0044|**[Execution Dependency](https://github.com/MBCProject/mbc-markdown/blob/main/execution/execution-dependency.md)**|EXECUTION|*none*|
|B0023|**[Install Additional Program](https://github.com/MBCProject/mbc-markdown/blob/main/execution/install-additional-program.md)**|EXECUTION|*none*|
|B0020|**[Send Email](https://github.com/MBCProject/mbc-markdown/blob/main/execution/send-email.md)**|EXECUTION, LATERAL MOVEMENT|Phishing ([T1566](https://attack.mitre.org/techniques/T1566/))|
|B0011|**[Remote Commands](https://github.com/MBCProject/mbc-markdown/blob/main/execution/remote-commands.md)**|EXECUTION|*none*|
|B0025|**[Conditional Execution](https://github.com/MBCProject/mbc-markdown/blob/main/execution/conditional-execution.md)**|EXECUTION, ANTI-BEHAVIORAL ANALYSIS, DEFENSE EVASION|Execution Guardrails  ([T1480](https://attack.mitre.org/techniques/T1480))|
|B0021|**[Send Poisoned Text Message](https://github.com/MBCProject/mbc-markdown/blob/main/execution/send-poisoned-text-message.md)**|EXECUTION, LATERAL MOVEMENT|*none*|
|B0026|**[Malicious Network Driver](https://github.com/MBCProject/mbc-markdown/blob/main/persistence/malicious-network-driver.md)**|LATERAL MOVEMENT, PERSISTENCE|*none*|
|B0035|**[Shutdown Event](https://github.com/MBCProject/mbc-markdown/blob/main/persistence/shutdown-event.md)**|PERSISTENCE|*none*|
|B0018|**[Resource Hijacking](https://github.com/MBCProject/mbc-markdown/blob/main/impact/resource-hijacking.md)**|IMPACT|Resource Hijacking ([T1496](https://attack.mitre.org/techniques/T1496/))|
|B0022|**[Remote Access](https://github.com/MBCProject/mbc-markdown/blob/main/impact/remote-access.md)**|IMPACT, PERSISTENCE|*none*|
|B0017|**[Destroy Hardware](https://github.com/MBCProject/mbc-markdown/blob/main/impact/destroy-hardware.md)**|IMPACT|*none*|
|B0016|**[Compromise Data Integrity](https://github.com/MBCProject/mbc-markdown/blob/main/impact/compromise-data-integrity.md)**|IMPACT|Data Manipulation: Stored Data Manipulation ([T1565.001](https://attack.mitre.org/techniques/T1565/001/))|
|B0033|**[Denial of Service](https://github.com/MBCProject/mbc-markdown/blob/main/impact/denial-of-service.md)**|IMPACT|Network Denial of Service ([T1498](https://attack.mitre.org/techniques/T1498/))|
|B0019|**[Manipulate Network Traffic](https://github.com/MBCProject/mbc-markdown/blob/main/impact/manipulate-network-traffic.md)**|IMPACT|Data Manipulation: Transmitted Data Manipulation ([T1565.002](https://attack.mitre.org/techniques/T1565/002/))|
|B0042|**[Modify Hardware](https://github.com/MBCProject/mbc-markdown/blob/main/impact/modify-hardware.md)**|IMPACT|*none*|
|B0039|**[Spamming](https://github.com/MBCProject/mbc-markdown/blob/main/impact/spamming.md)**|IMPACT|*none*|
|B0006|**[Memory Dump Evasion](https://github.com/MBCProject/mbc-markdown/blob/main/anti-behavioral-analysis/memory-dump-evasion.md)**|ANTI-BEHAVIORAL ANALYSIS|*none*|
|B0036|**[Capture Evasion](https://github.com/MBCProject/mbc-markdown/blob/main/anti-behavioral-analysis/capture-evasion.md)**|ANTI-BEHAVIORAL ANALYSIS|*none*|
|B0009|**[Virtual Machine Detection](https://github.com/MBCProject/mbc-markdown/blob/main/anti-behavioral-analysis/virtual-machine-detection.md)**|ANTI-BEHAVIORAL ANALYSIS|Virtualization/Sandbox Evasion ([T1497](https://attack.mitre.org/techniques/T1497/),[T1633](https://attack.mitre.org/techniques/T1633/))|
|B0007|**[Sandbox Detection](https://github.com/MBCProject/mbc-markdown/blob/main/anti-behavioral-analysis/sandbox-detection.md)**|ANTI-BEHAVIORAL ANALYSIS|Virtualization/Sandbox Evasion: System Checks ([T1497.001](https://attack.mitre.org/techniques/T1497/001/),[T1633.001](https://attack.mitre.org/techniques/T1633/001/)); Virtualization/Sandbox Evasion: User Activity Based Checks ([T1497.002](https://attack.mitre.org/techniques/T1497/002/))|
|B0005|**[Emulator Evasion](https://github.com/MBCProject/mbc-markdown/blob/main/anti-behavioral-analysis/emulator-evasion.md)**|ANTI-BEHAVIORAL ANALYSIS|*none*|
|B0002|**[Debugger Evasion](https://github.com/MBCProject/mbc-markdown/blob/main/anti-behavioral-analysis/debugger-evasion.md)**|ANTI-BEHAVIORAL ANALYSIS|Debugger Evasion ([T1622](https://attack.mitre.org/techniques/T1622/))|
|B0001|**[Debugger Detection](https://github.com/MBCProject/mbc-markdown/blob/main/anti-behavioral-analysis/debugger-detection.md)**|ANTI-BEHAVIORAL ANALYSIS|*none*|
|B0004|**[Emulator Detection](https://github.com/MBCProject/mbc-markdown/blob/main/anti-behavioral-analysis/emulator-detection.md)**|ANTI-BEHAVIORAL ANALYSIS|*none*|
|B0003|**[Dynamic Analysis Evasion](https://github.com/MBCProject/mbc-markdown/blob/main/anti-behavioral-analysis/dynamic-analysis-evasion.md)**|ANTI-BEHAVIORAL ANALYSIS|Virtualization/Sandbox Evasion ([T1497](https://attack.mitre.org/techniques/T1497/),[T1633](https://attack.mitre.org/techniques/T1633/))|
|B0037|**[Bypass Data Execution Prevention](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/bypass-data-execution-prevention.md)**|DEFENSE EVASION|*none*|
|B0047|**[Install Insecure or Malicious Configuration](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/install-insecure-or-malicious-configuration.md)**|DEFENSE EVASION, PERSISTENCE|*none*|
|B0040|**[Covert Location](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/covert-location.md)**|DEFENSE EVASION|*none*|
|B0029|**[Polymorphic Code](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/polymorphic-code.md)**|DEFENSE EVASION|*none*|
|B0027|**[Alternative Installation Location](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/alternative-installation-location.md)**|DEFENSE EVASION|*none*|

## Malware Micro-behaviors
| ID | Micro-behavior | Objective(s) |
|----|----------------|--------------|
|C0007|**[Allocate Memory](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/memory/allocate-memory.md)**|MEMORY|
|C0040|**[Allocate Thread Local Storage](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/allocate-thread-local-storage.md)**|PROCESS|
|C0015|**[Alter File Extension](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/alter-file-extension.md)**|FILE SYSTEM|
|C0008|**[Change Memory Protection](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/memory/change-memory-protection.md)**|MEMORY|
|C0043|**[Check Mutex](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/check-mutex.md)**|PROCESS|
|C0019|**[Check String](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/data/check-string.md)**|DATA|
|C0032|**[Checksum](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/data/checksum.md)**|DATA|
|C0024|**[Compress Data](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/data/compress-data.md)**|DATA|
|C0060|**[Compression Library](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/data/compression-library.md)**|DATA|
|C0033|**[Console](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/operating-system/console.md)**|OPERATING SYSTEM|
|C0045|**[Copy File](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/copy-file.md)**|FILE SYSTEM|
|C0046|**[Create Directory](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/create-directory.md)**|FILE SYSTEM|
|C0016|**[Create File](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/create-file.md)**|FILE SYSTEM|
|C0042|**[Create Mutex](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/create-mutex.md)**|PROCESS|
|C0017|**[Create Process](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/create-process.md)**|PROCESS|
|C0038|**[Create Thread](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/create-thread.md)**|PROCESS|
|C0068|**[Crypto Algorithm](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/cryptography/crypto-algorithm.md)**|CRYPTOGRAPHY|
|C0069|**[Crypto Constant](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/cryptography/crypto-constant.md)**|CRYPTOGRAPHY|
|C0059|**[Crypto Library](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/cryptography/crypto-library.md)**|CRYPTOGRAPHY|
|C0029|**[Cryptographic Hash](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/cryptography/cryptographic-hash.md)**|CRYPTOGRAPHY|
|C0011|**[DNS Communication](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/communication/dns-communication.md)**|COMMUNICATION|
|C0053|**[Decode Data](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/data/decode-data.md)**|DATA|
|C0025|**[Decompress Data](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/data/decompress-data.md)**|DATA|
|C0031|**[Decrypt Data](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/cryptography/decrypt-data.md)**|CRYPTOGRAPHY|
|C0048|**[Delete Directory](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/delete-directory.md)**|FILE SYSTEM|
|C0047|**[Delete File](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/delete-file.md)**|FILE SYSTEM|
|C0026|**[Encode Data](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/data/encode-data.md)**|DATA|
|C0027|**[Encrypt Data](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/cryptography/encrypt-data.md)**|CRYPTOGRAPHY|
|C0028|**[Encryption Key](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/cryptography/encryption-key.md)**|CRYPTOGRAPHY|
|C0064|**[Enumerate Threads](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/enumerate-threads.md)**|PROCESS|
|C0034|**[Environment Variable](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/operating-system/environment-variable.md)**|OPERATING SYSTEM|
|C0004|**[FTP Communication](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/communication/ftp-communication.md)**|COMMUNICATION|
|C0044|**[Free Memory](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/memory/free-memory.md)**|MEMORY|
|C0021|**[Generate Pseudo-random Sequence](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/cryptography/generate-pseudorandom-sequence.md)**|CRYPTOGRAPHY|
|C0049|**[Get File Attributes](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/get-file-attributes.md)**|FILE SYSTEM|
|C0002|**[HTTP Communication](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/communication/http-communication.md)**|COMMUNICATION|
|C0061|**[Hashed Message Authentication Code](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/cryptography/hashed-message-authentication-code.md)**|CRYPTOGRAPHY|
|C0006|**[Heap Spray](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/memory/heap-spray.md)**|MEMORY|
|C0014|**[ICMP Communication](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/communication/icmp-communication.md)**|COMMUNICATION|
|C0037|**[Install Driver](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/hardware/install-driver.md)**|HARDWARE|
|C0003|**[Interprocess Communication](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/communication/interprocess-communication.md)**|COMMUNICATION|
|C0023|**[Load Driver](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/hardware/load-driver.md)**|HARDWARE|
|C0058|**[Modulo](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/data/modulo.md)**|DATA|
|C0063|**[Move File](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/move-file.md)**|FILE SYSTEM|
|C0030|**[Non-Cryptographic Hash](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/data/noncryptographic-hash.md)**|DATA|
|C0065|**[Open Process](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/open-process.md)**|PROCESS|
|C0066|**[Open Thread](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/open-thread.md)**|PROCESS|
|C0010|**[Overflow Buffer](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/memory/overflow-buffer.md)**|MEMORY|
|C0051|**[Read File](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/read-file.md)**|FILE SYSTEM|
|C0056|**[Read Virtual Disk](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/read-virtual-disk.md)**|FILE SYSTEM|
|C0036|**[Registry](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/operating-system/registry.md)**|OPERATING SYSTEM|
|C0054|**[Resume Thread](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/resume-thread.md)**|PROCESS|
|C0012|**[SMTP Communication](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/communication/smtp-communication.md)**|COMMUNICATION|
|C0050|**[Set File Attributes](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/set-file-attributes.md)**|FILE SYSTEM|
|C0072|**[Set Thread Context](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/set-thread-context.md)**|PROCESS|
|C0041|**[Set Thread Local Storage Value](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/set-thread-local-storage-value.md)**|PROCESS|
|C0057|**[Simulate Hardware](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/hardware/simulate-hardware.md)**|HARDWARE|
|C0001|**[Socket Communication](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/communication/socket-communication.md)**|COMMUNICATION|
|C0009|**[Stack Pivot](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/memory/stack-pivot.md)**|MEMORY|
|C0055|**[Suspend Thread](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/suspend-thread.md)**|PROCESS|
|C0022|**[Synchronization](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/synchronization.md)**|PROCESS|
|C0018|**[Terminate Process](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/terminate-process.md)**|PROCESS|
|C0039|**[Terminate Thread](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/terminate-thread.md)**|PROCESS|
|C0070|**[Unmap Section View](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/unmap-section-view.md)**|PROCESS|
|C0020|**[Use Constant](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/data/use-constant.md)**|DATA|
|C0035|**[Wallpaper](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/operating-system/wallpaper.md)**|OPERATING SYSTEM|
|C0005|**[WinINet](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/communication/wininet.md)**|COMMUNICATION|
|C0071|**[Write Process Memory](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/process/write-process-memory.md)**|PROCESS|
|C0052|**[Writes File](https://github.com/MBCProject/mbc-markdown/blob/main/micro-behaviors/file-system/writes-file.md)**|FILE SYSTEM|

## Enhanced Malware ATT&CK Techniques
| ID | Technique | Objective(s) |
|----|-----------|--------------|
|E1010|**[Application Window Discovery](https://github.com/MBCProject/mbc-markdown/blob/main/discovery/application-window-discovery.md)**|DISCOVERY|
|E1560|**[Archive Collected Data](https://github.com/MBCProject/mbc-markdown/blob/main/collection/archive-collected-data.md)**|COLLECTION|
|E1020|**[Automated Exfiltration](https://github.com/MBCProject/mbc-markdown/blob/main/exfiltration/automated-exfiltration.md)**|EXFILTRATION|
|E1510|**[Clipboard Modification](https://github.com/MBCProject/mbc-markdown/blob/main/impact/clipboard-modification.md)**|IMPACT|
|E1059|**[Command and Scripting Interpreter](https://github.com/MBCProject/mbc-markdown/blob/main/execution/command-and-scripting-interpreter.md)**|EXECUTION|
|E1485|**[Data Destruction](https://github.com/MBCProject/mbc-markdown/blob/main/impact/data-destruction.md)**|IMPACT|
|E1486|**[Data Encrypted for Impact ](https://github.com/MBCProject/mbc-markdown/blob/main/impact/data-encrypted-for-impact-.md)**|IMPACT|
|E1190|**[Exploit Kit](https://github.com/MBCProject/mbc-markdown/blob/main/impact/exploit-kit.md)**|IMPACT|
|E1203|**[Exploitation for Client Execution](https://github.com/MBCProject/mbc-markdown/blob/main/execution/exploitation-for-client-execution.md)**|EXECUTION, IMPACT|
|E1083|**[File and Directory Discovery](https://github.com/MBCProject/mbc-markdown/blob/main/discovery/file-and-directory-discovery.md)**|DISCOVERY|
|E1643|**[Generate Traffic from Victim](https://github.com/MBCProject/mbc-markdown/blob/main/impact/generate-traffic-from-victim.md)**|IMPACT|
|E1564|**[Hide Artifacts](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/hide-artifacts.md)**|DEFENSE EVASION, PERSISTENCE|
|E1105|**[Ingress Tool Transfer](https://github.com/MBCProject/mbc-markdown/blob/main/command-and-control/ingress-tool-transfer.md)**|COMMAND AND CONTROL, LATERAL MOVEMENT, PERSISTENCE|
|E1056|**[Input Capture](https://github.com/MBCProject/mbc-markdown/blob/main/collection/input-capture.md)**|COLLECTION, CREDENTIAL ACCESS|
|E1608|**[Install Certificate](https://github.com/MBCProject/mbc-markdown/blob/main/privilege-escalation/install-certificate.md)**|PRIVILEGE ESCALATION|
|E1112|**[Modify Registry](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/modify-registry.md)**|DEFENSE EVASION, PERSISTENCE|
|E1027|**[Obfuscated Files or Information](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/obfuscated-files-or-information.md)**|ANTI-STATIC ANALYSIS, DEFENSE EVASION|
|E1055|**[Process Injection](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/process-injection.md)**|DEFENSE EVASION, PRIVILEGE ESCALATION|
|E1014|**[Rootkit](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/rootkit.md)**|DEFENSE EVASION|
|E1113|**[Screen Capture](https://github.com/MBCProject/mbc-markdown/blob/main/collection/screen-capture.md)**|COLLECTION, CREDENTIAL ACCESS|
|E1195|**[Supply Chain Compromise](https://github.com/MBCProject/mbc-markdown/blob/main/lateral-movement/supply-chain-compromise.md)**|LATERAL MOVEMENT|
|E1082|**[System Information Discovery](https://github.com/MBCProject/mbc-markdown/blob/main/discovery/system-information-discovery.md)**|DISCOVERY|
|E1569|**[System Services](https://github.com/MBCProject/mbc-markdown/blob/main/execution/system-services.md)**|EXECUTION|
|E1204|**[User Execution](https://github.com/MBCProject/mbc-markdown/blob/main/execution/user-execution.md)**|EXECUTION|

## Enhanced Malware ATT&CK Sub-techniques
| ID | Sub-technique | Objective(s) |
|----|---------------|--------------|
|F0013|**[Bootkit](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/bootkit.md)**|DEFENSE EVASION, PERSISTENCE|
|F0009|**[Component Firmware](https://github.com/MBCProject/mbc-markdown/blob/main/persistence/component-firmware.md)**|IMPACT, PERSISTENCE, DEFENSE EVASION|
|F0004|**[Disable or Evade Security Tools](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/disable-or-evade-security-tools.md)**|DEFENSE EVASION|
|F0014|**[Disk Wipe](https://github.com/MBCProject/mbc-markdown/blob/main/impact/disk-wipe.md)**|IMPACT|
|F0005|**[Hidden Files and Directories](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/hidden-files-and-directories.md)**|DEFENSE EVASION, PERSISTENCE|
|F0015|**[Hijack Execution Flow](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/hijack-execution-flow.md)**|ANTI-BEHAVIORAL ANALYSIS, COLLECTION, CREDENTIAL ACCESS, DEFENSE EVASION, PERSISTENCE, PRIVILEGE ESCALATION|
|F0006|**[Indicator Blocking](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/indicator-blocking.md)**|DEFENSE EVASION|
|F0010|**[Kernel Modules and Extensions](https://github.com/MBCProject/mbc-markdown/blob/main/persistence/kernel-modules-and-extensions.md)**|PERSISTENCE, PRIVILEGE ESCALATION|
|F0002|**[Keylogging](https://github.com/MBCProject/mbc-markdown/blob/main/collection/keylogging.md)**|COLLECTION, CREDENTIAL ACCESS|
|F0011|**[Modify Existing Service](https://github.com/MBCProject/mbc-markdown/blob/main/persistence/modify-existing-service.md)**|PERSISTENCE, PRIVILEGE ESCALATION|
|F0012|**[Registry Run Keys / Startup Folder](https://github.com/MBCProject/mbc-markdown/blob/main/persistence/registry-run-keys-/-startup-folder.md)**|PERSISTENCE|
|F0007|**[Self Deletion](https://github.com/MBCProject/mbc-markdown/blob/main/defense-evasion/self-deletion.md)**|DEFENSE EVASION|
|F0001|**[Software Packing](https://github.com/MBCProject/mbc-markdown/blob/main/anti-static-analysis/software-packing.md)**|ANTI-BEHAVIORAL ANALYSIS, ANTI-STATIC ANALYSIS, DEFENSE EVASION|

