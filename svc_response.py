#! /usr/bin/env python


class svc_response(object):
    def __init__(self, id):
        self.Id = id


class ping(object):
    def __init(self, api_version, build_version, is_debug_mode):
        self.api_version = api_version
        self.build_version = build_version
        self.is_debug_mode = is_debug_mode
