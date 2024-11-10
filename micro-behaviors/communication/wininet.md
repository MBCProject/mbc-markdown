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
<td><b>2.2</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>14 August 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>30 April 2024</b></td>
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

## Detection

|Tool: CAPE|Class|Mapping|APIs|
|---|---|---|---|
|[nemty_network_activity](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/ransomware_nemty.py)|NemtyNetworkActivity|WinINet (C0005)|InternetOpenA, InternetOpenUrlA|
|[nemty_network_activity](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/ransomware_nemty.py)|NemtyNetworkActivity|WinINet::InternetOpen (C0005.002)|InternetOpenA|
|[nemty_network_activity](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/ransomware_nemty.py)|NemtyNetworkActivity|WinINet::InternetOpenURL (C0005.003)|InternetOpenUrlA|
|[powershell_network_connection](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/powershell_command.py)|PowerShellNetworkConnection|WinINet (C0005)|InternetCrackUrlW, InternetCrackUrlA|

### C0005.001 Snippet
<details>
<summary> Communication::WinINet::InternetConnect </summary>
SHA256: 3ac8c22eb7c59d35fe49c20f2a0eca06765543dfb15f455a5557af4428066641
Location: 0x1800010b2
<pre>
call    qword ptr [->WININET.DLL::InternetOpenA]        ; Open a connection to the Internet and return the handle into rax
mov     rbp, rax        ; store the handle in rbp
test    rax, rax
jz      LAB_1800013de
mov     param_1, 0x17
call    thunk_FUN_180004114
mov     r10, rax
mov     rdi, rax
xor     eax, eax
mov     param_1, 0x17
stosb.rep       rdi
mov     rdi, r10
mov     param_2, rbx
nop     dword ptr [rax]
nop     word ptr [rax + rax*0x1]
movzx   param_1, byte ptr [param_2 + rsi*offset DAT_18001ea00]       ; first instruction in loop
add     param_2, 0x3    ; increase loop variable
mov     byte ptr [rdi], param_1
lea     rdi, [rdi + 0x1]
cmp     param_2, 0x42   ; test for loop end
jl      LAB_1800010f0   ; jump to beginning of loop
movzx   param_3, word ptr [DAT_18001ea44]       ; TCP/IP port to connect to.  DAT_18001ea44 contains 443, so this connection will occur on the default HTTPS port
xor     r9d, r9d        ; name of user (if FTP connection), or NULL
mov     qword ptr [rsp + local_390], rbx        ; pointer to application context for the returned handle to the internet connection
mov     param_2, r10    ; pointer to host name for internet server
mov     dword ptr [rsp + local_398], ebx        ; pointer to flags specific for service used
mov     param_1, rbp    ; handle to the internet connection established earlier
mov     dword ptr [rsp + local_3a0], 0x3        ; service type to access (0x3 indicates use of HTTP)
mov     qword ptr [rsp + local_3a8], rbx        ; password for FTP (if needed)
call    qword ptr [->WININET.DLL::InternetConnectA]     ; Windows API function to initiate an HTTP connection
</pre>
</details>

## References

<a name="1">[1]</a> https://docs.microsoft.com/en-us/windows/win32/wininet/wininet-functions
