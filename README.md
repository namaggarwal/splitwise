# Splitwise Python SDK

This is the python sdk for Splitwise APIs. At this point only GET requests are supported. Pull requests and bug reports are welcomed.

## Installation

Install using pip :
```sh
$ pip install splitwise
```
## Register your application

Register your application on [splitwise](https://secure.splitwise.com/oauth_clients) and get your consumer key and consumer secret.

## Include splitwise in your application
```python
from splitwise import Splitwise
```

## Get splitwise instance

To get an instance to splitwise just provide the consumer key and secret.


```python
sObj = Splitwise("<consumer key>","<consumer secret>")
```

## Usage

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

### Get Friends

You can use ```getFriends()``` to get all the friends of the current user along with the balances. It returns a list of ```Friend``` objects.

```python
sObj = Splitwise(Config.consumer_key,Config.consumer_secret)
sObj.setAccessToken(session['access_token'])
sObj.getFriends()
```

### Get Groups

You can use ```getGroups()``` to get all the groups of the current user along with the members and balances. It returns a list of ```Group``` objects.

```python
sObj = Splitwise(Config.consumer_key,Config.consumer_secret)
sObj.setAccessToken(session['access_token'])
sObj.getGroups()
```

### Get Currencies

You can use ```getCurrencies()``` to get all the currencies supported by splitwise. It returns a list of ```Currency``` objects.

```python
sObj = Splitwise(Config.consumer_key,Config.consumer_secret)
sObj.setAccessToken(session['access_token'])
sObj.getCurrencies()
```

### Get Category


You can use ```getCategories()``` to get all the categories and sub categories provided by splitwise. It returns a list of ```Category``` objects.

```python
sObj = Splitwise(Config.consumer_key,Config.consumer_secret)
sObj.setAccessToken(session['access_token'])
sObj.getCategories()
```

### Get Group

You can use ```getGroup(id)``` to get the particular group of the current user along with the members and balances. It returns a ```Group``` object. Use id as 0 to get all non group expenses.

```python
sObj = Splitwise(Config.consumer_key,Config.consumer_secret)
sObj.setAccessToken(session['access_token'])
sObj.getGroup(43233)
```

### Get Expenses

You can use ```getExpenses(offset,limit,group_id,friendship_id,dated_after,dated_before,updated_after,updated_before)``` to get all the expenses of the current user based on filter options. It returns a list of ```Expense``` objects.

```python
sObj = Splitwise(Config.consumer_key,Config.consumer_secret)
sObj.setAccessToken(session['access_token'])
sObj.getExpenses()
```

### Get Expense

You can use ```getExpense(id)``` to get the particular expense of the current user. It returns a ```Expense``` object. 

```python
sObj = Splitwise(Config.consumer_key,Config.consumer_secret)
sObj.setAccessToken(session['access_token'])
sObj.getExpense(43233)
```


## Objects

### User

Methods:

1. getId() - Returns the id of the user
2. getFirstName() - Returns the first name of user
3. getLastName() - Returns the last name of user
4. getEmail() - Returns the email of the user
5. getRegistrationStatus() - Returns the registraion status of the user
6. getPicture() - Returns a ```Picture``` object containing picture details

### CurrentUser

Current user is inherited from ```User```. All the methods of user are available for current user.

Methods:

1. getDefaultCurrency() - Returns the default currency
2. getLocale() - Returns the locale
3. getDateFormat() - Returns the date format
4. getDefaultGroupId() - Returns the default group id of user

### Friend

Friend is inherited from ```User```. All the methods of user are available for friend.

Methods:

1. getUpdatedAt() - Gets the time when this user information was last updated
2. getBalances() - Returns a list of ```Balance``` objects
3. getGroups() - Returns a list of ```FriendGroup``` objects

### Expense User
ExpenseUser is inherited from ```User```. All the methods of user are available for Expense User.


Methods:

1. getPaidShare() - Returns the Paid Share
2. getOwedShare() - Returns the Owed Share
3. getNetBalance() - Returns the Net Balance

### Group

Methods:

1. getId() - Returns the id of the group
2. getName() - Returns the name of the group
3. getUpdatedAt() - Get the time this group was last updated
4. getWhiteBoard() - Get the whiteboard contents of this group
5. isSimplifiedByDefault() - Returns if group is simplified by default or not
6. getMembers() - Returns a list of ```Friend``` objects
7. getOriginalDebts() - Returns a list of  ```Debt``` objects
8. getType() - Returns the type of group
9. getSimplifiedDebts() - Returns a list of  ```Debt``` objects
10. getInviteLink() - Returns the invite link

### FriendGroup

Methods:

1. getId() - Returns the id of the group
2. getBalances() - Returns a list of ```Balance``` object



License
----

MIT
