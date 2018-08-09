import os
import sys
import requests
import random
import string
import json
import argparse

if len(sys.argv) > 1:
    parser = argparse.ArgumentParser(description='Send Spam info to a place.')
    parser.add_argument("-l", "--link", required=True, help="path to url")
    parser.add_argument("-u", "--user", required=True, help="userkey")
    parser.add_argument("-p", "--pass", required=True, help="passkey")
    args = vars(parser.parse_args())

    url = args["link"]
    userkey = args["user"]
    passkey = args["pass"]
else:
    url = input('Please enter the URL to post to: ')
    print('URL : %s' % url)
    userkey = input('Please enter userkey: ')
    print('Userkey : %s' % userkey)
    passkey = input('Please enter the passkey: ')
    print('Passkey : %s' % passkey)


names = json.loads(open('names.json').read())

for name in names: 
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@yahoo.com'
    password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(8))

    requests.post(url, allow_redirects=False, data={
        userkey: username,
        passkey: password
    })

    print ('%s user: %s and %s password: %s to %s' % (userkey, username, passkey, password, url))