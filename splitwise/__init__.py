import oauth2 as oauth
import time
import json
from splitwise.user import Friend
from splitwise.currency import Currency
from splitwise.group import Group
from splitwise.category import Category
from splitwise.expense import Expense

try:
    from urlparse import parse_qsl #Python 2.x
except ImportError: #Python 3
    from urllib.parse import parse_qsl


class Splitwise(object):
    """ The Splitwise class to make the requests to splitwise server.
    """

    #URLs to make the request
    REQUEST_TOKEN_URL   = "https://secure.splitwise.com/api/v3.0/get_request_token"
    ACCESS_TOKEN_URL    = "https://secure.splitwise.com/api/v3.0/get_access_token"
    AUTHORIZE_URL       = "https://secure.splitwise.com/authorize"
    GET_FRIENDS_URL     = "https://secure.splitwise.com/api/v3.0/get_friends"
    GET_GROUPS_URL      = "https://secure.splitwise.com/api/v3.0/get_groups"
    GET_GROUP_URL       = "https://secure.splitwise.com/api/v3.0/get_group"
    GET_CURRENCY_URL    = "https://secure.splitwise.com/api/v3.0/get_currencies"
    GET_CATEGORY_URL    = "https://secure.splitwise.com/api/v3.0/get_categories"
    GET_EXPENSES_URL    = "https://secure.splitwise.com/api/v3.0/get_expenses"
    GET_EXPENSE_URL     = "https://secure.splitwise.com/api/v3.0/get_expense"

    debug = False


    def __init__(self,consumer_key,consumer_secret,access_token=None,debug=False):
        """ Initializes the splitwise class. Sets consumer and access token

        Args:
            consumer_key (str) : Consumer Key provided by Spliwise
            consumer_secret (str): Consumer Secret provided by Splitwise
            access_token (:obj: `dict`) Access Token is a combination of oauth_token and oauth_token_secret

        Returns:
            A Splitwise Object
        """
        self.consumer = oauth.Consumer(consumer_key, consumer_secret)

        #If access token is present then set the Access token
        if access_token:
            self.setAccessToken(access_token)

    @classmethod
    def setDebug(cls,debug):
        cls.debug = debug

    @classmethod
    def isDebug(cls):
        return cls.debug

    def getAuthorizeURL(self):

        client = oauth.Client(self.consumer)

        #Get the request token
        resp, content = client.request(Splitwise.REQUEST_TOKEN_URL, "POST")

        if Splitwise.isDebug():
            print(resp, content)

        #Check if the response is correct
        if resp['status'] != '200':
            raise Exception("Invalid response %s. Please check your consumer key and secret." % resp['status'])

        request_token = dict(parse_qsl(content.decode("utf-8")))

        return "%s?oauth_token=%s" % (Splitwise.AUTHORIZE_URL, request_token['oauth_token']), request_token['oauth_token_secret']


    def getAccessToken(self,oauth_token,oauth_token_secret,oauth_verifier):

        token = oauth.Token(oauth_token,oauth_token_secret)
        token.set_verifier(oauth_verifier)
        client = oauth.Client(self.consumer, token)

        resp, content = client.request(Splitwise.ACCESS_TOKEN_URL, "POST")

        if Splitwise.isDebug():
            print(resp, content)

        #Check if the response is correct
        if resp['status'] != '200':
            raise Exception("Invalid response %s. Please check your consumer key and secret." % resp['status'])

        access_token = dict(parse_qsl(content.decode("utf-8")))

        return access_token

    def setAccessToken(self,access_token):
        self.token = oauth.Token(key=access_token["oauth_token"], secret=access_token["oauth_token_secret"])
        self.client = oauth.Client(self.consumer, self.token)


    def __makeRequest(self,url):

        resp, content = self.client.request(url, "GET")

        if Splitwise.isDebug():
            print(resp, content)

        #Check if the response is correct
        if resp['status'] != '200':
            raise Exception("Invalid response %s. Please check your consumer key and secret." % resp['status'])

        return content

    def __prepareOptionsUrl(self,options={}):
        if not isinstance(options,dict) or len(options) == 0:
            return ""

        optstr = "?"

        try:
            opt = options.iteritems()
        except AttributeError: #Python 3
            opt = options.items()

        optstr += "&".join([k+"="+str(v) for k,v in opt])

        return optstr

    def getFriends(self):

        content = self.__makeRequest(Splitwise.GET_FRIENDS_URL)
        content = json.loads(content.decode("utf-8"))

        friends = []
        if "friends" in content:
            for f in content["friends"]:
                friends.append(Friend(f))

        return friends

    def getGroups(self):

        content = self.__makeRequest(Splitwise.GET_GROUPS_URL)
        content = json.loads(content.decode("utf-8"))

        groups = []
        if "groups" in content:
            for g in content["groups"]:
                groups.append(Group(g))

        return groups

    def getCurrencies(self):

        content = self.__makeRequest(Splitwise.GET_CURRENCY_URL)
        content = json.loads(content.decode("utf-8"))

        currencies = []
        if "currencies" in content:
            for c in content["currencies"]:
                currencies.append(Currency(c))

        return currencies

    def getCategories(self):

        content = self.__makeRequest(Splitwise.GET_CATEGORY_URL)
        content = json.loads(content.decode("utf-8"))
        categories = []

        if "categories" in content:
            for c in content["categories"]:
                categories.append(Category(c))

        return categories

    def getGroup(self,id=0):

        content = self.__makeRequest(Splitwise.GET_GROUP_URL+"/"+str(id))
        content = json.loads(content.decode("utf-8"))
        group = None
        if "group" in content:
            group = Group(content["group"])

        return group

    def getExpenses(self,offset=None,limit=None,group_id=None,friendship_id=None,dated_after=None,dated_before=None,updated_after=None,updated_before=None):

        options = {}

        #Copy of the locals is created as if I directly work on
        #locals and create variables in the loop a dictionary changed
        #error is thrown. Refer to bug #2 on Github
        localCopy = dict(locals())
        params = localCopy.keys()
        for param in params:
            if param != 'self' and param != 'options' and localCopy.get(param) is not None:
                options[param] = localCopy.get(param)

        url = Splitwise.GET_EXPENSES_URL

        url += self.__prepareOptionsUrl(options)
        content = self.__makeRequest(url)
        content = json.loads(content.decode("utf-8"))
        expenses = []
        if "expenses" in content:
            for e in content["expenses"]:
                expenses.append(Expense(e))

        return expenses

    def getExpense(self,id):
        content = self.__makeRequest(Splitwise.GET_EXPENSE_URL+"/"+str(id))
        content = json.loads(content.decode("utf-8"))
        expense = None
        if "expense" in content:
            expense = Expense(content["expense"])

        return expense
