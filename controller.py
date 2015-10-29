#! /usr/bin/env python
# -*- coding: utf-8 -*-

import status as status
import jsonpickle
from data_access import DataAccess
from flask import Flask, request, make_response
from flask.ext.api import status
from service import Service
from svc_config import SvcConfig
from svc_utils import SvcUtils

app = Flask(__name__)


@app.route('/{0:.1f}/admin/status'.format(SvcConfig.api_version), methods=['GET', 'OPTIONS'])
def ping():
    svc = Service()
    ping = svc.ping()
    ping_response = SvcUtils.serialize_object(ping)

    svc_response = make_response(ping_response)
    svc_response.mimetype = 'application/json'
    svc_response.status_code = status.HTTP_200_OK
    return svc_response


@app.route('/{0:.1f}/events/<customer_id>'.format(SvcConfig.api_version), methods=['POST', 'OPTIONS'])
def device_registration(customer_id):
    if request.data is None or request.data == '':
        error = Error('No request was submitted')
        error_response = SvcUtils.serialize_object(error)
        svc_response = make_response(error_response)
        svc_response.mimetype = 'application/json'
        svc_response.status_code = status.HTTP_400_BAD_REQUEST

        return svc_response
    else:
        try:
            #To-DO: handle requests
            return svc_response

        except Exception as ex:
            error = Error(ex.message)
            error_response = SvcUtils.serialize_object(error)
            svc_response = make_response(error_response)
            svc_response.mimetype = 'application/json'
            svc_response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

            return svc_response
