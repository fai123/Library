import requests
# Try executing this block of code.
try:
    r = requests.get('http://www.udacity.com')
    print(r.status_code)
# I it's an error then execute this instead of craching.
except requests.exceptions.ConnectionError:
    print('cant reach this site!! ')
