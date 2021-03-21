from helpers.leads import LeadsHelper


class Application:

    def __init__(self, baseurl, api_version, api_token):
        self.url = baseurl+api_version
        self.basic_headers = {'Accept': 'application/json',
                              'Authorization': 'Bearer {}'.format(api_token)}
        self.lead = LeadsHelper(self)
