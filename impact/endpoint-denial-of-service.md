|||
|---------|------------------------|
|**ID**|**T1499**|
|**Objective(s)**|[Impact](https://github.com/MAECProject/malware-behaviors/tree/master/impact)|
|**Related ATT&CK Technique(s)**|[**Endpoint Denial of Service**](https://attack.mitre.org/techniques/T1499/), [Lock User Out of Device](https://attack.mitre.org/techniques/T1446/)|


Endpoint Denial of Service
==========================
Malware may make a system unavailable, for example, by locking a user out of a system. The ATT&CK technique, [Lock User Out of Device](https://attack.mitre.org/techniques/T1446/), pertains to the Android platform; the technique [Endpoint Denial of Service](https://attack.mitre.org/techniques/T1499/) is applicable to other platforms.

Network denial of service behaviors are captured by the [Denial of Service](https://github.com/MAECProject/malware-behaviors/blob/master/impact/denial-of-service.md) Behavior.

See ATT&CK: [**Endpoint Denial of Service**](https://attack.mitre.org/techniques/T1499/) and [**Lock User Out of Device**](https://attack.mitre.org/techniques/T1446/).

Methods
-------
* **User Lock Out**: Locks user out of a system.

Malware Examples
----------------
|Name|Date|Description|
|-----------------------------|-----------|-----------------------------|
|BlackEnergy| October 2007| Launches distributed denial of service attacks that can target more than one IP address per hostname. [[1]](#1)|

References
----------
<a name="1">[1]</a> http://atlas-public.ec2.arbor.net/docs/BlackEnergy+DDoS+Bot+Analysis.pdf


 