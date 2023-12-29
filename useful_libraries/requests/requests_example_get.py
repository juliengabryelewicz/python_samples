import requests
x = requests.get('https://www.google.fr')
print(x.text)
