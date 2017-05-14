class Debt(object):

    def __init__(self,data=None):

        self.fromUser = data["from"]
        self.toUser   = data["to"]
        self.amount = data["amount"]
        if "currency_code" in data:
            self.currency_code = data["currency_code"]
        else:
            self.currency_code = None


    def getFromUser(self):
        return self.fromUser

    def getToUser(self):
        return self.toUser

    def getAmount(self):
        return self.amount

    def getCurrencyCode(self):
        return self.currency_code
