from splitwise.user import User


class Comment(object):
    """
    Contains comments made on an expense

    Attributes:
        id(long): Comment Id
        content(string): Comment posted
        comment_type(string): User
        relation_type(string): ExpenseComment
        relation_id(long): Expense Id
        created_at(datetime): Comment creation datetime
        deleted_at(datetime, optional): Comment deletion datetime
        user: Author of the comment


    """
    def __init__(self, data=None):
        """
          Args:
              data(:obj:`json`, optional): JSON object representing comment object
        """

        if data:
            self.id = data["id"]
            self.content = data["content"]
            self.comment_type = data["comment_type"]
            self.relation_type = data["relation_type"]
            self.relation_id = data["relation_id"]
            self.created_at = data["created_at"]
            self.deleted_at = data["deleted_at"]
            self.user = User(data["user"])

    def getId(self):
        """ Returns comment's Id

        Returns:
            str: Comment's Id
        """

        return self.id

    def getContent(self):
        """ Returns comment message

        Returns:
            str: Content of the comment
        """

        return self.content

    def getCommentType(self):
        """ Returns comment type

        Returns:
            str: Comment type
        """

        return self.comment_type

    def getRelationType(self):
        """ Returns relation type of the comment

        Returns:
            str: Relation type of the comment
        """

        return self.relation_type

    def getRelationId(self):
        """ Returns relation id

        Returns:
            str: Relation Id
        """

        return self.relation_id

    def getCreatedAt(self):
        """ Returns datetime at which comment was created

        Returns:
            datetime: Comment's creation date
        """

        return self.created_at

    def getDeletedAt(self):
        """ Returns datetime at which comment was deleted

        Returns:
            datetime: Comment's deletion date
        """

        return self.deleted_at

    def getCommentedUser(self):
        """ Returns commented user's details

        Returns:
            :obj:`splitwise.user.User`: Commented user object
        """

        return self.user
