#! /usr/bin/env python


class event(object):
    def __init__(self, alertTime, deviceId, deviceVersion, dstDomain, dstUrl, eventTime, protocolVersion, providerName):
        self.alertTime = alertTime # e.g. 2013-02-08T11:14:26.0Z
        self.deviceId = deviceId # e.g.ba6a59f4-e692-4724-ba36-c28132c761de
        self.deviceVersion = deviceVersion # e.g.13.7a
        self.dstDomain = dstDomain # e.g.internetbadguys.com
        self.dstUrl = dstUrl # e.g.http://internetbadguys.com/a-bad-url
        self.eventTime = eventTime # e.g.2013-02-08T09:30:26.0Z
        self.protocolVersion = protocolVersion # e.g.1.0a
        self.providerName = providerName # e.g.Security Platform
