# -*- coding: utf-8 -*-
import logging
from ...utils import util
logger = logging.getLogger(__name__)


class UserHandler:

    def __init__(self, session, api_version, urls_map):
        self.session = session
        self.user_urls_map = urls_map
        self.acceptEULA = False
        super(UserHandler, self).__init__()

    def __get_obj(self, parameter={}, user_list=False, format="json"):

        if user_list:
            uri = self.user_urls_map.user_list
        else:
            uri = self.user_urls_map.user
        resp = self.session.post(uri, parameter)
        if format == "xml":
            return resp.text
        return util.decode_xml(resp.text)

    # @property
    # def verifyEULA(self):
    #     return self.acceptEULA

    # @verifyEULA.setter
    # def verifyEULA(self, user):
    #     print(user)

    def activate_user(self, username):
        parameter = {"action": "activate", "login": username}
        return self.__get_obj(parameter)

    def deactivate_user(self, username):
        parameter = {"action": "deactivate", "login": username}
        return self.__get_obj(parameter)

    def add_user(self, **parameter):
        """
        Create new user and became part of a given service.

        :param parameter: contain the user information.
        :type parameter: dict

        :parameter
        {
            'first_name': 'fname',
            'last_name': 'lname',
            'title': 'My Title',
            'phone': '012345689',
            'fax': '022',
            'email': 'fname@company.com',
            'address1': 'Panchshil Tech Park',
            'address2': 'Shivaji Nagar',
            'city': 'Pune',
            'country': 'India',
            'state': 'Maharashtra',
            'zip_code': 411022,
            'external_id': 101,

            'send_email': 0,

            'user_role': 'scanner',
            'business_unit': 'aa',
            'asset_group': 'grp1, grp2',
            'ui_interface_style': 'navy_blue',
        }
        """
        acceptEULA = False
        parameter["action"] = "add"
        response = self.__get_obj(parameter)
        if acceptEULA:
            logger.info(response)
        return response

    def edit_user(self, **parameter):
        """
        Update the user details.

        :param parameter: contain the updated user filed.
        :type parameter: dict
        """
        parameter["action"] = "edit"
        if "login" not in parameter:
            logger.error("Please pass login id.")
            return
        return self.__get_obj(**parameter)

    def get_users(self):
        """
        Return list of users.
        """
        return self.__get_obj(user_list=True, format="xml")

    def search_user(self, query):
        """
        Find the user by the help of given query.

        :param query: multiple search terms in one string.
                    username=qualys* AND ip=10.*
        :param query: string
        """
        pass

    def delete_user(self, username, force=True):
        """
        Delete the user from records.

        :param username: username of user.
        :type username: string

        :param force: clean all user informations.
        :type force: bool
        """
