import requests
import json

url = "https://test.liankeyun.com/wsg/vms/page"
headers = {
    "authorization": "eyJhbGciOiJIUzUxMiJ9"
                     ".eyJsb2dpbl91c2VyX2tleSI6IjM4ZjFiY2QxLTgzNjQtNGRjYi04NmNhLWY0YjQ1Yjg5ZDY2YSJ9"
                     ".jcXrlIAcxmL5Q23GzGLR8qLStwQX9DcPG6c--htHI5Wg0j4ouWZDXEBzvEHbz_Mdk8mEbIn-LAmdpxvcYuxSwA "
}
data = {
    "page": 1,
    "size": 5,
    "query": {
        "departmentIds": [],
        "expireTimeStart": "",
        "expireTimeEnd": "",
        "rightsId": 530
    }
}

r = requests.post(url=url, json=data, headers=headers)
r_json = r.json()
print(json.dumps(r_json, indent=2, ensure_ascii=False))
