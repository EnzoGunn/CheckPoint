#! /usr/bin/env python

from svc_response import PingDto
import unittest

api_version = 1.0
build_version = '1.0.0.0'
is_debug_mode = True


class TestSvcResponse(unittest.TestCase):

    def test_service_status(self):
        ping = PingDto(api_version, build_version, is_debug_mode)

        self.assertEqual(api_version, ping.api_version)
        self.assertEqual(build_version, ping.build_version)
        self.assertTrue(ping.is_debug_mode)


if __name__ == '__main__':
    unittest.main()
