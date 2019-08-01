|||
|---------|------------------------|
|**ID**|**M0035**|
|**Objective(s)**| [Persistence](https://github.com/MAECProject/malware-behaviors/tree/master/persistence)|
|**Related ATT&CK Technique(s)**|None|


Shutdown Event
==============
Malware can register the shutdown event triggered by WinLogon to allow a malicious DLL to execute every time the machine shuts down: when the machine is shutdown the malware will be loaded into memory; then it will download the primary malware and reinfect the machine. The malware will also lie dormant during incident reporting processes. To check whether malware has registered for login events, check the registry key: HKEY_LOCAL_MACHINESoftwareMicrosoftWindows NTCurrentVersionWinlogonNotify. If a subkey with any name exists and it has a "shutdown" value then the dll in the "DLLName" key will be launched during the shutdown process. [[1]](#1)

References
----------
<a name="1">[1]</a> https://isc.sans.edu/diary/Wipe+the+drive!++Stealthy+Malware+Persistence+-+Part+4/15460