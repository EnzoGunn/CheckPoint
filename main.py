#! /usr/bin/env python

import controller
import sys
from data_access import DataAccess
from service import Service
from svc_config import SvcConfig

if __name__ == '__main__':

    controller.app.run(host=SvcConfig.host, debug=SvcConfig.is_debug_mode, port=SvcConfig.http_port_number)
