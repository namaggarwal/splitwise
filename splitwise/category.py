class Category(object):

    def __init__(self,data=None):
        if data:
            self.id = data["id"]
            self.name = data["name"]
            self.subcategories = []
            if "subcategories" in data:
                for sub in data["subcategories"]:
                    self.subcategories.append(Category(sub))

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getSubcategories(self):
        return self.subcategories

    def setId(self, id):
        self.id = id
