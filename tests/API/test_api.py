import requests
import pytest
from requests.auth import HTTPBasicAuth
import simplejson
import re

from global_scope import url_api
from tests.API.api_pathes import create_issue, createmeta
from tests.API.test_data_api import Payload

class Test_Api(Payload):

    def test_get_issue(self):
        r = requests.get(url_api + create_issue + 'WEBINAR-4671', auth=HTTPBasicAuth('webinar5', 'webinar5'))
        print(r.json())
        body = r.json()
        assert r.status_code == 200
        assert body['id'] == '52002'
        assert body['fields']['issuetype']['id'] == '10104'

    def test_create_meta(self):
        r = requests.get(url_api + createmeta, auth=HTTPBasicAuth('webinar5', 'webinar5'))
        print(r.json())
        body = r.json()
        assert r.status_code == 200


    def test_create_issue(self):
        payload = self.create_issue_payload("WEBINAR", "Test issue", "test issue", "10107")
        r = requests.post(url_api + create_issue, auth=HTTPBasicAuth('webinar5', 'webinar5'), json=payload)
        assert r.status_code == 201
        body = r.json()
        assert body['key'].startswith('WEBINAR')
        self = body['self']
        assert re.match(".*?([0-9])+$", self)
        issue_key = body["key"]
        d = requests.delete(url_api + create_issue + issue_key, auth=HTTPBasicAuth('webinar5', 'webinar5'))
        assert d.status_code == 204



        # / rest / api / 2 / issue / createmeta
