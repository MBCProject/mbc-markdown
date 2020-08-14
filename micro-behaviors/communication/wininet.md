|||
|---------|------------------------|
|**ID**|**C0005**|
|**Objective(s)**|[Communication](https://github.com/MBCProject/mbc-beta/tree/master/micro-behaviors/communication)|
|**Related ATT&CK Technique**|None|


WinINet
=======
The Windows Internet (WinINet) application programming interface (API) is used by malware to interact with FTP and HTTP protocols to access Internet resources.

The methods below are those of most interest in malware analysis. Details can be found at [[1]](#1). 

Methods
-------
|ID|Name|Description|
|-----------------------------|--------|-----------------------------|
|C0005.001|**InternetConnect**|Opens an FTP or HTTP session for a given site.|
|C0005.002|**InternetOpen**|Initializes an application's use of the WinINet functions.|
|C0005.003|**InternetOpenURL**|Opens a resource specified by a complete FTP or HTTP URL.|
|C0005.004|**InternetReadFile**|Reads data from an open Internet file (URL data).|
|C0005.005|**InternetWriteFile**|Writes data to an open Internet file.|

References
----------
<a name="1">[1]</a> https://docs.microsoft.com/en-us/windows/win32/wininet/wininet-functions. 

