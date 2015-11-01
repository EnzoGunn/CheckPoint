#! /usr/bin/env python

from model import Event, EventDetail
import unittest

alert_time = '2013-02-08T11:14:26.0Z'
device_id = 'ba6a59f4-e692-4724-ba36-c28132c761de'
device_version = '13.7a'
dst_domain = 'internetbadguys.com'
dst_url = 'http://internetbadguys.com/a-bad-url'
event_time = '2013-02-08T09:30:26.0Z'
protocol_version = '1.0a'
provider_name = 'Security Platform'
disable_dst_safeguards = True
dst_ip = '8.8.8.8'
event_severity = 'Severe'
event_type = 'Cryptolocker'
event_description = 'Win32/Crilock.A'
event_hash = 'd41d8cd98f00b204e9800998ecf8427e'
file_name = '%AppData%RoamingMicrosoftWindowsTemplatesrandom.exe'
file_hash = 'da39a3ee5e6b4b0d3255bfef95601890afd80709'
external_url = 'http://groogle.com/malware.html'
src = '192.168.100.101'


class TestEvent(unittest.TestCase):

    def test_event_model(self):
        event_obj = Event(alert_time, device_id, device_version, dst_domain, dst_url, event_time, protocol_version, provider_name)

        self.assertEqual(alert_time, event_obj.alertTime)
        self.assertEqual(device_id, event_obj.deviceId)
        self.assertEqual(device_version, event_obj.deviceVersion)
        self.assertEqual(dst_domain, event_obj.dstDomain)
        self.assertEqual(dst_url, event_obj.dstUrl)
        self.assertEqual(event_time, event_obj.eventTime)
        self.assertEqual(protocol_version, event_obj.protocolVersion)
        self.assertEqual(provider_name, event_obj.providerName)

    def test_event_extended_model(self):
        event_detail_obj = EventDetail(alert_time, device_id, device_version, dst_domain, dst_url, event_time, protocol_version, provider_name)

        self.assertEqual(alert_time, event_detail_obj.alertTime)
        self.assertEqual(device_id, event_detail_obj.deviceId)
        self.assertEqual(device_version, event_detail_obj.deviceVersion)
        self.assertEqual(dst_domain, event_detail_obj.dstDomain)
        self.assertEqual(dst_url, event_detail_obj.dstUrl)
        self.assertEqual(event_time, event_detail_obj.eventTime)
        self.assertEqual(protocol_version, event_detail_obj.protocolVersion)
        self.assertEqual(provider_name, event_detail_obj.providerName)
        self.assertEqual(disable_dst_safeguards, event_detail_obj.disableDstSafeguards)
        self.assertEqual(dst_ip, event_detail_obj.dstIp)
        self.assertEqual(event_severity, event_detail_obj.eventSeverity)
        self.assertEqual(event_type, event_detail_obj.eventType)
        self.assertEqual(event_description, event_detail_obj.eventDescription)
        self.assertEqual(event_hash, event_detail_obj.eventHash)
        self.assertEqual(file_name, event_detail_obj.fileName)
        self.assertEqual(file_hash, event_detail_obj.fileHash)
        self.assertEqual(external_url, event_detail_obj.externalUrl)
        self.assertEqual(src, event_detail_obj.src)


if __name__ == '__main__':
    unittest.main()