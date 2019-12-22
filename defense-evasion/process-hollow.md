|||
|---------|------------------------|
|**ID**|**T1093**|
|**Objective(s)**| [Defense Evasion](https://github.com/MBCProject/mbc-markdown/tree/master/defense-evasion)|
|**Related ATT&CK Technique**|[Process Hollowing](https://attack.mitre.org/techniques/T1093)|


Process Hollowing
=================
Instead of performing [Process Injection](https://github.com/MBCProject/mbc-markdown/blob/master/defense-evasion/process-inject.md), malware may unmap (hollows out) legitimate code from the target process's memory (e.g., svchost.exe) and overwrite the memory space with a malicious code. [[1]](#1)

See ATT&CK: [**Process Hollowing**](https://attack.mitre.org/techniques/T1093).

References
----------
<a name="1"[1]</a> https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process 