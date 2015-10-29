#! /usr/bin/env python


class SvcConstants(object):
    # configuration keys
    API_VERSION_KEY = 'apiVersion'
    LOG_MESSAGE_FORMAT_KEY = 'logMessageFormat'
    IS_DEBUG_MODE_KEY = 'isDebugMode'
    HTTP_PORT_NUMBER_KEY = 'httpPortNumber'
    HOST_KEY = 'host'
    # default values
    API_VERSION = 1.0
    LOG_MESSAGE_FORMAT = '[%(asctime)s UTC] %(levelname)s: %(message)s'
    IS_DEBUG_MODE = False
    HTTP_PORT_NUMBER = 5000
    HOST = '127.0.0.1'
