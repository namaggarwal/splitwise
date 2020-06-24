from splitwise import Splitwise
import unittest
try:
    from unittest.mock import patch
except ImportError:  # Python 2
    from mock import patch


@patch('splitwise.Splitwise._Splitwise__makeRequest')
class GetFriendsTestCase(unittest.TestCase):

    def setUp(self):
        self.sObj = Splitwise('consumerkey', 'consumersecret')

    def test_getFriends_success(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"friends":[{"id":79773,"first_name":"Tirthankar","last_name":null,"email":"trh@gmail.com","registration_status":"confirmed","picture":{"small":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79773/small_avatar.jpeg","medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79773/medium_avatar.jpeg","large":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79773/large_avatar.jpeg"},"balance":[],"groups":[{"group_id":3449541,"balance":[]},{"group_id":6195367,"balance":[]},{"group_id":0,"balance":[]}],"updated_at":"2020-01-12T15:55:09Z"},{"id":281236,"first_name":"Siddharth","last_name":"Goel","email":"sid@gmail.com","registration_status":"confirmed","picture":{"small":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/small_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg","medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/medium_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg","large":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/large_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg"},"balance":[{"currency_code":"SGD","amount":"-20.13"}],"groups":[{"group_id":489361,"balance":[]},{"group_id":629385,"balance":[]},{"group_id":961648,"balance":[]},{"group_id":1282223,"balance":[]},{"group_id":1376285,"balance":[]},{"group_id":1427377,"balance":[]},{"group_id":1591839,"balance":[]},{"group_id":1911503,"balance":[]},{"group_id":2829420,"balance":[]},{"group_id":2831598,"balance":[]},{"group_id":3001684,"balance":[]},{"group_id":3137253,"balance":[]},{"group_id":4149325,"balance":[]},{"group_id":5938420,"balance":[]},{"group_id":7517182,"balance":[]},{"group_id":10843533,"balance":[{"currency_code":"SGD","amount":"-20.13"}]},{"group_id":12991099,"balance":[]},{"group_id":17090245,"balance":[]},{"group_id":0,"balance":[]}],"updated_at":"2020-06-22T07:17:54Z"}]}'.encode('utf-8')  # noqa: E501
        friends = self.sObj.getFriends()
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/get_friends")
        self.assertEqual(len(friends), 2)
        self.assertEqual(friends[0].getId(), 79773)
        self.assertEqual(friends[0].getFirstName(), "Tirthankar")
        self.assertEqual(friends[0].getLastName(), None)
        self.assertEqual(friends[0].getEmail(), "trh@gmail.com")
        self.assertEqual(friends[0].getRegistrationStatus(), "confirmed")
        self.assertEqual(friends[0].getPicture().getSmall(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79773/small_avatar.jpeg")
        self.assertEqual(friends[0].getPicture().getMedium(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79773/medium_avatar.jpeg")
        self.assertEqual(friends[0].getPicture().getLarge(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79773/large_avatar.jpeg")
        self.assertEqual(friends[0].getRegistrationStatus(), "confirmed")
        self.assertEqual(len(friends[0].getBalances()), 0)
        self.assertEqual(len(friends[0].getGroups()), 3)
        self.assertEqual(friends[0].getGroups()[0].getId(), 3449541)
        self.assertEqual(len(friends[0].getGroups()[0].getBalances()), 0)
        self.assertEqual(friends[1].getId(), 281236)
        self.assertEqual(friends[1].getFirstName(), "Siddharth")
        self.assertEqual(friends[1].getLastName(), "Goel")
        self.assertEqual(friends[1].getEmail(), "sid@gmail.com")
        self.assertEqual(friends[1].getRegistrationStatus(), "confirmed")
        self.assertEqual(len(friends[1].getBalances()), 1)
        self.assertEqual(friends[1].getBalances()[0].getAmount(), '-20.13')
        self.assertEqual(friends[1].getBalances()[0].getCurrencyCode(), 'SGD')
        self.assertEqual(len(friends[1].getGroups()), 19)
        self.assertEqual(friends[1].getGroups()[15].getId(), 10843533)
        self.assertEqual(len(friends[1].getGroups()[15].getBalances()), 1)
        self.assertEqual(friends[1].getGroups()[15].getBalances()[0].getCurrencyCode(), 'SGD')
        self.assertEqual(friends[1].getGroups()[15].getBalances()[0].getAmount(), '-20.13')

    def test_getFriends_exception(self, mockMakeRequest):
        mockMakeRequest.side_effect = Exception(
            "Invalid response %s. Please check your consumer key and secret." % 404)
        with self.assertRaises(Exception):
            self.sObj.getFriends()
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/get_friends")
