from splitwise import Splitwise
import unittest
try:
    from unittest.mock import patch
except ImportError:  # Python 2
    from mock import patch


@patch('splitwise.Splitwise._Splitwise__makeRequest')
class CreateCommentTestCase(unittest.TestCase):

    def setUp(self):
        self.sObj = Splitwise('consumerkey', 'consumersecret')

    def test_createComment_success(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"comment": {"id": 211110000, "content": "Test for create comment", "comment_type": "User", "relation_type": "ExpenseComment", "relation_id": 982430660, "created_at": "2020-08-09T16:14:52Z", "deleted_at": null, "user": {"id": 784241, "first_name": "ruks", "last_name": null, "picture": {"medium": "https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-ruby47-100px.png"}}}, "errors":{}}'  # noqa: E501
        expense_id = 982430660
        content = "Test for create comment"
        comment, errors = self.sObj.createComment(expense_id, content)
        data = dict()
        data["expense_id"] = 982430660
        data["content"] = "Test for create comment"
        mockMakeRequest.assert_called_with("https://secure.splitwise.com/api/v3.0/create_comment",
                                           "POST",
                                           data)
        self.assertEqual(comment.getId(), 211110000)
        self.assertEqual(comment.getContent(), 'Test for create comment')
        self.assertEqual(comment.getCommentType(), 'User')
        self.assertEqual(comment.getRelationType(), 'ExpenseComment')
        self.assertEqual(comment.getRelationId(), 982430660)
        self.assertEqual(comment.getCreatedAt(), '2020-08-09T16:14:52Z')
        self.assertEqual(comment.getDeletedAt(), None)
        user = comment.getCommentedUser()
        self.assertEqual(user.getFirstName(), 'ruks')
        self.assertEqual(user.getLastName(), None)

    def test_createComment_error(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"comment":{},"errors":{"base":["An unknown error occurred. Please try again or contact support@splitwise.com if you experience repeated issues. Sorry for the trouble!"]}}'  # noqa: E501
        expense_id = 982430660
        content = "Test for create comment"
        data = dict()
        data["expense_id"] = 982430660
        data["content"] = "Test for create comment"
        comment, errors = self.sObj.createComment(expense_id, content)
        mockMakeRequest.assert_called_with("https://secure.splitwise.com/api/v3.0/create_comment",
                                           "POST",
                                           data)
        self.assertEqual(errors.getErrors(), {
            'base': [
                'An unknown error occurred. Please try again or contact support@splitwise.com if you experience repeated issues. \
Sorry for the trouble!'
            ]})

    def test_createComment_exception(self, mockMakeRequest):
        mockMakeRequest.side_effect = Exception(
            "Invalid response %s. Please check your consumer key and secret." % 404)
        expense_id = 982430660
        content = "Test for create comment"
        data = dict()
        data["expense_id"] = 982430660
        data["content"] = "Test for create comment"
        with self.assertRaises(Exception):
            comment, errors = self.sObj.createComment(expense_id, content)
            mockMakeRequest.assert_called_with("https://secure.splitwise.com/api/v3.0/create_comment",
                                               "POST",
                                               data)
