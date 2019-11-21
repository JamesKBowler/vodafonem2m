# GNU GENERAL PUBLIC LICENSE
# Author: James Bowler
# vodafonem2m.py
# 30/10/2019


from datetime import datetime

import requests


class VodafoneM2M:
    """
    Provides access to Vodafone M2M endpoints via the REST API.
    All requests default to the production `api_url`: 'https://api.m2m.vodafone.com'.
    Attributes:
        url (str): The api url for this client instance to use.
        session (requests.Session): Persistent HTTP connection object.
    """

    token = None
    home = None
    scope = None

    def __init__(self, username, password, client_id, client_secret,
                 api_url="https://api.m2m.vodafone.com"):
        """
        Create an instance of the VodafoneM2M class.

        :param username: (str): The users username.
        :param password: (str): The users password.
        :param client_id: (str): Application Consumer Key obtained from your operator.
        :param client_secret: (str): Application Consumer Secret obtained from your operator.
        :param api_url: (str) url

        """
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.session = requests.Session()
        self.url = api_url
        self.set_auth_token(username, password)

    def set_auth_token(self, username, password):
        """
        Set the auth token.

        :param username:
        :param password:
        :return:
        """
        headers = {
            'Authorization': "Basic " + base64.standard_b64encode(username+":"+password),
            'Content-Type': "application/x-www-form-urlencoded",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Host': "api.m2m.vodafone.com",
            'Accept-Encoding': "gzip, deflate",
            'Content-Length': "125",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        string = "grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}&scope={scope}"
        data = string.format(client_id=self.__client_id, client_secret=self.__client_secret, scope=self.scope)
        self.token = self._send_message('post', '/m2m/v1/oauth2/access-token', data=data, headers=headers)
        self.token['utc_timestamp'] = datetime.utcnow()

    def get_home_document(self):
        """
        This is the top level resource that returns URIs to all other resources in this API.

        :return:

        {'links': {'self': {'href': 'https://dev-prd.api.m2m.vodafone.com/m2m/v1/devices'},
          'http://a42.vodafone.com/rels/a42/getDeviceDetails': {'href': 'https://dev-prd.api.m2m.vodafone.com/m2m/v1/devices/{deviceId}',
           'method': 'GET',
           'template': 'https://dev-prd.api.m2m.vodafone.com/m2m/v1/devices/{deviceId}',
           'type': 'application/vnd.vodafone.a42.m2m.devices+json'},
          'http://a42.vodafone.com/rels/a42/getDeviceHistoryV2 ': {'href': 'https://dev-prd.api.m2m.vodafone.com/m2m/v1/devices/{deviceId}/history',
           'method': 'GET',
           'template': 'https://dev-prd.api.m2m.vodafone.com/m2m/v1/devices/{deviceId}/history{?startDate,endDate,pageSize,pageNumber}',
           'type': 'application/vnd.vodafone.a42.m2m.devices+json'},
          'http://a42.vodafone.com/rels/a42/getDeviceRegistrationDetails': {'href': 'https://dev-prd.api.m2m.vodafone.com/m2m/v1/devices/{deviceId}/registration',
           'method': 'GET',
           'template': 'https://dev-prd.api.m2m.vodafone.com/m2m/v1/devices/{deviceId}/registration',
           'type': 'application/vnd.vodafone.a42.m2m.devices+json'}}}

        """
        return self._send_message('get', '/m2m/v1/{}'.format(self.home))

    @staticmethod
    def _handle_api_response(json_response):
        """
        Throw exceptions on errors from API.

        :param json_response:
        :return:
        """

        if not json_response:
            raise ValueError('Error getting data from the api, no data returned')
        if "error" in json_response:
            raise ValueError("Standard Error:: {} : {}".format(
                json_response["error"], json_response["error_description"]))
        elif "description" in json_response:
            if "Service Error" in json_response['description']:
                raise ValueError("Service Error:: {} : {}".format(
                    json_response["id"], json_response["description"]))
        else:
            try:
                codes = json_response[list(json_response.keys())[0]]['return']['returnCode']
                if codes['majorReturnCode'] != '000' or codes['minorReturnCode'] != '0000':
                    raise ValueError(
                        "Return Code Error:: Major: {}, Minor: {}".format(
                            codes['majorReturnCode'], codes['minorReturnCode'])
                    )
            except KeyError:
                pass
        return json_response

    def _send_message(self, method, endpoint, params=None, headers=None, data=None):
        """
        Send API request.

        :param method:
        :param endpoint:
        :param params:
        :param headers:
        :param data:
        :return: dict

        """
        if not headers:
            headers = {'Authorization': "Bearer {}".format(self.token['access_token'])}
        url = self.url + endpoint
        r = self.session.request(method, url, data=data,
                                 params=params, headers=headers)
        return self._handle_api_response(r.json())
