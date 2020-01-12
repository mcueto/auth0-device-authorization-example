import os
import json
import http.client
from dotenv import (
    load_dotenv,
)

load_dotenv()

conn = http.client.HTTPSConnection(os.environ.get('AUTH0_DOMAIN'))

payload = {
    'client_id': os.environ.get('AUTH0_CLIENT_ID'),
    'client_secret': os.environ.get('AUTH0_CLIENT_SECRET'),
    'audience': os.environ.get('AUTH0_AUDIENCE'),
    'grant_type': 'client_credentials'
}

headers = {
    'content-type': "application/json"
}

conn.request(
    "POST",
    "/oauth/token",
    json.dumps(payload),
    headers
)

res = conn.getresponse()
data = res.read()

print('#'*30)
print('YOUR ACCESS TOKEN')
print('#'*30)
print(data.decode("utf-8"))
print('#'*30)
