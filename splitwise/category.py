class Category(object):
    """ Category in splitwise.

    Attributes:
        id(long): ID of the category
        name(str): Name of the category
        subcategories(:obj:`list` of :obj:`splitwise.category.Category`): Subcategories of this category
    """
    def __init__(self, data=None):
        """
          Args:
              data(:obj:`json`, optional): JSON object representing category object
        """
        if data:
            self.id = data["id"]
            self.name = data["name"]
            self.subcategories = []
            if "subcategories" in data:
                for sub in data["subcategories"]:
                    self.subcategories.append(Category(sub))

    def getId(self):
        """ Returns the id of the category

        Returns:
            long: ID of the category
        """
        return self.id

    def getName(self):
        """ Returns the name of the category

        Returns:
            str: name of the category
        """
        return self.name

    def getSubcategories(self):
        """ Returns the list of sub categories for the category

        Returns:
            :obj:`list` of :obj:`splitwise.category.Category`: List of sub categories
        """
        return self.subcategories

    def setId(self, id):
        """ Returns the id of the category

        Returns:
            long: id of the category
        """
        self.id = id
