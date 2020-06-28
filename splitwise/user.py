from splitwise.picture import Picture
from splitwise.balance import Balance
import splitwise.group as Group


class User(object):
    """ Contains basic user data.

    Attributes:
        id(long, optional): ID of the user
        first_name(str, optional): First name of the user
        last_name(str, optional): Last name of the user
        email(str, optional): Email of the user
        registration_status(str, optional): Registration status of the user
        picture(:obj:`splitwise.picture.Picture`, optional): Profile picture of the user
    """
    def __init__(self, data=None):
        """
          Args:
              data(:obj:`json`, optional): JSON object representing user object
        """
        if data:
            self.first_name = data["first_name"]
            self.last_name = data["last_name"]

            if 'id' in data:
                self.id = data["id"]
            else:
                self.id = None

            if 'email' in data:
                self.email = data["email"]
            else:
                self.email = None

            if 'registration_status' in data:
                self.registration_status = data["registration_status"]
            else:
                self.registration_status = None

            if 'picture' in data:
                self.picture = Picture(data["picture"])
            else:
                self.picture = None

    def getId(self):
        """ Returns id of the user

        Returns:
            long: ID of the user
        """
        return self.id

    def getFirstName(self):
        """ Returns first name of the user

        Returns:
            str: First name of the user
        """
        return self.first_name

    def getLastName(self):
        """ Returns last name of the user

        Returns:
            str: Last name of the user
        """
        return self.last_name

    def getEmail(self):
        """ Returns email of the user

        Returns:
            str: Email of the user
        """
        return self.email

    def getRegistrationStatus(self):
        """ Returns registration status of the user

        Returns:
            str: Registration status of the user
        """
        return self.registration_status

    def getPicture(self):
        """ Returns profile picture of the user

        Returns:
            :obj:`splitwise.picture.Picture`: Picture of the user
        """
        return self.picture

    def setFirstName(self, first_name):
        """ Sets the first name of the user

        Agrs:
            first_name(str): First name of the user
        """
        self.first_name = first_name

    def setLastName(self, last_name):
        """ Sets the last name of the user

        Agrs:
            last_name(str): Last name of the user
        """
        self.last_name = last_name

    def setEmail(self, email):
        """ Sets the email of the user

        Agrs:
            email(str): Email of the user
        """
        self.email = email

    def setId(self, id):
        """ Sets the id of the user

        Agrs:
            id(long): ID of the user
        """
        self.id = id


class CurrentUser(User):
    """ Represents the current logged in user.

    Inherits: :class:`splitwise.user.User`

    Attributes:
        default_currency(str, optional): Default Currency
        locale(str, optional): Locale
        date_format(str, optional): Date format used by the user
        default_group_id(long, optional): User's default group id
    """
    def __init__(self, data=None):
        """
          Args:
              data(:obj:`json`, optional): JSON object representing current user object
        """
        User.__init__(self, data)
        self.default_currency = data["default_currency"]
        self.locale = data["locale"]
        self.date_format = data["date_format"]
        self.default_group_id = data["default_group_id"]

    def getDefaultCurrency(self):
        """ Returns default currency of the user

        Returns:
            str: Default currency of the user
        """
        return self.default_currency

    def getLocale(self):
        """ Returns locale of the user

        Returns:
            str: locale of the user
        """
        return self.locale

    def getDateFormat(self):
        """ Returns Date format used by the user

        Returns:
            str: Date format used by the user
        """
        return self.date_format

    def getDefaultGroupId(self):
        """ Returns default group id the user

        Returns:
            long: default group id the user
        """
        return self.default_group_id


class Friend(User):
    """ Represents a friend user.

    Inherits: :class:`splitwise.user.User`

    Attributes:
        balances(:obj:`list` of :obj:`splitwise.balance.Balance`, optional): List of balances
        groups(:obj:`list` of :obj:`splitwise.group.FriendGroup`, optional): List of groups
        updated_at(str, optional): ISO 8601 Date time. The last updated date time of user
    """
    def __init__(self, data=None):
        """
          Args:
              data(:obj:`json`, optional): JSON object representing friend user object
        """
        User.__init__(self, data)

        if data:
            if 'updated_at' in data:
                self.updated_at = data["updated_at"]
            else:
                self.updated_at = None

            self.balances = []

            for balance in data["balance"]:
                self.balances.append(Balance(balance))

            self.groups = []
            if "groups" in data:
                for group in data["groups"]:
                    self.groups.append(Group.FriendGroup(group))
            else:
                self.groups = None

    def getUpdatedAt(self):
        """ Returns last updated date of the user

        Returns:
            str: last updated date of the user
        """
        return self.updated_at

    def getBalances(self):
        """ Returns balances of the user

        Returns:
            :obj:`list` of :obj:`splitwise.balance.Balance`: List of balances
        """
        return self.balances

    def getGroups(self):
        """ Returns balances of the user

        Returns:
            :obj:`list` of :obj:`splitwise.group.Group`: List of groups
        """
        return self.groups


class ExpenseUser(User):
    """ Represents a user in an expense.

    Inherits: :class:`splitwise.user.User`

    Attributes:
        paid_share(str, optional): Paid share for the expense
        owed_share(str, optional): Owed share for the expense
        net_balance(str, optional): Net balance for the expense
    """
    def __init__(self, data=None):
        """
          Args:
              data(:obj:`json`, optional): JSON object representing user object
        """
        if data:
            User.__init__(self, data["user"])

            self.paid_share = data["paid_share"]
            self.owed_share = data["owed_share"]
            self.net_balance = data["net_balance"]

    def getPaidShare(self):
        """ Returns paid share of the user

        Returns:
            str: paid share of the user
        """
        return self.paid_share

    def getOwedShare(self):
        """ Returns owed share of the user

        Returns:
            str: owed share of the user
        """
        return self.owed_share

    def getNetBalance(self):
        """ Returns net balance of the user

        Returns:
            str: net balance of the user
        """
        return self.net_balance

    def setPaidShare(self, paid_share):
        """ Sets the paid share of the user

        Args:
            paid_share(str): Paid share share of the user
        """
        self.paid_share = paid_share

    def setOwedShare(self, owed_share):
        """ Sets the owed share of the user

        Args:
            owed_share(str): Owed share share of the user
        """
        self.owed_share = owed_share
