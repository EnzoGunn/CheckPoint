#! /usr/bin/env python


class Event(object):
    def __init__(self, alert_time, device_id, device_version, dst_domain, dst_url, event_time, protocol_version, provider_name):
        # Time event was sent to OpenDNS, must match the following style 2013-02-08T09:30:26Z
        self.alertTime = alert_time  # e.g. 2013-02-08T11:14:26.0Z
        # The ID of the device sending the event
        self.deviceId = device_id  # e.g.ba6a59f4-e692-4724-ba36-c28132c761de
        # Version of device sending the event
        self.deviceVersion = device_version  # e.g.13.7a
        # The destination domain, specified following RFC3986 guidelines and without the protocol included. An example would be 'www.badguys.com'
        self.dstDomain = dst_domain  # e.g.internetbadguys.com
        # The destination URL encoded, following RFC3986 guidelines. An example would be 'http://badguys.com/path?foo=word%20spaces'
        self.dstUrl = dst_url  # e.g.http://internetbadguys.com/a-bad-url
        # Time event was detected, must match the following style 2013-02-08T09:30:26Z
        self.eventTime = event_time  # e.g.2013-02-08T09:30:26.0Z
        # The version of the protocol for the API. Value should always be "1.0a"
        self.protocolVersion = protocol_version  # e.g.1.0a
        # The provider name for the API. Value should always be "Security Platform"
        self.providerName = provider_name  # e.g.Security Platform


class EventDetail(Event):
    def __init__(self, alert_time, device_id, device_version, dst_domain, dst_url, event_time, protocol_version, provider_name, disable_dst_safeguards, dst_ip, event_severity, event_type, event_description, event_hash, file_name, file_hash, external_url, src):
        Event.__init__(self, alert_time, device_id, device_version, dst_domain, dst_url, event_time, protocol_version, provider_name)
        # Boolean value. 'false' is the same as not providing this field at all
        self.disableDstSafeguards = disable_dst_safeguards  # e.g. true
        # The destination IP of the domain, specified in IPv4 dotted-decimal notation. An example would be '8.8.8.8'
        self.dstIp = dst_ip  # e.g. "8.8.8.8"
        # The partner threat level or rating, eg: severe, bad, high, etc.
        self.eventSeverity = event_severity  # e.g. "Severe"
        # Common name or classification of threat
        self.eventType = event_type  # e.g. "Cryptolocker"
        # Variant or other descriptor of event type
        self.eventDescription = event_description  # e.g. "Win32/Crilock.A"
        # A unique hash of the event
        self.eventHash = event_hash  # e.g. "d41d8cd98f00b204e9800998ecf8427e"
        # Path to file exhibiting malicious behavior
        self.fileName = file_name  # e.g. "%AppData%RoamingMicrosoftWindowsTemplatesrandom.exe"
        # SHA-1 of file reported by appliance
        self.fileHash = file_hash  # e.g.  "da39a3ee5e6b4b0d3255bfef95601890afd80709"
        # External page containing additional information about event
        self.externalUrl = external_url  # e.g. http://groogle.com/malware.html
        # IP/Host of the infected computer/device that was patient 0 for the event
        self.src = src  # e.g. 192.168.100.101
