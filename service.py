#! /usr/bin/env python

import datetime
import svc_enums
from svc_config import SvcConfig
from svc_utils import SvcUtils
from svc_response import PingDto
import setup

logger = SvcUtils.get_logger(__name__)


class Service(object):
    def ping(self):
        ping = PingDto(SvcConfig.api_version, setup.get('version'))
        return ping

    def process_request(self):
        self.test = 1
