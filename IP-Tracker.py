from urllib import request
import json
import os

while True:
    ip = input('Enter Target IP : ')
    url = "http://ip-api.com/json/"
    r = request.urlopen(url + ip)
    data = r.read()
    m = json.loads(data)

    print(f"""
    Status : {m['status']}
    IP : {m['query']}
    ISP : {m['isp']}
    Organization : {m['org']}
    Country : {m['country']}
    Region : {m['region']}
    City : {m['city']}
    Time Zone : {m['timezone']}
    """)

    break