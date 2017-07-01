from splitwise.debt import Debt
from splitwise.balance import Balance

class Group(object):

    def __init__(self,data=None):
        from splitwise.user import Friend

        if data:
            self.id            = data["id"]
            self.name          = data["name"]
            self.updated_at    = data["updated_at"]
            self.simplify_by_default = data["simplify_by_default"]

            if "group_type" in data:
                self.group_type    = data["group_type"]
            else:
                self.group_type = None
            if "whiteboard" in data:
                self.whiteboard = data["whiteboard"]
            else:
                self.whiteboard = None

            if "invite_link" in data:
                self.invite_link = data["invite_link"]
            else:
                self.invite_link = None

            if "country_code" in data:
                self.country_code = data["country_code"]
            else:
                self.country_code = None

            self.original_debts = []
            for debt in data["original_debts"]:
                self.original_debts.append(Debt(debt))

            self.simplified_debts = []
            for debt in data["simplified_debts"]:
                self.simplified_debts.append(Debt(debt))

            self.members = []
            for member in data["members"]:
                self.members.append(Friend(member))


    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getUpdatedAt(self):
        return self.updated_at

    def getWhiteBoard(self):
        return self.whiteboard

    def isSimplifiedByDefault(self):
        return self.simplify_by_default

    def getMembers(self):
        return self.members

    def getOriginalDebts(self):
        return self.original_debts

    def getType(self):
        return self.group_type

    def getSimplifiedDebts(self):
        return self.simplified_debts

    def getInviteLink(self):
        return self.invite_link

    def setName(self, name):
        self.name = name

    def setGroupType(self, group_type):
        self.group_type = group_type

    def setCountryCode(self, country_code):
        self.country_code = country_code

    def setMembers(self, members):
        self.members = members

class FriendGroup(object):


    def __init__(self,data=None):

        self.id = data["group_id"]
        self.balances = []
        for balance in data["balance"]:
            self.balances.append(Balance(balance))

    def getId(self):
        return self.id

    def getBalances(self):
        return self.balance
