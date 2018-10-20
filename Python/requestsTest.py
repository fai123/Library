# You need to import the requests module first.
import requests
# This is the command to meke a request, and its stored in a variable (r).
r = requests.get('https://www.google.com')
# To get the request status, if it returns 404 then there is a problem reaching the server,
# if it returns 200 then connected succussfuly.
print(r.status_code)
# To print the (r) content after sending the request.
print(r.text)
