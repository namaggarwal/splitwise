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


OAuth 2.0
---------

You can also use OAuth2.0 to authenticate a user

1. Register your app on `splitwise <https://secure.splitwise.com/apps>`_ to get a consumer key and consumer secret.

2. Import Splitwise class and create an object.

        >>> from splitwise import Splitwise
        >>> s = Splitwise("consumer_key", "consumer_secret")

3. Get Authorize URL using the object and save the state. You will need to provide a redirect uri where user should be redirected to after authorization.

        >>> url, state = s.getOAuth2AuthorizeURL(redirect_uri)

4. Redirect the user to `url`. After authorization, Splitwise will redirect back to redirect_uri with `code` and `state` in the query params. Make sure `state` is same the one stored earlier and then get the access token.

        >>> access_token = s.getOAuth2AccessToken(code, redirect_uri)

5. You can save the access token for later use. You can now use this access token to get an authenticated splitwise object and make authenticated calls.

        >>> s.setOAuth2AccessToken(access_token)
        >>> user = s.getCurrentUser()
