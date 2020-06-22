class SplitwiseError(object):

    def __init__(self, data=None):
        if data:
            self.errors = data

    def getErrors(self):
        return self.errors
