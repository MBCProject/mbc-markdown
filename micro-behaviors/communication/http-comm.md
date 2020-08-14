|||
|---------|------------------------|
|**ID**|**C0002**|
|**Objective(s)**|[Communication](https://github.com/MBCProject/mbc-beta/tree/master/micro-behaviors/communication)|
|**Related ATT&CK Technique**|None|


HTTP Communication
==================
This micro-behavior is related to HTTP communication. 

Methods
-------
|ID|Name|Description|
|-----------------------------|--------|-----------------------------|
|C0002.001|**Server**|General HTTP server behavior.|
|C0002.002|**Client**|General HTTP client behavior.|
|C0002.003|**Request**|Non-specific HTTP request.|
|C0002.004|**GET Request**|HTTP Get request.|
|C0002.005|**POST Request**|HTTP Post request.|
|C0002.006|**PUT Request**|HTTP Put request.| 
|C0002.007|**WinINet API**|A HTTP request is made via the Windows Internet (WinINet) application programming interface (API). A specific function can be specified as a method on the [WinInet](https://github.com/MBCProject/mbc-beta/blob/master/micro-behaviors/communication/wininet.md) microbehavior.
|C0002.008|**WinHTTP API**|An HTTP request is made via the Windows HTTP Services (WinHTTP) application programming interface (API).|
|C0002.008|**URLMON Function**|A HTTP request is made via a URLMON function. Specific functions can be captured: e.g., COMMUNICATION::HTTP Communication::URLMON Function.URLDownloadToFileW.  
|C0002.008|**IWebBrowser**|The IWebBrowser interface exposes methods and properties implemented by the WebBrowser control or implemented by an instance of the InternetExplorer application. Specific methods and properties can be captured: e.g., COMMUNICATION::HTTP Communication::IWebBrowser.get_Document.
|C0002.008|**IHTMLDocument**|Specific methods and properties can be captured: e.g., COMMUNICATION::HTTP Communication::IHTMLDocument Interface.get_body.
|C0002.008|**IHTMLElement**|Specific methods and properties can be captured: e.g., COMMUNICATION::HTTP Communication::IHTMLElement Interface.get_innerText.

