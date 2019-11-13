from vodafonem2m.vodafonem2m import VodafoneM2M


class M2MNetwork(VodafoneM2M):
    home = 'network'
    scope = "M2M_NETWORK_ALL"

    def get_sim_details(self, sim_id, sim_id_type):
        """
        This API is provided to allow Customer Systems to retrieve detailed
        information for a specific SIM, identified by its simId, which can
        be "IMSI" or "ICCID". The information returned will be a fixed set
        of named fields of the sim data type followed by a
        deviceInformationItem list of SIM information items of
        name/type/value triplets containing information relating to the SIM
        The list of SIM information items is subject to change; items will
        be added to this list, but will never be removed.

        :param sim_id:
        :param sim_id_type:
        :return: dict

        """
        endpoint = "/m2m/rest/v1/network/sim"
        params = {"simId": sim_id, "simIdType": sim_id_type}
        return self._send_message('get', endpoint, params=params)

    def set_sim_details(self, sim_id, sim_id_type, customer_service_profile=None, state=None, imei=None):
        """
        Update the details from a certain SIM.
        Note:
        • In a single invocation only one of customerServiceProfile or state may be changed.
        • baseCountry can only be changed if the customerServiceProfile does not have a base country set.
        • only one of stateChangeReason or stateChangeReasonOther may be provided.

        :param sim_id: (str)
        :param sim_id_type: (str)
        :param customer_service_profile: Up to 32 (str)
            Customer Service Profile
        :param state: (str)
            The new state to set. Only one of either state or customerServiceProfile
            may be changed at any one time, as changing the customerServiceProfile
            changes the state of the device.
                Available states:
                    T - Active.Test
                    R - Active.Ready
                    A - Active.Live
                    S - Active.Suspend
                    U - Active.Standby
                    C - Active.Sleep
                    D - Inactive.Stopped
        :param imei: Up to 16 (str)/(int)

        :return:

        {"setSimDetailsResponse":
            {"return": {
                "returnCode": {
                    "majorReturnCode":000,
                    "minorReturnCode":0000
                }
            }
        }

        """
        endpoint = "/m2m/rest/v1/sim"
        params_data = {
            "simId": sim_id,
            "simIdType": sim_id_type,
            "customerServiceProfile": customer_service_profile,
            "State": state
        }
        data = {"setSimDetails": dict((k, v) for k, v in params_data.items() if v is not None)}
        return self._send_message('put', endpoint, data=data)

    def get_sim_details_v2(self, sim_id, sim_id_type):
        """
        This API is provided to allow Customer Systems to retrieve detailed
        information for a specific SIM, identified by its simId, which can
        be "IMSI" or "ICCID". The information returned will be a fixed set
        of named fields of the sim data type followed by a
        deviceInformationItem list of SIM information items of
        name/type/value triplets containing information relating to the SIM
        The list of SIM information items is subject to change; items will
        be added to this list, but will never be removed.

        :param sim_id:
        :param sim_id_type:
        :return: dict

        """
        endpoint = "/m2m/rest/v2/network/sim"
        params = {"simId": sim_id, "simIdType": sim_id_type}
        return self._send_message('get', endpoint, params=params)

    def set_sim_details_v2(self, sim_id, sim_id_type, customer_service_profile=None, state=None, imei=None):
        """
        Update the details from a certain SIM.
        Note:
        • In a single invocation only one of customerServiceProfile or state may be changed.
        • baseCountry can only be changed if the customerServiceProfile does not have a base country set.
        • only one of stateChangeReason or stateChangeReasonOther may be provided.

        :param sim_id:
        :param sim_id_type:
        :param customer_service_profile:
        :param state:
        :param imei:
        :return:

        {"setSimDetailsResponseV2":
            {"return": {
                "returnCode": {
                    "majorReturnCode":000,
                    "minorReturnCode":0000
                }
            }
        }

        """
        endpoint = "/m2m/rest/v2/network/sim"
        params_data = {
            "simId": sim_id,
            "simIdType": sim_id_type,
            "customerServiceProfile": customer_service_profile,
            "State": state,
            "imei": imei
        }
        data = {"setSimDetailsV2": dict((k, v) for k, v in params_data.items() if v is not None)}
        return self._send_message('put', endpoint, data=data)

    def get_access_list(self,
                        access_list_type='sms',
                        hierarchy_flag=None,
                        access_list_id=None,
                        customer_id=None,
                        access_list_name=None,
                        page_number=None,
                        page_size=None,
                        sort_field=None,
                        sort_field_order_direction=None):
        """
        This service retrieves the Access Control Lists (ACL). The Access Control Lists
        allows to configure blacklist/whitelist incoming/outgoing MSISDNs. The Access
        Control Lists can be linked to a Customer Service Profile, which will enforce
        its configuration to all SIMs underneath it (only for the SMS feature).

        The Access Control Lists can be linked to a device (SIM), which will enforce
        its configuration to that SIM only (for both Voice and SMS feature).

        :param access_list_type:
        :param hierarchy_flag:
        :param access_list_id:
        :param customer_id:
        :param access_list_name:
        :param page_number:
        :param page_size:
        :param sort_field:
        :param sort_field_order_direction:
        :return:

        {'getAccessListResponse': {'return': {'accessList': {'accessListDesc': 'TestingAccessList1',
            'accessListId': 100001600,
            'accessListName': 'TestingAccessList1',
            'customerId': 112004260,
            'numberLinkedCSP': 0,
            'numberLinkedSims': 0,
            'profileInUseFlag': 'N',
            'updatedAt': '2017-03-03T09:10:00+00:00',
            'updatedByUserId': 10002408670},
           'accessListLength': 1,
           'accessListTableLength': 1,
           'returnCode': {'majorReturnCode': '000', 'minorReturnCode': '0000'}}}}

        """
        endpoint = "/m2m/rest/v1/network/access_list/{access_list_type}".format(access_list_type=access_list_type)
        params_data = {
            "accessListType": access_list_type,
            "hierarchyFlag": hierarchy_flag,
            "accessListId":access_list_id,
            "customerId": customer_id,
            "accessListName": access_list_name,
            "pageNumber": page_number,
            "pageSize": page_size,
            "sortField": sort_field,
            "sortFieldOrderDirection": sort_field_order_direction
        }
        params = dict((k, v) for k, v in params_data.items() if v is not None)
        return self._send_message('get', endpoint, params=params)

    def create_access_list(self,
                           customer_id,
                           access_list_name,
                           access_member_list,
                           access_list_desc=None,
                           access_list_type='sms',
                           apn_profile_id=None):
        """

        :param customer_id:
        :param access_list_name:
        :param access_member_list:
        :param access_list_desc:
        :param access_list_type:
        :param apn_profile_id:
        :return:

        {'createAccessListResponse': {'return': {'accessListId': 100001600,
           'returnCode': {'majorReturnCode': '000', 'minorReturnCode': '0000'}}}}

        """
        endpoint = "/m2m/rest/v1/network/access_list/{access_list_type}".format(access_list_type=access_list_type)
        # access_member_list = TODO
        post_data = {
            "customerId": customer_id,
            "accessListName": access_list_name,
            "accessMemberList": access_member_list,
            "accessListDesc": access_list_desc,
            "accessListType": access_list_type,
            "apnProfileId": apn_profile_id
        }
        data = dict((k, v) for k, v in post_data.items() if v is not None)
        # return self._send_message('post', endpoint, data=data)

    def update_access_list(self,
                           customer_id,
                           access_list_id,
                           access_list_name,
                           access_list_type='sms',
                           access_list_desc=None,
                           access_member_list=None):
        """
        This service updates an Access Control Lists (ACL) and Access Control Members
        List ( Allow or Deny Identifiers). The Access Control Lists allows to configure
        blacklist/whitelist incoming/outgoing MSISDNs.The Access Control Lists can be
        linked to a Customer Service Profile, which will enforce its configuration to all
        SIMs underneath it (only for the SMS feature). The Access Control Lists can b
        linked to a device (SIM), which will enforce its configuration to that SIM only
        (for both Voice and SMS feature). This API will replace accessMemberList.
        If only some accessMemberList are passed on the request the rest of the
        members list will be removed.

        :param customer_id:
        :param access_list_id:
        :param access_list_name:
        :param access_list_type:
        :param access_list_desc:
        :param access_member_list:
        :return:

        {'updateAccessListResponse': {'return': {'accessListId': 100001600,
           'returnCode': {'majorReturnCode': '000', 'minorReturnCode': '0000'}}}}

        """
        endpoint = "/m2m/rest/v1/network/access_list/{access_list_type}".format(access_list_type=access_list_type)
        # access_member_list = TODO
        post_data = {
            "customerId": customer_id,
            "accessListName": access_list_name,
            "accessMemberList": access_member_list,
            "accessListDesc": access_list_desc,
            "accessListType": access_list_type,
            "accessListId": access_list_id
        }
        data = dict((k, v) for k, v in post_data.items() if v is not None)
        # return self._send_message('put', endpoint, data=data)

    def delete_access_list(self,
                               access_list_id,
                               access_list_type='sms'):
        """
        This service deletes an Access Control Lists (ACL) and Access Control
        Members List ( Allow or Deny Identifiers). An Access Control List
        cannot be deleted if it is in use..

        :param access_list_id:
        :param access_list_type:
        :return:

        {'deleteAccessListResponse': {'return': {'accessListId': 100001600,
           'returnCode': {'majorReturnCode': '000', 'minorReturnCode': '0000'}}}}


        """
        endpoint = "/m2m/rest/v1/network/access_list/sms/{access_list_id}".format(access_list_id=access_list_id)
        params_data = {
            "accessListType": access_list_type,
            "accessListId": access_list_id
        }
        params = dict((k, v) for k, v in params_data.items() if v is not None)
        return self._send_message('delete', endpoint, params=params)

    def get_accesslist_members(self,
                               access_list_id,
                               access_list_name=None,
                               access_list_type='sms',
                               access_list_desc=None,
                               access_list_member_id=None,
                               page_number=None,
                               page_size=None,
                               sort_field=None,
                               sort_field_order_direction=None):
        """
        This service retrieves Access Control List member’s information.

        :param access_list_id:
        :param access_list_name:
        :param access_list_type:
        :param access_list_desc:
        :param access_list_member_id:
        :param page_number:
        :param page_size:
        :param sort_field:
        :param sort_field_order_direction:
        :return:

        {'getAccessListMembersResponse': {'return': {'accessListDesc': 'Test2',
           'accessListId': 100001200,
           'accessListName': 'Test',
           'accessListMembers': {'accessListMemberId': 100001210,
            'action': 'A',
            'direction': 'B',
            'identifier': 4466003724,
            'memberUseCounter': 0,
            'updatedAt': '2017-02-15T12:08:32+00:00',
            'updatedByUserId': 100008900},
           'accessListMembersLength': 1,
           'accessListMembersTableLength': 1,
           'returnCode': {'majorReturnCode': '000', 'minorReturnCode': '0000'}}}}

        """
        endpoint = "/m2m/rest/v1/network/access_list/{access_list_type}".format(access_list_type=access_list_type)
        params_data = {
            "accessListType": access_list_type,
            "accessListId": access_list_id,
            "accessList_Desc": access_list_desc,
            "accessListName": access_list_name,
            "accessListMemberId": access_list_member_id,
            "pageNumber": page_number,
            "pageSize": page_size,
            "sortField": sort_field,
            "sortFieldOrderDirection": sort_field_order_direction
        }
        params = dict((k, v) for k, v in params_data.items() if v is not None)
        return self._send_message('get', endpoint, params=params)
