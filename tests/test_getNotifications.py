from splitwise import Splitwise
import unittest
try:
    from unittest.mock import patch
except ImportError:  # Python 2
    from mock import patch


@patch('splitwise.Splitwise._Splitwise__makeRequest')
class GetNotifications(unittest.TestCase):

    def setUp(self):
        self.sObj = Splitwise('consumerkey', 'consumersecret')

    def test_getNotifications_success(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"notifications": [{"id": 32514315,"type": 0,"created_at": "2019-08-24T14:15:22Z","created_by": 2,"source": {"type": "Expense","id": 865077,"url": "string"},"image_url": "https://s3.amazonaws.com/splitwise/uploads/notifications/v2/0-venmo.png","image_shape": "square","content": "<strong>You</strong> paid <strong>Jon H.</strong>.<br><font color=\\\"#5bc5a7\\\">You paid $23.45</font>"}]}'  # noqa: E501
        notifications = self.sObj.getNotifications()  # TODO: Coverage of updated_after, limit: 0 arguments
        mockMakeRequest.assert_called_with("https://secure.splitwise.com/api/v3.0/get_notifications")

        self.assertEqual(notifications[0].getId(), 32514315)
        self.assertEqual(notifications[0].getType(), 0)  # TODO: Constants?
        self.assertEqual(notifications[0].getCreatedAt(), "2019-08-24T14:15:22Z")
        self.assertEqual(notifications[0].getCreatedBy(), 2)  # TODO: Users?
        self.assertEqual(notifications[0].getImageUrl(),
                         "https://s3.amazonaws.com/splitwise/uploads/notifications/v2/0-venmo.png")
        self.assertEqual(notifications[0].getImageShape(), "square")
        self.assertEqual(notifications[0].getContent(),
                         "<strong>You</strong> paid <strong>Jon H.</strong>.<br><font color=\"#5bc5a7\">You paid $23.45</font>")  # noqa: 501

        self.assertEqual(notifications[0].source.getType(), "Expense")
        self.assertEqual(notifications[0].source.getId(), 865077)
        self.assertEqual(notifications[0].source.getUrl(), "string")

    def test_getNotifications_exception(self, mockMakeRequest):
        mockMakeRequest.side_effect = Exception(
            "Invalid response %s. Please check your consumer key and secret." % 404)
        with self.assertRaises(Exception):
            self.sObj.getNotifications()
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/get_notifications")
