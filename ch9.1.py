import requests
from bs4 import BeautifulSoup as BS
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

#params = {'firstname':'Eric', 'lastname':'Cartman'}
#r = requests.post('http://www.pythonscraping.com/pages/files/processing.php', data=params)

url = 'http://pythonscraping.com/pages/cookies/welcome.php'
params = {'username':'Ryan', 'password':'password'}

#r = requests.post(url, params)
r = requests.post(url, params, timeout=2)
print('Cookie is set to:')
print(r.cookies.get_dict())
print('================')
print('Getting in to profile ...')

url_profile = 'http://pythonscraping.com/pages/cookies/profile.php'
r2 = requests.get(url_profile, cookies=r.cookies)
print('r2: ', r2.text)

auth = HTTPBasicAuth('kkk', 'password')
r3 = requests.post(url='http://pythonscraping.com/pages/auth/login.php', auth=auth)
print('r3: ', r3.text)

