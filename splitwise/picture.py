class Picture(object):
    """ Profile picture of the user.

    Attributes:
        small(str, optional): Link to small size picture
        medium(str, optional): Link to medium size picture
        large(str, optional): Link to large size picture
    """
    def __init__(self, data=None):
        """
          Args:
              data(:obj:`json`, optional): JSON object representing picture object
        """
        if data:
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
        """ Returns the link to small size picture of the user

        Returns:
            str: Link to small size picture of the user
        """
        return self.small

    def getMedium(self):
        """ Returns the link to medium size picture of the user

        Returns:
            str: Link to medium size picture of the user
        """
        return self.medium

    def getLarge(self):
        """ Returns the link to large size picture of the user

        Returns:
            str: Link to large size picture of the user
        """
        return self.large
