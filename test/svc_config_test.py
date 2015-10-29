#! /usr/bin/env python

from svc_config import svc_config
import unittest


class test_svc_config(unittest.TestCase):

    def test_api_version(self):
        self.assertTrue(svc_config.api_version > 0)


if __name__ == '__main__':
    unittest.main()
