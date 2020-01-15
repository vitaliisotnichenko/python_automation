import requests
import pytest
from requests.auth import HTTPBasicAuth
import simplejson


class Test_Api:

    def test_get_issue(self):
        r = requests.get('http://jira.hillel.it/rest/api/2/issue/WEBINAR-4671', auth=HTTPBasicAuth('webinar5', 'webinar5'))
        print(r.json())
        body = r.json()
        assert r.status_code == 200
        assert body['id'] == '52002'
        assert body['fields']['issuetype']['id'] == '10104'

    def test_create_meta(self):
        r = requests.get('http://jira.hillel.it/rest/api/2/issue/createmeta', auth=HTTPBasicAuth('webinar5', 'webinar5'))
        print(r.json())
        body = r.json()
        assert r.status_code == 200


    def test_create_issue(self):
        payload = {
            "fields": {
                "project": {
                    "key": "WEBINAR"
                },
                "summary": "Test issue",
                "description": "test issue",
                "issuetype": {
                    "id": "10107"
                }
            }
        }
        r = requests.post('https://jira.hillel.it/rest/api/2/issue', auth=HTTPBasicAuth('webinar5', 'webinar5'), json=payload)
        assert r.status_code == 201
        body = r.json()
        print(body)
        issue_key = body["key"]
        d = requests.delete("https://jira.hillel.it/rest/api/2/issue/" + issue_key, auth=HTTPBasicAuth('webinar5', 'webinar5'))
        assert d.status_code == 204



        # / rest / api / 2 / issue / createmeta
