from splitwise import Splitwise
import unittest
try:
    from unittest.mock import patch
    from urllib.parse import parse_qs
    import urllib.parse as urlparse
except ImportError:  # Python 2
    from mock import patch
    from urlparse import parse_qs
    import urlparse


@patch('splitwise.Splitwise._Splitwise__makeRequest')
class GetExpensesTestCase(unittest.TestCase):

    def setUp(self):
        self.sObj = Splitwise('consumerkey', 'consumersecret')

    def test_getExpenses_limit_and_offset_success(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"expenses":[{"id":1010395720,"group_id":10843533,"friendship_id":null,"expense_bundle_id":null,"description":"Potato","repeats":false,"repeat_interval":"never","email_reminder":false,"email_reminder_in_advance":-1,"next_repeat":null,"details":null,"comments_count":0,"payment":false,"creation_method":"equal","transaction_method":"offline","transaction_confirmed":false,"transaction_id":null,"cost":"0.9","currency_code":"SGD","repayments":[{"from":281236,"to":79774,"amount":"0.3"},{"from":643871,"to":79774,"amount":"0.3"}],"date":"2020-06-23T09:32:56Z","created_at":"2020-06-23T09:33:05Z","created_by":{"id":79774,"first_name":"Naman","last_name":"Aggarwal","picture":{"medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg"},"custom_picture":true},"updated_at":"2020-06-23T09:33:05Z","updated_by":null,"deleted_at":null,"deleted_by":null,"category":{"id":12,"name":"Groceries"},"receipt":{"large":null,"original":null},"users":[{"user":{"id":79774,"first_name":"Naman","last_name":"Aggarwal","picture":{"medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg"}},"user_id":79774,"paid_share":"0.9","owed_share":"0.3","net_balance":"0.6"},{"user":{"id":281236,"first_name":"Siddharth","last_name":"Goel","picture":{"medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/medium_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg"}},"user_id":281236,"paid_share":"0.0","owed_share":"0.3","net_balance":"-0.3"},{"user":{"id":643871,"first_name":"Shantanu","last_name":"Alshi","picture":{"medium":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-blue19-100px.png"}},"user_id":643871,"paid_share":"0.0","owed_share":"0.3","net_balance":"-0.3"}]},{"id":1009711631,"group_id":10843533,"friendship_id":null,"expense_bundle_id":null,"description":"Mexican Dinner","repeats":false,"repeat_interval":"never","email_reminder":true,"email_reminder_in_advance":null,"next_repeat":null,"details":"","comments_count":0,"payment":false,"creation_method":"split","transaction_method":"offline","transaction_confirmed":false,"transaction_id":null,"cost":"32.7","currency_code":"SGD","repayments":[{"from":281236,"to":79774,"amount":"10.9"},{"from":643871,"to":79774,"amount":"10.9"}],"date":"2020-06-22T07:17:32Z","created_at":"2020-06-22T07:17:54Z","created_by":{"id":79774,"first_name":"Naman","last_name":"Aggarwal","picture":{"medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg"},"custom_picture":true},"updated_at":"2020-06-22T07:17:54Z","updated_by":null,"deleted_at":null,"deleted_by":null,"category":{"id":13,"name":"Dining out"},"receipt":{"large":null,"original":null},"users":[{"user":{"id":281236,"first_name":"Siddharth","last_name":"Goel","picture":{"medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/medium_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg"}},"user_id":281236,"paid_share":"0.0","owed_share":"10.9","net_balance":"-10.9"},{"user":{"id":643871,"first_name":"Shantanu","last_name":"Alshi","picture":{"medium":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-blue19-100px.png"}},"user_id":643871,"paid_share":"0.0","owed_share":"10.9","net_balance":"-10.9"},{"user":{"id":79774,"first_name":"Naman","last_name":"Aggarwal","picture":{"medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg"}},"user_id":79774,"paid_share":"32.7","owed_share":"10.9","net_balance":"21.8"}]}]}'.encode('utf-8')  # noqa: E501
        expenses = self.sObj.getExpenses(2, 3)
        args, kwargs = mockMakeRequest.call_args
        parsed = urlparse.urlparse(args[0])
        qs = parse_qs(parsed.query)
        self.assertEqual(qs['offset'], ['2'])
        self.assertEqual(qs['limit'], ['3'])
        self.assertEqual(len(expenses), 2)
        self.assertEqual(expenses[0].getId(), 1010395720)
        self.assertEqual(expenses[0].getGroupId(), 10843533)
        self.assertEqual(expenses[0].getFriendshipId(), None)
        self.assertEqual(expenses[0].getExpenseBundleId(), None)
        self.assertEqual(expenses[0].getDescription(), "Potato")
        self.assertEqual(expenses[0].getRepeatInterval(), "never")
        self.assertEqual(expenses[0].getEmailReminderInAdvance(), -1)
        self.assertEqual(expenses[0].getNextRepeat(), None)
        self.assertEqual(expenses[0].getDetails(), None)
        self.assertEqual(expenses[0].getCommentsCount(), 0)
        self.assertEqual(expenses[0].getCreationMethod(), "equal")
        self.assertEqual(expenses[0].getTransactionMethod(), "offline")
        # self.assertEqual(expenses[0].getTransactionId(), None)
        self.assertEqual(expenses[0].getCost(), "0.9")
        self.assertEqual(expenses[0].getCurrencyCode(), "SGD")
        self.assertEqual(len(expenses[0].getRepayments()), 2)
        self.assertEqual(expenses[0].getRepayments()[0].getFromUser(), 281236)
        self.assertEqual(expenses[0].getRepayments()[0].getToUser(), 79774)
        self.assertEqual(expenses[0].getRepayments()[0].getAmount(), "0.3")
        self.assertEqual(expenses[0].getRepayments()[1].getFromUser(), 643871)
        self.assertEqual(expenses[0].getRepayments()[1].getToUser(), 79774)
        self.assertEqual(expenses[0].getRepayments()[1].getAmount(), "0.3")
        self.assertEqual(expenses[0].getDate(), "2020-06-23T09:32:56Z")
        self.assertEqual(expenses[0].getCreatedAt(), "2020-06-23T09:33:05Z")
        self.assertEqual(expenses[0].getCreatedBy().getId(), 79774)
        self.assertEqual(expenses[0].getCreatedBy().getFirstName(), "Naman")
        self.assertEqual(expenses[0].getCreatedBy().getLastName(), "Aggarwal")
        self.assertEqual(expenses[0].getCreatedBy().getPicture().getMedium(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg")
        self.assertEqual(expenses[0].getUpdatedAt(), "2020-06-23T09:33:05Z")
        self.assertEqual(expenses[0].getUpdatedBy(), None)
        self.assertEqual(expenses[0].getDeletedAt(), None)
        self.assertEqual(expenses[0].getDeletedBy(), None)
        self.assertEqual(expenses[0].getCategory().getId(), 12)
        self.assertEqual(expenses[0].getCategory().getName(), "Groceries")
        self.assertEqual(expenses[0].getReceipt().getLarge(), None)
        self.assertEqual(expenses[0].getReceipt().getOriginal(), None)
        self.assertEqual(len(expenses[0].getUsers()), 3)
        self.assertEqual(expenses[0].getUsers()[0].getId(), 79774)
        self.assertEqual(expenses[0].getUsers()[0].getFirstName(), "Naman")
        self.assertEqual(expenses[0].getUsers()[0].getLastName(), "Aggarwal")
        self.assertEqual(expenses[0].getUsers()[0].getPicture().getMedium(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg")
        self.assertEqual(expenses[0].getUsers()[0].getPaidShare(), "0.9")
        self.assertEqual(expenses[0].getUsers()[0].getOwedShare(), "0.3")
        self.assertEqual(expenses[0].getUsers()[0].getNetBalance(), "0.6")
        self.assertEqual(expenses[0].getUsers()[1].getId(), 281236)
        self.assertEqual(expenses[0].getUsers()[1].getFirstName(), "Siddharth")
        self.assertEqual(expenses[0].getUsers()[1].getLastName(), "Goel")
        self.assertEqual(expenses[0].getUsers()[1].getPicture().getMedium(
        ), "https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/medium_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg")
        self.assertEqual(expenses[0].getUsers()[1].getPaidShare(), "0.0")
        self.assertEqual(expenses[0].getUsers()[1].getOwedShare(), "0.3")
        self.assertEqual(expenses[0].getUsers()[1].getNetBalance(), "-0.3")
        self.assertEqual(expenses[0].getUsers()[2].getId(), 643871)
        self.assertEqual(expenses[0].getUsers()[2].getFirstName(), "Shantanu")
        self.assertEqual(expenses[0].getUsers()[2].getLastName(), "Alshi")
        self.assertEqual(expenses[0].getUsers()[2].getPicture().getMedium(),
                         "https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-blue19-100px.png")
        self.assertEqual(expenses[0].getUsers()[2].getPaidShare(), "0.0")
        self.assertEqual(expenses[0].getUsers()[2].getOwedShare(), "0.3")
        self.assertEqual(expenses[0].getUsers()[2].getNetBalance(), "-0.3")
        self.assertEqual(expenses[1].getId(), 1009711631)
        self.assertEqual(expenses[1].getGroupId(), 10843533)
        self.assertEqual(expenses[1].getFriendshipId(), None)
        self.assertEqual(expenses[1].getExpenseBundleId(), None)
        self.assertEqual(expenses[1].getDescription(), "Mexican Dinner")
        self.assertEqual(expenses[1].getRepeatInterval(), "never")
        self.assertEqual(expenses[1].getEmailReminderInAdvance(), None)
        self.assertEqual(expenses[1].getNextRepeat(), None)
        self.assertEqual(expenses[1].getDetails(), "")
        self.assertEqual(expenses[1].getCommentsCount(), 0)
        self.assertEqual(expenses[1].getCreationMethod(), "split")
        self.assertEqual(expenses[1].getTransactionMethod(), "offline")
        # self.assertEqual(expenses[1].getTransactionId(), None)
        self.assertEqual(expenses[1].getCost(), "32.7")
        self.assertEqual(expenses[1].getCurrencyCode(), "SGD")
        self.assertEqual(len(expenses[1].getRepayments()), 2)
        self.assertEqual(expenses[1].getRepayments()[0].getFromUser(), 281236)
        self.assertEqual(expenses[1].getRepayments()[0].getToUser(), 79774)
        self.assertEqual(expenses[1].getRepayments()[0].getAmount(), "10.9")
        self.assertEqual(expenses[1].getRepayments()[1].getFromUser(), 643871)
        self.assertEqual(expenses[1].getRepayments()[1].getToUser(), 79774)
        self.assertEqual(expenses[1].getRepayments()[1].getAmount(), "10.9")
        self.assertEqual(expenses[1].getDate(), "2020-06-22T07:17:32Z")
        self.assertEqual(expenses[1].getCreatedAt(), "2020-06-22T07:17:54Z")
        self.assertEqual(expenses[1].getCreatedBy().getId(), 79774)
        self.assertEqual(expenses[1].getCreatedBy().getFirstName(), "Naman")
        self.assertEqual(expenses[1].getCreatedBy().getLastName(), "Aggarwal")
        self.assertEqual(expenses[1].getCreatedBy().getPicture().getMedium(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg")
        self.assertEqual(expenses[1].getUpdatedAt(), "2020-06-22T07:17:54Z")
        self.assertEqual(expenses[1].getUpdatedBy(), None)
        self.assertEqual(expenses[1].getDeletedAt(), None)
        self.assertEqual(expenses[1].getDeletedBy(), None)
        self.assertEqual(expenses[1].getCategory().getId(), 13)
        self.assertEqual(expenses[1].getCategory().getName(), "Dining out")
        self.assertEqual(expenses[1].getReceipt().getLarge(), None)
        self.assertEqual(expenses[1].getReceipt().getOriginal(), None)
        self.assertEqual(len(expenses[1].getUsers()), 3)
        self.assertEqual(expenses[1].getUsers()[0].getId(), 281236)
        self.assertEqual(expenses[1].getUsers()[0].getFirstName(), "Siddharth")
        self.assertEqual(expenses[1].getUsers()[0].getLastName(), "Goel")
        self.assertEqual(expenses[1].getUsers()[0].getPicture().getMedium(
        ), "https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/medium_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg")
        self.assertEqual(expenses[1].getUsers()[0].getPaidShare(), "0.0")
        self.assertEqual(expenses[1].getUsers()[0].getOwedShare(), "10.9")
        self.assertEqual(expenses[1].getUsers()[0].getNetBalance(), "-10.9")
        self.assertEqual(expenses[1].getUsers()[1].getId(), 643871)
        self.assertEqual(expenses[1].getUsers()[1].getFirstName(), "Shantanu")
        self.assertEqual(expenses[1].getUsers()[1].getLastName(), "Alshi")
        self.assertEqual(expenses[1].getUsers()[1].getPicture().getMedium(),
                         "https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-blue19-100px.png")
        self.assertEqual(expenses[1].getUsers()[1].getPaidShare(), "0.0")
        self.assertEqual(expenses[1].getUsers()[1].getOwedShare(), "10.9")
        self.assertEqual(expenses[1].getUsers()[1].getNetBalance(), "-10.9")
        self.assertEqual(expenses[1].getUsers()[2].getId(), 79774)
        self.assertEqual(expenses[1].getUsers()[2].getFirstName(), "Naman")
        self.assertEqual(expenses[1].getUsers()[2].getLastName(), "Aggarwal")
        self.assertEqual(expenses[1].getUsers()[2].getPicture().getMedium(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg")
        self.assertEqual(expenses[1].getUsers()[2].getPaidShare(), "32.7")
        self.assertEqual(expenses[1].getUsers()[2].getOwedShare(), "10.9")
        self.assertEqual(expenses[1].getUsers()[2].getNetBalance(), "21.8")

    def test_getExpenses_all_options_success(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"expenses":[{"id":1010395720,"group_id":10843533,"friendship_id":null,"expense_bundle_id":null,"description":"Potato","repeats":false,"repeat_interval":"never","email_reminder":false,"email_reminder_in_advance":-1,"next_repeat":null,"details":null,"comments_count":0,"payment":false,"creation_method":"equal","transaction_method":"offline","transaction_confirmed":false,"transaction_id":null,"cost":"0.9","currency_code":"SGD","repayments":[{"from":281236,"to":79774,"amount":"0.3"},{"from":643871,"to":79774,"amount":"0.3"}],"date":"2020-06-23T09:32:56Z","created_at":"2020-06-23T09:33:05Z","created_by":{"id":79774,"first_name":"Naman","last_name":"Aggarwal","picture":{"medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg"},"custom_picture":true},"updated_at":"2020-06-23T09:33:05Z","updated_by":null,"deleted_at":null,"deleted_by":null,"category":{"id":12,"name":"Groceries"},"receipt":{"large":null,"original":null},"users":[{"user":{"id":79774,"first_name":"Naman","last_name":"Aggarwal","picture":{"medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg"}},"user_id":79774,"paid_share":"0.9","owed_share":"0.3","net_balance":"0.6"},{"user":{"id":281236,"first_name":"Siddharth","last_name":"Goel","picture":{"medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/medium_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg"}},"user_id":281236,"paid_share":"0.0","owed_share":"0.3","net_balance":"-0.3"},{"user":{"id":643871,"first_name":"Shantanu","last_name":"Alshi","picture":{"medium":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-blue19-100px.png"}},"user_id":643871,"paid_share":"0.0","owed_share":"0.3","net_balance":"-0.3"}]},{"id":1009711631,"group_id":10843533,"friendship_id":null,"expense_bundle_id":null,"description":"Mexican Dinner","repeats":false,"repeat_interval":"never","email_reminder":true,"email_reminder_in_advance":null,"next_repeat":null,"details":"","comments_count":0,"payment":false,"creation_method":"split","transaction_method":"offline","transaction_confirmed":false,"transaction_id":null,"cost":"32.7","currency_code":"SGD","repayments":[{"from":281236,"to":79774,"amount":"10.9"},{"from":643871,"to":79774,"amount":"10.9"}],"date":"2020-06-22T07:17:32Z","created_at":"2020-06-22T07:17:54Z","created_by":{"id":79774,"first_name":"Naman","last_name":"Aggarwal","picture":{"medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg"},"custom_picture":true},"updated_at":"2020-06-22T07:17:54Z","updated_by":null,"deleted_at":null,"deleted_by":null,"category":{"id":13,"name":"Dining out"},"receipt":{"large":null,"original":null},"users":[{"user":{"id":281236,"first_name":"Siddharth","last_name":"Goel","picture":{"medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/medium_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg"}},"user_id":281236,"paid_share":"0.0","owed_share":"10.9","net_balance":"-10.9"},{"user":{"id":643871,"first_name":"Shantanu","last_name":"Alshi","picture":{"medium":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-blue19-100px.png"}},"user_id":643871,"paid_share":"0.0","owed_share":"10.9","net_balance":"-10.9"},{"user":{"id":79774,"first_name":"Naman","last_name":"Aggarwal","picture":{"medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg"}},"user_id":79774,"paid_share":"32.7","owed_share":"10.9","net_balance":"21.8"}]}]}'.encode('utf-8')  # noqa: E501
        self.sObj.getExpenses(2, 3, "123", "1234", "2020-12-12", "2020-12-19", "2020-12-13", "2020-12-18")
        args, kwargs = mockMakeRequest.call_args
        parsed = urlparse.urlparse(args[0])
        qs = parse_qs(parsed.query)
        self.assertEqual(qs['offset'], ['2'])
        self.assertEqual(qs['limit'], ['3'])
        self.assertEqual(qs['group_id'], ['123'])
        self.assertEqual(qs['friendship_id'], ['1234'])
        self.assertEqual(qs['dated_after'], ['2020-12-12'])
        self.assertEqual(qs['dated_before'], ['2020-12-19'])
        self.assertEqual(qs['updated_after'], ['2020-12-13'])
        self.assertEqual(qs['updated_before'], ['2020-12-18'])

    def test_getExpenses_exception(self, mockMakeRequest):
        mockMakeRequest.side_effect = Exception(
            "Invalid response %s. Please check your consumer key and secret." % 404)
        with self.assertRaises(Exception):
            self.sObj.getExpenses(2, 3)
        args, kwargs = mockMakeRequest.call_args
        parsed = urlparse.urlparse(args[0])
        qs = parse_qs(parsed.query)
        self.assertEqual(qs['offset'], ['2'])
        self.assertEqual(qs['limit'], ['3'])
