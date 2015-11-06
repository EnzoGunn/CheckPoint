#! /usr/bin/env python

from svc_config import SvcConfig
from svc_utils import SvcUtils


class EventRequest(object):
    def __init__(self, customer_key, device_id, device_version, dst_url, event_time):
        # a fixed UUID-v4 unique customer key
        self.customerKey = customer_key
        # The ID of the device sending the event
        self.deviceId = device_id
        # Version of device sending the event
        self.deviceVersion = device_version
        # The destination URL encoded, following RFC3986 guidelines
        self.dstUrl = dst_url
        # Time event was detected, must match the following style 2013-02-08T09:30:26Z
        self.eventTime = event_time

    def validate_request(self):
        if self.customerKey is None:
            raise Exception('Invalid event request, customer key is missing')
        if self.deviceId is None:
            raise Exception('Invalid event request, device ID is missing')
        if self.deviceVersion is None:
            raise Exception('Invalid event request, device version is missing')
        if self.dstUrl is None:
            raise Exception('Invalid event request, destination URL is missing')
        if self.eventTime is None:
            raise Exception('Invalid event request, event time (UTC) is missing')
        if SvcUtils.regex_validate(SvcConfig.uuid_validation_regex, self.customerKey) is False:
            error_msg = SvcUtils.error_message('Invalid event request, customer key is invalid', {'customer key': self.customerKey})
            raise ValueError(error_msg)
        if SvcUtils.regex_validate(SvcConfig.uri_validation_regex, self.dstUrl) is False:
            error_msg = SvcUtils.error_message('Invalid event request, destination URL is invalid', {'destination URL': self.dstUrl})
            raise ValueError(error_msg)
        if SvcUtils.validate_timestamp(self.eventTime)is False:
            error_msg = SvcUtils.error_message('Invalid event request, event time is invalid', {'event time': self.eventTime})
            raise ValueError(error_msg)


class EventExtendedRequest(EventRequest):
    def __init__(self, customer_key, device_id, device_version, dst_url, event_time, disable_dst_safeguards, dst_ip, event_severity, event_type, event_description, file_name, external_url, src):
        EventRequest.__init__(self, customer_key, device_id, device_version, dst_url, event_time)
        # Boolean value. 'false' is the same as not providing this field at all
        self.disableDstSafeguards = disable_dst_safeguards
        # The destination IP of the domain, specified in IPv4 dotted-decimal notation. An example would be '8.8.8.8'
        self.dstIp = dst_ip
        # The partner threat level or rating, eg: severe, bad, high, etc.
        self.eventSeverity = event_severity
        # Common name or classification of threat
        self.eventType = event_type
        # Variant or other descriptor of event type
        self.eventDescription = event_description
        # Path to file exhibiting malicious behavior
        self.fileName = file_name
        # External page containing additional information about event
        self.externalUrl = external_url
        # IP/Host of the infected computer/device that was patient 0 for the event
        self.src = src

    def validate_request(self):
        EventRequest.validate_request(self)
        if self.dstIp is not None:
            # first, validation IPv4 format
            if SvcUtils.regex_validate(SvcConfig.ipv4_validation_regex) is False:
                # second, if not IPv4 compliant, validate for IPv6 format
                if SvcUtils.regex_validate(SvcConfig.ipv6_validation_regex) is False:
                    error_msg = SvcUtils.error_message('Invalid event request, destination IP is invalid', {'destination IP': self.dstIp})
                    raise ValueError(error_msg)
        if SvcUtils.regex_validate(SvcConfig.uri_validation_regex, self.externalUrl) is False:
            error_msg = SvcUtils.error_message('Invalid event request, external URL is invalid', {'external URL': self.externalUrl})
            raise ValueError(error_msg)
