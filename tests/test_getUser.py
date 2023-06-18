from splitwise import Splitwise
import unittest
from unittest.mock import patch


@patch('splitwise.Splitwise._Splitwise__makeRequest')
class GetUserTestCase(unittest.TestCase):

    def setUp(self):
        self.sObj = Splitwise('consumerkey', 'consumersecret')

    def test_getUser_success(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"user":{"id":12323,"first_name":"Naman","last_name":"Aggarwal","picture":{"small":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/small_mypic.jpg","medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg","large":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/large_mypic.jpg"},"email":"naman@naman.com","registration_status":"confirmed"}}'  # noqa: E501
        user = self.sObj.getUser(12323)
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/get_user/12323")
        self.assertEqual(user.getId(), 12323)
        self.assertEqual(user.getFirstName(), "Naman")
        self.assertEqual(user.getLastName(), "Aggarwal")
        self.assertEqual(user.getEmail(), "naman@naman.com")

    def test_getUser_exception(self, mockMakeRequest):
        mockMakeRequest.side_effect = Exception(
            "Invalid response %s. Please check your consumer key and secret." % 404)
        with self.assertRaises(Exception):
            self.sObj.getUser(12323)
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/get_user/12323")
