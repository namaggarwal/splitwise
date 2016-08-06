class Currency(object):

    def __init__(self,data=None):

        self.code = data["currency_code"]
        self.unit = data["unit"]


    def getCode(self):
        return self.code

    def getUnit(self):
        return self.unit
