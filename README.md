# Splitwise Python SDK

This is the python sdk for Splitwise APIs. At this point only GET requests are supported. Pull requests and bug reports are welcomed.

### Installation

Install using pip :
```sh
$ pip install splitwise
```
### Register your application

Register your application on [splitwise](https://secure.splitwise.com/oauth_clients) and get your consumer key and consumer secret.

### Include splitwise in your application
```python
from splitwise import Splitwise
```

### Get splitwise instance

To get an instance to splitwise just provide the consumer key and secret.


```python
sObj = Splitwise("<consumer key>","<consumer secret>")
```

### Authorize splitwise 

Before you can make call to splitwise, you need to get access token of the user on whose behalf you will be making call. Think of it as login with splitwise. Its based on OAuth2 and its a 2 step process.

1. Get the Authorize URL and Secret. Redirect the user to the Authorize url and store the secret in somewhere for eg in session.

```python
sObj = Splitwise("<consumer key>","<consumer secret>")
url, secret = sObj.getAuthorizeURL()
#Store secret so you can retrieve it later
#redirect user to url
```

2. After authorization splitwise will redirect the user back to the callback url that you provided during registration. It will also provide oauth_token and oauth_verifier that can be used along with secret from step 1 to get access token. The below snippet is from Flask application to extract parameters and then using SDK to get access token. This access token can be stored in your db to make calls on his/her behalf.

```python
oauth_token    = request.args.get('oauth_token')
oauth_verifier = request.args.get('oauth_verifier')

sObj = Splitwise(Config.consumer_key,Config.consumer_secret)
access_token = sObj.getAccessToken(oauth_token,session['secret'],oauth_verifier)

session['access_token'] = access_token
```

### Get data from splitwise

Once you have the access token you can make the calls to splitwise. Get the splitwise instance and set the access token and then make authorized calls.

```python
sObj = Splitwise(Config.consumer_key,Config.consumer_secret)
sObj.setAccessToken(session['access_token'])
sObj.getFriends()
```

License
----

MIT
