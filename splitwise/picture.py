class Picture(object):


    def __init__(self, data=None):

        self.medium = data["medium"]

        if "small" in data:
            self.small = data["small"]
        else:
            self.small = None

        if "large" in data:
            self.large = data["large"]
        else:
            self.large = None

    def getSmall(self):
        return self.small

    def getMedium(self):
        return self.medium

    def getLarge(self):
        return self.large
