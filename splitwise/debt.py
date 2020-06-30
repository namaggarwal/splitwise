class Debt(object):
    """ Debt of an expense/group.

    Attributes:
        from(long): UserID of the user who paid
        to(long): UserID of the user who owes
        amount(str): Amount of the debt
        currency_code(str, optional): Currency code of the debt
    """
    def __init__(self, data=None):
        """
          Args:
              data(:obj:`json`, optional): JSON object representing debt
        """
        self.fromUser = data["from"]
        self.toUser = data["to"]
        self.amount = data["amount"]
        if "currency_code" in data:
            self.currency_code = data["currency_code"]
        else:
            self.currency_code = None

    def getFromUser(self):
        """ Returns the from user in the debt

        Returns:
            long: From user in the debt
        """
        return self.fromUser

    def getToUser(self):
        """ Returns the to user in the debt

        Returns:
            long: To user in the debt
        """
        return self.toUser

    def getAmount(self):
        """ Returns the amount in the debt

        Returns:
            long: Amount in the debt
        """
        return self.amount

    def getCurrencyCode(self):
        """ Returns the currency code in the debt

        Returns:
            long: Currency code in the debt
        """
        return self.currency_code
