# Destiny Harris
# 04/20/2026
# 9. server side request forgery

# Incorrect

url = input("Enter URL: ")
response = requests.get(url)
print(response.text)

# Fixed

import requests
from urllib.parse import urlparse

ALLOWED_DOMAINS = ["example.com"]

def is_safe_url(url):
    try:
        parsed = urlparse(url)

        return (
            parsed.scheme in ["http", "https"] and
            parsed.hostname in ALLOWED_DOMAINS
        )
    except:
        return False

url = input("Enter URL: ")

if not is_safe_url(url):
    raise Exception("Blocked: unsafe or unauthorized URL")

response = requests.get(url, timeout=5)
print(response.text)