from splitwise import Splitwise, SplitwiseBadRequestException
from splitwise.expense import Expense, ExpenseUser
import unittest
try:
    from unittest.mock import patch, MagicMock
except ImportError:  # Python 2
    from mock import patch, MagicMock


@patch('splitwise.Splitwise._Splitwise__makeRequest')
class UpdateExpenseTestCase(unittest.TestCase):

    def setUp(self):
        self.sObj = Splitwise('consumerkey', 'consumersecret')

    @patch('io.open')
    def test_updateExpense_split_equally_with_receipt_success(self, mockOpen, mockMakeRequest):
        mockFile = MagicMock()
        mockOpen.return_value = mockFile
        mockMakeRequest.return_value = '{"expenses":[{"id":1010906976,"group_id":19433671,"friendship_id":null,"expense_bundle_id":null,"description":"Testing","repeats":false,"repeat_interval":"never","email_reminder":false,"email_reminder_in_advance":-1,"next_repeat":null,"details":"Full details of the expense","comments_count":0,"payment":false,"creation_method":null,"transaction_method":"offline","transaction_confirmed":false,"transaction_id":null,"cost":"12.0","currency_code":"SGD","repayments":[{"from":643871,"to":79774,"amount":"5.0"}],"date":"2020-06-24T06:57:29Z","created_at":"2020-06-24T06:57:29Z","created_by":{"id":79774,"first_name":"Naman","last_name":"Aggarwal","picture":{"medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg"},"custom_picture":true},"updated_at":"2020-06-24T06:57:29Z","updated_by":null,"deleted_at":null,"deleted_by":null,"category":{"id":18,"name":"General"},"receipt":{"large":null,"original":null},"users":[{"user":{"id":79774,"first_name":"Naman","last_name":"Aggarwal","picture":{"medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg"}},"user_id":79774,"paid_share":"10.0","owed_share":"5.0","net_balance":"5.0"},{"user":{"id":643871,"first_name":"Shantanu","last_name":"Alshi","picture":{"medium":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-blue19-100px.png"}},"user_id":643871,"paid_share":"0.0","owed_share":"5.0","net_balance":"-5.0"}]}],"errors":{}}'  # noqa: E501
        expense = Expense()
        expense.id = 1010906976
        expense.setCost('12')
        expense.setDescription("Testing")
        expense.setDetails("Full details of the expense")
        expenseRes, errors = self.sObj.updateExpense(expense)
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/update_expense/1010906976", "POST",
            {'cost': '12', 'description': 'Testing', 'details': 'Full details of the expense'},
            files=None)
        self.assertIsNone(errors)
        self.assertEqual(expenseRes.getId(), 1010906976)
        self.assertEqual(expenseRes.getGroupId(), 19433671)
        self.assertEqual(expenseRes.getFriendshipId(), None)
        self.assertEqual(expenseRes.getExpenseBundleId(), None)
        self.assertEqual(expenseRes.getDescription(), "Testing")
        self.assertEqual(expenseRes.getRepeatInterval(), "never")
        self.assertEqual(expenseRes.getEmailReminderInAdvance(), -1)
        self.assertEqual(expenseRes.getNextRepeat(), None)
        self.assertEqual(expenseRes.getDetails(), "Full details of the expense")
        self.assertEqual(expenseRes.getCommentsCount(), 0)
        self.assertEqual(expenseRes.getCreationMethod(), None)
        self.assertEqual(expenseRes.getTransactionMethod(), "offline")
        self.assertEqual(expenseRes.getTransactionId(), None)
        self.assertEqual(expenseRes.getCost(), "12.0")
        self.assertEqual(expenseRes.getCurrencyCode(), "SGD")
        self.assertEqual(len(expenseRes.getRepayments()), 1)
        self.assertEqual(expenseRes.getRepayments()[0].getFromUser(), 643871)
        self.assertEqual(expenseRes.getRepayments()[0].getToUser(), 79774)
        self.assertEqual(expenseRes.getRepayments()[0].getAmount(), "5.0")
        self.assertEqual(expenseRes.getDate(), "2020-06-24T06:57:29Z")
        self.assertEqual(expenseRes.getCreatedAt(), "2020-06-24T06:57:29Z")
        self.assertEqual(expenseRes.getCreatedBy().getId(), 79774)
        self.assertEqual(expenseRes.getCreatedBy().getFirstName(), "Naman")
        self.assertEqual(expenseRes.getCreatedBy().getLastName(), "Aggarwal")
        self.assertEqual(expenseRes.getCreatedBy().getPicture().getMedium(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg")
        self.assertEqual(expenseRes.getUpdatedAt(), "2020-06-24T06:57:29Z")
        self.assertEqual(expenseRes.getUpdatedBy(), None)
        self.assertEqual(expenseRes.getDeletedAt(), None)
        self.assertEqual(expenseRes.getDeletedBy(), None)
        self.assertEqual(expenseRes.getCategory().getId(), 18)
        self.assertEqual(expenseRes.getCategory().getName(), "General")
        self.assertEqual(expenseRes.getReceipt().getLarge(), None)
        self.assertEqual(expenseRes.getReceipt().getOriginal(), None)
        self.assertEqual(len(expenseRes.getUsers()), 2)
        self.assertEqual(expenseRes.getUsers()[0].getId(), 79774)
        self.assertEqual(expenseRes.getUsers()[0].getFirstName(), "Naman")
        self.assertEqual(expenseRes.getUsers()[0].getLastName(), "Aggarwal")
        self.assertEqual(expenseRes.getUsers()[0].getPicture().getMedium(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg")
        self.assertEqual(expenseRes.getUsers()[0].getPaidShare(), "10.0")
        self.assertEqual(expenseRes.getUsers()[0].getOwedShare(), "5.0")
        self.assertEqual(expenseRes.getUsers()[0].getNetBalance(), "5.0")
        self.assertEqual(expenseRes.getUsers()[1].getId(), 643871)
        self.assertEqual(expenseRes.getUsers()[1].getFirstName(), "Shantanu")
        self.assertEqual(expenseRes.getUsers()[1].getLastName(), "Alshi")
        self.assertEqual(expenseRes.getUsers()[1].getPicture().getMedium(
        ), "https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-blue19-100px.png")
        self.assertEqual(expenseRes.getUsers()[1].getPaidShare(), "0.0")
        self.assertEqual(expenseRes.getUsers()[1].getOwedShare(), "5.0")
        self.assertEqual(expenseRes.getUsers()[1].getNetBalance(), "-5.0")

    def test_updateExpense_split_equally_success(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"expenses":[{"id":1010906976,"group_id":19433671,"friendship_id":null,"expense_bundle_id":null,"description":"Testing","repeats":false,"repeat_interval":"never","email_reminder":false,"email_reminder_in_advance":-1,"next_repeat":null,"details":"Full details of the expense","comments_count":0,"payment":false,"creation_method":null,"transaction_method":"offline","transaction_confirmed":false,"transaction_id":null,"cost":"13.0","currency_code":"SGD","repayments":[{"from":643871,"to":79774,"amount":"5.0"}],"date":"2020-06-24T06:57:29Z","created_at":"2020-06-24T06:57:29Z","created_by":{"id":79774,"first_name":"Naman","last_name":"Aggarwal","picture":{"medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg"},"custom_picture":true},"updated_at":"2020-06-24T06:57:29Z","updated_by":null,"deleted_at":null,"deleted_by":null,"category":{"id":18,"name":"General"},"receipt":{"large":null,"original":null},"users":[{"user":{"id":79774,"first_name":"Naman","last_name":"Aggarwal","picture":{"medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg"}},"user_id":79774,"paid_share":"10.0","owed_share":"5.0","net_balance":"5.0"},{"user":{"id":643871,"first_name":"Shantanu","last_name":"Alshi","picture":{"medium":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-blue19-100px.png"}},"user_id":643871,"paid_share":"0.0","owed_share":"5.0","net_balance":"-5.0"}]}],"errors":{}}'  # noqa: E501
        expense = Expense()
        expense.id = 1010906976
        expense.setCost('13')
        expense.setDescription("Testing")
        expense.setGroupId(19433671)
        expense.setDetails("Full details of the expense")
        expense.setSplitEqually()
        expenseRes, errors = self.sObj.updateExpense(expense)
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/update_expense/1010906976", "POST",
            {'cost': '13', 'description': 'Testing', 'details': 'Full details of the expense',
             'group_id': 19433671, 'split_equally': True}, files=None)
        self.assertIsNone(errors)
        self.assertEqual(expenseRes.getId(), 1010906976)
        self.assertEqual(expenseRes.getGroupId(), 19433671)
        self.assertEqual(expenseRes.getFriendshipId(), None)
        self.assertEqual(expenseRes.getExpenseBundleId(), None)
        self.assertEqual(expenseRes.getDescription(), "Testing")
        self.assertEqual(expenseRes.getRepeatInterval(), "never")
        self.assertEqual(expenseRes.getEmailReminderInAdvance(), -1)
        self.assertEqual(expenseRes.getNextRepeat(), None)
        self.assertEqual(expenseRes.getDetails(), "Full details of the expense")
        self.assertEqual(expenseRes.getCommentsCount(), 0)
        self.assertEqual(expenseRes.getCreationMethod(), None)
        self.assertEqual(expenseRes.getTransactionMethod(), "offline")
        self.assertEqual(expenseRes.getTransactionId(), None)
        self.assertEqual(expenseRes.getCost(), "13.0")
        self.assertEqual(expenseRes.getCurrencyCode(), "SGD")
        self.assertEqual(len(expenseRes.getRepayments()), 1)
        self.assertEqual(expenseRes.getRepayments()[0].getFromUser(), 643871)
        self.assertEqual(expenseRes.getRepayments()[0].getToUser(), 79774)
        self.assertEqual(expenseRes.getRepayments()[0].getAmount(), "5.0")
        self.assertEqual(expenseRes.getDate(), "2020-06-24T06:57:29Z")
        self.assertEqual(expenseRes.getCreatedAt(), "2020-06-24T06:57:29Z")
        self.assertEqual(expenseRes.getCreatedBy().getId(), 79774)
        self.assertEqual(expenseRes.getCreatedBy().getFirstName(), "Naman")
        self.assertEqual(expenseRes.getCreatedBy().getLastName(), "Aggarwal")
        self.assertEqual(expenseRes.getCreatedBy().getPicture().getMedium(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg")
        self.assertEqual(expenseRes.getUpdatedAt(), "2020-06-24T06:57:29Z")
        self.assertEqual(expenseRes.getUpdatedBy(), None)
        self.assertEqual(expenseRes.getDeletedAt(), None)
        self.assertEqual(expenseRes.getDeletedBy(), None)
        self.assertEqual(expenseRes.getCategory().getId(), 18)
        self.assertEqual(expenseRes.getCategory().getName(), "General")
        self.assertEqual(expenseRes.getReceipt().getLarge(), None)
        self.assertEqual(expenseRes.getReceipt().getOriginal(), None)
        self.assertEqual(len(expenseRes.getUsers()), 2)
        self.assertEqual(expenseRes.getUsers()[0].getId(), 79774)
        self.assertEqual(expenseRes.getUsers()[0].getFirstName(), "Naman")
        self.assertEqual(expenseRes.getUsers()[0].getLastName(), "Aggarwal")
        self.assertEqual(expenseRes.getUsers()[0].getPicture().getMedium(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg")
        self.assertEqual(expenseRes.getUsers()[0].getPaidShare(), "10.0")
        self.assertEqual(expenseRes.getUsers()[0].getOwedShare(), "5.0")
        self.assertEqual(expenseRes.getUsers()[0].getNetBalance(), "5.0")
        self.assertEqual(expenseRes.getUsers()[1].getId(), 643871)
        self.assertEqual(expenseRes.getUsers()[1].getFirstName(), "Shantanu")
        self.assertEqual(expenseRes.getUsers()[1].getLastName(), "Alshi")
        self.assertEqual(expenseRes.getUsers()[1].getPicture().getMedium(
        ), "https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-blue19-100px.png")
        self.assertEqual(expenseRes.getUsers()[1].getPaidShare(), "0.0")
        self.assertEqual(expenseRes.getUsers()[1].getOwedShare(), "5.0")
        self.assertEqual(expenseRes.getUsers()[1].getNetBalance(), "-5.0")

    def test_updateExpense_split_manually_success(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"expenses":[{"id":1010934284,"group_id":null,"friendship_id":null,"expense_bundle_id":null,"description":"Testing","repeats":false,"repeat_interval":"never","email_reminder":false,"email_reminder_in_advance":-1,"next_repeat":null,"details":null,"comments_count":0,"payment":false,"creation_method":null,"transaction_method":"offline","transaction_confirmed":false,"transaction_id":null,"cost":"10.0","currency_code":"SGD","repayments":[{"from":281236,"to":79774,"amount":"8.0"}],"date":"2020-06-24T08:14:07Z","created_at":"2020-06-24T08:14:07Z","created_by":{"id":79774,"first_name":"Naman","last_name":"Aggarwal","picture":{"medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg"},"custom_picture":true},"updated_at":"2020-06-24T08:14:07Z","updated_by":null,"deleted_at":null,"deleted_by":null,"category":{"id":18,"name":"General"},"receipt":{"large":null,"original":null},"users":[{"user":{"id":79774,"first_name":"Naman","last_name":"Aggarwal","picture":{"medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg"}},"user_id":79774,"paid_share":"10.0","owed_share":"2.0","net_balance":"8.0"},{"user":{"id":281236,"first_name":"Siddharth","last_name":"Goel","picture":{"medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/medium_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg"}},"user_id":281236,"paid_share":"0.0","owed_share":"8.0","net_balance":"-8.0"}]}],"errors":{}}'  # noqa: E501
        expense = Expense()
        expense.id = 1010934284
        expense.setCost('10')
        expense.setDescription("Testing")
        user1 = ExpenseUser()
        user1.setId(79774)
        user1.setPaidShare('10.00')
        user1.setOwedShare('2.0')
        user2 = ExpenseUser()
        user2.setId(281236)
        user2.setPaidShare('0.00')
        user2.setOwedShare('8.00')
        users = []
        users.append(user1)
        users.append(user2)
        expense.setUsers(users)
        expenseRes, errors = self.sObj.updateExpense(expense)
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/update_expense/1010934284", "POST",
            {'cost': '10',
             'description': 'Testing',
             'users__0__user_id': 79774,
             'users__0__paid_share': '10.00',
             'users__0__owed_share': '2.0',
             'users__1__user_id': 281236,
             'users__1__paid_share': '0.00',
             'users__1__owed_share': '8.00'
             }, files=None)
        self.assertIsNone(errors)
        self.assertEqual(expenseRes.getId(), 1010934284)
        self.assertEqual(expenseRes.getGroupId(), None)
        self.assertEqual(expenseRes.getFriendshipId(), None)
        self.assertEqual(expenseRes.getExpenseBundleId(), None)
        self.assertEqual(expenseRes.getDescription(), "Testing")
        self.assertEqual(expenseRes.getRepeatInterval(), "never")
        self.assertEqual(expenseRes.getEmailReminderInAdvance(), -1)
        self.assertEqual(expenseRes.getNextRepeat(), None)
        self.assertEqual(expenseRes.getDetails(), None)
        self.assertEqual(expenseRes.getCommentsCount(), 0)
        self.assertEqual(expenseRes.getCreationMethod(), None)
        self.assertEqual(expenseRes.getTransactionMethod(), "offline")
        self.assertEqual(expenseRes.getTransactionId(), None)
        self.assertEqual(expenseRes.getCost(), "10.0")
        self.assertEqual(expenseRes.getCurrencyCode(), "SGD")
        self.assertEqual(len(expenseRes.getRepayments()), 1)
        self.assertEqual(expenseRes.getRepayments()[0].getFromUser(), 281236)
        self.assertEqual(expenseRes.getRepayments()[0].getToUser(), 79774)
        self.assertEqual(expenseRes.getRepayments()[0].getAmount(), "8.0")
        self.assertEqual(expenseRes.getDate(), "2020-06-24T08:14:07Z")
        self.assertEqual(expenseRes.getCreatedAt(), "2020-06-24T08:14:07Z")
        self.assertEqual(expenseRes.getCreatedBy().getId(), 79774)
        self.assertEqual(expenseRes.getCreatedBy().getFirstName(), "Naman")
        self.assertEqual(expenseRes.getCreatedBy().getLastName(), "Aggarwal")
        self.assertEqual(expenseRes.getCreatedBy().getPicture().getMedium(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg")
        self.assertEqual(expenseRes.getUpdatedAt(), "2020-06-24T08:14:07Z")
        self.assertEqual(expenseRes.getUpdatedBy(), None)
        self.assertEqual(expenseRes.getDeletedAt(), None)
        self.assertEqual(expenseRes.getDeletedBy(), None)
        self.assertEqual(expenseRes.getCategory().getId(), 18)
        self.assertEqual(expenseRes.getCategory().getName(), "General")
        self.assertEqual(expenseRes.getReceipt().getLarge(), None)
        self.assertEqual(expenseRes.getReceipt().getOriginal(), None)
        self.assertEqual(len(expenseRes.getUsers()), 2)
        self.assertEqual(expenseRes.getUsers()[0].getId(), 79774)
        self.assertEqual(expenseRes.getUsers()[0].getFirstName(), "Naman")
        self.assertEqual(expenseRes.getUsers()[0].getLastName(), "Aggarwal")
        self.assertEqual(expenseRes.getUsers()[0].getPicture().getMedium(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg")
        self.assertEqual(expenseRes.getUsers()[0].getPaidShare(), "10.0")
        self.assertEqual(expenseRes.getUsers()[0].getOwedShare(), "2.0")
        self.assertEqual(expenseRes.getUsers()[0].getNetBalance(), "8.0")
        self.assertEqual(expenseRes.getUsers()[1].getId(), 281236)
        self.assertEqual(expenseRes.getUsers()[1].getFirstName(), "Siddharth")
        self.assertEqual(expenseRes.getUsers()[1].getLastName(), "Goel")
        self.assertEqual(expenseRes.getUsers()[1].getPicture().getMedium(
        ), "https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/medium_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg")
        self.assertEqual(expenseRes.getUsers()[1].getPaidShare(), "0.0")
        self.assertEqual(expenseRes.getUsers()[1].getOwedShare(), "8.0")
        self.assertEqual(expenseRes.getUsers()[1].getNetBalance(), "-8.0")

    def test_updateExpense_error(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"expenses":[],"errors":{"base":["An unknown error occurred. Please try again or contact support@splitwise.com if you experience repeated issues. Sorry for the trouble!"]}}'  # noqa: E501
        expense = Expense()
        expense.id = 1010934284
        expense.setCost('10')
        expense.setDescription("Testing")
        user1 = ExpenseUser()
        user1.setId(79774)
        user1.setPaidShare('10.00')
        user1.setOwedShare('2.0')
        user2 = ExpenseUser()
        user2.setId(281236)
        user2.setPaidShare('0.00')
        user2.setOwedShare('8.00')
        users = []
        users.append(user1)
        users.append(user2)
        expense.setUsers(users)
        expenseRes, errors = self.sObj.updateExpense(expense)
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/update_expense/1010934284", "POST",
            {'cost': '10',
             'description': 'Testing',
             'users__0__user_id': 79774,
             'users__0__paid_share': '10.00',
             'users__0__owed_share': '2.0',
             'users__1__user_id': 281236,
             'users__1__paid_share': '0.00',
             'users__1__owed_share': '8.00'
             }, files=None)
        self.assertEqual(errors.getErrors(), {
            'base': [
                'An unknown error occurred. Please try again or contact support@splitwise.com if you experience repeated issues. \
Sorry for the trouble!'
            ]})

    def test_updateExpense_exception(self, mockMakeRequest):
        mockMakeRequest.side_effect = Exception(
            "Invalid response %s. Please check your consumer key and secret." % 404)
        expense = Expense()
        expense.id = 1010934284
        expense.setCost('10')
        expense.setDescription("Testing")
        user1 = ExpenseUser()
        user1.setId(79774)
        user1.setPaidShare('10.00')
        user1.setOwedShare('2.0')
        user2 = ExpenseUser()
        user2.setId(281236)
        user2.setPaidShare('0.00')
        user2.setOwedShare('8.00')
        users = []
        users.append(user1)
        users.append(user2)
        expense.setUsers(users)
        with self.assertRaises(Exception):
            expenseRes, errors = self.sObj.updateExpense(expense)
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/update_expense/1010934284", "POST",
            {'cost': '10',
             'description': 'Testing',
             'users__0__user_id': 79774,
             'users__0__paid_share': '10.00',
             'users__0__owed_share': '2.0',
             'users__1__user_id': 281236,
             'users__1__paid_share': '0.00',
             'users__1__owed_share': '8.00'
             }, files=None)

    def test_updateExpense_missingExpenseId_Exception(self, mockMakeRequest):
        mockMakeRequest.side_effect = SplitwiseBadRequestException(
            "Incorrect query parameters sent. Expense Id cannot be null")
        expense = Expense()
        expense.setCost('10')
        expense.setDescription("Testing")
        user1 = ExpenseUser()
        user1.setId(79774)
        user1.setPaidShare('10.00')
        user1.setOwedShare('2.0')
        user2 = ExpenseUser()
        user2.setId(281236)
        user2.setPaidShare('0.00')
        user2.setOwedShare('8.00')
        users = []
        users.append(user1)
        users.append(user2)
        expense.setUsers(users)
        with self.assertRaises(SplitwiseBadRequestException):
            expenseRes, errors = self.sObj.updateExpense(expense)
