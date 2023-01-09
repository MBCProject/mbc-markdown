<table>
<tr>
<td><b>ID</b></td>
<td><b>C0002</b></td>
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
<td><b>31 October 2022</b></td>
</tr>
</table>


# HTTP Communication

This micro-behavior is related to HTTP communication. 

Instead of being listed alphabetically, methods have been grouped to better faciliate labeling and mapping.

## Methods

|Name|ID|Description|
|---|---|---|
|**Server**|C0002.001|General HTTP server behavior.|
|**Client**|C0002.002|General HTTP client behavior.|
|**Connect to Server**|C0002.009|HTTP client connects to HTTP server.|
|**Open URL**|C0002.004|HTTP client connects to a URL.|
|**Download URL**|C0002.006|HTTP client downloads URL to file.|
|**Extract Body**|C0002.011|HTTP client extracts HTTP body.|
|**Create Request**|C0002.012|HTTP client creates request.|
|**Send Request**|C0002.003|HTTP client sends request (GET).|
|**Send Data**|C0002.005|HTTP clients sends data to a server (POST/PUT).|
|**Receive Request**|C0002.015|HTTP server receives request.|
|**Send Response**|C0002.016|HTTP server sends response.|
|**Get Response**|C0002.017|HTTP client receives response.|
|**Start Server**|C0002.018|HTTP server is started.|
|**Set Header**|C0002.013|HTTP header is set.|
|**Read Header**|C0002.014|HTTP read header.|
|**IWebBrowser**|C0002.010|The IWebBrowser interface exposes methods and properties implemented by the WebBrowser control or implemented by an instance of the InternetExplorer application. Specific methods and properties can be captured: e.g., COMMUNICATION::HTTP Communication::IWebBrowser.get_Document.|
|**WinHTTP**|C0002.008|An HTTP request is made via the Windows HTTP Services (WinHTTP) application programming interface (API).|
|**WinINet**|C0002.007|A HTTP request is made via the Windows Internet (WinINet) application programming interface (API). A specific function can be specified as a method on the [WinInet](../communication/wininet.md) microbehavior.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|C0002.011, C0002.010|Please see the BlackEnergy malware page for details. [[1]](#1)|
|[**Emotet**](../xample-malware/emotet.md)|2018|C0002.012|Create http request (this capa rule had 1 match) [[1]](#1)|
|[**Kovter**](../xample-malware/kovter.md)|2016|C0002.009, C0002.012|Please see the Kovter malware page for details. [[1]](#1)|

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022

