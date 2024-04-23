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
<td><b>2.1</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>14 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>5 December 2023</b></td>
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
|**WinINet**|C0002.007|A HTTP request is made via the Windows Internet (WinINet) application programming interface (API). A specific function can be specified as a method on the [WinInet](../communication/wininet.md) micro-behavior.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|C0002.010|The malware initializes IWebBrowser2. [[1]](#1)|
|[**BlackEnergy**](../xample-malware/blackenergy.md)|2007|C0002.011|The malware extracts the HTTP body. [[1]](#1)|
|[**Emotet**](../xample-malware/emotet.md)|2018|C0002.012|The malware creates a HTTP request. [[1]](#1)|
|[**Kovter**](../xample-malware/kovter.md)|2016|C0002.009|Kovter connects to a HTTP server. [[1]](#1)|
|[**Kovter**](../xample-malware/kovter.md)|2016|C0002.012|Kovter creates a HTTP request. [[1]](#1)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[read HTTP header](https://github.com/mandiant/capa-rules/blob/master/communication/http/read-http-header.yml)|HTTP Communication::Read Header (C0002.014)|winhttp.WinHttpQueryHeaders|
|[initialize WinHTTP library](https://github.com/mandiant/capa-rules/blob/master/communication/http/initialize-winhttp-library.yml)|HTTP Communication::WinHTTP (C0002.008)|winhttp.WinHttpOpen|
|[initialize IWebBrowser2](https://github.com/mandiant/capa-rules/blob/master/communication/http/initialize-iwebbrowser2.yml)|HTTP Communication::IWebBrowser (C0002.010)|ole32.CoCreateInstance|
|[get HTTP content length](https://github.com/mandiant/capa-rules/blob/master/communication/http/get-http-content-length.yml)|HTTP Communication (C0002)|wininet.HttpQueryInfo|
|[set HTTP header](https://github.com/mandiant/capa-rules/blob/master/communication/http/set-http-header.yml)|HTTP Communication::Set Header (C0002.013)|winhttp.WinHttpAddRequestHeaders, System.Net.WebHeaderCollection::Add|
|[reference HTTP User-Agent string](https://github.com/mandiant/capa-rules/blob/master/communication/http/reference-http-user-agent-string.yml)|HTTP Communication (C0002)|urlmon.ObtainUserAgentString|
|[start HTTP server](https://github.com/mandiant/capa-rules/blob/master/communication/http/server/start-http-server.yml)|HTTP Communication::Start Server (C0002.018)|httpapi.HttpInitialize, httpapi.HttpTerminate, System.Net.HttpListener::Start|
|[receive HTTP request](https://github.com/mandiant/capa-rules/blob/master/communication/http/server/receive-http-request.yml)|HTTP Communication::Receive Request (C0002.015)|httpapi.HttpReceiveHttpRequest, httpapi.HttpReceiveRequestEntityBody|
|[send HTTP response](https://github.com/mandiant/capa-rules/blob/master/communication/http/server/send-http-response.yml)|HTTP Communication::Send Response (C0002.016)|httpapi.HttpSendHttpResponse, httpapi.HttpSendResponseEntityBody|
|[receive HTTP response](https://github.com/mandiant/capa-rules/blob/master/communication/http/client/receive-http-response.yml)|HTTP Communication::Get Response (C0002.017)|System.Net.WebRequest::GetResponse, winhttp.WinHttpReceiveResponse, winhttp.WinHttpReadData, winhttp.WinHttpQueryDataAvailable|
|[send HTTP request](https://github.com/mandiant/capa-rules/blob/master/communication/http/client/send-http-request.yml)|HTTP Communication::Send Request (C0002.003)|System.Net.WebRequest::GetResponse, System.Net.WebRequest::GetResponseAsync, wininet.HttpOpenRequest, wininet.InternetConnect, wininet.HttpSendRequest, wininet.HttpSendRequestEx, winhttp.WinHttpSendRequest, winhttp.WinHttpWriteData, winhttp.WinHttpOpenRequest, winhttp.WinHttpConnect|
|[read data from Internet](https://github.com/mandiant/capa-rules/blob/master/communication/http/client/read-data-from-internet.yml)|HTTP Communication::Get Response (C0002.017)|wininet.InternetReadFile, wininet.InternetReadFileEx, System.Net.WebClient::DownloadString, System.Net.WebClient::DownloadStringAsync, System.Net.WebClient::DownloadStringTaskAsync, System.Net.WebClient::DownloadData, System.Net.WebClient::DownloadDataAsync, System.Net.WebClient::DownloadDataTaskAsync|
|[get HTTP document via IWebBrowser2](https://github.com/mandiant/capa-rules/blob/master/communication/http/client/get-http-document-via-iwebbrowser2.yml)|HTTP Communication::Get Response (C0002.017)|oleaut32.SysAllocString, oleaut32.VariantInit|
|[get HTTP document via IWebBrowser2](https://github.com/mandiant/capa-rules/blob/master/communication/http/client/get-http-document-via-iwebbrowser2.yml)|HTTP Communication::IWebBrowser (C0002.010)|oleaut32.SysAllocString, oleaut32.VariantInit|
|[download URL](https://github.com/mandiant/capa-rules/blob/master/communication/http/client/download-url.yml)|HTTP Communication::Download URL (C0002.006)|urlmon.URLDownloadToFile, urlmon.URLDownloadToCacheFile, urlmon.URLOpenBlockingStream, urlmon.URLOpenPullStream, urlmon.URLOpenStream, System.Net.WebClient::DownloadFile, System.Net.WebClient::DownloadFileAsync, System.Net.WebClient::DownloadFileTaskAsync, Microsoft.VisualBasic.Devices.Network::DownloadFile|
|[prepare HTTP request](https://github.com/mandiant/capa-rules/blob/master/communication/http/client/prepare-http-request.yml)|HTTP Communication::Create Request (C0002.012)|winhttp.WinHttpOpenRequest|
|[create HTTP request](https://github.com/mandiant/capa-rules/blob/master/communication/http/client/create-http-request.yml)|HTTP Communication::Create Request (C0002.012)|wininet.InternetOpen, System.Net.WebRequest::Create, System.Net.WebRequest::CreateDefault, System.Net.WebRequest::CreateHttp, wininet.InternetCloseHandle|
|[send file via HTTP](https://github.com/mandiant/capa-rules/blob/master/communication/http/client/send-file-via-http.yml)|HTTP Communication::Send Data (C0002.005)|wininet.InternetWriteFile|
|[decompress HTTP response via IEncodingFilterFactory](https://github.com/mandiant/capa-rules/blob/master/communication/http/client/decompress-http-response-via-iencodingfilterfactory.yml)|HTTP Communication::Get Response (C0002.017)|--|
|[check HTTP status code](https://github.com/mandiant/capa-rules/blob/master/communication/http/client/check-http-status-code.yml)|HTTP Communication::Read Header (C0002.014)|atoi, wininet.HttpQueryInfo|
|[get HTTP response content encoding](https://github.com/mandiant/capa-rules/blob/master/communication/http/client/get-http-response-content-encoding.yml)|HTTP Communication::Get Response (C0002.017)|wininet.HttpQueryInfo|
|[connect to URL](https://github.com/mandiant/capa-rules/blob/master/communication/http/client/connect-to-url.yml)|HTTP Communication::Open URL (C0002.004)|wininet.InternetOpenUrl|
|[connect to HTTP server](https://github.com/mandiant/capa-rules/blob/master/communication/http/client/connect-to-http-server.yml)|HTTP Communication::Connect to Server (C0002.009)|wininet.InternetConnect|
|[extract HTTP body](https://github.com/mandiant/capa-rules/blob/master/communication/http/client/extract-http-body.yml)|HTTP Communication::Extract Body (C0002.011)|--|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[internet_dropper](https://github.com/CAPESandbox/community/tree/master/modules/signatures/internet_dropper.py)|HTTP Communication (C0002)|HttpOpenRequestA, InternetConnectA, HttpOpenRequestW, InternetConnectW|
|[bot_madness](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bot_madness.py)|HTTP Communication (C0002)|--|
|[bot_madness](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bot_madness.py)|HTTP Communication::Send Request (C0002.003)|--|
|[bot_drive](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bot_drive.py)|HTTP Communication (C0002)|--|
|[bot_drive](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bot_drive.py)|HTTP Communication::Send Data (C0002.005)|--|
|[network_cnc_http](https://github.com/CAPESandbox/community/tree/master/modules/signatures/network_cnc_http.py)|HTTP Communication (C0002)|--|
|[recon_beacon](https://github.com/CAPESandbox/community/tree/master/modules/signatures/recon_beacon.py)|HTTP Communication (C0002)|HttpOpenRequestA, HttpSendRequestA|
|[network_http](https://github.com/CAPESandbox/community/tree/master/modules/signatures/network_http.py)|HTTP Communication (C0002)|--|
|[explorer_http](https://github.com/CAPESandbox/community/tree/master/modules/signatures/explorer_http.py)|HTTP Communication (C0002)|WinHttpConnect, WinHttpOpenRequest|
|[bot_drive2](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bot_drive2.py)|HTTP Communication (C0002)|--|
|[bot_drive2](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bot_drive2.py)|HTTP Communication::Send Data (C0002.005)|--|
|[bot_dirtjumper](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bot_dirtjumper.py)|HTTP Communication (C0002)|--|
|[bot_dirtjumper](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bot_dirtjumper.py)|HTTP Communication::Send Data (C0002.005)|--|
|[bot_athenahttp](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bot_athenahttp.py)|HTTP Communication (C0002)|--|
|[koadic_network_activity](https://github.com/CAPESandbox/community/tree/master/modules/signatures/koadic_network_activity.py)|HTTP Communication (C0002)|HttpOpenRequestW, WinHttpOpenRequest|
|[http_request](https://github.com/CAPESandbox/community/tree/master/modules/signatures/http_request.py)|HTTP Communication (C0002)|HttpOpenRequestA, HttpOpenRequestW, InternetConnectW, InternetOpenUrlA, InternetConnectA, InternetOpenUrlW, WinHttpGetProxyForUrl|
|[cmdline_http_link](https://github.com/CAPESandbox/community/tree/master/modules/signatures/cmdline_http_link.py)|HTTP Communication (C0002)|--|
|[cmdline_reversed_http_link](https://github.com/CAPESandbox/community/tree/master/modules/signatures/cmdline_reversed_http_link.py)|HTTP Communication (C0002)|--|
|[https_urls](https://github.com/CAPESandbox/community/tree/master/modules/signatures/https_urls.py)|HTTP Communication (C0002)|InternetOpenUrlW, InternetOpenUrlA|
|[network_document_http](https://github.com/CAPESandbox/community/tree/master/modules/signatures/network_document_http.py)|HTTP Communication (C0002)|URLDownloadToFileW, HttpOpenRequestW, InternetCrackUrlW, InternetCrackUrlA, WSASend, InternetReadFile|
|[banker_zeus_url](https://github.com/CAPESandbox/community/tree/master/modules/signatures/banker_zeus_url.py)|HTTP Communication (C0002)|--|
|[downloads_from_filehosting](https://github.com/CAPESandbox/community/tree/master/modules/signatures/downloads_from_filehosting.py)|HTTP Communication (C0002)|WinHttpOpenRequest, InternetOpenUrlA|
|[purplewave_network_activity](https://github.com/CAPESandbox/community/tree/master/modules/signatures/purplewave_network_activity.py)|HTTP Communication (C0002)|InternetOpenW, HttpOpenRequestW, HttpSendRequestW, HttpAddRequestHeadersA|

### C0002.017 Snippet
<details>
<summary> Communication::HTTP Communication::Get Response </summary>
SHA256: 3ac8c22eb7c59d35fe49c20f2a0eca06765543dfb15f455a5557af4428066641
Location: 0x180001380
<pre>
mov     param_2, ebx
lea     r9, [rsp + 0x44]        ; where to store the number of bytes read
add     param_2, r14    ; pointer to buffer to receive HTTP data
mov     param_3, 0x400  ; number of bytes to read (1024)
mov     param_1, rsi    ; handle to previously opened HTTP request
call    qword ptr [->WININET::InternetReadFile] ; Windows API for reading data from HTTP or FTP connections
</pre>
</details>

## References

<a name="1">[1]</a> capa v4.0, analyzed at MITRE on 10/12/2022
