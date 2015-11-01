#! /usr/bin/env python

from svc_config import SvcConfig
from svc_utils import SvcUtils


class EventRequest(object):
    def __init(self, device_id, device_version, dst_url, event_time):
        self.deviceId = device_id  # The ID of the device sending the event
        self.deviceVersion = device_version  # Version of device sending the event
        self.dstUrl = dst_url  # The destination URL encoded, following RFC3986 guidelines
        self.eventTime = event_time  # Time event was detected, must match the following style 2013-02-08T09:30:26Z

    def validate_request(self):
        if self.deviceId is None:
            raise Exception('Invalid event request, device ID is missing')
        if self.deviceVersion is None:
            raise Exception('Invalid event request, device version is missing')
        if self.dstUrl is None:
            raise Exception('Invalid event request, destination URL is missing')
        if self.eventTime is None:
            raise Exception('Invalid event request, event time (UTC) is missing')
        if SvcUtils.regex_validate(SvcConfig.uri_validation_regex, self.dstUrl) is False:
            raise ValueError('In')


class EventDetailRequest(EventRequest):
    def __init(self, device_id, device_version, dst_url, event_time, disable_dst_safeguards, dst_ip, event_severity, event_type, event_description, file_name, external_url, src):
        EventRequest.__init(self, device_id, device_version, dst_url, event_time)
        self.disableDstSafeguards = disable_dst_safeguards  # Boolean value. 'false' is the same as not providing this field at all
        self.dstIp = dst_ip  # The destination IP of the domain, specified in IPv4 dotted-decimal notation. An example would be '8.8.8.8'
        self.eventSeverity = event_severity  # The partner threat level or rating, eg: severe, bad, high, etc.
        self.eventType = event_type  # Common name or classification of threat
        self.eventDescription = event_description  # Variant or other descriptor of event type
        self.fileName = file_name  # Path to file exhibiting malicious behavior
        self.externalUrl = external_url  # External page containing additional information about event
        self.src = src  # IP/Host of the infected computer/device that was patient 0 for the event

    def validate_request(self):
        super(self)
        if self.deviceId is None:
            raise Exception('Invalid event request, device ID is missing')
