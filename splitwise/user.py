from splitwise.picture import Picture
from splitwise.balance import Balance
import splitwise.group as Group


class User(object):

    def __init__(self,data=None):

        if data:
            self.first_name = data["first_name"]
            self.last_name  = data["last_name"]

            if 'id' in data:
                self.id = data["id"]
            else:
                self.id = None

            if 'email' in data:
                self.email  = data["email"]
            else:
                self.email  = None

            if 'registration_status' in data:
                self.registration_status = data["registration_status"]
            else:
                self.registration_status = None

            if 'picture' in data:
                self.picture = Picture(data["picture"])
            else:
                self.picture = None

    def getId(self):
        return self.id

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getEmail(self):
        return self.email

    def getRegistrationStatus(self):
        return self.registration_status

    def getPicture(self):
        return self.picture

    def setFirstName(self,first_name):
        self.first_name = first_name

    def setLastName(self,last_name):
        self.last_name = last_name

    def setEmail(self,email):
        self.email = email

    def setId(self,id):
        self.id = id



class CurrentUser(User):

    def __init__(self,data=None):
        User.__init__(self,data)
        self.default_currency = data["default_currency"]
        self.locale = data["locale"]
        self.date_format = data["date_format"]
        self.default_group_id = data["default_group_id"]


    def getDefaultCurrency(self):
        return self.default_currency

    def getLocale(self):
        return self.locale

    def getDateFormat(self):
        return self.date_format

    def getDefaultGroupId(self):
        return self.default_group_id


class Friend(User):

    def __init__(self,data=None):
        User.__init__(self,data)

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
        return self.updated_at


    def getBalances(self):
        return self.balances

    def getGroups(self):
        return self.groups

class ExpenseUser(User):

    def __init__(self,data=None):

        if data:
            User.__init__(self,data["user"])

            self.paid_share  = data["paid_share"]
            self.owed_share  = data["owed_share"]
            self.net_balance = data["net_balance"]


    def getPaidShare(self):
        return self.paid_share

    def getOwedShare(self):
        return self.owed_share

    def getNetBalance(self):
        return self.net_balance

    def setPaidShare(self,paid_share):
        self.paid_share = paid_share

    def setOwedShare(self,owed_share):
        self.owed_share = owed_share
