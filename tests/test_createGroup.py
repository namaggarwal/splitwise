from splitwise import Splitwise
from splitwise.group import Group, FriendGroup
import unittest
try:
    from unittest.mock import patch
except ImportError:  # Python 2
    from mock import patch


@patch('splitwise.Splitwise._Splitwise__makeRequest')
class CreateGroupTestCase(unittest.TestCase):

    def setUp(self):
        self.sObj = Splitwise('consumerkey', 'consumersecret')

    def test_createGroup_success(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"group":{"id":19481273,"name":"TestName","created_at":"2020-06-24T05:02:06Z","updated_at":"2020-06-24T05:02:06Z","members":[{"id":79774,"first_name":"Naman","last_name":"Aggarwal","picture":{"small":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/small_mypic.jpg","medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg","large":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/large_mypic.jpg"},"custom_picture":true,"email":"nam.aggarwal@yahoo.com","registration_status":"confirmed","balance":[]},{"id":784241,"first_name":"ruks","last_name":null,"picture":{"small":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-ruby47-50px.png","medium":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-ruby47-100px.png","large":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-ruby47-200px.png"},"custom_picture":false,"email":"rukmanivaithy@gmail.com","registration_status":"confirmed","balance":[]}],"simplify_by_default":false,"original_debts":[],"simplified_debts":[],"whiteboard":null,"group_type":"apartment","invite_link":"https://www.splitwise.com/join/1EUrTyyCHj7+1pjy","avatar":{"original":null,"xxlarge":"https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-ruby9-house-1000px.png","xlarge":"https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-ruby9-house-500px.png","large":"https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-ruby9-house-200px.png","medium":"https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-ruby9-house-100px.png","small":"https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-ruby9-house-50px.png"},"custom_avatar":false,"cover_photo":{"xxlarge":"https://s3.amazonaws.com/splitwise/uploads/group/default_cover_photos/coverphoto-ruby-1000px.png","xlarge":"https://s3.amazonaws.com/splitwise/uploads/group/default_cover_photos/coverphoto-ruby-500px.png"}}}'.encode('utf-8')  # noqa: E501
        group = Group()
        group.setName("TestName")
        group.setWhiteBoard("test Whiteboard")
        group.setType("apartment")
        user = FriendGroup()
        user.setId(784241)
        group.addMember(user)
        user2 = FriendGroup()
        user2.setId(123)
        group.addMember(user2)
        groupRes, error = self.sObj.createGroup(group)
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/create_group", "POST",
            {
                "users__0__user_id": 784241,
                "users__1__user_id": 123,
                "name": "TestName", "whiteboard":
                "test Whiteboard",
                "group_type": "apartment"
            })
        self.assertIsNone(error)
        self.assertEqual(groupRes.getId(), 19481273)
        self.assertEqual(groupRes.getName(), "TestName")
        self.assertEqual(groupRes.getCreatedAt(), "2020-06-24T05:02:06Z")
        self.assertEqual(groupRes.getUpdatedAt(), "2020-06-24T05:02:06Z")
        self.assertEqual(len(groupRes.getMembers()), 2)
        self.assertEqual(groupRes.getMembers()[0].getId(), 79774)
        self.assertEqual(groupRes.getMembers()[0].getFirstName(), "Naman")
        self.assertEqual(groupRes.getMembers()[0].getLastName(), "Aggarwal")
        self.assertEqual(groupRes.getMembers()[0].getPicture().getSmall(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/small_mypic.jpg")
        self.assertEqual(groupRes.getMembers()[0].getPicture().getMedium(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg")
        self.assertEqual(groupRes.getMembers()[0].getPicture().getLarge(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/large_mypic.jpg")
        self.assertEqual(groupRes.getMembers()[0].getEmail(), "nam.aggarwal@yahoo.com")
        self.assertEqual(groupRes.getMembers()[0].getRegistrationStatus(), "confirmed")
        self.assertEqual(len(groupRes.getMembers()[0].getBalances()), 0)
        self.assertEqual(groupRes.getMembers()[1].getId(), 784241)
        self.assertEqual(groupRes.getMembers()[1].getFirstName(), "ruks")
        self.assertEqual(groupRes.getMembers()[1].getLastName(), None)
        self.assertEqual(groupRes.getMembers()[1].getPicture().getSmall(),
                         "https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-ruby47-50px.png")
        self.assertEqual(groupRes.getMembers()[1].getPicture().getMedium(),
                         "https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-ruby47-100px.png")
        self.assertEqual(groupRes.getMembers()[1].getPicture().getLarge(),
                         "https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-ruby47-200px.png")
        self.assertEqual(groupRes.getMembers()[1].getEmail(), "rukmanivaithy@gmail.com")
        self.assertEqual(groupRes.getMembers()[1].getRegistrationStatus(), "confirmed")
        self.assertEqual(len(groupRes.getMembers()[1].getBalances()), 0)
        self.assertEqual(len(groupRes.getOriginalDebts()), 0)
        self.assertEqual(len(groupRes.getSimplifiedDebts()), 0)
        self.assertEqual(groupRes.getWhiteBoard(), None)
        self.assertEqual(groupRes.getType(), "apartment")
        self.assertEqual(groupRes.getInviteLink(), "https://www.splitwise.com/join/1EUrTyyCHj7+1pjy")
        # self.assertEqual(groupRes.getAvatar().getOriginal(), None)
        # self.assertEqual(groupRes.getAvatar().getXxlarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-ruby9-house-1000px.png")
        # self.assertEqual(groupRes.getAvatar().getXlarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-ruby9-house-500px.png")
        # self.assertEqual(groupRes.getAvatar().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-ruby9-house-200px.png")
        # self.assertEqual(groupRes.getAvatar().getMedium(),
        # "https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-ruby9-house-100px.png")
        # self.assertEqual(groupRes.getAvatar().getSmall(),
        # "https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-ruby9-house-50px.png")
        # self.assertEqual(groupRes.getCoverPhoto().getXxlarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/group/default_cover_photos/coverphoto-ruby-1000px.png")
        # self.assertEqual(groupRes.getCoverPhoto().getXlarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/group/default_cover_photos/coverphoto-ruby-500px.png")

    def test_createGroup_error(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"group":{"id":null,"name":null,"created_at":null,"updated_at":null,"members":[],"simplify_by_default":false,"original_debts":[],"simplified_debts":[],"whiteboard":null,"group_type":"apartment","invite_link":"https://www.splitwise.com/join/vmz4CdiY3LM+1pjy","errors":{"name":["can\'t be blank"]},"avatar":{"original":null,"xxlarge":"https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-teal1-house-1000px.png","xlarge":"https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-teal1-house-500px.png","large":"https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-teal1-house-200px.png","medium":"https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-teal1-house-100px.png","small":"https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-teal1-house-50px.png"},"custom_avatar":false,"cover_photo":{"xxlarge":"https://s3.amazonaws.com/splitwise/uploads/group/default_cover_photos/coverphoto-teal-1000px.png","xlarge":"https://s3.amazonaws.com/splitwise/uploads/group/default_cover_photos/coverphoto-teal-500px.png"}}}'.encode('utf-8')  # noqa: E501
        group = Group()
        user = FriendGroup()
        user.setId(784241)
        group.addMember(user)
        groupRes, error = self.sObj.createGroup(group)
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/create_group", "POST",
            {"users__0__user_id": 784241})
        self.assertEqual(error.getErrors(), {"name": ["can\'t be blank"]})

    def test_createGroup_exception(self, mockMakeRequest):
        mockMakeRequest.side_effect = Exception(
            "Invalid response %s. Please check your consumer key and secret." % 404)
        group = Group()
        user = FriendGroup()
        user.setId(784241)
        group.addMember(user)
        with self.assertRaises(Exception):
            self.sObj.createGroup(group)
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/create_group", "POST",
            {"users__0__user_id": 784241})
