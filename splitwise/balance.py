class Balance(object):
    """ Balance of an expense/group.

    Attributes:
        currency_code(str): Currency code of the balance
        amount(str): Amount of the balance
    """
    def __init__(self, data=None):
        """
          Args:
              data(:obj:`json`, optional): JSON object representing balance
        """
        self.currency_code = data["currency_code"]
        self.amount = data["amount"]

    def getCurrencyCode(self):
        """ Returns the currency code of the balance

        Returns:
            str: Currency code of the balance
        """
        return self.currency_code

    def getAmount(self):
        """ Returns the amount of the balance

        Returns:
            str: Amount of the balance
        """
        return self.amount
