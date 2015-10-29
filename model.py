#! /usr/bin/env python


class event(object):
    def __init__(self, alert_time, device_id, device_version, dst_domain, dst_url, event_time, protocol_version, provider_name):
        self.alertTime = alert_time # e.g. 2013-02-08T11:14:26.0Z
        self.deviceId = device_id # e.g.ba6a59f4-e692-4724-ba36-c28132c761de
        self.deviceVersion = device_version # e.g.13.7a
        self.dstDomain = dst_domain # e.g.internetbadguys.com
        self.dstUrl = dst_url # e.g.http://internetbadguys.com/a-bad-url
        self.eventTime = event_time # e.g.2013-02-08T09:30:26.0Z
        self.protocolVersion = protocol_version # e.g.1.0a
        self.providerName = provider_name # e.g.Security Platform

class event_detail(event):
    def __init__(self, alert_time, device_id, device_version, dst_domain, dst_url, event_time, protocol_version, provider_name, disable_dst_safeguards, dst_ip, event_severity, event_type, event_description, event_hash, file_name, file_hash, external_url, src):
        self.alertTime = alert_time # e.g. 2013-02-08T11:14:26.0Z
        self.deviceId = device_id # e.g.ba6a59f4-e692-4724-ba36-c28132c761de
        self.deviceVersion = device_version # e.g.13.7a
        self.dstDomain = dst_domain # e.g.internetbadguys.com
        self.dstUrl = dst_url # e.g.http://internetbadguys.com/a-bad-url
        self.eventTime = event_time # e.g.2013-02-08T09:30:26.0Z
        self.protocolVersion = protocol_version # e.g.1.0a
        self.providerName = provider_name # e.g.Security Platform
        self.disableDstSafeguards = disable_dst_safeguards # e.g. true
        self.dstIp = dst_ip # e.g. "8.8.8.8"
        self.eventSeverity = event_severity # e.g. "Severe"
        self.eventType = event_type # e.g. "Cryptolocker"
        self.eventDescription = event_description # e.g. "Win32/Crilock.A"
        self.eventHash = event_hash # e.g. "d41d8cd98f00b204e9800998ecf8427e"
        self.fileName = file_name # e.g. "%AppData%RoamingMicrosoftWindowsTemplatesrandom.exe"
        self.fileHash = file_hash # e.g.  "da39a3ee5e6b4b0d3255bfef95601890afd80709"
        self.externalUrl = external_url # e.g. http://groogle.com/malware.html
        self.src = src # e.g. 192.168.100.101