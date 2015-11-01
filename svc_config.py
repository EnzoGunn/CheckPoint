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
    isDebugMode = settings.get(SvcConstants.IS_DEBUG_MODE_KEY, SvcConstants.IS_DEBUG_MODE)
    uri_validation_regex = settings.get(SvcConstants.URI_VALIDATION_REGEX_KEY, SvcConstants.URI_VALIDATION_REGEX)
