import requests

# Basic Authentication request:
r = requests.post('http://pulse-rest-testing.herokuapp.com/books2',
                  data={'title': 'Anna Karenina', 'author': '111'},
                  auth=('admin', 'pass'))
print(r.status_code)
print(r.headers)
print(r.text)

### Using Session
s = requests.Session()
s.auth = ('admin', 'pass')

r2 = s.get('http://pulse-rest-testing.herokuapp.com/roles2?level=100500')
print(r2.status_code)
print(r2.headers)
print(r2.text)
