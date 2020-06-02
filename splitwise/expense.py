from splitwise.debt import Debt
from splitwise.user import User,ExpenseUser
from splitwise.receipt import Receipt
from splitwise.category import Category

class Expense(object):

    def __init__(self,data=None):

        if data:

            self.id                        = data["id"]
            self.group_id                  = data["group_id"]
            self.description               = data["description"]
            self.repeats                   = data["repeats"]
            self.repeat_interval           = data["repeat_interval"]
            self.email_reminder            = data["email_reminder"]
            self.email_reminder_in_advance = data["email_reminder_in_advance"]
            self.next_repeat               = data["next_repeat"]
            self.details                   = data["details"]
            self.comments_count            = data["comments_count"]
            self.payment                   = data["payment"]
            self.creation_method           = data["creation_method"]
            self.transaction_method        = data["transaction_method"]
            self.transaction_confirmed     = data["transaction_confirmed"]
            self.cost                      = data["cost"]
            self.currency_code             = data["currency_code"]
            self.created_by                = User(data["created_by"])
            self.date                      = data["date"]
            self.created_at                = data["created_at"]
            self.updated_at                = data["updated_at"]
            self.deleted_at                = data["deleted_at"]
            self.receipt                   = Receipt(data["receipt"])
            self.category                  = Category(data["category"])

            if data["updated_by"] is not None:
                self.updated_by                = User(data["updated_by"])
            else:
                self.updated_by = None

            if data["deleted_by"] is not None:
                self.deleted_by                = User(data["deleted_by"])
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


    def getId(self):
        return self.id

    def getGroupId(self):
        return self.group_id

    def getDescription(self):
        return self.description

    def isRepeat(self):
        return self.repeats

    def getRepeatInterval(self):
        return self.repeat_interval

    def getEmailReminder(self):
        return self.email_reminder

    def getEmailReminderInAdvance(self):
        return self.email_reminder_in_advance

    def getNextRepeat(self):
        return self.next_repeat

    def getDetails(self):
        return self.details

    def getCommentsCount(self):
        return self.comments_count

    def getPayment(self):
        return self.payment

    def getCreationMethod(self):
        return self.creation_method

    def getTransactionMethod(self):
        return self.transaction_method

    def getTransactionConfirmed(self):
        return self.transaction_confirmed

    def getCost(self):
        return self.cost

    def getCurrencyCode(self):
        return self.currency_code

    def getCreatedBy(self):
        return self.created_by

    def getDate(self):
        return self.date

    def getCreatedAt(self):
        return self.created_at

    def getUpdatedAt(self):
        return self.updated_at

    def getDeletedAt(self):
        return self.deleted_at

    def getReceipt(self):
        return self.receipt

    def getCategory(self):
        return self.category

    def getUpdatedBy(self):
        return self.updated_by

    def getDeletedBy(self):
        return self.deleted_by

    def getUsers(self):
        return self.users

    def getExpenseBundleId(self):
        return self.expense_bundle_id

    def getFriendshipId(self):
        return self.friendship_id

    def getRepayments(self):
        return self.repayments

    def setGroupId(self,id):
        self.group_id = id

    def setDescription(self,desc):
        self.description = desc

    def setPayment(self,payment):
        self.payment = payment

    def setCost(self,cost):
        self.cost = cost

    def setFriendshipId(self,f_id):
        self.friendship_id = f_id

    def setCreationMethod(self,creation_method):
        self.creation_method = creation_method

    def setDate(self,date):
        self.date = date

    def setRepeatInterval(self,repeat_interval):
        self.repeat_interval = repeat_interval

    def setCurrencyCode(self,currency_code):
        self.currency_code = currency_code

    def setCategory(self,category):
        self.category = category

    def setUsers(self,users):
        self.users = users

    def __getattr__(self, item):
        return None
