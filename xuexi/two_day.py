import requests
import json

# url = "https://work.liankeyun.com/scrm-admin-api/wechat/group/material/upload"
download_url = "https://work.liankeyun.com/wsg/sop/groupTaskBoard/exportGroupTaskBoard"

head = {
    "Authorization": "eyJhbGciOiJIUzUxMiJ9"
                     ".eyJsb2dpbl91c2VyX2tleSI6IjM5N2RjNWZhLTUxYTgtNDkwYy05ZDBiLTcwYzhhZmExNzJkOSJ9"
                     ".DrwZ6ajjKVDcq9QDTw8s29raEWJ0_1BGhmxHlYfr1FKZpqrK0HA-xvue9wHf9p-jAoIIT4Q_bz5Y0yvOrFsOBQ "
}

data = {
    "ids": [49]
}

# file = {
#     "file": ("神盾局.png", open("C:/Users/10647/Pictures/Saved Pictures/神盾局.png", "rb"), "image/png")
# }

# r = requests.post(url=url, files=file, headers=head).json()
r = requests.post(download_url, headers=head, json=data)
with open("123.xlsx", "wb") as f:
    f.write(r.content)
# print(json.dumps(r, indent=2, ensure_ascii=False))
print(r)
