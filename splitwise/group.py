from splitwise.debt import Debt
from splitwise.balance import Balance


class Group(object):
    """ Represents a splitwise group.

    Attributes:
        id(long, optional): ID of the group
        name(str, optional): Name of the group
        updated_at(str, optional): ISO 8601 Date time. The last updated date time of group
        created_at(str, optional): ISO 8601 Date time. The created date time of group
        simplify_by_default(bool, optional): Is Simplified expenses by default
        group_type(str, optional): Type of the group
        whiteboard(str, optional): Whiteboard of the group
        invite_link(str, optional): Invitation link of the group
        country_code(str, optional): Country of the group
        original_debts(:obj:`list` of :obj:`splitwise.debt.Debt`, optional): List of original debts
        simplfied_debts(:obj:`list` of :obj:`splitwise.debt.Debt`, optional): List of simplfied debts
        members(:obj:`list` of :obj:`splitwise.user.Friend`, optional): List of members of the group
    """
    def __init__(self, data=None):
        """
        Args:
            data(:obj:`json`, optional): JSON object representing group object
        """
        from splitwise.user import Friend

        if data:
            self.id = data["id"]
            self.name = data["name"]
            self.updated_at = data["updated_at"]
            self.created_at = data["created_at"]
            self.simplify_by_default = data["simplify_by_default"]

            if "group_type" in data:
                self.group_type = data["group_type"]
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
        """ Returns the id of the group

        Returns:
            long: ID of the group
        """
        return self.id

    def getName(self):
        """ Returns the name of the group

        Returns:
            str: name of the group
        """
        return self.name

    def getCreatedAt(self):
        """ Returns the ISO 8601 create date time of the group

        Returns:
            str: ISO 8601 create date time of the group
        """
        return self.created_at

    def getUpdatedAt(self):
        """ Returns the ISO 8601 update date time of the group

        Returns:
            str: ISO 8601 update date time of the group
        """
        return self.updated_at

    def getWhiteBoard(self):
        """ Returns the whiteboard of the group

        Returns:
            str: whiteboard of the group
        """
        return self.whiteboard

    def isSimplifiedByDefault(self):
        """ Returns if simplified by default

        Returns:
            bool: simplified by default
        """
        return self.simplify_by_default

    def getMembers(self):
        """ Returns the list of group members

        Returns:
            :obj:`list` of :obj:`splitwise.user.Friend`: List of members of the group
        """
        return self.members

    def getOriginalDebts(self):
        """ Returns the list of original debts

        Returns:
            :obj:`list` of :obj:`splitwise.debt.Debt`: List of original debt of the group
        """
        return self.original_debts

    def getType(self):
        """ Returns the type of the group

        Returns:
            str: type of the group
        """
        return self.group_type

    def getGroupType(self):
        """ Returns the type of the group

        Returns:
            str: type of the group
        """
        return self.group_type

    def getSimplifiedDebts(self):
        """ Returns the list of simplified debts

        Returns:
            :obj:`list` of :obj:`splitwise.debt.Debt`: List of simplified debt of the group
        """
        return self.simplified_debts

    def getInviteLink(self):
        """ Returns the invitation link of the group

        Returns:
            str: invitation link of the group
        """
        return self.invite_link

    def setName(self, name):
        """ Sets the name of the group

        Args:
            name(str): name of the group
        """
        self.name = name

    def setType(self, group_type):
        """ Sets the type of the group

        Args:
            group_type(str): type of the group
        """
        self.group_type = group_type

    def setGroupType(self, group_type):
        """ Sets the type of the group

        Args:
            group_type(str): type of the group
        """
        self.group_type = group_type

    def setWhiteBoard(self, whiteboard):
        """ Sets the whiteboard of the group

        Args:
            whiteboard(str): whiteboard of the group
        """
        self.whiteboard = whiteboard

    def setCountryCode(self, country_code):
        """ Sets the country code of the group

        Args:
            country_code(str): country code of the group
        """
        self.country_code = country_code

    def setMembers(self, members):
        """ Sets the members of the group

        Args:
            members(:obj:`list` of :obj:`splitwise.user.Friend`): list of members of the group
        """
        self.members = members

    def addMember(self, member):
        """ Adds a member to the group

        Args:
            member(:obj:`splitwise.user.Friend`): members of the group
        """
        if not hasattr(self, 'members'):
            self.members = []
        self.members.append(member)


class FriendGroup(object):
    """ Simplified Group while representing a Friend.

    Attributes:
        id(long, optional): ID of the group
        balances(:obj:`list` of :obj:`splitwise.balance.Balance`, optional): List of balances of the group
    """
    def __init__(self, data=None):
        """
        Args:
            data(:obj:`json`, optional): JSON object representing group
        """
        if data:
            self.id = data["group_id"]
            self.balances = []
            for balance in data["balance"]:
                self.balances.append(Balance(balance))

    def setId(self, id):
        """ Sets the id of the group

        Args:
            id(long): ID of the group
        """
        self.id = id

    def getId(self):
        """ Returns the id of the group

        Returns:
            long: ID of the group
        """
        return self.id

    def getBalances(self):
        """ Returns the balances of the group

        Returns:
            :obj:`list` of :obj:`splitwise.balance.Balance`: Balances of the group
        """
        return self.balances
