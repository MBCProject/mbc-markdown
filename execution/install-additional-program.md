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
|[**WebCobra**](../xample-malware/webcobra.md)|November 2018|B0023|Drops software to mine for cryptocurrency. [[1]](#1)|
|[**Geneio**](../xample-malware/geneio.md)|August 2015|B0023|Geneio installs the browser extension ~/Library/Safari/Extensions/Omnibar.safariextz. It also creates app files. [[7]](#7)|
|[**GoBotKR**](../xample-malware/gobotkr.md)|2019|B0023|GoBotKR reinstalls its running instance if it is removed. [[3]](#3)|
|[**MazarBot**](../xample-malware/mazarbot.md)|2016|B0023|Installs a backdoor. [[8]](#8)|
|[**Mebromi**](../xample-malware/mebromi.md)|2011|B0023|Malware contains a dropper that installs additional programs like Cbrom.exe. [[9]](#9)|
|[**YiSpecter**](../xample-malware/yispecter.md)|2015|B0023|Can download and install arbitrary iOS apps. [[10]](#10)|
|[**UP007**](../xample-malware/up007.md)|2016|--|The malware is a dropper that creates multiple files [[4]](#4)|
|[**CozyCar**](../xample-malware/cozycar.md)|2010|B0023|Upon execution, CozyCar drops a decoy file and a secondary dropper [[5]](#5)|
|[**Clipminer**](../xample-malware/clipminer.md)|2011|B0023|Clipminer drops a file masquerading as a Control Panel (CPL) file [[6]](#6)|
|[**Dark Comet**](../xample-malware/dark-comet.md)|2008|B0023|Contain an embedded PE file (This capa rule had 1 match) [[11]](#11)|
|[**Gamut**](../xample-malware/gamut.md)|2014|B0023|Contain an embedded PE file (This capa rule had 1 match) [[11]](#11)|
|[**Redhip**](../xample-malware/rebhip.md)|2011|B0023|Contain an embedded PE file (This capa rule had 1 match) [[11]](#11)|
|[**SearchAwesome**](../xample-malware/searchawesome.md)|2018|B0023|The malware installs an open-source program called mitmproxy. [[12]](#12)|
|[**UP007 Malware Family**](../xample-malware/up007.md)|2016|B0023|The malware is a dropper that creates multiple files [[4]](#4)|

## References

<a name="1">[1]</a> https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/webcobra-malware-uses-victims-computers-to-mine-cryptocurrency/

<a name="2">[2]</a> https://www.fortinet.com/blog/threat-research/deep-analysis-of-driver-based-mitm-malware-itranslator.html

<a name="3">[3]</a> https://www.welivesecurity.com/2019/07/08/south-korean-users-backdoor-torrents/

<a name="4">[4]</a> https://citizenlab.ca/2016/04/between-hong-kong-and-burma/

<a name="5">[5]</a> https://unit42.paloaltonetworks.com/tracking-minidionis-cozycars-new-ride-is-related-to-seaduke

<a name="6">[6]</a> https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/clipminer-bitcoin-mining-hijacking

<a name="7">[7]</a> https://blog.malwarebytes.org/mac/2015/08/genieo-installer-tricks-keychain/

<a name="8">[8]</a> https://us.norton.com/internetsecurity-emerging-threats-mazar-bot-malware-invades-and-erases-android-devices.html

<a name="9">[9]</a> https://www.webroot.com/blog/2011/09/13/mebromi-the-first-bios-rootkit-in-the-wild/

<a name="10">[10]</a> http://researchcenter.paloaltonetworks.com/2015/10/yispecter-first-ios-malware-attacks-non-jailbroken-ios-devices-by-abusing-private-apis/

<a name="11">[11]</a> capa v4.0, analyzed at MITRE on 10/12/2022

<a name="12">[12]</a> https://blog.malwarebytes.com/threat-analysis/2018/10/mac-malware-intercepts-encrypted-web-traffic-for-ad-injection/

