#! /usr/bin/env python

from ..svc_request import EventRequest, EventExtendedRequest
import unittest

customer_key = 'bf56bb78-6df8-4eb3-8696-2e59a5e3a2aa'
device_id = 'ID 123'
device_version = 'Version 123'
dst_url = 'https://www.badguys.com/badpage.html'
event_time = '2015-11-03T14:00:00Z'
disable_dst_safeguards = False
dst_ip = '127.0.0.1'
event_severity = 'high'
event_type = 'intrusion'
event_description = 'systems compromised by malware'
file_name = 'badprocess.exe'
external_url = 'https://www.badguys.com/badpage.html'
src = None


class TestEventRequest(unittest.TestCase):

    def test_event_with_no_errors(self):
        event = EventRequest(customer_key, device_id, device_version, dst_url, event_time)
        event.validate_request()
        self.assertEqual(customer_key, event.customer_key)
        self.assertEqual(device_id, event.device_id)
        self.assertEqual(device_version, event.device_version)
        self.assertEqual(dst_url, event.dst_url)
        self.assertEqual(event_time, event.event_time)


if __name__ == '__main__':
    unittest.main()
