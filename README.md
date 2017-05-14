# Splitwise Python SDK

This is the python sdk for Splitwise APIs. At this point only GET requests and a single POST request ```createExpense``` is supported. Pull requests and bug reports are welcomed.

## Latest Version

The latest version of splitwise SDK is Splitwise-0.0.5

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

## Debug

To get the debug logs use

```python
Splitwise.setDebug(True)
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

### Get Current User

You can use ```getCurrentUser()``` to get the current user. It returns a ```CurrentUser``` object.

```python
sObj = Splitwise(Config.consumer_key,Config.consumer_secret)
sObj.setAccessToken(session['access_token'])
sObj.getCurrentUser()
```

### Get User

You can use ```getUser(id)``` to get the user. It returns a ```User``` object.

```python
sObj = Splitwise(Config.consumer_key,Config.consumer_secret)
sObj.setAccessToken(session['access_token'])
id = 7123
user = sObj.getUser(id)
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

### Create Expense

You can use ```createExpense(Expense)``` to create a new Expense. It takes in parameter a partial ```Expense``` object and returns an ```Expense``` object.

Following things need to be set on the ```Expense``` object.

1. Cost
2. Description
3. Users - Should be a list of ```ExpenseUser``` with id and paidShare and owedShare set.

```python
from splitwise.expense import Expense
from splitwise.user import ExpenseUser

sObj = Splitwise(Config.consumer_key,Config.consumer_secret)
sObj.setAccessToken(session['access_token'])

expense = Expense()
expense.setCost('10')
expense.setDescription("Testing")

user1 = ExpenseUser()
user1.setId(79774)
user1.setPaidShare('10.00')
user1.setOwedShare('2.0')

user2 = ExpenseUser()
user2.setId(281236)
user2.setPaidShare('0.00')
user2.setOwedShare('8.00')

users = []
users.append(user1)
users.append(user2)

expense.setUsers(users)

expense = sObj.createExpense(expense)
print expense.getId()
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



### Balance

Methods:

1. getCurrencyCode() - Returns the currency code.
2. getAmount() - Returns the amount

### Category

Methods:

1. getSubcategories() - Returns a list of ```Category``` objects
2. getId() - Returns the id of category
3. getName() - Returns the name of the category

### Currency

Methods:

1. getCode() - Returns the Currency Code
2. getUnit() - Returns the Currency Unit

### Debt

Methods:

1. getFromUser() - Returns the id of the from user
2. getToUser() - Returns the id of the to user
3. getAmount() - Returns the amount of the debt
4. getCurrencyCode() - Returns the currency code of debt


### Expense

Methods:

1. getId() - Returns the id of expense
2. getGroupId() - Returns the id of the group expense belongs to
3. getDescription() - Returns the description of expense
4. isRepeat() - Returns if expense is repeat or not
5. getRepeatInterval() - Returns the repeat interval of expense
6. getEmailReminder() - Returns Email reminder
7. getEmailReminderInAdvance() - Returns email reminder in advance
8. getNextRepeat() - Returns the time of next repeat
9. getDetails() - Returns the detail of expense
10. getCommentsCount() - Returns the number of comments
11. getPayment() - Returns the payment of expense
12. getCreationMethod() - Returns the creation method of expense
13. getTransactionMethod() - Returns the transaction method of expense
14. getTransactionConfirmed() - Returns if transaction is confirmed
15. getCost() - Returns the cost of transaction
16. getCurrencyCode() - Returns the currency code of transaction
17. getCreatedBy() - Returns a ```User``` object of user who created the expense
18. getDate() - Returns the expense date.
19. getCreatedAt() - Returns the date time expense was created
20. getUpdatedAt() - Returns the date time expense was last updated
21. getDeletedAt() - Returns the date time expense was deleted
22. getReceipt() - Returns a ```Receipt``` object for receipt
23. getCategory() - Returns a ```Category``` object for category
24. getUpdatedBy() - Returns a ```User``` object of user who last updated the expense
25. getDeletedBy() - Returns a ```User``` object of user who deleted the expense
26. getUsers() - Returns a list of ```ExpenseUser``` objects
27. getExpenseBundleId() - Returns Expense Bundle ID
28. getFriendshipId() - Returns the Friendship ID
29. getRepayments() - Returns a list of ```Debt``` objects


### Picture

Methods:

1. getSmall() - Returns the link to the small image
2. getMedium() - Returns the link to the medium image
3. getLarge() - Returns the link to the large image

### Receipt

Methods:

1. getOriginal() - Returns the link to the original uploaded receipt
2. getLarge() - Returns the link to large image of uploaded receipt


## Sample Application

This is the [GitHub Link](https://github.com/namaggarwal/flask-splitwise-example) to the sample application written in Flask to show the usage of splitwise application.

License
----

MIT

Donate
----

If you think this helped you and you want to donate, you can do it via -

### Paypal
[https://www.paypal.me/namanagg](https://www.paypal.me/namanagg)

### Bitcoin
1DNhyZ696ekq6sY5vYMcmBLxLzAtq3oYpM
