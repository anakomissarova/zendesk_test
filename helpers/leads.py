import requests


class LeadsHelper:
    """
    A class providing methods to operate leads via REST API

    Attributes
    ----------
    RESOURCE : str
        resource for operations on leads

    Methods
    -------
    create(lead_data)
        Creates a lead and returns its parameters if the server returned 200
    get_lead(lead_id)
        Gets a lead by id and returns its parameters if the lead exists on a server
    exists(lead_id)
        Returns True if the lead with a given id exists on a server
    modify(lead_id, lead_data)
        Modifies lead with the given id and returns its parameters if the server returned 200
    """

    RESOURCE = '/leads'

    def __init__(self, app):
        """
        Parameters
        ----------
        app : Application
            The Application object with necessary setting to use REST API
        """
        self.app = app
        self.url = app.url + self.RESOURCE

    def create(self, lead_data):
        """
        Parameters
        ----------
        lead_data : dict
            Parameters of the lead to be created

        Returns
        _______
        dict
            JSON with created lead parameters if server returned 200, otherwise JSON with server errors
        """
        headers = {**self.app.basic_headers, 'Content-Type': 'application/json'}
        r = requests.post(self.url, headers=headers, json=lead_data)
        if r.status_code == 200:
            return r.json()['data']
        else:
            return r.json()

    def get_lead(self, lead_id):
        """
        Parameters
        ----------
        lead_id : int
            Lead ID

        Returns
        _______
        dict
            JSON with lead parameters if server returned 200, otherwise JSON with server errors
        """
        r = requests.get('{url}/{lead_id}'.format(url=self.url, lead_id=str(lead_id)),
                         headers=self.app.basic_headers)
        if r.status_code == 200:
            return r.json()['data']
        else:
            return r.json()

    def exists(self, lead_id):
        """
        Parameters
        ----------
        lead_id : int
            Lead ID

        Returns
        _______
        bool
            True if server returned 200, False if server returned 404 and None if server returned something else
        """
        r = requests.get('{url}/{lead_id}'.format(url=self.url, lead_id=str(lead_id)),
                         headers=self.app.basic_headers)
        if r.status_code == 200:
            return True
        elif r.status_code == 404:
            return False
        else:
            return None

    def modify(self, lead_id, lead_data):
        """
        Parameters
        ----------
        lead_id : int
            Lead ID
        lead_data : dict
            Lead parameters to be modified

        Returns
        _______
        dict
            JSON with lead parameters if server returned 200, otherwise JSON with server errors
        """
        headers = {**self.app.basic_headers, 'Content-Type': 'application/json'}
        r = requests.put('{url}/{lead_id}'.format(url=self.url, lead_id=str(lead_id)),
                         headers=headers, json={'data': lead_data})
        if r.status_code == 200:
            return r.json()['data']
        else:
            return r.json()
