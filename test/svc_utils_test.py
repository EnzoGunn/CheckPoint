#! /usr/bin/env python

import unittest
from ..svc_utils import SvcUtils


obj = {'attr1': 'val1', 'attr2': 'val2'}
objJson = '{"attr2": "val2", "attr1": "val1"}'


class TestSvcUtils(unittest.TestCase):

    def test_serialize_object(self):
        result = SvcUtils.serialize_object(obj)
        self.assertEqual(objJson, result)

    def test_deserialize_object(self):
        result = SvcUtils.deserialize_object(objJson)
        self.assertEqual(obj, result)

    def test_error_message(self):
        error = 'Invalid request input'
        error_args = {'Key': '123'}
        error_message = 'Invalid request input - Key: 123'
        result = SvcUtils.error_message(error, error_args)
        self.assertEqual(error_message, result)

    def test_regex_validate(self):
        regex = '[0-9]{2}-[a-f]{2}'
        valid_argument = '12-ab'
        invalid_argument = '123-ab'
        result = SvcUtils.regex_validate(regex, valid_argument)
        self.assertTrue(result)
        result = SvcUtils.regex_validate(regex, invalid_argument)
        self.assertFalse(result)

    def test_validate_timestamp(self):
        valid_timestamp = '2015-11-03T14:34:25Z'
        invalid_timestamp = '2015-13-03T14:34:25Z'
        malformatted_timestamp = '11-2015/03T24:24:24'
        result = SvcUtils.validate_timestamp(valid_timestamp)
        self.assertTrue(result)
        result = SvcUtils.validate_timestamp(invalid_timestamp)
        self.assertFalse(result)
        result = SvcUtils.validate_timestamp(malformatted_timestamp)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
