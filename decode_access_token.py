import os
import json
import http.client
import jwt
from dotenv import (
    load_dotenv,
)
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend

load_dotenv()

certificate_text = open("rsa_certificates/certificate.pem", 'rb').read()
certificate = load_pem_x509_certificate(certificate_text, default_backend())
certificate_publickey = certificate.public_key()


encoded_jwt = input("Please paste your access_token and press [ENTER]\n")

decoded_data = jwt.decode(
    encoded_jwt,
    certificate_publickey,
    audience=os.environ.get('AUTH0_AUDIENCE'),
    algorithm='RS256'
)

print('#'*30)
print('YOUR DECODED PAYLOAD')
print('#'*30)
print(decoded_data)
print('#'*30)
