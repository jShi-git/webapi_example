import sys
import os
import base64
import hmac
import hashlib
import urllib
import time
import requests

'''
This demo shows how to use the RESTful API to upload an audio file ( "data_type":"audio" ) into your bucket.
You can find account_access_key and account_access_secret in your account page.
Log into http://console.acrcloud.com -> "Your Name"(top right corner) -> "Account" -> "Console API Keys" -> "Create Key Pair". 
Be Careful, they are different with access_key and access_secret of your project.
'''
account_access_key = "<your account access key>"
account_access_secret = "<your account access secret>"

requrl = "https://api.acrcloud.com/v1/buckets/eu_test/channels"
http_method = "GET"
http_uri = "/v1/buckets/<your_bucket>/channels"
signature_version = "1"
timestamp = time.time()

string_to_sign = http_method+"\n"+http_uri+"\n"+account_access_key+"\n"+signature_version+"\n"+str(timestamp)

sign = base64.b64encode(
        hmac.new(account_access_secret, string_to_sign, digestmod=hashlib.sha1)
        .digest())

headers = {'access-key': account_access_key, 'signature-version': signature_version, 'signature': sign, 'timestamp':timestamp}

r = requests.get(requrl, headers=headers, verify=True)
r.encoding = "utf-8"
print r.text
