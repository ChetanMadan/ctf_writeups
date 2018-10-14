import requests

# I received this header, it acts weird
headers='''Request URL: http://35.200.172.236:6135x/index.php
Request Method: GET
Status Code: 200 OK
Remote Address: 35.200.172.236:61356
Referrer Policy: no-referrer-when-downgrade
Connection: Keep-Alive
Content-Encoding: gzip
Content-Length: 30
Content-Type: text/html; charset=UTF-8
Date: Sat, 13 Oct 2018 17:30:06 GMT
Keep-Alive: timeout=5, max=100
Server: Apache/2.4.18 (Ubuntu)
Vary: Accept-Encoding
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
DNT: 1
Host: 35.200.172.236:6135x
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'''
#I coded it wrong maybe, but I don't do mistakes
url='http://35.200.172.236:61356/index.php'
payload={'id':'1'}
r = requests.get(url,data=payload)
print(r.text)