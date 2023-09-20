<table>
<tr>
<td><b>ID</b></td>
<td><b>C0005</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../communication">Communication</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>14 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>10 November 2022</b></td>
</tr>
</table>


# WinINet

The Windows Internet (WinINet) application programming interface (API) is used by malware to interact with FTP and HTTP protocols to access Internet resources.

The methods below are those of most interest in malware analysis. Details can be found at [[1]](#1). 

## Methods

|Name|ID|Description|
|---|---|---|
|**InternetConnect**|C0005.001|Opens an FTP or HTTP session for a given site.|
|**InternetOpen**|C0005.002|Initializes an application's use of the WinINet functions.|
|**InternetOpenURL**|C0005.003|Opens a resource specified by a complete FTP or HTTP URL.|
|**InternetReadFile**|C0005.004|Reads data from an open Internet file (URL data).|
|**InternetWriteFile**|C0005.005|Writes data to an open Internet file.|

## References

<a name="1">[1]</a> https://docs.microsoft.com/en-us/windows/win32/wininet/wininet-functions
