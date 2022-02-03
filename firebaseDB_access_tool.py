#!/usr/bin/python3
import argparse
import requests
import subprocess as mk
parser = argparse.ArgumentParser(description="tool to check URL is accessible")

parser.add_argument("-apk", type=str, help="enter URL to check availability", required=True)
a = parser.parse_args()

url = mk.getoutput("strings {} | egrep -o 'https\:\/\/(.*).firebaseio.com'".format(a.apk)) 

h = url+"/.json"

req1 = requests.get(h)
rcode = req1.status_code
payload = {'name':'tom', 'job':'astro'}

req2 = requests.put(h, data=payload)
wcode = req2.status_code

if rcode == 200 :
    if (wcode == 200) or (wcode == 201) :
        print("readable & writable")
    else:
        print("only readable")
elif wcode == 200 or wcode == 201 :
    print("writable")
else :
    print("No read No write allowed")

