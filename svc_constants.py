#! /usr/bin/env python


class SvcConstants(object):
    # configuration keys
    API_VERSION_KEY = 'apiVersion'
    LOG_MESSAGE_FORMAT_KEY = 'logMessageFormat'
    IS_DEBUG_MODE_KEY = 'isDebugMode'
    INCLUDE_JSON_METADATA_KEY = 'includeJsonMetadata'
    HTTP_PORT_NUMBER_KEY = 'httpPortNumber'
    HOST_KEY = 'host'
    SP_INTEGRATION_URL_KEY = 'securityPlatformIntegrationUrl'
    URI_VALIDATION_REGEX_KEY = 'uriValidationRegex'
    DATETIME_FORMAT_KEY = 'dateTimeFormat'
    UUID_VALIDATION_REGEX_KEY = 'uuidValidationRegex'
    IP_V4_VALIDATION_REGEX_KEY = 'ipv4ValidationRegex'
    IP_V6_VALIDATION_REGEX_KEY = 'ipv6ValidationRegex'
    # default values
    LOG_MESSAGE_FORMAT = '[%(asctime)s UTC] %(levelname)s: %(message)s'
    IS_DEBUG_MODE = False
    INCLUDE_JSON_METADATA = False
    HTTP_PORT_NUMBER = 5000
    HOST = '127.0.0.1'
    URI_VALIDATION_REGEX = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
    UUID_VALIDATION_REGEX = '^[0-9A-Fa-f]{8}(-[0-9A-Fa-f]{4}){3}-[0-9A-Fa-f]{12}$'
    IP_V4_VALIDATION_REGEX = '^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
    IP_V6_VALIDATION_REGEX = '^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$'
