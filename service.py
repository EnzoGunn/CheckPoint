#! /usr/bin/env python

from datetime import datetime
from flask.ext.api import status
from model import Event, EventExtended
from svc_config import SvcConfig
from svc_error import SvcException
from svc_request import EventRequest, EventExtendedRequest
from svc_response import PingDto
from svc_utils import SvcUtils
import requests

logger = SvcUtils.get_logger(__name__)


class Service(object):
    def ping(self):
        ping = PingDto(SvcConfig.api_version, SvcUtils.get_build_version(), SvcConfig.is_debug_mode)
        return ping

    def process_event(self, request):
        if request is None or request == '':
            raise SvcException('invalid event request, no valid request was submitted')
        request_dict = SvcUtils.deserialize_object(request)

        try:
            event_request_obj = SvcUtils.get_obj_from_dict(request_dict, 'EventRequest')

            if 'disableDstSafeguards' in request_dict.keys():
                event_request = EventExtendedRequest(event_request_obj.customerKey, event_request_obj.deviceId, event_request_obj.deviceVersion, event_request_obj.dstUrl, event_request_obj.eventTime, event_request_obj.disableDstSafeguards, event_request_obj.dstIp, event_request_obj.eventSeverity, event_request_obj.eventType, event_request_obj.eventDescription, event_request_obj.fileName, event_request_obj.externalUrl, event_request_obj.src)
            else:
                event_request = EventRequest(event_request_obj.customerKey, event_request_obj.deviceId, event_request_obj.deviceVersion, event_request_obj.dstUrl, event_request_obj.eventTime)
        except:
            raise SvcException(SvcUtils.error_message('invalid event request, request is not valid', {'request': request_dict}))

        # validate request
        event_request.validate_request()
        # forward request to security platform
        if type(event_request) == EventRequest:
            request_body = Event(alert_time=datetime.utcnow(), device_id=event_request.device_id, device_version=event_request.device_version, dst_domain=SvcUtils.get_domain_from_url(event_request.dstUrl), dst_url=event_request.dst_url, event_time=event_request.event_time, protocol_version=SvcConfig.protocol_version, provider_name=SvcConfig.provider_name)
        else:
            request_body = EventExtended(alert_time=datetime.utcnow(), device_id=event_request.device_id, device_version=event_request.device_version, dst_domain=SvcUtils.get_domain_from_url(event_request.dstUrl), dst_url=event_request.dst_url, event_time=event_request.event_time, protocol_version=SvcConfig.protocol_version, provider_name=SvcConfig.provider_name, event_request.disable_dst_safeguards, event_request.dst_ip, event_request.event_severity, event_request.event_type, event_request.event_description, event_request.event_hash, event_request.file_name, event_request.file_hash, event_request.external_url, event_request.src)

        http_headers = {'Content-Type':'application/json'}
        url_params = {'customerKey': event_request.customerKey}
        http_response = requests.post(SvcConfig.sp_integration_url, headers=http_headers, params=url_params, data=request_body)

        # handle non-200 responses
        if http_response.status_code >= status.HTTP_300_MULTIPLE_CHOICES:
            if http_response.status_code == status.HTTP_403_FORBIDDEN:
                raise SvcException(http_response.content)
            if http_response.status_code == status.HTTP_403_FORBIDDEN:
                raise SvcException('unauthorized access attempt')
            elif http_response.status_code == status.HTTP_404_NOT_FOUND:
                raise KeyError(SvcUtils.error_message('security platform client not found', {'customer key': event_request.customerKey}))
            else:
                raise Exception()
