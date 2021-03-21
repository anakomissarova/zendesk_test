import requests


class LeadsHelper:

    RESOURCE = '/leads'

    def __init__(self, app):
        self.app = app
        self.url = app.url + self.RESOURCE

    def create(self, lead_data):
        headers = {**self.app.basic_headers, 'Content-Type': 'application/json'}
        r = requests.post(self.url, headers=headers, json=lead_data)
        if r.status_code == 200:
            return r.json()['data']
        else:
            return r.json()

    def get_lead(self, lead_id):
        r = requests.get('{url}/{lead_id}'.format(url=self.url, lead_id=str(lead_id)),
                         headers=self.app.basic_headers)
        if r.status_code == 200:
            return r.json()['data']
        else:
            return r.json()

    def exists(self, lead_id):
        r = requests.get('{url}/{lead_id}'.format(url=self.url, lead_id=str(lead_id)),
                         headers=self.app.basic_headers)
        if r.status_code == 200:
            return True
        elif r.status_code == 404:
            return False
        else:
            return None

    def modify(self, lead_id, lead_data):
        headers = {**self.app.basic_headers, 'Content-Type': 'application/json'}
        r = requests.put('{url}/{lead_id}'.format(url=self.url, lead_id=str(lead_id)),
                         headers=headers, json={'data': lead_data})
        if r.status_code == 200:
            return r.json()['data']
        else:
            return r.json()
