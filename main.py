#! /usr/bin/env python

import controller
import sys
from data_access import data_access
from service import service
from svc_config import svc_config

if __name__ == '__main__':

    controller.app.run(host=svc_config.host, debug=svc_config.is_debug_mode, port=svc_config.http_port_number)
