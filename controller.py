#! /usr/bin/env python
# -*- coding: utf-8 -*-

import status as status
import jsonpickle
from data_access import data_access
from flask import Flask, request, make_response
from flask.ext.api import status
from service import service
from svc_config import svc_config
from svc_utils import svc_utils
from svc_response import Error

app = Flask(__name__)


@app.route('/{0:.1f}/admin/status'.format(svc_config.api_version), methods=['GET', 'OPTIONS'])
@svc_utils.crossdomain(origin='*', methods=['PATCH', 'OPTIONS'], headers=['Content-Type', 'Authorization'])
def ping():
    svc = service()
    ping = svc.ping()
    ping_response = svc_utils.serialize_object(ping)

    svc_response = make_response(ping_response)
    svc_response.mimetype = 'application/json'
    svc_response.status_code = status.HTTP_200_OK
    return svc_response


@app.route('/{0:.1f}/events/<customer_id>'.format(svc_config.api_version), methods=['POST', 'OPTIONS'])
@svc_utils.crossdomain(origin='*', methods=['PATCH', 'OPTIONS'], headers=['Content-Type', 'Authorization'])
def device_registration(event_id):
    if request.data is None or request.data == '':
        error = Error('No request was submitted')
        error_response = svc_utils.serialize_object(error)
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
            error_response = svc_utils.serialize_object(error)
            svc_response = make_response(error_response)
            svc_response.mimetype = 'application/json'
            svc_response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

            return svc_response
