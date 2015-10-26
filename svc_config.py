#! /usr/bin/env python

import json
import sys
from svc_constants import svc_constants

# configuration parsing setup
configFilePath = './settings.development.json'

for arg in sys.argv:
    if '.json' in arg:
        configFilePath = arg

with open(configFilePath, 'r') as file:
    settings = json.load(file)


class svc_config(object):
    # required parameters
    
    # optional parameters
