class Receipt(object):
    """ Receipt of an expense.

    Attributes:
        original(str): Link to original receipt
        large(str): Link to large size receipt
    """
    def __init__(self, data):
        self.original = data["original"]
        self.large = data["large"]

    def getOriginal(self):
        """ Returns the link to original size picture of the receipt

        Returns:
            str: Link to original size picture of the receipt
        """
        return self.original

    def getLarge(self):
        """ Returns the link to large size picture of the receipt

        Returns:
            str: Link to large size picture of the receipt
        """
        return self.large
