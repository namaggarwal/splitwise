class Currency(object):
    """ Currency in splitwise.

    Attributes:
        code(str): Code of the currency
        unit(str): Unit of the currency
    """
    def __init__(self, data=None):
        """
          Args:
              data(:obj:`json`, optional): JSON object representing currency object
        """
        self.code = data["currency_code"]
        self.unit = data["unit"]

    def getCode(self):
        """ Returns the code of the currency

        Returns:
            str: code of the currency
        """
        return self.code

    def getUnit(self):
        """ Returns the unit of the currency

        Returns:
            str: unit of the currency
        """
        return self.unit
