import unittest
import os
from splitwise import Splitwise
from splitwise.expense import Expense
from splitwise.exception import SplitwiseUnauthorizedException


class ExpenseTestCase(unittest.TestCase):

    def setUp(self):
        consumer_key = os.environ['CONSUMER_KEY']
        consumer_secret = os.environ['CONSUMER_SECRET']
        oauth_token = os.environ['OAUTH_TOKEN']
        oauth_token_secret = os.environ['OAUTH_TOKEN_SECRET']

        self.sObj = Splitwise(consumer_key, consumer_secret)
        self.sObj.setAccessToken({'oauth_token': oauth_token, 'oauth_token_secret': oauth_token_secret})

    def test_expense_flow(self):
        receipt = os.path.join(os.path.dirname(os.path.realpath(__file__)), "receipt.jpg")
        expense = Expense()
        expense.setDescription("End2EndTest")
        expense.setCost('10')
        expense.setGroupId(19571167)
        expense.setSplitEqually()
        expense.setReceipt(receipt)
        # create expense
        expense, error = self.sObj.createExpense(expense)
        self.assertIsNone(error)
        self.assertIsNotNone(expense.getId())
        # update expense
        expense.setDescription("I am now new expense")
        expense, error = self.sObj.updateExpense(expense)
        self.assertIsNone(error)
        self.assertIsNotNone(expense.getId())
        self.assertEqual(expense.getDescription(), "I am now new expense")
        # delete expense
        success, error = self.sObj.deleteExpense(expense.getId())
        self.assertIsNone(error)
        self.assertTrue(success)

    def test_expense_update_independent_flow(self):
        receipt = os.path.join(os.path.dirname(os.path.realpath(__file__)), "receipt.jpg")
        expense = Expense()
        expense.setDescription("End2EndTest")
        expense.setCost('10')
        expense.setGroupId(19571167)
        expense.setSplitEqually()
        expense.setReceipt(receipt)
        # create expense
        expense, error = self.sObj.createExpense(expense)
        self.assertIsNone(error)
        self.assertIsNotNone(expense.getId())
        # update expense
        newexpense = Expense()
        newexpense.setId(expense.getId())
        newexpense.setDescription("End2EndTestUpdated")
        expense, error = self.sObj.updateExpense(newexpense)
        self.assertIsNone(error)
        self.assertIsNotNone(expense.getId())
        self.assertEqual(expense.getDescription(), "End2EndTestUpdated")
        # delete expense
        success, error = self.sObj.deleteExpense(expense.getId())
        self.assertIsNone(error)
        self.assertTrue(success)

    def test_expense_invalidkeys_fail(self):
        sObj = Splitwise('consumerkey', 'consumersecret', {"oauth_token": "sdsd", "oauth_token_secret": "sdsdd"})
        expense = Expense()
        with self.assertRaises(SplitwiseUnauthorizedException):
            sObj.createExpense(expense)

    def test_get_expenses_success(self):
        expenses = self.sObj.getExpenses(limit=2, group_id=19571167)
        self.assertEqual(len(expenses), 2)
