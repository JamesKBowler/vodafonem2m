# vodafonem2m (Unofficial)
Provides access to Vodafone M2M endpoints via the REST API.

### Install
`pip install vodafonem2m`

### Basic Usage
```python

from vodafonem2m.m2m_device import M2MDevices

username = "youremail@company.com"
password = " password "
client_id = "api_key"
client_secret = "api_secret"

m2m = M2MDevices(username, password, client_id, client_secret)

home_doc = m2m.get_home_document()

```
