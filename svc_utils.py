#! /usr/bin/env python

import jsonpickle
import logging
import os
import time
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper
from logging.handlers import TimedRotatingFileHandler
from svc_config import svc_config
from svc_constants import svc_constants


class svc_utils(object):

    @staticmethod
    def serialize_object(obj):
        return jsonpickle.encode(obj, unpicklable=svc_config.include_json_metadata)

    @staticmethod
    def deserialize_object(obj):
        return jsonpickle.decode(obj)

    @staticmethod
    def get_logger(class_name):
        logging.Formatter.converter = time.gmtime
        log_level = logging.DEBUG if svc_config.is_debug_mode else logging.WARNING
        logging.basicConfig(format=svc_config.logMessageFormat, level=log_level, datefmt=svc_constants.DATETIME_FORMAT)
        logger = logging.getLogger(class_name)

        if not svc_config.is_debug_mode:
            if not os.path.exists(svc_constants.LOG_FILE_FOLDER):
                os.makedirs(svc_constants.LOG_FILE_FOLDER)
            handler = TimedRotatingFileHandler(filename=svc_constants.LOG_FILE_PATH, when='midnight', utc=True)
            handler.suffix = '%Y-%m-%d.log'
            handler.mode = 'a'
            handler_formatter = logging.Formatter(fmt=svc_config.logMessageFormat, datefmt=svc_constants.DATETIME_FORMAT)
            handler.setFormatter(handler_formatter)
            logger.addHandler(handler)

        return logger

    @staticmethod
    def error_message(error_source, args):
        return '{0} - '.format(error_source) + ', '.join('{0}: {1}'.format(key, str(value)) for key, value in args.items())

    @staticmethod
    def crossdomain(origin=None, methods=None, headers=None, max_age=21600, attach_to_all=True, automatic_options=True):
        if methods is not None:
            methods = ', '.join(sorted(x.upper() for x in methods))
        if headers is not None and not isinstance(headers, basestring):
            headers = ', '.join(x.upper() for x in headers)
        if not isinstance(origin, basestring):
            origin = ', '.join(origin)
        if isinstance(max_age, timedelta):
            max_age = max_age.total_seconds()

        def get_methods():
            if methods is not None:
                return methods

            options_resp = current_app.make_default_options_response()
            return options_resp.headers['allow']

        def decorator(f):
            def wrapped_function(*args, **kwargs):
                if automatic_options and request.method == 'OPTIONS':
                    resp = current_app.make_default_options_response()
                else:
                    resp = make_response(f(*args, **kwargs))
                if not attach_to_all and request.method != 'OPTIONS':
                    return resp

                h = resp.headers

                h['Access-Control-Allow-Origin'] = origin
                h['Access-Control-Allow-Methods'] = get_methods()
                h['Access-Control-Max-Age'] = str(max_age)
                if headers is not None:
                    h['Access-Control-Allow-Headers'] = headers
                return resp

            f.provide_automatic_options = False
            return update_wrapper(wrapped_function, f)

        return decorator

    @staticmethod
    def experimental(func):
        def inner(*args, **kwargs):
            # logging.warn(func.__name__+" has been marked as experimental and should not be used in production")
            return func(*args, **kwargs)

        return inner

    @staticmethod
    def skip(test_case, reason=None):
        def decorator(func):
            def inner(*args, **kwargs):
                if reason:
                    print "\nSkipping %s.%s (reason: %s)" % (test_case, func.__name__, reason)
                else:
                    print "\nSkipping %s.%s" % (test_case, func.__name__)
                return

            return update_wrapper(inner, func)

        return decorator
