from vodafonem2m.vodafonem2m import VodafoneM2M


class M2MTariffs(VodafoneM2M):
    """
    The M2MTariffs class is specifically designed to obtain a list of
    the names of available tariffs from the M2M Service platform.

    BaseClass : VodafoneM2M
    """

    home = 'tariff'
    scope = "M2M_TARIFFS_ALL"

    def get_tariff_list(self):
        """
        Retrieves a list of Tariffs from the M2M Service platform.

        :return:

        {'getTariffListResponse': {'return': {'returnCode': {'majorReturnCode': '000',
            'minorReturnCode': '0000'},
           'tariffList': {'tariff': [{'tariffName': 'JohnbTest'},
             {'tariffName': 'JCIDEMOTARIFF'},
             {'tariffName': 'VF-ONLY-TEST'}]}}}}

        """
        endpoint = "/m2m/v1/ tariff/list"
        self._send_message('get', endpoint)
