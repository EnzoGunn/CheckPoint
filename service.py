#! /usr/bin/env python

import datetime
import svc_enums
from model import model
from svc_config import svc_config
from svc_utils import svc_utils
from response import response

logger = svc_utils.get_logger(__name__)


class service(object):
