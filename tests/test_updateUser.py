from splitwise import Splitwise
from splitwise.user import User
from splitwise.exception import SplitwiseBadRequestException
import unittest
from unittest.mock import patch


@patch('splitwise.Splitwise._Splitwise__makeRequest')
class UpdateUserTestCase(unittest.TestCase):

    def setUp(self):
        self.sObj = Splitwise('consumerkey', 'consumersecret')

    def test_updateUser_success(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"user": {"id": 79774, "first_name": "Naman", "last_name": "Aggarwal", "picture": {"small": "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/small_mypic.jpg", "medium": "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg", "large": "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/large_mypic.jpg"}, "custom_picture": true, "email": "nam.aggarwal@yahoo.com", "registration_status": "confirmed", "locale": "en", "country_code": "IN", "date_format": "MM/DD/YYYY", "default_currency": "SGD", "default_group_id": null, "notifications_read": "2020-07-01T16:00:19Z", "notifications_count": 0, "notifications": {"added_as_friend": true, "added_to_group": true, "expense_added": false, "expense_updated": false, "bills": true, "payments": true, "monthly_summary": true, "announcements": true}}, "errors": []}'  # noqa: E501
        user = User()
        user.setId(10)
        user.setLastName('Aggarwal')
        updated_user, error = self.sObj.updateUser(user)
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/update_user", "POST", {"id": 10, "last_name": "Aggarwal"})
        self.assertEqual(updated_user.getId(), 79774)
        self.assertEqual(updated_user.getFirstName(), "Naman")
        self.assertEqual(updated_user.getLastName(), "Aggarwal")
        self.assertEqual(updated_user.getPicture().getSmall(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/small_mypic.jpg")
        self.assertEqual(updated_user.getPicture().getMedium(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg")
        self.assertEqual(updated_user.getPicture().getLarge(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/large_mypic.jpg")
        self.assertEqual(updated_user.getEmail(), "nam.aggarwal@yahoo.com")
        self.assertEqual(updated_user.getRegistrationStatus(), "confirmed")
        self.assertEqual(updated_user.getLocale(), "en")
        self.assertEqual(updated_user.getDateFormat(), "MM/DD/YYYY")
        self.assertEqual(updated_user.getDefaultCurrency(), "SGD")
        self.assertEqual(updated_user.getDefaultGroupId(), None)
        self.assertIsNone(error)

    def test_updateUser_error(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"user": null, "errors": {"base": ["Unknown error"]} }'  # noqa: E501
        user = User()
        user.setId(10)
        user.setLastName('Aggarwal')
        updated_user, error = self.sObj.updateUser(user)
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/update_user", "POST", {"id": 10, "last_name": "Aggarwal"})
        self.assertIsNone(updated_user)
        self.assertIsNotNone(error)

    def test_updateUser_raise_exception_when_no_id(self, mockMakeRequest):
        user = User()
        user.setLastName('Aggarwal')
        with self.assertRaises(SplitwiseBadRequestException):
            self.sObj.updateUser(user)
        mockMakeRequest.assert_not_called()

    def test_updateUser_exception(self, mockMakeRequest):
        mockMakeRequest.side_effect = Exception(
            "Invalid response %s. Please check your consumer key and secret." % 404)
        user = User()
        user.setId(10)
        user.setLastName('Aggarwal')
        with self.assertRaises(Exception):
            self.sObj.updateUser(user)
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/update_user", "POST", {"id": 10, "last_name": "Aggarwal"})
