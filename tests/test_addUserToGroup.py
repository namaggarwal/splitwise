from splitwise import Splitwise
from splitwise.user import User
import unittest
try:
    from unittest.mock import patch
except ImportError:  # Python 2
    from mock import patch


@patch('splitwise.Splitwise._Splitwise__makeRequest')
class AddUserToGroupTestCase(unittest.TestCase):

    def setUp(self):
        self.sObj = Splitwise('consumerkey', 'consumersecret')

    def test_addUserToGroup_withid_success(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"success":true,"user":{"id":281236,"first_name":"Siddharth","last_name":"Goel","picture":{"small":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/small_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg","medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/medium_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg","large":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/large_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg"},"custom_picture":true,"email":"siddharth98391@gmail.com","registration_status":"confirmed","balance":[]},"errors":{}}'.encode('utf-8')  # noqa: E501
        user = User()
        user.setId(281236)
        success, userRes, errors = self.sObj.addUserToGroup(user, 19481273)
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/add_user_to_group", "POST",
            {'group_id': 19481273, 'user_id': 281236})
        self.assertTrue(success)
        self.assertIsNone(errors)
        self.assertEqual(userRes.getId(), 281236)
        self.assertEqual(userRes.getFirstName(), "Siddharth")
        self.assertEqual(userRes.getLastName(), "Goel")
        self.assertEqual(userRes.getPicture().getSmall(
        ), "https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/small_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg")
        self.assertEqual(userRes.getPicture().getMedium(
        ), "https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/medium_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg")
        self.assertEqual(userRes.getPicture().getLarge(
        ), "https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/large_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg")
        self.assertEqual(userRes.getEmail(), "siddharth98391@gmail.com")
        self.assertEqual(userRes.getRegistrationStatus(), "confirmed")
        self.assertEqual(len(userRes.getBalances()), 0)

    def test_addUserToGroup_with_email_success(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"success":true,"user":{"id":62,"first_name":"Testes","last_name":null,"picture":{"small":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-orange16-50px.png","medium":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-orange16-100px.png","large":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-orange16-200px.png"},"custom_picture":false,"email":"test@test.com","registration_status":"confirmed","balance":[]},"errors":{}}'.encode('utf-8')  # noqa: E501
        user = User()
        user.setFirstName("testFirst")
        user.setLastName("testLast")
        user.setEmail("test@test.com")
        success, userRes, errors = self.sObj.addUserToGroup(user, 19481273)
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/add_user_to_group", "POST",
            {'first_name': 'testFirst',
             'last_name': 'testLast',
             'email': 'test@test.com',
             'group_id': 19481273
             })
        self.assertTrue(success)
        self.assertIsNone(errors)
        self.assertEqual(userRes.getId(), 62)
        self.assertEqual(userRes.getFirstName(), "Testes")
        self.assertEqual(userRes.getLastName(), None)
        self.assertEqual(userRes.getPicture().getSmall(),
                         "https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-orange16-50px.png")
        self.assertEqual(userRes.getPicture().getMedium(),
                         "https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-orange16-100px.png")
        self.assertEqual(userRes.getPicture().getLarge(),
                         "https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-orange16-200px.png")
        self.assertEqual(userRes.getEmail(), "test@test.com")
        self.assertEqual(userRes.getRegistrationStatus(), "confirmed")
        self.assertEqual(len(userRes.getBalances()), 0)

    def test_addUserToGroup_error(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"success":false,"user":null,"errors":{"memberships.user.first_name":["can\'t be blank"]}}'.encode('utf-8')  # noqa: E501
        user = User()
        success, userRes, errors = self.sObj.addUserToGroup(user, 19481273)
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/add_user_to_group", "POST",
            {
                'group_id': 19481273
            })
        self.assertIsNone(userRes)
        self.assertFalse(success)
        self.assertEqual(errors.getErrors(), {'memberships.user.first_name': ["can't be blank"]})

    def test_createGroup_exception(self, mockMakeRequest):
        mockMakeRequest.side_effect = Exception(
            "Invalid response %s. Please check your consumer key and secret." % 404)
        user = User()
        user.setId(281236)
        with self.assertRaises(Exception):
            success, userRes, errors = self.sObj.addUserToGroup(user, 19481273)
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/add_user_to_group", "POST",
            {'group_id': 19481273, 'user_id': 281236})
