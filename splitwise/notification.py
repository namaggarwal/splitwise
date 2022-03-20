class Notification(object):
    """
    Contains comments made on an expense
    Attributes:
        id(long): Notification Id
        content(string): Notification content
        type(long): Notification type
        image_url(string): Url
        image_shape(string): Shape of image
        created_at(datetime): Notification creation datetime
        created_by(long): User Id of the notification creator
        source: The related thing (ie, Expense)
    """
    def __init__(self, data=None):
        """
          Args:
              data(:obj:`json`, optional): JSON object representing comment object
        """

        if data:
            self.id = data["id"]
            self.content = data["content"]
            self.type = data["type"]
            self.created_at = data["created_at"]
            self.created_by = data["created_by"]
            self.image_shape = data["image_shape"]
            self.image_url = data["image_url"]
            self.source = data["source"]

    def getId(self):
        """ Returns Notifications's Id
        Returns:
            str: Notification's Id
        """

        return self.id

    def getContent(self):
        """ Returns message
        Returns:
            str: Content of the notification - text and HTML.
        """

        return self.content

    def getType(self):
        """ Returns Notification type
        Returns:
            long: Notification type
        """

        return self.type

    def getCreatedBy(self):
        """ Returns id who triggered Notification was created
        Returns:
            long: Notifications's creator id
        """

        return self.created_by

    def getCreatedAt(self):
        """ Returns datetime at which notification was created
        Returns:
            datetime: Notificaton's creation date
        """

        return self.created_at

    def getImageShape(self):
        """ Returns shape of image
        Returns:
            string: Image shape, ie square
        """

        return self.image_shape

    def getImageUrl(self):
        """ Returns url of image
        Returns:
            string: Image url
        """

        return self.image_url