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
<td><b>2.0</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>1 August 2019</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>21 November 2022</b></td>
</tr>
</table>


# Install Additional Program

Installs another, different program on the system. The additional program can be any secondary module; examples include backdoors, malicious drivers, kernel modules, and OS X Apps. 

Malware that installs another component is called a "dropper." If the code is contained in the malware, it's a "single stage" dropper; "two stage" droppers download the code from a remote location (the associated download behavior is covered by the **Ingress Tool Transfer ([E1105](../command-and-control/ingress-tool-transfer.md))** behavior.

## Use in Malware

|Name|Date|Method|Description|
|---|---|---|---|
|[**WebCobra**](../xample-malware/webcobra.md)|2018|--|The malware downloads and executes Claymore's Zcash miner from a remote server. [[1]](#1)|
|[**Geneio**](../xample-malware/geneio.md)|August 2015|--|Malware tricks OS X keychain to create application files. Malware also installs the browser extension Omnibar.safariextz. [[10]](#10)|
|[**GotBotKR**](../xample-malware/gobotkr.md)|July 2019|--|GotBotKR reinstalls its running instance if it is removed. [[3]](#3)|
|[**MazarBot**](../xample-malware/mazarbot.md)|2016|--|Installs a backdoor.|
|[**Mebromi**](../xample-malware/mebromi.md)|2011|--|Malware contains a dropper that installs additional programs like Cbrom.exe. [[11]](#11)|
|[**YiSpecter**](../xample-malware/yispecter.md)|2015|--|The malware can download and install arbitrary iOS apps. [[13]](#13)|
|[**UP007**](../xample-malware/up007.md)|2016|--|The malware is a dropper that creates multiple files [[4]](#4)|
|[**CozyCar**](../xample-malware/cozycar.md)|2010|--|Upon execution, CozyCar drops a decoy file and a secondary dropper [[5]](#5)|
|[**Clipminer**](../xample-malware/clipminer.md)|2011|--|Clipminer drops a file masquerading as a Control Panel (CPL) file [[6]](#6)|
|[**Vobfus**](../xample-malware/vobfus.md)|2016|--|Vobfus downloads malware from other malware families [[7]](#7)|
|[**Matanbuchus**](../xample-malware/matanbuchus.md)|2021|--|Malware drops the first loader which is responsible for loading the main loader into memory. [[8]](#8) [[9]](#9)|
|[**SearchAwesome**](../xample-malware/searchawesome.md)|2018|--|The malware installs an open-source program called mitmproxy. [[12]](#12)|

## References

<a name="1">[1]</a> https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/

<a name="2">[2]</a> https://www.fortinet.com/blog/threat-research/deep-analysis-of-driver-based-mitm-malware-itranslator.html

<a name="3">[3]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="4">[4]</a> https://citizenlab.ca/2016/04/between-hong-kong-and-burma/

<a name="5">[5]</a> https://unit42.paloaltonetworks.com/tracking-minidionis-cozycars-new-ride-is-related-to-seaduke

<a name="6">[6]</a> https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/clipminer-bitcoin-mining-hijacking

<a name="7">[7]</a> https://securitynews.sonicwall.com/xmlpost/revisiting-vobfus-worm-mar-8-2013/

<a name="8">[8]</a> https://www.0ffset.net/reverse-engineering/matanbuchus-loader-analysis/

<a name="9">[9]</a> https://www.cyberark.com/resources/threat-research-blog/inside-matanbuchus-a-quirky-loader

<a name="10">[10]</a> https://blog.malwarebytes.org/mac/2015/08/genieo-installer-tricks-keychain/

<a name="11">[11]</a> https://www.webroot.com/blog/2011/09/13/mebromi-the-first-bios-rootkit-in-the-wild/

<a name="12">[12]</a> https://blog.malwarebytes.com/threat-analysis/2018/10/mac-malware-intercepts-encrypted-web-traffic-for-ad-injection/

<a name="13">[13]</a> http://researchcenter.paloaltonetworks.com/2015/10/yispecter-first-ios-malware-attacks-non-jailbroken-ios-devices-by-abusing-private-apis/