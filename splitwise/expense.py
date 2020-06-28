from splitwise.debt import Debt
from splitwise.user import User, ExpenseUser
from splitwise.receipt import Receipt
from splitwise.category import Category


class Expense(object):
    """ Expense in Splitwise

    Attributes:
        id(long, optional): ID of the expense
        group_id(long, optional): GroupID of the expense
        description(str, optional): Description of the expense
        repeats(bool, optional): True if expense repeats, false otherwise
        repeat_interval(str, optional): Repeat interval of the expense
        email_reminder(bool, optional): True if email reminder is set, false otherwise
        email_reminder_in_advance(int, optional): Days of email reminder
        next_repeat(str, optional): Date of next repeat
        details(str, optional): Additional details of the expense
        comments_count(int, optional): Comment count of the expense
        payment(bool, optional): Is payment done
        creation_method(str, optional): Creation method
        transaction_method(str, optional): Transaction method
        transaction_confirmed(bool, optional): Is Transaction confirmed or not
        cost(str, optional): Amount of the expense
        currency_code(str, optional): Currency code of the expense
        created_by(:obj:`splitwise.user.User`, optional): User who created the expense
        date(str, optional): Date of the expense
        created_at(str, optional): Creation date of the expense
        updated_at(str, optional): Last updation date of the expense
        deleted_at(str, optional): Deletion date of the expense
        receipt(:obj:`splitwise.receipt.Receipt`, optional): Receipt of the expense
        category(:obj:`splitwise.category.Category`, optional): Category of the expense
        updated_by(:obj:`splitwise.user.User`, optional): User who updated the expense
        deleted_by(:obj:`splitwise.user.User`, optional): User who deleted the expense
        friendship_id(long, optional): Friendship id of the users in expense
        expense_bundle_id(long, optional): Expense bundle id of the expense
        repayments(:obj:`list` of :obj:`splitwise.debt.Debt`, optional): List of repayments expressed as Debt
        user(:obj:`list` of :obj:`splitwise.user.ExpenseUser`, optional): List of users with balances
        transaction_id(long, optional): Transaction id of the expense
    """
    def __init__(self, data=None):
        """
          Args:
              data(:obj:`json`, optional): JSON object representing expense
        """
        if data:
            self.id = data["id"]
            self.group_id = data["group_id"]
            self.description = data["description"]
            self.repeats = data["repeats"]
            self.repeat_interval = data["repeat_interval"]
            self.email_reminder = data["email_reminder"]
            self.email_reminder_in_advance = data["email_reminder_in_advance"]
            self.next_repeat = data["next_repeat"]
            self.details = data["details"]
            self.comments_count = data["comments_count"]
            self.payment = data["payment"]
            self.creation_method = data["creation_method"]
            self.transaction_method = data["transaction_method"]
            self.transaction_confirmed = data["transaction_confirmed"]
            self.cost = data["cost"]
            self.currency_code = data["currency_code"]
            self.created_by = User(data["created_by"])
            self.date = data["date"]
            self.created_at = data["created_at"]
            self.updated_at = data["updated_at"]
            self.deleted_at = data["deleted_at"]
            self.receipt = Receipt(data["receipt"])
            self.category = Category(data["category"])

            if data["updated_by"] is not None:
                self.updated_by = User(data["updated_by"])
            else:
                self.updated_by = None

            if data["deleted_by"] is not None:
                self.deleted_by = User(data["deleted_by"])
            else:
                self.deleted_by = None

            if "friendship_id" in data:
                self.friendship_id = data["friendship_id"]
            else:
                self.friendship_id = None

            if "expense_bundle_id" in data:
                self.expense_bundle_id = data["expense_bundle_id"]
            else:
                self.expense_bundle_id = None

            self.repayments = []
            for repayment in data["repayments"]:
                self.repayments.append(Debt(repayment))

            self.users = []
            for user in data["users"]:
                self.users.append(ExpenseUser(user))

            if "transaction_id" in data:
                self.transaction_id = data["transaction_id"]
            else:
                self.transaction_id = None

    def getId(self):
        """ Returns the ID of the expense

        Returns:
            long: ID of the expense
        """
        return self.id

    def getGroupId(self):
        """ Returns the GroupID of the expense

        Returns:
            long: GroupID of the expense
        """
        return self.group_id

    def getDescription(self):
        """ Returns the Description of the expense

        Returns:
            str: Description of the expense
        """
        return self.description

    def isRepeat(self):
        """ Returns if expense repeats

        Returns:
            bool: True if expense repeats, False otherwise
        """
        return self.repeats

    def getRepeatInterval(self):
        """ Returns the repeat interval of the expense

        Returns:
            str: Repeat interval of expense
        """
        return self.repeat_interval

    def getEmailReminder(self):
        """ Returns if email reminder is set

        Returns:
            bool: True if email reminder is set, False otherwise
        """
        return self.email_reminder

    def getEmailReminderInAdvance(self):
        """ Returns the email reminder in advance of the expense

        Returns:
            int: email reminder in advance of expense
        """
        return self.email_reminder_in_advance

    def getNextRepeat(self):
        """ Returns the next repeat of the expense

        Returns:
            str: next repeat of expense
        """
        return self.next_repeat

    def getDetails(self):
        """ Returns the details of the expense

        Returns:
            str: details of expense
        """
        return self.details

    def getCommentsCount(self):
        """ Returns the comment count of the expense

        Returns:
            int: comment count of expense
        """
        return self.comments_count

    def getPayment(self):
        """ Returns if payment is done in expense

        Returns:
            bool: True if payment done, False otherwise
        """
        return self.payment

    def getCreationMethod(self):
        """ Returns the creation method of the expense

        Returns:
            str: creation method of expense
        """
        return self.creation_method

    def getTransactionMethod(self):
        """ Returns the transaction method of the expense

        Returns:
            str: transaction method of expense
        """
        return self.transaction_method

    def getTransactionConfirmed(self):
        """ Returns if transaction is confirmed in expense

        Returns:
            bool: True if transaction confirmed, False otherwise
        """
        return self.transaction_confirmed

    def getCost(self):
        """ Returns the amount of the expense

        Returns:
            str: amount of expense
        """
        return self.cost

    def getCurrencyCode(self):
        """ Returns the currency code of the expense

        Returns:
            str: currency code of expense
        """
        return self.currency_code

    def getCreatedBy(self):
        """ Returns the user who created the expense

        Returns:
            :obj:`splitwise.user.User`: User who created the expense
        """
        return self.created_by

    def getDate(self):
        """ Returns the date of the expense

        Returns:
            str: date of expense
        """
        return self.date

    def getCreatedAt(self):
        """ Returns the created at date of the expense

        Returns:
            str: created at date of expense
        """
        return self.created_at

    def getUpdatedAt(self):
        """ Returns the updated at date of the expense

        Returns:
            str: updated at date of expense
        """
        return self.updated_at

    def getDeletedAt(self):
        """ Returns the deleted at date of the expense

        Returns:
            str: deleted at date of expense
        """
        return self.deleted_at

    def getReceipt(self):
        """ Returns the receipt of the expense

        Returns:
            :obj:`splitwise.receipt.Receipt`: receipt of the expense
        """
        return self.receipt

    def getCategory(self):
        """ Returns the category of the expense

        Returns:
            :obj:`splitwise.category.Category`: category of the expense
        """
        return self.category

    def getUpdatedBy(self):
        """ Returns the user who updated the expense

        Returns:
            :obj:`splitwise.user.User`: User who updated the expense
        """
        return self.updated_by

    def getDeletedBy(self):
        """ Returns the user who deleted the expense

        Returns:
            :obj:`splitwise.user.User`: User who deleted the expense
        """
        return self.deleted_by

    def getUsers(self):
        """ Returns the list of users in the expense along with balance

        Returns:
            :obj:`list` of :obj:`splitwise.user.ExpenseUser`: list of users in the expense along with balance
        """
        return self.users

    def getExpenseBundleId(self):
        """ Returns the expense bundle id of the expense

        Returns:
            long: expense bundle id of expense
        """
        return self.expense_bundle_id

    def getFriendshipId(self):
        """ Returns the friendship id of the expense

        Returns:
            long: friendship id of expense
        """
        return self.friendship_id

    def getRepayments(self):
        return self.repayments

    def setGroupId(self, id):
        self.group_id = id

    def setDescription(self, desc):
        self.description = desc

    def setPayment(self, payment):
        self.payment = payment

    def setCost(self, cost):
        self.cost = cost

    def setFriendshipId(self, f_id):
        self.friendship_id = f_id

    def setCreationMethod(self, creation_method):
        self.creation_method = creation_method

    def setDate(self, date):
        self.date = date

    def setRepeatInterval(self, repeat_interval):
        self.repeat_interval = repeat_interval

    def setCurrencyCode(self, currency_code):
        self.currency_code = currency_code

    def setCategory(self, category):
        self.category = category

    def setUsers(self, users):
        self.users = users

    def addUser(self, user):
        if not self.users:
            self.users = []
        self.users.append(user)

    def setSplitEqually(self, shouldSplit=True):
        self.split_equally = shouldSplit

    def getTransactionId(self):
        return self.transaction_id

    def __getattr__(self, item):
        return None
