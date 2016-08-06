class Receipt(object):

    def __init__(self,data=None):

        self.original = data["original"]
        self.large    = data["large"]

    def getOriginal(self):
        return self.original

    def getLarge(self):
        return self.large
