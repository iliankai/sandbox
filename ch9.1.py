import requests
from bs4 import BeautifulSoup as BS
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

#params = {'firstname':'Eric', 'lastname':'Cartman'}
#r = requests.post('http://www.pythonscraping.com/pages/files/processing.php', data=params)

url1 = 'http://pythonscraping.com/pages/cookies/welcome.php'
params = {'username':'Ryan', 'password':'password'}
r1= requests.post(url1, params, timeout=3)
print('Cookie is set to:')
print(r1.cookies.get_dict())
print('================')
print('Getting in to profile ...')

url2 = 'http://pythonscraping.com/pages/cookies/profile.php'
r2 = requests.get(url2, cookies=r1.cookies, timeout=3)
print('r2: ', r2.text)

auth = HTTPBasicAuth('kkk', 'password')
url3 = 'http://pythonscraping.com/pages/auth/login.php'
r3 = requests.post(url=url3, auth=auth, timeout=3)
print('r3: ', r3.text)

url4 = 'http://www.pythonscraping.com/pages/javascript/ajaxDemo.html'
r4 = requests.post(url4, timeout=3)
print('r4: ', r4.text)

