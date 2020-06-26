from splitwise import Splitwise
from splitwise.exception import SplitwiseNotFoundException, SplitwiseNotAllowedException
import unittest
try:
    from unittest.mock import patch
except ImportError:  # Python 2
    from mock import patch


@patch('splitwise.Splitwise._Splitwise__makeRequest')
class DeleteGroupTestCase(unittest.TestCase):

    def setUp(self):
        self.sObj = Splitwise('consumerkey', 'consumersecret')

    def test_deleteGroup_success(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"success":true}'  # noqa: E501
        success, errors = self.sObj.deleteGroup(19481273)
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/delete_group/19481273", "POST")
        self.assertTrue(success)
        self.assertIsNone(errors)

    def test_deleteGroup_error(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"success":false, "errors": {"base": ["some error occured"]}}'  # noqa: E501
        success, errors = self.sObj.deleteGroup(19481273)
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/delete_group/19481273", "POST")
        self.assertFalse(success)
        self.assertIsNotNone(errors)

    def test_deleteGroup_notallowed_exception(self, mockMakeRequest):
        mockMakeRequest.side_effect = SplitwiseNotAllowedException(
          "message"
        )

        with self.assertRaises(SplitwiseNotAllowedException):
            self.sObj.deleteGroup(19481273)

        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/delete_group/19481273", "POST")

    def test_deleteGroup_notfound_exception(self, mockMakeRequest):
        mockMakeRequest.side_effect = SplitwiseNotFoundException(
          "message"
        )

        with self.assertRaises(SplitwiseNotFoundException):
            self.sObj.deleteGroup(19481273)

        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/delete_group/19481273", "POST")
