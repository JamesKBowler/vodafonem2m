from vodafonem2m.vodafonem2m import VodafoneM2M


class M2MTProvisioningProfiles(VodafoneM2M):
    """
    The M2MTProvisioningProfiles class is specifically designed for applications
    to retrieve Provisioning Profiles stored in the M2M Service platform.

    BaseClass : VodafoneM2M
    """

    home = 'provisioningprofiles'
    scope = "M2M_PROVISIONINGPROFILES_ALL"

    def get_provisioning_profilest(self):
        """
        Retrieves list of customer Provisioning Profiles stored on the Global M2M Services Platform.

        :return:

        {'getProvisioningProfileListResponse': {'return': {'returnCode': {'majorReturnCode': '000',
            'minorReturnCode': '0000'},
           'provisioningProfileList': {'provisioningProfile': {
                'provisioningProfileName': 'ADI_Cust_20404_apix'}}}}}

        """
        endpoint = "/m2m/v1/provisioningprofiles/list"
        self._send_message('get', endpoint)
