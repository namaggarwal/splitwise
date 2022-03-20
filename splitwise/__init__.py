"""Splitwise Python SDK

Splitwise Python SDK provides a simple interface to access splitwise APIs

    Typical usage:

    >>> s = Splitwise("consumer_key", "consumer_secret")
    >>> s.setAccessToken(access_token)
    >>> s.getCurrentUser().getId()
    78322
    >>> expense = Expense()
    >>> expense.setGroupId("19433671")
    >>> expense.setSplitEqually()
    >>> expense.setCost("10")
    >>> created_expense, errors = s.createExpense(expense)
    >>> created_expense.getId()
    897763

"""
import json
import io
from splitwise.user import User, Friend, CurrentUser
from splitwise.currency import Currency
from splitwise.group import Group
from splitwise.category import Category
from splitwise.expense import Expense
from splitwise.comment import Comment
from splitwise.error import SplitwiseError
from requests_oauthlib import OAuth1, OAuth2Session, OAuth2
from requests import Request, sessions
from splitwise.exception import (SplitwiseException,
                                 SplitwiseUnauthorizedException,
                                 SplitwiseBadRequestException,
                                 SplitwiseNotAllowedException,
                                 SplitwiseNotFoundException
                                 )

from .__version__ import __version__  # noqa: F401

try:
    from urlparse import parse_qs  # Python 2.x
    from urllib import urlencode
except ImportError:  # Python 3
    from urllib.parse import parse_qs, urlencode


class Splitwise(object):
    """ The Splitwise class that provides all the functionality.

    Attributes:
        consumer_key(str): Consumer Key provided by Splitwise.
        consumer_secret(str): Consumer Secret provided by Splitwise.
        auth(:obj:`requests.AuthBase`, optional): A request.AuthBase object that defines an auth.
    """

    SPLITWISE_BASE_URL = "https://secure.splitwise.com/"
    SPLITWISE_VERSION = "v3.0"
    OAUTH_BASE_URL = "https://www.splitwise.com/"
    # URLs to make the request
    REQUEST_TOKEN_URL = SPLITWISE_BASE_URL+"api/" + \
        SPLITWISE_VERSION+"/get_request_token"
    ACCESS_TOKEN_URL = SPLITWISE_BASE_URL+"api/" + \
        SPLITWISE_VERSION+"/get_access_token"
    AUTHORIZE_URL = SPLITWISE_BASE_URL + \
        "authorize"
    OAUTH_AUTHORIZE_URL = OAUTH_BASE_URL + "oauth/" \
        "authorize"
    OAUTH2_TOKEN_URL = OAUTH_BASE_URL + "oauth/" \
        "token"
    GET_CURRENT_USER_URL = SPLITWISE_BASE_URL + \
        "api/"+SPLITWISE_VERSION+"/get_current_user"
    GET_USER_URL = SPLITWISE_BASE_URL + \
        "api/"+SPLITWISE_VERSION+"/get_user"
    UPDATE_USER_URL = SPLITWISE_BASE_URL + \
        "api/"+SPLITWISE_VERSION+"/update_user"
    GET_FRIENDS_URL = SPLITWISE_BASE_URL + \
        "api/"+SPLITWISE_VERSION+"/get_friends"
    GET_GROUPS_URL = SPLITWISE_BASE_URL + \
        "api/"+SPLITWISE_VERSION+"/get_groups"
    GET_GROUP_URL = SPLITWISE_BASE_URL + \
        "api/"+SPLITWISE_VERSION+"/get_group"
    GET_CURRENCY_URL = SPLITWISE_BASE_URL + \
        "api/"+SPLITWISE_VERSION+"/get_currencies"
    GET_CATEGORY_URL = SPLITWISE_BASE_URL + \
        "api/"+SPLITWISE_VERSION+"/get_categories"
    GET_EXPENSES_URL = SPLITWISE_BASE_URL + \
        "api/"+SPLITWISE_VERSION+"/get_expenses"
    GET_EXPENSE_URL = SPLITWISE_BASE_URL + \
        "api/"+SPLITWISE_VERSION+"/get_expense"
    CREATE_EXPENSE_URL = SPLITWISE_BASE_URL + \
        "api/"+SPLITWISE_VERSION+"/create_expense"
    UPDATE_EXPENSE_URL = SPLITWISE_BASE_URL + \
        "api/" + SPLITWISE_VERSION + "/update_expense"
    DELETE_EXPENSE_URL = SPLITWISE_BASE_URL + \
        "api/"+SPLITWISE_VERSION+"/delete_expense"
    CREATE_GROUP_URL = SPLITWISE_BASE_URL + \
        "api/"+SPLITWISE_VERSION+"/create_group"
    ADD_USER_TO_GROUP_URL = SPLITWISE_BASE_URL + \
        "api/"+SPLITWISE_VERSION+"/add_user_to_group"
    DELETE_GROUP_URL = SPLITWISE_BASE_URL + \
        "api/"+SPLITWISE_VERSION+"/delete_group"
    GET_COMMENTS_URL = SPLITWISE_BASE_URL + \
        "api/"+SPLITWISE_VERSION+"/get_comments"
    CREATE_COMMENT_URL = SPLITWISE_BASE_URL + \
        "api/"+SPLITWISE_VERSION+"/create_comment"

    debug = False

    def __init__(self, consumer_key, consumer_secret, access_token=None, oauth2_access_token=None, api_key=None):
        """

        Args:
            consumer_key(str): Consumer Key provided by Spliwise
            consumer_secret(str): Consumer Secret provided by Splitwise
            access_token(:obj:`dict`, optional): Access Token is a combination of
                                        oauth_token and oauth_token_secret
            oauth2_access_token(:obj:`dict`, optional): OAuth2 Access Token is a combination of
                                        access_token and token_type
            api_key(str, optional):  API key provided by Splitwise

        """
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.auth = None
        self.api_key = api_key
        # If access token is present then set the Access token
        if access_token:
            self.setAccessToken(access_token)

        if oauth2_access_token:
            self.setOAuth2AccessToken(oauth2_access_token)

    def getOAuth2AuthorizeURL(self, redirect_uri, state=None):
        """ Provides the Authorize URL for end user's authentication

        Returns:
            tuple: tuple containing:
              auth_url(str): URL that user should be redirected to for authorization

              oauth_token_secret(str): Token secret that should be saved to redeem token
        """
        oauth = OAuth2Session(self.consumer_key, redirect_uri=redirect_uri, state=state)
        authorization_url, state = oauth.authorization_url(Splitwise.OAUTH_AUTHORIZE_URL)

        return authorization_url, state

    def getAuthorizeURL(self):
        """ Provides the Authorize URL for end user's authentication

        Returns:
            tuple: tuple containing:
              auth_url(str): URL that user should be redirected to for authorization

              oauth_token_secret(str): Token secret that should be saved to redeem token
        """
        oauth1 = OAuth1(
            self.consumer_key,
            client_secret=self.consumer_secret
        )

        content = self.__makeRequest(Splitwise.REQUEST_TOKEN_URL, method='POST', auth=oauth1)
        credentials = parse_qs(content)

        return "%s?oauth_token=%s" % (
            Splitwise.AUTHORIZE_URL, credentials.get('oauth_token')[0]
        ), credentials.get('oauth_token_secret')[0]

    def getOAuth2AccessToken(self, code, redirect_uri):
        """ Provides the OAuth1.0 access token

        Args:
            code(str): code from the query param after redirect
            redirect_uri(str): Redirect uri specified while getting code

        Returns:
            dict: dict containing:
              access_token(str): The OAuth 2.0 token

              token_type(str): The OAuth 2.0 token type
        """
        data = "client_id=%s&client_secret=%s&grant_type=authorization_code&code=%s&redirect_uri=%s" % (
            self.consumer_key, self.consumer_secret, code, redirect_uri)

        content = self.__makeRequest(Splitwise.OAUTH2_TOKEN_URL, 'POST', data=data)
        if content == "false":
            return None

        content = json.loads(content)
        return content

    def getAccessToken(self, oauth_token, oauth_token_secret, oauth_verifier):
        """ Provides the OAuth1.0 access token

        Args:
            oauth_token(str): The OAuth 1.0 token got from the redirect URL
            oauth_token_secret(str): The OAuth 1.0 token secret got while generating the auth URL
            oauth_verifier(str): The OAuth 1.0 token verifier got from the redirect URL

        Returns:
            dict: dict containing:
              oauth_token(str): The OAuth 1.0 token

              oauth_token_secret(str): The OAuth 1.0 token secret
        """
        oauth1 = OAuth1(
            self.consumer_key,
            client_secret=self.consumer_secret,
            resource_owner_key=oauth_token,
            resource_owner_secret=oauth_token_secret,
            verifier=oauth_verifier
        )

        try:
            content = self.__makeRequest(Splitwise.ACCESS_TOKEN_URL, 'POST', auth=oauth1)
        except SplitwiseUnauthorizedException as e:
            e.setMessage("Your oauth token could be expired or check your consumer id and secret")
            raise

        credentials = parse_qs(content)
        return {
            "oauth_token": credentials.get("oauth_token")[0],
            "oauth_token_secret": credentials.get("oauth_token_secret")[0],
        }

    def setAccessToken(self, access_token):
        """ Sets the OAuth1.0 access token, this should be done to make any authorized calls

        Args:
            access_token(:obj:`dict`): dict containing

                                oauth_token(str): The OAuth 1.0 token

                                oauth_token_secret(str): The OAuth 1.0 token secret

        """
        oauth1 = OAuth1(self.consumer_key,
                        client_secret=self.consumer_secret,
                        resource_owner_key=access_token['oauth_token'],
                        resource_owner_secret=access_token['oauth_token_secret'])

        self.auth = oauth1

    def setOAuth2AccessToken(self, access_token):
        """ Sets the OAuth2.0 access token, this should be done to make any authorized calls

        Args:
            access_token(:obj:`dict`): dict containing

                                access_token(str): The OAuth 2.0 token

                                token_type(str): The OAuth 2.0 token type


        """
        oauth2 = OAuth2(self.consumer_key,
                        token=access_token)

        self.auth = oauth2

    def __makeRequest(self, url, method="GET", data=None, auth=None, files=None):
        headers = {}

        if auth is None:
            if self.auth:
                auth = self.auth
            elif self.api_key:
                headers = {'Authorization': 'Bearer {}'.format(self.api_key)}

        requestObj = Request(method=method, url=url, headers=headers, data=data, auth=auth, files=files)

        prep_req = requestObj.prepare()

        with sessions.Session() as session:
            response = session.send(prep_req)

        if response.status_code == 200:
            if (response.content and hasattr(response.content, "decode")):
                return response.content.decode("utf-8")
            return response.content

        if response.status_code == 401:
            raise SplitwiseUnauthorizedException("Please check your token or consumer id and secret", response=response)

        if response.status_code == 403:
            raise SplitwiseNotAllowedException("You are not allowed to perform this operation", response=response)

        if response.status_code == 400:
            raise SplitwiseBadRequestException("Please check your request", response=response)

        if response.status_code == 404:
            raise SplitwiseNotFoundException("Required resource is not found", response)

        raise SplitwiseException("Unknown error happened", response)

    def __prepareOptionsUrl(self, options={}):
        return "?"+urlencode(options)

    def getCurrentUser(self):
        """ Gets the current authorized user's data

        Returns:
            :obj:`splitwise.user.CurrentUser`: CurrentUser object containing user data
        """
        content = self.__makeRequest(Splitwise.GET_CURRENT_USER_URL)
        content = json.loads(content)
        return CurrentUser(content["user"])

    def getUser(self, id):
        """ Gets the friends user's data given the ids

        Args:
            id (long): ID of the user whose information is needed

        Returns:
            :obj:`splitwise.user.User`: User object containing user data
        """
        try:
            content = self.__makeRequest(Splitwise.GET_USER_URL + "/"+str(id))
        except SplitwiseNotAllowedException as e:
            e.setMessage("You are not allowed to fetch user with id %d" % id)
            raise
        except SplitwiseNotFoundException as e:
            e.setMessage("User with id %d does not exist" % id)
            raise

        content = json.loads(content)
        return User(content["user"])

    def updateUser(self, user):
        """ Updates the user.

        Args:
            :obj:`splitwise.user.CurrentUser`: User object with atleast id set

        Returns:
            tuple: tuple containing:
              user(:obj:`splitwise.user.CurrentUser`): Object with User detail

              errors(:obj:`splitwise.error.SplitwiseError`): Object representing errors
        """

        if user.getId() is None:
            raise SplitwiseBadRequestException("User ID is required to update user")

        user_data = user.__dict__

        try:
            content = self.__makeRequest(Splitwise.UPDATE_USER_URL, 'POST', user_data)
        except SplitwiseNotAllowedException as e:
            e.setMessage("You are not allowed to access user with id %d" % user.getId())
            raise
        except SplitwiseNotFoundException as e:
            e.setMessage("User with id %d does not exist" % user.getId())
            raise
        content = json.loads(content)

        user = None
        errors = None
        if "user" in content:
            if content["user"] is not None:
                user = CurrentUser(content["user"])

        if "errors" in content:
            if len(content['errors']) != 0:
                errors = SplitwiseError(content["errors"])

        return user, errors

    def getFriends(self):
        """ Gets the list of users friends.

        Returns:
            :obj:`list` of :obj:`splitwise.user.Friend`: List of Friends
        """
        content = self.__makeRequest(Splitwise.GET_FRIENDS_URL)
        content = json.loads(content)

        friends = []
        if "friends" in content:
            for f in content["friends"]:
                friends.append(Friend(f))

        return friends

    def getGroups(self):
        """ Gets the list of groups a user is part of.

        Returns:
            :obj:`list` of :obj:`splitwise.group.Group`: List of Groups
        """
        content = self.__makeRequest(Splitwise.GET_GROUPS_URL)
        content = json.loads(content)

        groups = []
        if "groups" in content:
            for g in content["groups"]:
                groups.append(Group(g))

        return groups

    def getCurrencies(self):
        """ Gets the list of curriencies in Splitwise.

        Returns:
            :obj:`list` of :obj:`splitwise.currency.Currency`: List of Currency
        """
        content = self.__makeRequest(Splitwise.GET_CURRENCY_URL)
        content = json.loads(content)

        currencies = []
        if "currencies" in content:
            for c in content["currencies"]:
                currencies.append(Currency(c))

        return currencies

    def getCategories(self):
        """ Gets the list of categories in Splitwise.

        Returns:
            :obj:`list` of :obj:`splitwise.category.Category`: List of Category
        """
        content = self.__makeRequest(Splitwise.GET_CATEGORY_URL)
        content = json.loads(content)
        categories = []

        if "categories" in content:
            for c in content["categories"]:
                categories.append(Category(c))

        return categories

    def getGroup(self, id=0):
        """ Gets the detail of particular group a user is part of.

        Args:
            id(long, optional): ID of the group. Default value is 0, and means non-group expenses

        Returns:
            :obj:`splitwise.group.Group`: Object representing a group
        """
        try:
            content = self.__makeRequest(Splitwise.GET_GROUP_URL+"/"+str(id))
        except SplitwiseNotAllowedException as e:
            e.setMessage("You are not allowed to fetch group with id %d" % id)
            raise
        except SplitwiseNotFoundException as e:
            e.setMessage("Group with id %d does not exist" % id)
            raise

        content = json.loads(content)
        group = None
        if "group" in content:
            group = Group(content["group"])

        return group

    def getExpenses(self,
                    offset=None,
                    limit=None,
                    group_id=None,
                    friend=None,
                    dated_after=None,
                    dated_before=None,
                    updated_after=None,
                    updated_before=None
                    ):
        """ Gets the list of expenses given parameters.

        Args:
            offset(int, optional): Number of expenses to be skipped
            limit(int, optional): Number of expenses to be returned
            group_id(long, optional): GroupID of the expenses
            friend_id(long, optional): FriendshipID of the expenses
            dated_after(str, optional): ISO 8601 Date time. Return expenses later that this date
            dated_before(str, optional): ISO 8601 Date time. Return expenses earlier than this date
            updated_after(str, optional): ISO 8601 Date time. Return expenses updated after this date
            updated_before(str, optional): ISO 8601 Date time. Return expenses updated before this date

        Returns:
            :obj:`list` of :obj:`splitwise.expense.Expense`: List of Expense
        """

        options = {}

        # Copy of the locals is created as if I directly work on
        # locals and create variables in the loop a dictionary changed
        # error is thrown. Refer to bug #2 on Github
        localCopy = dict(locals())
        params = localCopy.keys()
        for param in params:
            if param != 'self' and param != 'options' and localCopy.get(param) is not None:
                options[param] = localCopy.get(param)

        url = Splitwise.GET_EXPENSES_URL

        url += self.__prepareOptionsUrl(options)
        content = self.__makeRequest(url)
        content = json.loads(content)
        expenses = []
        if "expenses" in content:
            for e in content["expenses"]:
                expenses.append(Expense(e))

        return expenses

    def getExpense(self, id):
        """ Gets the detail of the expense given the expense id.

        Args:
            id(long, optional): ID of the expense.

        Returns:
            :obj:`splitwise.expense.Expense`: Object representing an expense
        """
        content = self.__makeRequest(Splitwise.GET_EXPENSE_URL+"/"+str(id))
        content = json.loads(content)
        expense = None
        if "expense" in content:
            expense = Expense(content["expense"])

        return expense

    def createExpense(self, expense):
        """ Creates a new expense.

        Args:
            expense(:obj:`splitwise.expense.Expense`): Splitwise Expense Object.

        Returns:
            tuple: tuple containing:
              expense(:obj:`splitwise.expense.Expense`): Object with Expense detail

              errors(:obj:`splitwise.error.SplitwiseError`): Object representing errors
        """
        # Get the expense Dict
        expense_data = expense.__dict__

        # Get users and store in a separate var
        expense_users = expense.getUsers()

        if expense_users:
            # Delete users from original dict as we
            # need to put like users_1_
            del expense_data['users']
            # Add user values to expense_data
            Splitwise.setUserArray(expense_users, expense_data)

        category = expense.getCategory()
        if category:
            expense_data["category_id"] = category.getId()

        receipt = expense.getReceiptPath()
        files = None
        if receipt:
            files = {"receipt":  io.open(receipt, "rb")}

        content = self.__makeRequest(
            Splitwise.CREATE_EXPENSE_URL, "POST", expense_data, files=files)
        content = json.loads(content)
        expense = None
        errors = None

        if files:
            files["receipt"].close()

        if 'expenses' in content:
            if len(content['expenses']) > 0:
                expense = Expense(content["expenses"][0])

        if 'errors' in content:
            if len(content['errors']) != 0:
                errors = SplitwiseError(content['errors'])

        return expense, errors

    def updateExpense(self, expense):
        """ Updates an existing expense.

        Args:
            expense(:obj:`splitwise.expense.Expense`): Splitwise Expense Object.
            expense id must be set. Include only the fields that should be updated. null fields are ignored

        Returns:
            tuple: tuple containing:
              expense(:obj:`splitwise.expense.Expense`): Object with Expense detail

              errors(:obj:`splitwise.error.SplitwiseError`): Object representing errors
        """
        expense_id = expense.id
        if expense_id is None:
            raise SplitwiseBadRequestException("Incorrect query parameters sent. Expense Id cannot be null")

        # Get the expense Dict
        expense_data = expense.__dict__

        del expense_data['id']

        # Get users and store in a separate var
        expense_users = expense.getUsers()

        if expense_users:
            # Delete users from original dict as we
            # need to put like users_1_
            del expense_data['users']
            # Add user values to expense_data
            Splitwise.setUserArray(expense_users, expense_data)

        category = expense.getCategory()
        if category:
            expense_data["category_id"] = category.getId()

        receipt = expense.getReceiptPath()
        files = None
        if receipt:
            files = {"receipt":  io.open(receipt, "rb")}

        content = self.__makeRequest(
            Splitwise.UPDATE_EXPENSE_URL+"/"+str(expense_id), "POST", expense_data, files=files)
        content = json.loads(content)
        expense = None
        errors = None

        if files:
            files["receipt"].close()

        if 'expenses' in content:
            if len(content['expenses']) > 0:
                expense = Expense(content["expenses"][0])

        if 'errors' in content:
            if len(content['errors']) != 0:
                errors = SplitwiseError(content['errors'])

        return expense, errors

    def deleteExpense(self, id):
        """ Deletes the expense with given id.

        Args:
            id(long): ID of the expense to be deleted.

        Returns:
            tuple: tuple containing:
              success(bool): True if group deleted, False otherwise

              errors(:obj:`splitwise.error.SplitwiseError`): Object representing errors
        """
        errors = None
        success = False
        try:
            content = self.__makeRequest(
                Splitwise.DELETE_EXPENSE_URL+"/"+str(id), "POST")
        except SplitwiseNotAllowedException as e:
            e.setMessage("You are not allowed to access expense with id %d" % id)
            raise
        except SplitwiseNotFoundException as e:
            e.setMessage("Expense with id %d does not exist" % id)
            raise

        content = json.loads(content)
        if 'success' in content:
            success = content["success"]

        if 'errors' in content:
            if len(content['errors']) != 0:
                errors = SplitwiseError(content['errors'])

        return success, errors

    def createGroup(self, group):
        """ Creates a new Group.

        Args:
            group(:obj:`splitwise.group.Group`): Splitwise Group Object.

        Returns:
            tuple: tuple containing:
              group(:obj:`splitwise.group.Group`): Object with Group detail

              errors(:obj:`splitwise.error.SplitwiseError`): Object representing errors
        """
        # create group
        group_info = group.__dict__

        if "members" in group_info:
            group_members = group.getMembers()
            del group_info["members"]
            Splitwise.setUserArray(group_members, group_info)

        content = self.__makeRequest(
            Splitwise.CREATE_GROUP_URL, "POST", group_info)
        content = json.loads(content)
        group_detail = None
        errors = None
        if "group" in content:
            group_detail = Group(content["group"])
            if "errors" in content["group"]:
                if len(content["group"]['errors']) != 0:
                    errors = SplitwiseError(content["group"]["errors"])

        return group_detail, errors

    def addUserToGroup(self, user, group_id):
        """ Adds a user to the group.

        Args:
            user(:obj:`splitwise.user.User`): User to be added
            group_id(long): ID of the group

        Returns:
            tuple: tuple containing:
              success(bool): True if group deleted, False otherwise

              user(:obj:`splitwise.user.Friend`): Object representing added user details

              errors(:obj:`splitwise.error.SplitwiseError`): Object representing errors
        """
        # Get the user data
        request_data = user.__dict__
        request_data["group_id"] = group_id

        if "id" in request_data:
            request_data["user_id"] = request_data["id"]
            del request_data["id"]
        try:
            content = self.__makeRequest(
                Splitwise.ADD_USER_TO_GROUP_URL, "POST", request_data)
        except SplitwiseNotAllowedException as e:
            e.setMessage("You are not allowed to access group with id %d" % group_id)
            raise
        except SplitwiseNotFoundException as e:
            e.setMessage("Group with id %d does not exist" % group_id)
            raise
        content = json.loads(content)
        errors = None
        success = False
        user = None
        if 'success' in content:
            success = content["success"]

        if 'errors' in content:
            if len(content['errors']) != 0:
                errors = SplitwiseError(content['errors'])

        if 'user' in content:
            if content['user'] is not None:
                user = Friend(content['user'])

        return success, user, errors

    def deleteGroup(self, id):
        """ Deletes the group with given id.

        Args:
            id(long): ID of the group to be deleted.

        Returns:
            tuple: tuple containing:
              success(bool): True if group deleted, False otherwise

              errors(:obj:`splitwise.error.SplitwiseError`): Object representing errors
        """
        errors = None
        success = False
        try:
            content = self.__makeRequest(
                Splitwise.DELETE_GROUP_URL+"/"+str(id), "POST")
        except SplitwiseNotAllowedException as e:
            e.setMessage("You are not allowed to access group with id %d" % id)
            raise
        except SplitwiseNotFoundException as e:
            e.setMessage("Group with id %d does not exist" % id)
            raise

        content = json.loads(content)
        if 'success' in content:
            success = content["success"]

        if 'errors' in content:
            if len(content['errors']) != 0:
                errors = SplitwiseError(content['errors'])

        return success, errors

    @staticmethod
    def setUserArray(users, user_array):
        for count, user in enumerate(users):
            user_dict = user.__dict__
            for key in user_dict:
                if key == "id":
                    gen_key = "user_id"
                else:
                    gen_key = key
                user_array["users__" +
                           str(count) + "__" + gen_key] = user_dict[key]

    def getComments(self, expense_id):
        """
        Get expense comments.

        Args:
            expense_id(long): Expense Id

        Returns:
            :obj:`splitwise.comment.Comment`: Object representing a comment
        """

        try:
            content = self.__makeRequest(Splitwise.GET_COMMENTS_URL + "?expense_id=" + str(expense_id))
        except SplitwiseNotAllowedException as e:
            e.setMessage("You are not allowed to fetch user with id %d" % expense_id)
            raise
        except SplitwiseNotFoundException as e:
            e.setMessage("Expense with id %d does not exist" % expense_id)
            raise

        content = json.loads(content)
        comments = []
        if "comments" in content:
            for c in content["comments"]:
                comments.append(Comment(c))

        return comments

    def createComment(self, expense_id, content):
        """ Creates a new comment.

        Args:
            expense_id: Expense transaction on which a comment has to be made
            comment content: Content of the comment

        Returns:
            tuple: tuple containing:
              comment(:obj:`splitwise.comment.Comment`): Object with Comment detail

              errors(:obj:`splitwise.error.SplitwiseError`): Object representing errors
        """

        comment = None
        errors = None

        if content is None:
            raise SplitwiseBadRequestException("Incorrect query parameters sent. git statContent cannot be empty")

        data = dict()
        data["expense_id"] = expense_id
        data["content"] = content

        try:
            content = self.__makeRequest(
                Splitwise.CREATE_COMMENT_URL, "POST", data)
        except SplitwiseNotAllowedException as e:
            e.setMessage("You are not allowed to access expense with id %d" % id)
            raise
        except SplitwiseNotFoundException as e:
            e.setMessage("Expense with id %d does not exist" % id)

        content = json.loads(content)

        if 'comment' in content:
            if len(content['comment']) > 0:
                comment = Comment(content['comment'])

        if 'errors' in content:
            if len(content['errors']) != 0:
                errors = SplitwiseError(content['errors'])

        return comment, errors
