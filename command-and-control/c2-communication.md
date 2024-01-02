<table>
<tr>
<td><b>ID</b></td>
<td><b>B0030</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../command-and-control">Command and Control</a></b></td>
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
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>5 December 2023</b></td>
</tr>
</table>


# C2 Communication

All command and control malware use implant/controller communication. The methods listed below can be used to capture explicit communication details. Remote file copy behavior is captured separately, as is done in ATT&CK - see **Ingress Tool Transfer ([E1105](../command-and-control/ingress-tool-transfer.md))**.

Command and Control Communication relates to *autonomous* communications, not explicit, on-demand commands that malware provides to an adversary (such commands should be captured with [Remote Commands](../execution/remote-commands.md) under the Execution objective).

As "server" and "client" are confusing terminology, we use the terms "controller" and "implant". The controller is the software running on adversary-controlled infrastructure and used to send commands to the implant. The implant is the software running on victim-controlled infrastructure that receives commands from the adversary, executes those commands on the victim, and optionally sends the results back to the adversary.

## Methods

|Name|ID|Description|
|---|---|---|
|**Authenticate**|B0030.011|Implant may authenticate itself to the controller, controller may authenticate itself to implant, or both. This is often at or near the start of communication. Examples include but are not limited to a simple shared secret (e.g. password), challenge-response with symmetric encryption, or challenge-response with asymmetric encryption.|
|**Check for Payload**|B0030.005|An implant may check with the controller for additional payloads or instructions, sometimes at a regular interval. This is also known as beaconing.|
|**Directory Listing**|B0030.012|Controller requests a directory listing from the implant, optionally from a given path, optionally recursive.|
|**Execute File**|B0030.013|Execute/run/open the file using default operating system functionality, optionally with provided command-and-scripting-interpreter arguments. The file may or may not already exist on the victim.|
|**Execute Shell Command**|B0030.014|Execute/run the given command using a built-in program (e.g. cmd.exe, PowerShell, bash). This differs from Start Interactive Shell because the shell process is started only for the received command or set of commands and then exits. There is no loop looking for additional commands while the shell process is still running.|
|**File search**|B0030.015|Controller requests the implant to search for a given filename pattern, often a [glob](https://en.wikipedia.org/wiki/Glob_(programming)).|
|**Implant to Controller File Transfer**|B0030.004|File is transferred from implant to controller.|
|**Receive Data**|[B0030.002](#b0030002-snippet)|Receive data or command from a controller.|
|**Request Command**|B0030.008|Implant requests a command.|
|**Request Email Address List**|B0030.010|Request email address list.|
|**Request Email Template**|B0030.009|Request email template.|
|**Send Data**|B0030.001|Send data to a controller.|
|**Send Heartbeat**|B0030.007|Heartbeat sent.|
|**Send System Information**|B0030.006|Implant sends system information.|
|**Server to Client File Transfer**|B0030.003|File is transferred from controller to implant.|
|**Start Interactive Shell**|B0030.016|Starts an interactive shell using a built-in program (e.g. cmd.exe, PowerShell, bash). This is often implemented with polling the network connection from the controller for text commands to redirect to the shell's stdin and polling the shell's stdout and stderr to redirect over the network to the controller. This differs from Execute Shell Command because the shell process runs across multiple iterations of the recv-command(s)-send-result loop.|

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**CryptoWall**](../xample-malware/cryptowall.md)|2014|B0030.001|The malware sends a hash value generated from system information. [[1]](#1)|
|[**CryptoWall**](../xample-malware/cryptowall.md)|2014|B0030.002|The malware receives a public key from the C2. [[1]](#1)|
|[**CryptoLocker**](../xample-malware/cryptolocker.md)|2013|B0030.001|The malware sends a hash value generated from system information. [[14]](#14)|
|[**CryptoLocker**](../xample-malware/cryptolocker.md)|2013|B0030.002|The malware receives a public key from the C2. [[14]](#14)|
|[**CryptoLocker**](../xample-malware/cryptolocker.md)|2013|B0030.011|The malware sends a phone-home message with encryption to start. [[14]](#14)|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|B0030.002|GoBotKR receives data from the C2. [[2]](#2) [[19]](#19)|
|[**Terminator**](../xample-malware/terminator.md)|2013|B0030.001|The malware sends data to the C2. [[3]](#3)|
|[**UP007**](../xample-malware/up007.md)|2016|B0030.001|The malware sends hardened HTTP headers disguised as Microsoft Update traffic. [[4]](#4)|
|[**UP007**](../xample-malware/up007.md)|2016|B0030.002|The malware receives payloads. [[4]](#4)|
|[**YiSpecter**](../xample-malware/yispecter.md)|2015|B0030.006|The malware connects to the C2 server using HTTP to send device information. [[5]](#5)|
|[**Ursnif**](../xample-malware/ursnif.md)|2016|B0030.011|Ursnif variant Dreambot authenticates and encrypts traffic to the C2 server using TOR. [[6]](#6)|
|[**Emotet**](../xample-malware/emotet.md)|2018|B0030.010|New email addresses are collected automatically from the victim's address books. [[7]](#7)|
|[**CHOPSTICK**](../xample-malware/chopstick.md)|2015|B0030.001|CHOPSTICK sends data to the C2 server using HTTP POST requests. [[8]](#8)|
|[**CozyCar**](../xample-malware/cozycar.md)|2010|--|CozyCar communicates with a C2 server. [[9]](#9)|
|[**EvilBunny**](../xample-malware/evilbunny.md)|2011|--|EvilBunny communicates C2 via HTTP. [[10]](#10)|
|[**Clipminer**](../xample-malware/clipminer.md)|2011|--|Clipminer communicates to a Tor Onion Service via HTTP. [[11]](#11)|
|[**Matanbuchus**](../xample-malware/matanbuchus.md)|2021|B0030.001|The malware sends collected data about the system to C2 server. [[12]](#12) [[13]](#13)|
|[**Matanbuchus**](../xample-malware/matanbuchus.md)|2021|B0030.002|The C2 server returns Base64 encoded data containing the information about the next command for the loader. [[12]](#12) [[13]](#13)|
|[**Matanbuchus**](../xample-malware/matanbuchus.md)|2021|B0030.013|The payload is run by explorer.exe. [[12]](#12) [[13]](#13)|
|[**Gamut**](../xample-malware/gamut.md)|2014|B0030.002|Gamut receives data from the C2. [[15]](#15)|
|[**Gamut**](../xample-malware/gamut.md)|2014|B0030.003|The malware receives files from the C2. [[15]](#15)|
|[**GravityRAT**](../xample-malware/gravity-rat.md)|2018|B0030.002|GravityRAT receives data from the C2.  [[19]](#19)|
|[**Heriplor**](../xample-malware/heriplor.md)|2012|B0030.002|Heriplor malware has a capability to connect with a C2 to download arbitrary code. [[16]](#16)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|B0030.001|The malware sends data to the C2. [[17]](#17) [[19]](#19)|
|[**Rombertik**](../xample-malware/rombertik.md)|2015|B0030.002|The malware receives data from the C2. [[19]](#19)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|BB0030.001|The malware sends data to the C2. [[19]](#19)|
|[**Hupigon**](../xample-malware/hupigon.md)|2013|B0030.002|The malware receives data from the C2. [[19]](#19)|
|[**Kovter**](../xample-malware/kovter.md)|2016|B0030.001|The malware sends data to the C2. [[19]](#19)|
|[**Kovter**](../xample-malware/kovter.md)|2016|B0030.002|The malware receives data from the C2. [[19]](#19)|
|[**SearchAwesome**](../xample-malware/searchawesome.md)|2018|B0030.002|The malware receives data from the C2 server. [[18]](#18)|
|[**ElectroRAT**](../xample-malware/electrorat.md)|2020|--|ElectroRat communicates to a Pastebin site via HTTP. [[20]](#20)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[send data](https://github.com/mandiant/capa-rules/blob/master/communication/send-data.yml)|C2 Communication::Send Data (B0030.001)|--|
|[receive data](https://github.com/mandiant/capa-rules/blob/master/communication/receive-data.yml)|C2 Communication::Receive Data (B0030.002)|--|
|[download and write a file](https://github.com/mandiant/capa-rules/blob/master/communication/c2/file-transfer/download-and-write-a-file.yml)|C2 Communication::Server to Client File Transfer (B0030.003)|--|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[office_cve2017_11882_network](https://github.com/CAPESandbox/community/tree/master/modules/signatures/office_cve2017_11882_network.py)|C2 Communication (B0030)|ConnectEx, URLDownloadToFileW|
|[internet_dropper](https://github.com/CAPESandbox/community/tree/master/modules/signatures/internet_dropper.py)|C2 Communication (B0030)|HttpOpenRequestA, InternetConnectA, HttpOpenRequestW, InternetConnectW|
|[internet_dropper](https://github.com/CAPESandbox/community/tree/master/modules/signatures/internet_dropper.py)|C2 Communication::Check for Payload (B0030.005)|HttpOpenRequestA, InternetConnectA, HttpOpenRequestW, InternetConnectW|
|[bot_madness](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bot_madness.py)|C2 Communication (B0030)|--|
|[bot_drive](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bot_drive.py)|C2 Communication (B0030)|--|
|[recon_beacon](https://github.com/CAPESandbox/community/tree/master/modules/signatures/recon_beacon.py)|C2 Communication (B0030)|HttpOpenRequestA, HttpSendRequestA|
|[nemty_network_activity](https://github.com/CAPESandbox/community/tree/master/modules/signatures/nemty_network_activity.py)|C2 Communication (B0030)|InternetOpenA, InternetOpenUrlA|
|[bot_drive2](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bot_drive2.py)|C2 Communication (B0030)|--|
|[bot_dirtjumper](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bot_dirtjumper.py)|C2 Communication (B0030)|--|
|[bot_athenahttp](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bot_athenahttp.py)|C2 Communication (B0030)|--|
|[network_dns_tunneling_request](https://github.com/CAPESandbox/community/tree/master/modules/signatures/network_dns_tunneling_request.py)|C2 Communication (B0030)|DnsQuery_A, DnsQuery_W|
|[network_questionable_host](https://github.com/CAPESandbox/community/tree/master/modules/signatures/network_questionable_host.py)|C2 Communication (B0030)|--|
|[injection_network_traffic](https://github.com/CAPESandbox/community/tree/master/modules/signatures/injection_network_traffic.py)|C2 Communication (B0030)|HttpOpenRequestA, URLDownloadToFileW, HttpOpenRequestW, InternetConnectW, InternetConnectA, connect, InternetCrackUrlW, InternetCrackUrlA, WSASend|
|[network_bind](https://github.com/CAPESandbox/community/tree/master/modules/signatures/network_bind.py)|C2 Communication (B0030)|listen, bind|
|[network_document_http](https://github.com/CAPESandbox/community/tree/master/modules/signatures/network_document_http.py)|C2 Communication (B0030)|URLDownloadToFileW, HttpOpenRequestW, InternetCrackUrlW, InternetCrackUrlA, WSASend, InternetReadFile|
|[network_country_distribution](https://github.com/CAPESandbox/community/tree/master/modules/signatures/network_country_distribution.py)|C2 Communication (B0030)|--|
|[banker_zeus_url](https://github.com/CAPESandbox/community/tree/master/modules/signatures/banker_zeus_url.py)|C2 Communication (B0030)|--|
|[network_dyndns](https://github.com/CAPESandbox/community/tree/master/modules/signatures/network_dyndns.py)|C2 Communication (B0030)|--|
|[script_network_activity](https://github.com/CAPESandbox/community/tree/master/modules/signatures/script_network_activity.py)|C2 Communication (B0030)|URLDownloadToFileW, HttpOpenRequestW, send, WSAConnect, InternetCrackUrlW, InternetCrackUrlA, SslEncryptPacket, InternetReadFile|

## Code Snippets

### B0030.002 Snippet
<details>
<summary> C2 Communication::Receive Data </summary>
SHA256: 304f533ce9ea4a9ee5c19bc81c49838857c63469e26023f330823c3240ee4e0
<pre>
asm
loc_401981
mov ecx, s
mov edx, edi
sub edx, esi
push 0 ; flags
lea eax, [esi+ebx]
push edx ;len
push eax ;buf
push ecx ;s
call recv
jmp short loc_4019A2
</pre>
</details>

## References

<a name="1">[1]</a> https://news.sophos.com/en-us/2015/12/17/the-current-state-of-ransomware-cryptowall/

<a name="2">[2]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="3">[3]</a> https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2013/FireEye-Terminator_RAT.pdf

<a name="4">[4]</a> https://citizenlab.ca/2016/04/between-hong-kong-and-burma/

<a name="5">[5]</a> https://unit42.paloaltonetworks.com/yispecter-first-ios-malware-attacks-non-jailbroken-ios-devices-by-abusing-private-apis/

<a name="6">[6]</a> https://www.proofpoint.com/us/threat-insight/post/ursnif-variant-dreambot-adds-tor-functionality

<a name="7">[7]</a> https://securelist.com/the-banking-trojan-emotet-detailed-analysis/69560/

<a name="8">[8]</a> https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf

<a name="9">[9]</a> https://unit42.paloaltonetworks.com/tracking-minidionis-cozycars-new-ride-is-related-to-seaduke

<a name="10">[10]</a> https://web.archive.org/web/20150311013500/http://www.cyphort.com/evilbunny-malware-instrumented-lua/

<a name="11">[11]</a> https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/clipminer-bitcoin-mining-hijacking

<a name="12">[12]</a> https://www.0ffset.net/reverse-engineering/matanbuchus-loader-analysis/

<a name="13">[13]</a> https://www.cyberark.com/resources/threat-research-blog/inside-matanbuchus-a-quirky-loader

<a name="14">[14]</a> https://www.secureworks.com/research/cryptolocker-ransomware

<a name="15">[15]</a> https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/gamut-spambot-analysis/

<a name="16">[16]</a> https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/troj_heriplor.a

<a name="17">[17]</a> https://blogs.cisco.com/security/talos/rombertik

<a name="18">[18]</a> https://www.malwarebytes.com/blog/news/2018/10/mac-malware-intercepts-encrypted-web-traffic-for-ad-injection

<a name="19">[19]</a> capa v4.0, analyzed at MITRE on 10/12/2022

<a name="20">[20]</a> https://www.intezer.com/blog/research/operation-electrorat-attacker-creates-fake-companies-to-drain-your-crypto-wallets/