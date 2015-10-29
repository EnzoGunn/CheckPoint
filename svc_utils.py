#! /usr/bin/env python

import jsonpickle
import logging
import os
import time
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper
from logging.handlers import TimedRotatingFileHandler
from svc_config import SvcConfig
from svc_constants import SvcConstants


class SvcUtils(object):

    @staticmethod
    def serialize_object(obj):
        return jsonpickle.encode(obj, unpicklable=SvcConfig.include_json_metadata)

    @staticmethod
    def deserialize_object(obj):
        return jsonpickle.decode(obj)

    @staticmethod
    def get_logger(class_name):
        logging.Formatter.converter = time.gmtime
        log_level = logging.DEBUG if SvcConfig.is_debug_mode else logging.WARNING
        logging.basicConfig(format=SvcConfig.logMessageFormat, level=log_level, datefmt=SvcConstants.DATETIME_FORMAT)
        logger = logging.getLogger(class_name)

        if not SvcConfig.is_debug_mode:
            if not os.path.exists(SvcConstants.LOG_FILE_FOLDER):
                os.makedirs(SvcConstants.LOG_FILE_FOLDER)
            handler = TimedRotatingFileHandler(filename=SvcConstants.LOG_FILE_PATH, when='midnight', utc=True)
            handler.suffix = '%Y-%m-%d.log'
            handler.mode = 'a'
            handler_formatter = logging.Formatter(fmt=SvcConfig.logMessageFormat, datefmt=SvcConstants.DATETIME_FORMAT)
            handler.setFormatter(handler_formatter)
            logger.addHandler(handler)

        return logger

    @staticmethod
    def error_message(error_source, args):
        return '{0} - '.format(error_source) + ', '.join('{0}: {1}'.format(key, str(value)) for key, value in args.items())
