from vodafonem2m.vodafonem2m import VodafoneM2M


class M2MUsers(VodafoneM2M):
    """
    The M2MUsers class is specifically designed for applications to retrieve list of
    users, to retrieve individual user details, to update user details and to
    create new users.

    BaseClass : VodafoneM2M
    """

    home = 'users'
    scope = "M2M_USERS_ALL"

    def create_user(self,
                    username,
                    fullname,
                    access_rights,
                    password,
                    email=None,
                    address1=None,
                    address2=None,
                    address3=None,
                    address4=None,
                    address5=None,
                    telephone1=None,
                    telephone2=None
                    ):
        """
        Creates a new user details in the Global M2M Services Platform.

        :param username:
        :param fullname:
        :param access_rights:
        :param password:
        :param email: (optional)
        :param address1: (optional)
        :param address2: (optional)
        :param address3: (optional)
        :param address4: (optional)
        :param address5: (optional)
        :param telephone1: (optional)
        :param telephone2: (optional)
        :return:

            {'createUser': {
                'return': {
                    returnCode': {
                        'majorReturnCode': '000',
                        'minorReturnCode': '0000'
                        }
                    }
                }
            }

        """
        endpoint = "/m2m/v1/users"
        post_data = {
            "userName": username,
            "fullName": fullname,
            "emailAddress": email,
            "addressLine1": address1,
            "addressLine2": address2,
            "addressLine3": address3,
            "addressLine4": address4,
            "addressLine5": address5,
            "telephone1": telephone1,
            "telephone2": telephone2,
            "accessRights": access_rights,
            "password": password
        }
        data = {'user': dict((k, v) for k, v in post_data.items() if v is not None)}
        return self._send_message('post', endpoint, data=data)

    def get_user_details(self, username):
        """
        Retrieves user detailed information stored on the Global M2M Services Platform.

        :param username:
        :return:

             {'getUserDetailsResponse': {'return': {'returnCode': {'majorReturnCode': '000',
                'minorReturnCode': '0000'},
                'userInfo': {'userName': 'RoboCop',
                'fullName': 'Alex Murphy',
                'emailAddress': 'robocop@hollywood.com',
                'addressLine1': '100 Dystopia St',
                'addressLine2': 'Michigan',
                'addressLine3': 'Detroit',
                'telephone1': 12131322,
                'accessRights': 'R'}}}}

        """
        endpoint = "/m2m/v1/users/{username}".format(username=username)
        return self._send_message('get', endpoint)

    def get_user_list(self, page_size=None, page_number=None):
        """
        Retrieves a list of users stored on the Global M2M Services Platform.

        :param page_size:
        :param page_number:
        :return:

            {'getUserListResponse': {'return': {'returnCode': {'majorReturnCode': '000',
                'minorReturnCode': '0000'},
               'matchedResults': 3,
               'userList': {'user': [{'userName': 'KIT_1982',
                  'fullName': ' William Daniels'},
                 {'userName': 'RoboCop', 'fullName': 'Peter Weller'},
                 {'userName': 'tic_tac_toe', 'fullName': 'Mathew Broderick'}]}}}}

        """
        endpoint = "/m2m/v1/users/list"
        params_data = {
            "pageSize": page_size,
            "pageNumber": page_number,
        }
        params = dict((k, v) for k, v in params_data.items() if v is not None)
        if not params:
            params = None
        return self._send_message('get', endpoint, params=params)

    def set_user_details(self,
                         username,
                         fullname=None,
                         access_rights=None,
                         password=None,
                         email=None,
                         address1=None,
                         address2=None,
                         address3=None,
                         address4=None,
                         address5=None,
                         telephone1=None,
                         telephone2=None
                         ):
        """
        Updates the user details in the Global M2M Services Platform.

        :param username:
        :param fullname:
        :param access_rights:
        :param password:
        :param email:
        :param address1:
        :param address2:
        :param address3:
        :param address4:
        :param address5:
        :param telephone1:
        :param telephone2:
        :return:

            {'setUserDetailsResponse': {
                'return': {
                    returnCode': {
                        'majorReturnCode': '000',
                        'minorReturnCode': '0000'
                        }
                    }
                }
            }

        """
        endpoint = "/m2m/v1/users/{username}".format(username=username)
        put_data = {
            "userName": username,
            "fullName": fullname,
            "emailAddress": email,
            "addressLine1": address1,
            "addressLine2": address2,
            "addressLine3": address3,
            "addressLine4": address4,
            "addressLine5": address5,
            "telephone1": telephone1,
            "telephone2": telephone2,
            "accessRights": access_rights,
            "password": password
        }
        data = {'user': dict((k, v) for k, v in put_data.items() if v is not None)}
        return self._send_message('put', endpoint, data=data)
