from vodafonem2m.vodafonem2m import VodafoneM2M


class M2MDevices(VodafoneM2M):
    home = 'devices'
    scope = "M2M_DEVICES_ALL"

    def get_device_details_v2(self, device_id):
        """
        Retrieves device details information stored on the Global M2M Services Platform.

        :param device_id:
        :return:

        {'getDeviceDetailsv2Response': {'return': {'returnCode': {'majorReturnCode': '000',
           'minorReturnCode': '0000'},
           'deviceId': 204043251458076,
           'customerServiceProfile': 'ADI_CSP_20404_apix',
           'state': 'A',
           'imei': 3569425602473200,
           'baseCountry': 'IN',
           'customAttribute1': 'Y',
           'customAttribute2': 'N',
           'customAttribute3': 'Y',
           'customAttribute4': 'N',
           'customAttribute5': 'Y',
           'deviceInformationList': {'deviceInformationItem': [{'itemName': 'customerOrderNumber',
              'itemType': 'String'},
             {'itemName': 'simProfile',
              'itemType': 'String',
              'itemValue': 'M2MMP0005'},
             {'itemName': 'ragStatus', 'itemType': 'String', 'itemValue': 'R'},
             {'itemName': 'provisioningStatus',
              'itemType': 'String',
              'itemValue': 'B'},
             {'itemName': 'provisionedAtTimestamp',
              'itemType': 'dateTime',
              'itemValue': '2014-10-30T23:37:00+00:00'},
             {'itemName': 'lastChangeTimestamp',
              'itemType': 'dateTime',
              'itemValue': '2015-01-19T13:04:29+00:00'},
             {'itemName': 'simGeofenceAssignmentId',
              'itemType': 'long',
              'itemValue': 0}]}}}}

        """
        endpoint = "/m2m/v1/devices/{device_id}".format(device_id=device_id)
        return self._send_message('get', endpoint)

    def get_device_history_v2(self, device_id, start_date, end_date, page_size, page_number):
        """
        Retrieves device history information stored on the Global M2M Services Platform.

        :param device_id:
        :param start_date:
        :param end_date:
        :param page_size:
        :param page_number:
        :return:

        {'getDeviceHistoryResponse': {'return': {'returnCode': {'majorReturnCode': '000',
            'minorReturnCode': '0000'},
           'matchedResults': 24,
           'deviceHistoryList': {'deviceHistoryItem': [{'timestamp': '2014-12-24T13:21:26+00:00',
              'operation': 'C'},
             {'timestamp': '2014-12-24T12:48:37+00:00', 'operation': 'C'},
             {'timestamp': '2014-12-24T12:48:10+00:00', 'operation': 'C'},
             {'timestamp': '2014-12-24T12:47:55+00:00', 'operation': 'C'},
             {'timestamp': '2014-12-24T12:47:41+00:00', 'operation': 'C'},
             {'timestamp': '2014-12-24T12:47:31+00:00', 'operation': 'C'},
             {'timestamp': '2014-12-24T12:42:20+00:00', 'operation': 'C'},
             {'timestamp': '2014-12-24T12:42:19+00:00', 'operation': 'C'},
             {'timestamp': '2014-12-24T12:41:25+00:00', 'operation': 'C'},
             {'timestamp': '2014-12-24T12:41:25+00:00', 'operation': 'C'}]}}}}

        """
        endpoint = "/m2m/v1/devices/{device_id}/history".format(device_id=device_id)
        params = {'startDate': start_date,
                  'endDate': end_date,
                  'pageSize': page_size,
                  'pageNumber': page_number
                  }
        return self._send_message('get', endpoint, params=params)

    def get_device_registration_details(self, device_id):
        """
        Retrieves detailed mobile network registration information stored on the Global M2M Services Platform.

        :param device_id:
        :return:

        {'getDeviceHistoryResponse': {'return': {'returnCode': {'majorReturnCode': '000',
            'minorReturnCode': '0000'},
           'matchedResults': 24,
           'deviceHistoryList': {'deviceHistoryItem': [{'timestamp': '2014-12-24T13:21:26+00:00',
              'operation': 'C'},
             {'timestamp': '2014-12-24T12:48:37+00:00', 'operation': 'C'},
             {'timestamp': '2014-12-24T12:48:10+00:00', 'operation': 'C'},
             {'timestamp': '2014-12-24T12:47:55+00:00', 'operation': 'C'},
             {'timestamp': '2014-12-24T12:47:41+00:00', 'operation': 'C'},
             {'timestamp': '2014-12-24T12:47:31+00:00', 'operation': 'C'},
             {'timestamp': '2014-12-24T12:42:20+00:00', 'operation': 'C'},
             {'timestamp': '2014-12-24T12:42:19+00:00', 'operation': 'C'},
             {'timestamp': '2014-12-24T12:41:25+00:00', 'operation': 'C'},
             {'timestamp': '2014-12-24T12:41:25+00:00', 'operation': 'C'}]}}}}

        """
        endpoint = "/m2m/v1/devices/{device_id}/registration".format(device_id=device_id)
        return self._send_message('get', endpoint)

    def set_device_details_v4(self,
                           device_id,
                           customer_service_profile,
                           apn_list=None,
                           state=None,
                           imei=None,
                           base_country=None,
                           custom_attribute1=None,
                           custom_attribute2=None,
                           custom_attribute3=None,
                           custom_attribute4=None,
                           custom_attribute5=None,
                           sim_state_change_reason=None,
                           sim_state_change_reason_other=None):
        """
        Updates a restricted set of fields stored in the M2M Service platform for a specific device.

        :param device_id:
        :param customer_service_profile:
        :param apn_list:
        :param state:
        :param imei:
        :param base_country:
        :param custom_attribute1:
        :param custom_attribute2:
        :param custom_attribute3:
        :param custom_attribute4:
        :param custom_attribute5:
        :param sim_state_change_reason:
        :param sim_state_change_reason_other:
        :return:

        {'setDeviceDetailsv4Response': {
            'return': {
                'returnCode': {
                    'majorReturnCode': '000',
                    'minorReturnCode': '0000'
                    }
                }
            }
        }

        """
        endpoint = "/m2m/v1/devices/{device_id}".format(device_id=device_id)
        data = {'deviceId': device_id,
                'customerServiceProfile': customer_service_profile,
                'state': state,
                'imei': imei,
                'baseCountry': base_country,
                'customAttribute1': custom_attribute1,
                'customAttribute2': custom_attribute2,
                'customAttribute3': custom_attribute3,
                'customAttribute4': custom_attribute4,
                'customAttribute5': custom_attribute5,
                'apnList': apn_list,
                'simStateChangeReason': sim_state_change_reason,
                'simStateChangeReasonOther': sim_state_change_reason_other}
        data = dict((k, v) for k, v in data.items() if v is not None)
        return self._send_message('put', endpoint, data=data)

    def set_device_credentials_v2(self,
                               device_id,
                               apn,
                               user_id,
                               password):
        """
        Create a new device credentials record for the customer's IMSI.

        :param device_id:
        :param apn:
        :param user_id:
        :param password:
        :return:

        {'setDeviceCredentialsv2Response': {'return': {'deviceId': 204043251458076,
           'returnCode': {'majorReturnCode': '000', 'minorReturnCode': '0000'},
           'apnCredentailsResponse': [{'apnName': 'ppinternet.gdsp',
             'returnCode': {'majorReturnCode': '000', 'minorReturnCode': '0000'}}]}}}

        """
        endpoint = "/m2m/v1/devices/{device_id}/credentials".format(device_id=device_id)
        data = {
            "deviceCredentials": {
                "deviceId": device_id,
                "credentialList": {
                    "credentialItem": [
                        {
                            "apn": apn,
                            "userId": user_id,
                            "password": password
                        }
                    ]
                }
            }
        }
        return self._send_message('post', endpoint, data=data)

    def update_device_credential_v2(self,
                                 device_id,
                                 apn,
                                 password):
        """
        Updates device Credentials stored in the M2M Service plataform.

        :param device_id:
        :param apn:
        :param password:
        :return:

        {'updateDeviceCredentialsv2Response': {'return': {'deviceId': 204043251458076,
           'returnCode': {'majorReturnCode': '000', 'minorReturnCode': '0000'},
           'apnCredentailsResponse': [{'apnName': 'ppinternet.gdsp',
             'returnCode': {'majorReturnCode': '000', 'minorReturnCode': '0000'}}]}}}

        """
        endpoint = "/m2m/v1/devices/{device_id}".format(device_id=device_id)
        data = {
            "deviceCredentials": {
                "deviceId": device_id,
                "credentialList": {
                    "credentialListItem": [
                        {
                            "apn": apn,
                            "password": password
                        }
                    ]
                }
            }
        }
        return self._send_message('put', endpoint, data=data)

    def submit_wu_trigger_v3(self,
                          device_id,
                          source_id=None,
                          trigger_type=None,
                          priority=None,
                          validity_period=None,
                          replace_if_present=None):
        """
        Request the M2M system to execute an SMS Message or Circuit Switch Call
        ‘wake up’ trigger to a specific device.

        :param device_id:
        :param source_id:
        :param trigger_type:
        :param priority:
        :param validity_period:
        :param replace_if_present:
        :return:

        {'submitWUTriggerv3Response': {'return': {'deviceId': 204043251458076,
           'returnCode': {'majorReturnCode': '000', 'minorReturnCode': '0000'},
           'triggerType': 'SMS',
           'messageReference': '\\/41b92f776a02ae59\\/12882393251458076'}}}

        """
        endpoint = "/m2m/v1/devices/{device_id}?action=submitWUTrigger".format(device_id=device_id)
        datas = {
            "deviceId": device_id,
            "sourceId": source_id,
            "triggerType": trigger_type,
            "priority": priority,
            "validityPeriod": validity_period,
            "replaceIfPresent": replace_if_present
        }
        data = {'WUTrigger': dict((k, v) for k, v in datas.items() if v is not None)}
        return self._send_message('post', endpoint, data=data)

    def submit_sms_v3(self,
                   device_id,
                   source_id,
                   message_data,
                   message_type=None,
                   validity_period=None,
                   replace_if_present=None
                   ):
        """
        Sends a text message to a target device identified by its deviceId.

        :param device_id:
        :param source_id:
        :param message_data:
        :param message_type:
        :param validity_period:
        :param replace_if_present:
        :return:

        {'submitSMSv3Response': {'return': {'deviceId': 204043251458076,
           'messageReference': '\\/41b92f796a036fc3\\/12882393251458076',
           'returnCode': {'majorReturnCode': '000', 'minorReturnCode': '0000'}}}}

        """
        endpoint = "/m2m/v1/devices/{device_id}?action=submitsms".format(device_id=device_id)
        datas = {
            "deviceId": device_id,
            "sourceId": source_id,
            "messageData": message_data,
            "messageType": message_type,
            "validityPeriod": validity_period,
            "replaceIfPresent": replace_if_present
        }
        data = {'submitSMS': dict((k, v) for k, v in datas.items() if v is not None)}
        return self._send_message('post', endpoint, data=data)

    def submit_transactional_sms(self,
                                 device_id,
                                 source_id,
                                 message_data,
                                 message_type=None,
                                 data_coding_scheme=None,
                                 message_udh=None
                                 ):
        """
        Sends a transactional short message to a target device identified by its deviceId.

        :param device_id:
        :param source_id:
        :param message_data:
        :param message_type:
        :param data_coding_scheme:
        :param message_udh:
        :return:

        {'submitTransactionalSMSResponse': {'return': {'deviceId': 204043251458076,
           'messageReference': '\\/41b92f7a6a039e5b\\/12882393251458076',
           'returnCode': {'majorReturnCode': '000', 'minorReturnCode': '0000'}}}}

        """
        endpoint = "/m2m/v1/devices/{device_id}?action=submitTransactionalSMS".format(device_id=device_id)
        datas = {
            "deviceId": device_id,
            "sourceId": source_id,
            "messageData": message_data,
            "messageType": message_type,
            "dataCodingScheme": data_coding_scheme,
            "messageUDH": message_udh
        }
        data = {'submitTransactionalSMS': dict((k, v) for k, v in datas.items() if v is not None)}
        return self._send_message('post', endpoint, data=data)

    def filtered_device_list_v4(self,
                                page_size,
                                page_number,
                                match_imsi,
                                match_msisdn=None,
                                match_iccid=None,
                                match_customer=None,
                                match_rag_status=None,
                                match_device_state=None,
                                match_alert=None,
                                match_earliest_first_used_date=None,
                                match_customer_order_number=None,
                                match_custom_attribute=None,
                                sort_field=None,
                                sort_field_order_direction=None
                                ):
        """
        Retrieve a list of devices filtered by one or more of the device’s parameters.

        :param page_size:
        :param page_number:
        :param match_imsi:
        :param match_msisdn:
        :param match_iccid:
        :param match_customer:
        :param match_rag_status:
        :param match_device_state:
        :param match_alert:
        :param match_earliest_first_used_date:
        :param match_customer_order_number:
        :param match_custom_attribute:
        :param sort_field:
        :param sort_field_order_direction:
        :return:

        {'getFilteredDeviceListv4Response': {'return': {'returnCode': {'majorReturnCode': '000',
            'minorReturnCode': '0000'},
           'matchedResults': 1,
           'deviceList': {'device': {'imsi': 204043251458076,
             'msisdn': 882393251458076,
             'iccid': 89314404000093042381,
             'customerServiceProfile': 'ADI_CSP_20404_apix_cloneedy',
             'ragStatus': 'R',
             'state': 'A',
             'rogueUsageAlertPresent': 'N',
             'highUsageAlertPresent': 'N',
             'customAttribute1': 1,
             'customAttribute2': 1,
             'customAttribute3': 2,
             'customAttribute4': 7,
             'customAttribute5': 8,
             'locationRequestedFlag': 'N',
             'locationPollingInterval': 30,
             'locationTrackingPeriod': 120}}}}}

        """
        if match_msisdn is not None and match_iccid is not None:
            raise AttributeError(
                "Value can not be null and both values must not be passed."
            )
        if match_msisdn is None and match_iccid is None:
            raise AttributeError(
                "One value from these two fields must be provided. "
            )
        if match_msisdn is not None:
            if not isinstance(match_msisdn, list):
                match_msisdn = [match_msisdn]
            key = "matchImsi"
            match = {"imsi": [match_msisdn]}
        elif match_iccid is not None:
            if not isinstance(match_iccid, list):
                match_iccid = [match_iccid]
            key = "matchIccid"
            match = {"ccid": match_iccid}
        else:
            raise KeyError("Missing either match_msisdn or match_iccid")

        endpoint = "/m2m/v1/devices/list"
        datas = {
            "pageSize": page_size,
            "pageNumber": page_number,
            "matchImsi": match_imsi,
            "{}".format(key): match,
            "matchCustomer": match_customer,
            "matchRagStatus": match_rag_status,
            "matchDeviceState": match_device_state,
            "matchAlert": match_alert,
            "matchEarliestFirstUsedDate": match_earliest_first_used_date,
            "matchCustomerOrderNumber": match_customer_order_number,
            "matchCustomAttribute{N}": match_custom_attribute,
            "sortField": sort_field,
            "sortFieldOrderDirection": sort_field_order_direction
        }
        data = {'getFilteredDeviceList': dict((k, v) for k, v in datas.items() if v is not None)}
        return self._send_message('post', endpoint, data=data)

    def get_device_location_details(self, device_id):
        """
        Retrieves location details for specified a specified device from the Global M2M Services Platform.

        :param device_id:
        :return:

        {'getDeviceLocationDetailsResponse': {'return': {'deviceLocation': {'address': 'London Road , RG14 2DA Newbury, United Kingdom',
            'latitude': 51.405,
            'longitude': -1.30388888,
            'msisdn': 882393251458075,
            'radius': 1500,
            'timestamp': '2015-01-15T18:52:52.000+0000'},
           'returnCode': {'majorReturnCode': '000', 'minorReturnCode': '0000'}}}}

        """
        endpoint = "/m2m/v1/devices/{device_id}/location".format(device_id=device_id)
        return self._send_message('get', endpoint)

    def get_device_location_history_details(self, device_id, start_time, stop_time):
        """
        Retrieves location details for specified a specified device from the Global M2M Services Platform.

        :param device_id:
        :param start_time:
        :param stop_time:
        :return:

        {'getDeviceLocationHistoryDetailsResponse': {'return': {'deviceLocationHistory': [{'area': 'N\\/A',
             'city': 'Newbury',
             'country': 'United Kingdom',
             'direction': 'N\\/A',
             'distance': -1.0,
             'latitude': 51.40444444,
             'longitude': -1.30277777,
             'msisdn': 882393251458075,
             'radius': 50,
             'speed': 0,
             'status': 'Stopped',
             'street': 'London Road',
             'timestamp': '2014-12-29T13:47:15.000+0000'},
            {'area': 'N\\/A',
             'city': 'Newbury',
             'country': 'United Kingdom',
             'direction': 'N\\/A',
             'distance': -1.0,
             'latitude': 51.40444444,
             'longitude': -1.30277777,
             'msisdn': 882393251458075,
             'radius': 50,
             'speed': 0,
             'status': 'Stopped',
             'street': 'London Road',
             'timestamp': '2014-12-29T13:46:48.000+0000'},
            {'area': 'N\\/A',
             'city': 'Newbury',
             'country': 'United Kingdom',
             'direction': 'N\\/A',
             'distance': -1.0,
             'latitude': 51.40444444,
             'longitude': -1.30277777,
             'msisdn': 882393251458075,
             'radius': 50,
             'speed': 0,
             'status': 'Stopped',
             'street': 'London Road',
             'timestamp': '2014-12-29T11:44:19.000+0000'},
            {'area': 'N\\/A',
             'city': 'Newbury',
             'country': 'United Kingdom',
             'direction': 'N\\/A',
             'distance': -1.0,
             'latitude': 51.40444444,
             'longitude': -1.30277777,
             'msisdn': 882393251458075,
             'radius': 50,
             'speed': 0,
             'status': 'Stopped',
             'street': 'London Road',
             'timestamp': '2014-12-29T11:43:48.000+0000'}],
           'deviceLocationHistoryListLength': 4,
           'deviceLocationHistoryTableLength': 4,
           'returnCode': {'majorReturnCode': '000', 'minorReturnCode': '0000'}}}}

        """
        endpoint = "/m2m/v1/devices/{device_id}/location".format(device_id=device_id)
        params = {"startTime": start_time, "stopTime": stop_time}
        return self._send_message('get', endpoint, params=params)

    def get_sms_communication_overview_v2(self,
                                          user_id,
                                          customer_id,
                                          selected_imsi,
                                          message_direction,
                                          start_date,
                                          end_date,
                                          page_number,
                                          page_size,
                                          sort_field,
                                          sort_field_order_direction
                                          ):
        """
        Retrieves SMS communication details stored on the Global M2M Services Platform for a specific device.

        :param user_id:
        :param customer_id:
        :param selected_imsi:
        :param message_direction:
        :param start_date:
        :param end_date:
        :param page_number:
        :param page_size:
        :param sort_field:
        :param sort_field_order_direction:
        :return:

        {'getSmsCommunicationOverviewv2Response': {'return': {'returnCode': {'majorReturnCode': '000',
            'minorReturnCode': '0000'},
           'smsCommunicationList': [{'associatedUserId': 710000001,
             'eventId': 9636419,
             'eventStatus': 'Delivered',
             'eventTimestamp': '2015-01-16T15:34:17+00:00',
             'eventType': 'SMS-MT-Payload',
             'imsi': 204043251458076,
             'messageBody': 'Y2lkOjEyNDUyMTc1OTM3MjU=',
             'messageType': 'T',
             'simIdentifier': 204043251458076},
            {'associatedUserId': 710000001,
             'eventId': 9636372,
             'eventStatus': 'Delivered',
             'eventTimestamp': '2015-01-16T15:33:37+00:00',
             'eventType': 'SMS-MT-Payload',
             'imsi': 204043251458076,
             'messageBody': 'Y2lkOjEyNDUyMTc1OTM3MjU=',
             'messageType': 'T',
             'simIdentifier': 204043251458076},
            {'associatedUserId': 710000001,
             'eventId': 8882548,
             'eventStatus': 'Failed',
             'eventTimestamp': '2015-01-05T15:48:07+00:00',
             'eventType': 'SMS-MT-Payload',
             'imsi': 204043251458076,
             'messageBody': 'Y2lkOjEyNDUyMTc1OTM3MjU=',
             'messageType': 'T',
             'simIdentifier': 204043251458076},
            {'associatedUserId': 710000001,
             'eventId': 8883195,
             'eventStatus': 'Delivered',
             'eventTimestamp': '2015-01-06T11:47:21+00:00',
             'eventType': 'SMS-MT-Payload',
             'imsi': 204043251458076,
             'messageBody': 'Y2lkOjEyNDUyMTc1OTM3MjU=',
             'messageType': 'T',
             'simIdentifier': 204043251458076}],
           'smsCommunicationListLength': 64,
           'smsCommunicationTableLength': 64}}}

        """
        endpoint = "/m2m/v1/devices/smsCommunicationOverview"
        params_data = {
            "userId": user_id,
            "customerId": customer_id,
            "selectedImsi": selected_imsi,
            "messageDirection": message_direction,
            "startDate": start_date,
            "endDate": end_date,
            "pageNumber": page_number,
            "pageSize": page_size,
            "sortField": sort_field,
            "sortFieldOrderDirection": sort_field_order_direction
        }
        params = dict((k, v) for k, v in params_data.items() if v is not None)
        return self._send_message('get', endpoint, params=params)
