# -*- coding: utf-8 -*-
import importlib
from .session import APISession

class QualysAPI(object):

    def __init__(self, **kwargs):
        self.services = ["vulnerability"]
        username = kwargs.get("username")
        password = kwargs.get("password")
        host = kwargs.get("host")
        if not username or not password:
            print("Error: username or password missing.")
        elif not host:
            print("Error: host parameter is missing.")
        self.__session = APISession(**kwargs)

    def list_services(self):
        return self.services

    def service(self, service_name):
        if service_name not in self.services:
            print("{} Service is not available.".format(service_name))

        s = "pyqualys.services.{0}".format(service_name)
        Service = getattr(importlib.import_module(s), "VulnerabilityService")
        return Service(self.__session)

