from splitwise import Splitwise
import unittest
from unittest.mock import patch


@patch('splitwise.Splitwise._Splitwise__makeRequest')
class GetCurrentUserTestCase(unittest.TestCase):

    def setUp(self):
        self.sObj = Splitwise('consumerkey', 'consumersecret')

    def test_getCurrentUser_success(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"user":{"id":12345,"first_name":"Naman","last_name":"Aggarwal","picture":{"small":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/12345/small_mypic.jpg","medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/12345/medium_mypic.jpg","large":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/12345/large_mypic.jpg"},"custom_picture":true,"email":"naman@naman.com","registration_status":"confirmed","force_refresh_at":"2017-03-18T11:41:36Z","locale":"en","country_code":"IN","date_format":"MM/DD/YYYY","default_currency":"SGD","default_group_id":null,"notifications_read":"2020-06-10T14:12:01Z","notifications_count":8,"notifications":{"added_as_friend":true,"added_to_group":true,"expense_added":false,"expense_updated":false,"bills":true,"payments":true,"monthly_summary":true,"announcements":true}}}'  # noqa: E501
        user = self.sObj.getCurrentUser()
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/get_current_user")
        self.assertEqual(user.getId(), 12345)
        self.assertEqual(user.getFirstName(), "Naman")
        self.assertEqual(user.getLastName(), "Aggarwal")
        self.assertEqual(user.getEmail(), "naman@naman.com")
        self.assertEqual(user.getPicture().getSmall(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/12345/small_mypic.jpg")
        self.assertEqual(user.getPicture().getMedium(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/12345/medium_mypic.jpg")
        self.assertEqual(user.getPicture().getLarge(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/12345/large_mypic.jpg")
        self.assertEqual(user.getRegistrationStatus(), "confirmed")

    def test_getCurrentUser_exception(self, mockMakeRequest):
        mockMakeRequest.side_effect = Exception(
            "Invalid response %s. Please check your consumer key and secret." % 404)
        with self.assertRaises(Exception):
            self.sObj.getCurrentUser()
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/get_current_user")
