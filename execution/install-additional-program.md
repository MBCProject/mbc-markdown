<table>
<tr>
<td><b>ID</b></td>
<td><b>B0023</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../execution">Execution</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.3</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>30 April 2024</b></td>
</tr>
</table>


# Install Additional Program

Malware installs another, different program on the system. The additional program can be any secondary module as exemplified by backdoors, malicious drivers, kernel modules, and OS X Apps.

There are various ways to accomplish the installation. For example, malicious code can beacon to a C2 node for download of an additional program including updates (see **Ingress Tool Transfer ([E1105](../command-and-control/ingress-tool-transfer.md))**), which is then executed and installed [[1]](#1). A threat actor can achieve the same goal using a dropper embedded in the binary files of the original executable or using API calls to extract resource files that are in fact hidden executables. Extracted files are then dropped to the disk.

Examples of droppers include malicious
•	Microsoft Excel files
•	ISO image files 
•	self-extracting zip or archives files, which in turn may contain a second stage dropper as part of the payload [[2]](#2) [[3]](#3). 

Droppers may be described as “single stage” or “two stage.” While the former embeds the malicious code internally, the latter installs itself before downloading additional code from a remote location [[4]](#4).  


## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**WebCobra**](../xample-malware/webcobra.md)|2018|--|The malware downloads and executes Claymore's Zcash miner from a remote server. [[5]](#5)|
|[**Geneio**](../xample-malware/geneio.md)|2015|--|Malware tricks OS X keychain to create application files. Malware also installs the browser extension Omnibar.safariextz. [[14]](#14)|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|--|GoBotKR reinstalls its running instance if it is removed. [[7]](#7)|
|[**MazarBot**](../xample-malware/mazarbot.md)|2016|--|MazarBot installs a backdoor. [[18]](#18)|
|[**Mebromi**](../xample-malware/mebromi.md)|2011|--|Malware contains a dropper that installs additional programs like Cbrom.exe. [[15]](#15)|
|[**YiSpecter**](../xample-malware/yispecter.md)|2015|--|The malware can download and install arbitrary iOS apps. [[17]](#17)|
|[**UP007**](../xample-malware/up007.md)|2016|--|The malware is a dropper that creates multiple files. [[8]](#8)|
|[**CozyCar**](../xample-malware/cozycar.md)|2010|--|Upon execution, CozyCar drops a decoy file and a secondary dropper. [[9]](#9)|
|[**Clipminer**](../xample-malware/clipminer.md)|2011|--|Clipminer drops a file masquerading as a Control Panel (CPL) file. [[10]](#10)|
|[**Vobfus**](../xample-malware/vobfus.md)|2016|--|Vobfus downloads malware from other malware families. [[11]](#11)|
|[**Matanbuchus**](../xample-malware/matanbuchus.md)|2021|--|Malware drops the first loader which is responsible for loading the main loader into memory. [[12]](#12) [[13]](#13)|
|[**SearchAwesome**](../xample-malware/searchawesome.md)|2018|--|The malware installs an open-source program called mitmproxy. [[16]](#16)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|--|The malware contains an embedded PE file. [[19]](#19)|
|[**Gamut**](../xample-malware/gamut.md)|2014|--|Gamut contains an embedded PE file. [[19]](#19)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|--|Redhip contains an embedded PE file. [[19]](#19)|
|[**ElectroRAT**](../xample-malware/electrorat.md)|2020|--|ElectroRat looks for wallets to steal cryptocurrency. [[20]](#20)|

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[contain an embedded PE file](https://github.com/mandiant/capa-rules/blob/master/executable/subfile/pe/contain-an-embedded-pe-file.yml)|Install Additional Program (B0023)|--|
|[write and execute a file](https://github.com/mandiant/capa-rules/blob/master/communication/c2/file-transfer/write-and-execute-a-file.yml)|Install Additional Program (B0023)|--|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[bitcoin_opencl](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/bitcoin_opencl.py)|Install Additional Program (B0023)|--|
|[dropper](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/dropper.py)|Install Additional Program (B0023)|--|
|[sniffer_winpcap](https://github.com/CAPESandbox/community/tree/master/modules/signatures/windows/sniffer_winpcap.py)|Install Additional Program (B0023)|--|

## References
<a name="1">"Cyclops Blink: Malware Analysis Report, Version 1.0," National Cyber Security Centre/GCHQ, 23 Feb. 2022. [Online]. Available: https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf.

<a name="2"> Threat Hunter Team,"Shuckworm: Espionage Group Continues Intense Campaign Against Ukraine," Symantec, Enterprise Blogs/Threat Intelligence, 20 Apr. 2022. [Online]. Available: https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/shuckworm-intense-campaign-ukraine.

<a name="3">"What's behind APT29? | How they attack: the story of our hunt for the CozyDuke cybercriminal group," Kaspersky.com, [Online]. Available: https://www.kaspersky.com/enterprise-security/mitre/apt29.

<a name="4">"Dropper," Computersecurity.fandom.com, wiki, [Online]. Available: https://computersecurity.fandom.com/wiki/Dropper.

<a name="5">[5]</a> https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/

<a name="6">[6]</a> https://www.fortinet.com/blog/threat-research/deep-analysis-of-driver-based-mitm-malware-itranslator.html

<a name="7">[7]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="8">[8]</a> https://citizenlab.ca/2016/04/between-hong-kong-and-burma/

<a name="9">[9]</a> https://unit42.paloaltonetworks.com/tracking-minidionis-cozycars-new-ride-is-related-to-seaduke

<a name="10">[10]</a> https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/clipminer-bitcoin-mining-hijacking

<a name="11">[11]</a> https://securitynews.sonicwall.com/xmlpost/revisiting-vobfus-worm-mar-8-2013/

<a name="12">[12]</a> https://www.0ffset.net/reverse-engineering/matanbuchus-loader-analysis/

<a name="13">[13]</a> https://www.cyberark.com/resources/threat-research-blog/inside-matanbuchus-a-quirky-loader

<a name="14">[14]</a> https://blog.malwarebytes.org/mac/2015/08/genieo-installer-tricks-keychain/

<a name="15">[15]</a> https://www.webroot.com/blog/2011/09/13/mebromi-the-first-bios-rootkit-in-the-wild/

<a name="16">[16]</a> https://www.malwarebytes.com/blog/news/2018/10/mac-malware-intercepts-encrypted-web-traffic-for-ad-injection

<a name="17">[17]</a> https://unit42.paloaltonetworks.com/yispecter-first-ios-malware-attacks-non-jailbroken-ios-devices-by-abusing-private-apis/

<a name="18">[18]</a> https://us.norton.com/internetsecurity-emerging-threats-mazar-bot-malware-invades-and-erases-android-devices.html

<a name="19">[19]</a> capa v4.0, analyzed at MITRE on 10/12/2022

<a name="20">[20]</a> https://www.intezer.com/blog/research/operation-electrorat-attacker-creates-fake-companies-to-drain-your-crypto-wallets/