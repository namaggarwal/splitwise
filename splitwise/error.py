class SplitwiseError(object):
    """ Splitwise Error encapsulates the error.

    Attributes:
        errors(:obj:`json`): JSON object representing error
    """
    def __init__(self, data=None):
        """
          Args:
              data(:obj:`json`, optional): JSON object representing errors
        """
        if data:
            self.errors = data

    def getErrors(self):
        """ Returns the json errors object

        Returns:
            :obj:`json`: JSON error object
        """
        return self.errors
