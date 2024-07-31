<table>
<tr>
<td><b>ID</b></td>
<td><b>C0001</b></td>
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
<td><b>3.2</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>25 September 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>30 April 2024</b></td>
</tr>
</table>


# Socket Communication

This micro-behavior focuses on socket (TCP, UDP) communication. 

Instead of being listed alphabetically, methods have been grouped to better faciliate labeling and mapping.

## Methods

|Name|ID|Description|
|---|---|---|
|**Set Socket Config**|C0001.001|Configure socket.|
|**Initialize Winsock Library**|C0001.009|Winsock is initialized for TCP communication.|
|**Start TCP Server**|C0001.005|A TCP server listens for client requests.|
|**Create Socket**|C0001.003|A server or client creates a UDP or TCP socket.|
|**Create UDP Socket**|C0001.010|A UDP socket is created.|
|**Create TCP Socket**|C0001.011|A TCP socket is created.|
|**Connect Socket**|C0001.004|A server or client connects via a TCP socket.|
|**Get Socket Status**|C0001.012|Get socket status.|
|**Send Data**|C0001.007|Send data on socket.|
|**Send TCP Data**|C0001.014|Send TCP data.|
|**Send UDP Data**|C0001.015|Send UDP data.|
|**Receive Data**|C0001.006|Receive data on socket.|
|**Receive TCP Data**|C0001.016|Receive TCP data.|
|**Receive UDP Data**|C0001.017|Receive UDP data.|
|**TCP Server**|C0001.002|TCP server behavior.|
|**TCP Client**|C0001.008|TCP client behavior.|
|**UDP Client**|C0001.013|UDP client behavior.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**SYNful Knock**](../../xample-malware/synful-knock.md)|2015|C0001.014|SYNful Knock initiates communication with the C2 server via a uniquely crafted TCP SYN packet sent to port 80 of the "implanted" router. [[1]](#1)|
|[**Hupigon**](../../xample-malware/hupigon.md)|2013|C0001.010|Hupigon creates a UDP socket. [[2]](#2)|
|[**Rombertik**](../../xample-malware/rombertik.md)|2015|C0001.011|Rombertik creates a TCP socket. [[2]](#2)|
|[**Shamoon**](../../xample-malware/shamoon.md)|2012|C0001.009|Shamoon initializes a Winsock library. [[2]](#2)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[start TCP server](https://github.com/mandiant/capa-rules/blob/master/communication/tcp/serve/start-tcp-server.yml)|Socket Communication::Start TCP Server (C0001.005)|listen, accept, WSAAccept, System.Net.Sockets.TcpListener::Start, System.Net.Sockets.TcpListener::AcceptTcpClient, System.Net.Sockets.TcpListener::BeginAcceptTcpClient, System.Net.Sockets.TcpListener::AcceptTcpClientAsync, System.Net.Sockets.TcpListener::AcceptSocket, System.Net.Sockets.TcpListener::BeginAcceptSocket, System.Net.Sockets.TcpListener::AcceptSocketAsync|
|[act as TCP client](https://github.com/mandiant/capa-rules/blob/master/communication/tcp/client/act-as-tcp-client.yml)|Socket Communication::TCP Client (C0001.008)|System.Net.Sockets.TcpClient::ctor|
|[get socket status](https://github.com/mandiant/capa-rules/blob/master/communication/socket/get-socket-status.yml)|Socket Communication::Get Socket Status (C0001.012)|select, ws2_32.select|
|[create raw socket](https://github.com/mandiant/capa-rules/blob/master/communication/socket/create-raw-socket.yml)|Socket Communication::Create Socket (C0001.003)|socket, ws32_32.WSASocket, ws2_32.WSASocketA, WSASocketW|
|[set socket configuration](https://github.com/mandiant/capa-rules/blob/master/communication/socket/set-socket-configuration.yml)|Socket Communication::Set Socket Config (C0001.001)|ws2_32.setsockopt, ws2_32.ioctlsocket|
|[create VMCI socket](https://github.com/mandiant/capa-rules/blob/master/communication/socket/create-vmci-socket.yml)|Socket Communication::Create Socket (C0001.003)|socket, DeviceIoControl, socket, ioctl|
|[initialize Winsock library](https://github.com/mandiant/capa-rules/blob/master/communication/socket/initialize-winsock-library.yml)|Socket Communication::Initialize Winsock Library (C0001.009)|ws2_32.WSAStartup, WSAStartup|
|[connect TCP socket](https://github.com/mandiant/capa-rules/blob/master/communication/socket/tcp/connect-tcp-socket.yml)|Socket Communication::Connect Socket (C0001.004)|connect, ws2_32.connect, ws2_32.WSAConnect, ConnectEx, WSAIoctl, setsockopt, bind|
|[create TCP socket](https://github.com/mandiant/capa-rules/blob/master/communication/socket/tcp/create-tcp-socket.yml)|Socket Communication::Create TCP Socket (C0001.011)|ws2_32.socket, ws2_32.WSASocket, socket|
|[create TCP socket via raw AFD driver](https://github.com/mandiant/capa-rules/blob/master/communication/socket/tcp/create-tcp-socket-via-raw-afd-driver.yml)|Socket Communication::Create TCP Socket (C0001.011)|kernel32.CreateEvent, NtCreateFile, NtDeviceIoControlFile, kernel32.WaitForSingleObject|
|[obtain TransmitPackets callback function via WSAIoctl](https://github.com/mandiant/capa-rules/blob/master/communication/socket/tcp/send/obtain-transmitpackets-callback-function-via-wsaioctl.yml)|Socket Communication::Send TCP Data (C0001.014)|WSAIoctl, WSAGetLastError|
|[send TCP data via WFP API](https://github.com/mandiant/capa-rules/blob/master/communication/socket/tcp/send/send-tcp-data-via-wfp-api.yml)|Socket Communication::Send TCP Data (C0001.014)|fwpkclnt.FwpsStreamInjectAsync0|
|[create UDP socket](https://github.com/mandiant/capa-rules/blob/master/communication/socket/udp/send/create-udp-socket.yml)|Socket Communication::Create UDP Socket (C0001.010)|ws2_32.socket, ws2_32.WSASocket, socket, System.Net.Sockets.Socket::ctor, System.Net.Sockets.UdpClient::ctor|
|[send data on socket](https://github.com/mandiant/capa-rules/blob/master/communication/socket/send/send-data-on-socket.yml)|Socket Communication::Send Data (C0001.007)|ws2_32.send, ws2_32.sendto, ws2_32.WSASend, ws2_32.WSASendMsg, ws2_32.WSASendTo, send, sendto, WSASend, WSASendTo, System.Net.Sockets.Socket::Send, System.Net.Sockets.Socket::SendAsync, System.Net.Sockets.Socket::SendTo, System.Net.Sockets.Socket::SendToAsync, System.Net.Sockets.UdpClient::Send|
|[receive data on socket](https://github.com/mandiant/capa-rules/blob/master/communication/socket/receive/receive-data-on-socket.yml)|Socket Communication::Receive Data (C0001.006)|ws2_32.recv, ws2_32.recvfrom, ws2_32.WSARecv, ws2_32.WSARecvDisconnect, ws2_32.WSARecvEx, ws2_32.WSARecvFrom, ws2_32.WSARecvMsg, recv, WSARecv, WSARecvDisconnect, WSARecvFrom, recvmsg, System.Net.Sockets.Socket::Receive, System.Net.Sockets.Socket::ReceiveAsync, System.Net.Sockets.Socket::ReceiveFrom, System.Net.Sockets.Socket::ReceiveFromAsync, System.Net.Sockets.Socket::ReceiveMessageFrom, System.Net.Sockets.Socket::ReceiveMessageFromAsync, System.Net.Sockets.Socket::BeginReceive, System.Net.Sockets.Socket::BeginReceiveFrom, System.Net.Sockets.Socket::BeginReceiveMessageFrom, System.Net.Sockets.Socket::EndReceive, System.Net.Sockets.Socket::EndReceiveFrom, System.Net.Sockets.Socket::EndReceiveMessageFrom|

|Tool: CAPE|Class|Mapping|APIs|
|---|---|---|---|
|[network_excessive_udp](https://github.com/CAPESandbox/community/tree/master/modules/signatures/all/network_excessive_udp.py)|NetworkExcessiveUDP|Socket Communication (C0001)|--|
|[network_bind](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/network_bind.py)|NetworkBIND|Socket Communication (C0001)|listen, bind|
|[rat_blackremote](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/rat_blackremote.py)|BlackRATNetworkActivity|Socket Communication (C0001)|send|
|[rat_oblique](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/rat_oblique.py)|ObliquekRATNetworkActivity|Socket Communication (C0001)|send|

### C0001.009 Snippet
<details>
<summary> Communication::Socket Communication::Initialize Winsock Library </summary>
SHA256: 000b535ab2a4fec86e2d8254f8ed65c6ebd37309ed68692c929f8f93a99233f6
Location: 0x472C92
<pre>
push    eax     ; pointer to WSADATA structure that the call to start Winsock will populate with the Windows socket data
push    0x101   ; highest version of Winsock permitted for use in this application -- in this case, version 1.1 (major version in lowest-order byte, minor version in highest-order byte)
call    WSOCK.DLL::WSAStartup   ; Initiate the Winsock DLL
</pre>
</details>

## References

<a name="1">[1]</a> https://www.mandiant.com/resources/synful-knock-acis

<a name="2">[2]</a> capa v4.0, analyzed at MITRE on 10/12/2022

