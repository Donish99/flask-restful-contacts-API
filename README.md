# flask-restful-contacts-API

## Made by flask restful and SQLAlchemy

### Full List of Contacts   GET  __'url/all'__
returns list of contacts in database

### Get contact detail by id   GET  __'url/contact/(id)'__
returns contact in database

### Create contact   POST __'url/contact/(id)'__
keys(required):
  name, number, year
returns created contact

### Update contact by id   PUT  __'url/contact/(id)'__
keys(optional):
  name, number, year
returns updated contact

### Delete contact by id   DELETE  __'url/contact/(id)'__
returns None
