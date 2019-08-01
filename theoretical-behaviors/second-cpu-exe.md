|||
|---------|------------------------|
|**ID**|**M0015**|
|**Objective(s)**| [Defense Evasion](https://github.com/MAECProject/malware-behaviors/tree/master/defense-evasion)|
|**Related ATT&CK Technique(s)**|None|


Secondary CPU Execution (THEORETICAL)
======================================
Executes some or all of the code of the malware instance on a secondary, non-CPU processor (e.g., graphics processing unit (GPU)). This behavior is not included in the MBC because no real world examples have been found.

Proof-of-Concept Malware
------------------------
|Name|Date|Description|
|-----------------------------|--------|-----------------------------|
|Jellyfish Rootkit|2015| Created by the Jellyfish research group. Runs on the graphics card instead of CPU.|
|Demon|2013| A GPU-based proof-of-concept keylogger that records user keystrokes, stores them in the memory space of the GPU, and analyzes the recorded data in-place. [[2]](#2)|

References
----------
<a name="1">[1]</a> https://arstechnica.com/information-technology/2015/05/gpu-based-rootkit-and-keylogger-offer-superior-stealth-and-computing-power/

<a name="2">[2]</a> http://www.cs.columbia.edu/~mikepo/papers/gpukeylogger.eurosec13.pdf

<a name="3">[3]</a> https://news.softpedia.com/news/New-Malware-Pieces-Run-Completely-on-Graphics-Card-480809.shtml

<a name="4">[4]</a> https://news.softpedia.com/news/intel-researchers-gpu-based-malware-not-as-scary-as-intitially-thought-490490.shtml
