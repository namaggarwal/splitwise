class Balance(object):
    """Balance for a particular user
    """
    def __init__(self,data=None):

        self.currency_code = data["currency_code"]
        self.amount        = data["amount"]


    def getCurrencyCode(self):
        return self.currency_code

    def getAmount(self):
        return self.amount
