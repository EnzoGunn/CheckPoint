#! /usr/bin/env python

import json
import sys
from svc_constants import SvcConstants

# configuration parsing setup
configFilePath = './settings.development.json'

for arg in sys.argv:
    if '.json' in arg:
        configFilePath = arg

with open(configFilePath, 'r') as file:
    settings = json.load(file)


class SvcConfig(object):
    # required parameters
    api_version = settings.get(SvcConstants.API_VERSION_KEY)
    sp_integration_url = settings.get(SvcConstants.SP_INTEGRATION_URL_KEY)
    # optional parameters
    host = settings.get(SvcConstants.HOST_KEY, SvcConstants.HOST)
    http_port_number = settings.get(SvcConstants.HTTP_PORT_NUMBER_KEY, SvcConstants.HTTP_PORT_NUMBER)
    include_json_metadata = settings.get(SvcConstants.INCLUDE_JSON_METADATA_KEY, SvcConstants.INCLUDE_JSON_METADATA)
    is_debug_mode = settings.get(SvcConstants.IS_DEBUG_MODE_KEY, SvcConstants.IS_DEBUG_MODE)
    log_message_format = settings.get(SvcConstants.LOG_MESSAGE_FORMAT_KEY, SvcConstants.LOG_MESSAGE_FORMAT)
    uri_validation_regex = settings.get(SvcConstants.URI_VALIDATION_REGEX_KEY, SvcConstants.URI_VALIDATION_REGEX)
    datetime_format = settings.get(SvcConstants.DATETIME_FORMAT_KEY, SvcConstants.DATETIME_FORMAT)
    uuid_validation_regex = settings.get(SvcConstants.UUID_VALIDATION_REGEX_KEY, SvcConstants.UUID_VALIDATION_REGEX)
    ipv4_validation_regex = settings.get(SvcConstants.IP_V4_VALIDATION_REGEX_KEY, SvcConstants.IP_V4_VALIDATION_REGEX_KEY)
    ipv6_validation_regex = settings.get(SvcConstants.IP_V6_VALIDATION_REGEX_KEY, SvcConstants.IP_V6_VALIDATION_REGEX_KEY)
