#! /usr/bin/env python


class SvcConstants(object):
    # configuration keys
    API_VERSION_KEY = 'apiVersion'
    LOG_MESSAGE_FORMAT_KEY = 'logMessageFormat'
    IS_DEBUG_MODE_KEY = 'isDebugMode'
    HTTP_PORT_NUMBER_KEY = 'httpPortNumber'
    HOST_KEY = 'host'
    SP_INTEGRATION_URL_KEY = 'securityPlatformIntegrationUrl'
    URI_VALIDATION_REGEX_KEY = 'uriValidationRegex'
    # default values
    LOG_MESSAGE_FORMAT = '[%(asctime)s UTC] %(levelname)s: %(message)s'
    IS_DEBUG_MODE = False
    HTTP_PORT_NUMBER = 5000
    HOST = '127.0.0.1'
    URI_VALIDATION_REGEX = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
