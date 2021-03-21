from helpers.leads import LeadsHelper


class Application:
    """
    Basic fixture class

    Initializes variables needed to connect to REST API and provides access to helper classes
    (at the moment - only one class) to the tests
    """

    def __init__(self, baseurl, api_version, api_token):
        """
        Parameters
        ----------
        baseurl : str
            Sell API URL
        api_version : str
            API version prefix
        api_token : str
            API access token
        """
        self.url = baseurl+api_version
        self.basic_headers = {'Accept': 'application/json',
                              'Authorization': 'Bearer {}'.format(api_token)}
        self.lead = LeadsHelper(self)
