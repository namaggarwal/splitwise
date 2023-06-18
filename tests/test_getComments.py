from splitwise import Splitwise
import unittest
from unittest.mock import patch

@patch('splitwise.Splitwise._Splitwise__makeRequest')
class GetComments(unittest.TestCase):

    def setUp(self):
        self.sObj = Splitwise('consumerkey', 'consumersecret')

    def test_getComments_success(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"comments":[{"id":209497424,"content":"I copied this from hangout","comment_type":"User","relation_type":"ExpenseComment","relation_id":982430660,"created_at":"2020-08-01T16:38:56Z","deleted_at":null,"user":{"id":79774,"first_name":"Naman","last_name":"Aggarwal","picture":{"medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg"}}}]}'  # noqa: E501
        comment = self.sObj.getComments(982430660)
        mockMakeRequest.assert_called_with("https://secure.splitwise.com/api/v3.0/get_comments?expense_id=982430660")
        self.assertEqual(comment[0].getId(), 209497424)
        self.assertEqual(comment[0].getContent(), "I copied this from hangout")
        self.assertEqual(comment[0].getCommentType(), "User")
        self.assertEqual(comment[0].getRelationType(), "ExpenseComment")
        self.assertEqual(comment[0].getRelationId(), 982430660)
        self.assertEqual(comment[0].getCreatedAt(), "2020-08-01T16:38:56Z")
        self.assertEqual(comment[0].getDeletedAt(), None)
        self.assertEqual(comment[0].getCommentedUser().getId(), 79774)
        self.assertEqual(comment[0].getCommentedUser().getFirstName(), "Naman")
        self.assertEqual(comment[0].getCommentedUser().getLastName(), "Aggarwal")

    def test_getComments_exception(self, mockMakeRequest):
        mockMakeRequest.side_effect = Exception(
            "Invalid response %s. Please check your consumer key and secret." % 404)
        with self.assertRaises(Exception):
            self.sObj.getComments(982430660)
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/get_comments?expense_id=982430660")
