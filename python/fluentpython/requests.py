import requests
#r = requests.get("https://api.github.com/users/acombs/starred")
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.json()
