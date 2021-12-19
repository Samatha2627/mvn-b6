import requests
from requests.auth import HTTPBasicAuth
token = 'admin'
PARAM = {'component': 'mvn-poc', 'metricKeys': 'code_smells,bugs,vulnerabilities,ncloc,coverage'}
test_url = 'http://34.125.196.119:9000/api/measures/component'
test_response = requests.get(test_url,auth=HTTPBasicAuth(username=token, password="admin"), verify=False,params=PARAM)
test_json = test_response.json()
print(test_json)
