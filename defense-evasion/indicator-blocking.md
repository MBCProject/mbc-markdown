|||
|---|---|
|**ID**|**F0006**|
|**Objective(s)**|[Defense Evasion](../defense-evasion)|
|**Related ATT&CK Sub-Technique**|[Impair Defenses: Indicator Blocking](https://attack.mitre.org/techniques/T1562/006/)|


Indicator Blocking
==================
Malware blocks indicators or events that would indicate malicious activity. Methods relevant to the malware domain are below. 

See ATT&CK: [**Impair Defenses: Indicator Blocking**](https://attack.mitre.org/techniques/T1562/006/).

Methods
-------
|Name|ID|Description|
|---|---|---|
|**Remove SMS Warning Messages**|F0006.001|Malware captures the message body of incoming SMS messages and aborts displaying messages that meets a certain criteria.|


Malware Examples
----------------
|Name|Date|Description|
|---|---|---|
|[**BlackEnergy**](../defense-evasion/indicator-blocking.md)|2007|Clears windows event logs and removes the watermark associated with enabling the TESTSIGNING boot configuration option by removing the relevent strings in the user32.dll.mui of the system  [[1]](#1)|

|[**Conficker**](../defense-evasion/indicator-blocking.md)|2008|Terminates various services related to system security and Windows and prevents network access to various websites related to antivirus software  [[2]](#2)|

References
----------
<a name="1">[1]</a> https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf

<a name="2">[2]</a> https://en.wikipedia.org/wiki/Conficker
