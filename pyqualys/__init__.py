# -*- coding: utf-8 -*-
import importlib
from .utils.session import APISession

class QualysAPI(object):

    def __init__(self, username=None, password=None, host=None):
        self.services = ["vulnerability"]
        if not username or not password:
            print("Error: username or password missing.")
        elif not host:
            print("Error: host parameter is missing.")
        # super().__init__(username=username, password=password, host=host)
        self.__session = APISession(username=username, password=password, host=host)

    def list_services(self):
        return self.services

    def service(self, service_name):
        if service_name not in self.services:
            print("{} Service is not available.".format(service_name))

        s = "pyqualys.services.{0}".format(service_name)
        Service = getattr(importlib.import_module(s), "Service")
        return Service(self.__session)

