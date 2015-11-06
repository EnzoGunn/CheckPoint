#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
from flask.ext.api import status
from service import Service
from svc_config import SvcConfig
from svc_error import SvcError
from svc_utils import SvcUtils

app = Flask(__name__)


@app.route('/v{0:.1f}/admin/status'.format(SvcConfig.api_version), methods=['GET', 'OPTIONS'])
def ping():
    try:
        svc = Service()
        svc_response = svc.ping()
        return SvcUtils.handle_response(status.HTTP_200_OK, svc_response)
    except Exception as ex:
        return SvcError.handle_error(ex)

@app.route('/v{0:.1f}/events'.format(SvcConfig.api_version), methods=['POST', 'OPTIONS'])
def process_event():
    try:
        svc = Service()
        svc.process_event(request.data)
        return SvcUtils.handle_response(status.HTTP_200_OK)
    except Exception as ex:
        return SvcError.handle_error(ex)
