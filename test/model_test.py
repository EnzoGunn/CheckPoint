#! /usr/bin/env python

from model import event
import unittest


class test_event(unittest.TestCase):
    def test_event_model(self):
        alertTime = "2013-02-08T11:14:26.0Z"
        deviceId = "ba6a59f4-e692-4724-ba36-c28132c761de"
        deviceVersion = "13.7a"
        dstDomain = "internetbadguys.com"
        dstUrl = "http://internetbadguys.com/a-bad-url"
        eventTime = "2013-02-08T09:30:26.0Z"
        protocolVersion = "1.0a"
        providerName = "Security Platform"

        event_obj = event(alertTime, deviceId, deviceVersion, dstDomain, dstUrl, eventTime, protocolVersion, providerName)

        self.assertEqual(alertTime, event_obj.alertTime)
        self.assertEqual(deviceId, event_obj.deviceId)
        self.assertEqual(deviceVersion, event_obj.deviceVersion)
        self.assertEqual(dstDomain, event_obj.dstDomain)
        self.assertEqual(dstUrl, event_obj.dstUrl)
        self.assertEqual(eventTime, event_obj.eventTime)
        self.assertEqual(protocolVersion, event_obj.protocolVersion)
        self.assertEqual(providerName, event_obj.providerName)


if __name__ == '__main__':
    unittest.main()