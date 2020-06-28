.. _authenticate:

Authentication
==============

This document deals with how you authenticate a user to call splitwise function

OAuth 1.0
---------

OAuth1.0 provides a token that can be used to call apis. Note that this token is
valid forever, unless explicitely removed by user/splitwise.

1. Register your app on `splitwise <https://secure.splitwise.com/apps>`_ to get a consumer key and consumer secret.

2. Import Splitwise class and create an object.

        >>> from splitwise import Splitwise
        >>> s = Splitwise("consumer_key", "consumer_secret")

3. Get Authorize URL using the object and save the oauth secret

        >>> url, oauth_token_secret = s.getAuthorizeURL()

4. Redirect user to `url`, after the authorization, Splitwise will redirect back with oauth_token and oauth_verifier that can be used along with secret from step 3 to get access token.

        >>> access_token = s.getAccessToken(oauth_token, oauth_token_secret, oauth_verifier)

5. Save this access token in your DB or somewhere. Now you can set this accesstoken and use it to make authenticated calls

        >>> s.setAccessToken(access_token)
        >>> user = s.getCurrentUser()