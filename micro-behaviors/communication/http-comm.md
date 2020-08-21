|||
|---|---|
|**ID**|**C0002**|
|**Objective(s)**|[Communication](https://github.com/MBCProject/mbc-markdown/tree/master/micro-behaviors/communication)|
|**Related ATT&CK Technique**|None|


HTTP Communication
==================
This micro-behavior is related to HTTP communication. 

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Client**|C0002.002|General HTTP client behavior.|
|**GET Request**|C0002.004|HTTP Get request.|
|**IHTMLDocument**|C0002.008|Specific methods and properties can be captured: e.g., COMMUNICATION::HTTP Communication::IHTMLDocument Interface.get_body.|
|**IHTMLElement**|C0002.008|Specific methods and properties can be captured: e.g., COMMUNICATION::HTTP Communication::IHTMLElement Interface.get_innerText.|
|**IWebBrowser**|C0002.008|The IWebBrowser interface exposes methods and properties implemented by the WebBrowser control or implemented by an instance of the InternetExplorer application. Specific methods and properties can be captured: e.g., COMMUNICATION::HTTP Communication::IWebBrowser.get_Document.|
|**POST Request**|C0002.005|HTTP Post request.|
|**PUT Request**|C0002.006|HTTP Put request.|
|**Request**|C0002.003|Non-specific HTTP request.|
|**Server**|C0002.001|General HTTP server behavior.|
|**URLMON Function**|C0002.008|A HTTP request is made via a URLMON function. Specific functions can be captured: e.g., COMMUNICATION::HTTP Communication::URLMON Function.URLDownloadToFileW.|
|**WinHTTP API**|C0002.008|An HTTP request is made via the Windows HTTP Services (WinHTTP) application programming interface (API).|
|**WinINet API**|C0002.007|A HTTP request is made via the Windows Internet (WinINet) application programming interface (API). A specific function can be specified as a method on the [WinInet](https://github.com/MBCProject/mbc-markdown/blob/master/micro-behaviors/communication/wininet.md) microbehavior.|
