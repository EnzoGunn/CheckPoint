#! /usr/bin/env python

from svc_config import SvcConfig
import unittest


class TestSvcConfig(unittest.TestCase):

    def test_api_version(self):
        self.assertTrue(SvcConfig.api_version > 0)


if __name__ == '__main__':
    unittest.main()
