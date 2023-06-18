from splitwise import Splitwise
import unittest
from unittest.mock import patch


@patch('splitwise.Splitwise._Splitwise__makeRequest')
class GetCategoriesTestCase(unittest.TestCase):

    def setUp(self):
        self.sObj = Splitwise('consumerkey', 'consumersecret')

    def test_getGroup_default_group_success(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"group":{"id":0,"name":"Non-group expenses","created_at":"2012-08-21T16:11:14Z","updated_at":"2020-06-23T09:42:10Z","members":[{"id":79774,"first_name":"Naman","last_name":"Aggarwal","picture":{"small":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/small_mypic.jpg","medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg","large":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/large_mypic.jpg"},"custom_picture":true,"email":"nam.aggarwal@yahoo.com","registration_status":"confirmed","balance":[{"amount":"115000.0","currency_code":"INR"},{"amount":"2162.82","currency_code":"SGD"}]}],"simplify_by_default":false,"original_debts":[{"to":79774,"from":18145926,"amount":"115000.0","currency_code":"INR"},{"to":79774,"from":784241,"amount":"2162.82","currency_code":"SGD"}],"simplified_debts":[{"to":79774,"from":18145926,"amount":"115000.0","currency_code":"INR"},{"to":79774,"from":784241,"amount":"2162.82","currency_code":"SGD"}],"avatar":{"original":null,"xxlarge":"https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-nongroup-1000px.png","xlarge":"https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-nongroup-500px.png","large":"https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-nongroup-200px.png","medium":"https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-nongroup-100px.png","small":"https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-nongroup-50px.png"},"custom_avatar":false,"cover_photo":{"xxlarge":"https://s3.amazonaws.com/splitwise/uploads/group/default_cover_photos/coverphoto-nongroup-1000px.png","xlarge":"https://s3.amazonaws.com/splitwise/uploads/group/default_cover_photos/coverphoto-nongroup-500px.png"}}}'  # noqa: E501
        group = self.sObj.getGroup()
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/get_group/0")
        self.assertEqual(group.getId(), 0)
        self.assertEqual(group.getName(), "Non-group expenses")
        self.assertEqual(group.getUpdatedAt(), "2020-06-23T09:42:10Z")
        self.assertEqual(len(group.getMembers()), 1)
        self.assertEqual(group.getMembers()[0].getId(), 79774)
        self.assertEqual(group.getMembers()[0].getFirstName(), "Naman")
        self.assertEqual(group.getMembers()[0].getLastName(), "Aggarwal")
        self.assertEqual(group.getMembers()[0].getPicture().getSmall(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/small_mypic.jpg")
        self.assertEqual(group.getMembers()[0].getPicture().getMedium(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg")
        self.assertEqual(group.getMembers()[0].getPicture().getLarge(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/large_mypic.jpg")
        self.assertEqual(group.getMembers()[0].getEmail(), "nam.aggarwal@yahoo.com")
        self.assertEqual(group.getMembers()[0].getRegistrationStatus(), "confirmed")
        self.assertEqual(len(group.getMembers()[0].getBalances()), 2)
        self.assertEqual(group.getMembers()[0].getBalances()[0].getAmount(), "115000.0")
        self.assertEqual(group.getMembers()[0].getBalances()[0].getCurrencyCode(), "INR")
        self.assertEqual(group.getMembers()[0].getBalances()[1].getAmount(), "2162.82")
        self.assertEqual(group.getMembers()[0].getBalances()[1].getCurrencyCode(), "SGD")
        self.assertEqual(len(group.getOriginalDebts()), 2)
        self.assertEqual(group.getOriginalDebts()[0].getToUser(), 79774)
        self.assertEqual(group.getOriginalDebts()[0].getFromUser(), 18145926)
        self.assertEqual(group.getOriginalDebts()[0].getAmount(), "115000.0")
        self.assertEqual(group.getOriginalDebts()[0].getCurrencyCode(), "INR")
        self.assertEqual(group.getOriginalDebts()[1].getToUser(), 79774)
        self.assertEqual(group.getOriginalDebts()[1].getFromUser(), 784241)
        self.assertEqual(group.getOriginalDebts()[1].getAmount(), "2162.82")
        self.assertEqual(group.getOriginalDebts()[1].getCurrencyCode(), "SGD")
        self.assertEqual(len(group.getSimplifiedDebts()), 2)
        self.assertEqual(group.getSimplifiedDebts()[0].getToUser(), 79774)
        self.assertEqual(group.getSimplifiedDebts()[0].getFromUser(), 18145926)
        self.assertEqual(group.getSimplifiedDebts()[0].getAmount(), "115000.0")
        self.assertEqual(group.getSimplifiedDebts()[0].getCurrencyCode(), "INR")
        self.assertEqual(group.getSimplifiedDebts()[1].getToUser(), 79774)
        self.assertEqual(group.getSimplifiedDebts()[1].getFromUser(), 784241)
        self.assertEqual(group.getSimplifiedDebts()[1].getAmount(), "2162.82")
        self.assertEqual(group.getSimplifiedDebts()[1].getCurrencyCode(), "SGD")
        # self.assertEqual(group.getAvatar().getOriginal(), None)
        # self.assertEqual(group.getAvatar().getXxlarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-nongroup-1000px.png")
        # self.assertEqual(group.getAvatar().getXlarge(),
        #  "https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-nongroup-500px.png")
        # self.assertEqual(group.getAvatar().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-nongroup-200px.png")
        # self.assertEqual(group.getAvatar().getMedium(),
        #  "https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-nongroup-100px.png")
        # self.assertEqual(group.getAvatar().getSmall(),
        # "https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-nongroup-50px.png")
        # self.assertEqual(group.getCoverPhoto().getXxlarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/group/default_cover_photos/coverphoto-nongroup-1000px.png")
        # self.assertEqual(group.getCoverPhoto().getXlarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/group/default_cover_photos/coverphoto-nongroup-500px.png")

    def test_getGroup_success(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"group":{"id":10843533,"name":"Flatmates Again","created_at":"2019-01-01T06:01:57Z","updated_at":"2020-06-23T09:33:38Z","members":[{"id":79774,"first_name":"Naman","last_name":"Aggarwal","picture":{"small":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/small_mypic.jpg","medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg","large":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/large_mypic.jpg"},"custom_picture":true,"email":"nam.aggarwal@yahoo.com","registration_status":"confirmed","balance":[{"currency_code":"SGD","amount":"-14.2"}]},{"id":281236,"first_name":"Siddharth","last_name":"Goel","picture":{"small":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/small_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg","medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/medium_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg","large":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/large_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg"},"custom_picture":true,"email":"siddharth98391@gmail.com","registration_status":"confirmed","balance":[{"currency_code":"SGD","amount":"975.05"}]},{"id":643871,"first_name":"Shantanu","last_name":"Alshi","picture":{"small":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-blue19-50px.png","medium":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-blue19-100px.png","large":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-blue19-200px.png"},"custom_picture":false,"email":"shantanuals@gmail.com","registration_status":"confirmed","balance":[{"currency_code":"SGD","amount":"-960.85"}]},{"id":784241,"first_name":"ruks","last_name":null,"picture":{"small":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-ruby47-50px.png","medium":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-ruby47-100px.png","large":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-ruby47-200px.png"},"custom_picture":false,"email":"rukmanivaithy@gmail.com","registration_status":"confirmed","balance":[{"currency_code":"SGD","amount":"0.0"}]}],"simplify_by_default":true,"original_debts":[{"from":281236,"to":79774,"amount":"2307.23","currency_code":"SGD"},{"currency_code":"SGD","from":79774,"to":643871,"amount":"2311.77"},{"currency_code":"SGD","from":79774,"to":784241,"amount":"9.66"},{"from":643871,"to":281236,"amount":"2520.67","currency_code":"SGD"},{"from":784241,"to":281236,"amount":"761.61","currency_code":"SGD"},{"currency_code":"SGD","from":643871,"to":784241,"amount":"751.95"}],"simplified_debts":[{"from":79774,"to":281236,"amount":"14.2","currency_code":"SGD"},{"from":643871,"to":281236,"amount":"960.85","currency_code":"SGD"}],"whiteboard":null,"group_type":"apartment","invite_link":"https://www.splitwise.com/join/d7bsHriQF5A+1pjy","avatar":{"original":"https://splitwise.s3.amazonaws.com/uploads/group/avatar/10843533/a3734b4d-817e-42f4-9763-8001b12e33b8.jpeg","xxlarge":"https://splitwise.s3.amazonaws.com/uploads/group/avatar/10843533/xxlarge_a3734b4d-817e-42f4-9763-8001b12e33b8.jpeg","xlarge":"https://splitwise.s3.amazonaws.com/uploads/group/avatar/10843533/xlarge_a3734b4d-817e-42f4-9763-8001b12e33b8.jpeg","large":"https://splitwise.s3.amazonaws.com/uploads/group/avatar/10843533/large_a3734b4d-817e-42f4-9763-8001b12e33b8.jpeg","medium":"https://splitwise.s3.amazonaws.com/uploads/group/avatar/10843533/medium_a3734b4d-817e-42f4-9763-8001b12e33b8.jpeg","small":"https://splitwise.s3.amazonaws.com/uploads/group/avatar/10843533/small_a3734b4d-817e-42f4-9763-8001b12e33b8.jpeg"},"custom_avatar":true,"cover_photo":{"xxlarge":"https://splitwise.s3.amazonaws.com/uploads/group/avatar/10843533/xxlarge_a3734b4d-817e-42f4-9763-8001b12e33b8.jpeg","xlarge":"https://splitwise.s3.amazonaws.com/uploads/group/avatar/10843533/xlarge_a3734b4d-817e-42f4-9763-8001b12e33b8.jpeg"}}}'  # noqa: E501
        group = self.sObj.getGroup(10843533)
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/get_group/10843533")

        self.assertEqual(group.getId(), 10843533)
        self.assertEqual(group.getName(), "Flatmates Again")
        # self.assertEqual(group.getCreatedAt(), "2019-01-01T06:01:57Z")
        self.assertEqual(group.getUpdatedAt(), "2020-06-23T09:33:38Z")
        self.assertEqual(len(group.getMembers()), 4)
        self.assertEqual(group.getMembers()[0].getId(), 79774)
        self.assertEqual(group.getMembers()[0].getFirstName(), "Naman")
        self.assertEqual(group.getMembers()[0].getLastName(), "Aggarwal")
        self.assertEqual(group.getMembers()[0].getPicture().getSmall(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/small_mypic.jpg")
        self.assertEqual(group.getMembers()[0].getPicture().getMedium(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg")
        self.assertEqual(group.getMembers()[0].getPicture().getLarge(),
                         "https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/large_mypic.jpg")
        self.assertEqual(group.getMembers()[0].getEmail(), "nam.aggarwal@yahoo.com")
        self.assertEqual(group.getMembers()[0].getRegistrationStatus(), "confirmed")
        self.assertEqual(len(group.getMembers()[0].getBalances()), 1)
        self.assertEqual(group.getMembers()[0].getBalances()[0].getCurrencyCode(), "SGD")
        self.assertEqual(group.getMembers()[0].getBalances()[0].getAmount(), "-14.2")
        self.assertEqual(group.getMembers()[1].getId(), 281236)
        self.assertEqual(group.getMembers()[1].getFirstName(), "Siddharth")
        self.assertEqual(group.getMembers()[1].getLastName(), "Goel")
        self.assertEqual(group.getMembers()[1].getPicture().getSmall(
        ), "https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/small_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg")
        self.assertEqual(group.getMembers()[1].getPicture().getMedium(
        ), "https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/medium_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg")
        self.assertEqual(group.getMembers()[1].getPicture().getLarge(
        ), "https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/large_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg")
        self.assertEqual(group.getMembers()[1].getEmail(), "siddharth98391@gmail.com")
        self.assertEqual(group.getMembers()[1].getRegistrationStatus(), "confirmed")
        self.assertEqual(len(group.getMembers()[1].getBalances()), 1)
        self.assertEqual(group.getMembers()[1].getBalances()[0].getCurrencyCode(), "SGD")
        self.assertEqual(group.getMembers()[1].getBalances()[0].getAmount(), "975.05")
        self.assertEqual(group.getMembers()[2].getId(), 643871)
        self.assertEqual(group.getMembers()[2].getFirstName(), "Shantanu")
        self.assertEqual(group.getMembers()[2].getLastName(), "Alshi")
        self.assertEqual(group.getMembers()[2].getPicture().getSmall(
        ), "https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-blue19-50px.png")
        self.assertEqual(group.getMembers()[2].getPicture().getMedium(
        ), "https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-blue19-100px.png")
        self.assertEqual(group.getMembers()[2].getPicture().getLarge(
        ), "https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-blue19-200px.png")
        self.assertEqual(group.getMembers()[2].getEmail(), "shantanuals@gmail.com")
        self.assertEqual(group.getMembers()[2].getRegistrationStatus(), "confirmed")
        self.assertEqual(len(group.getMembers()[2].getBalances()), 1)
        self.assertEqual(group.getMembers()[2].getBalances()[0].getCurrencyCode(), "SGD")
        self.assertEqual(group.getMembers()[2].getBalances()[0].getAmount(), "-960.85")
        self.assertEqual(group.getMembers()[3].getId(), 784241)
        self.assertEqual(group.getMembers()[3].getFirstName(), "ruks")
        self.assertEqual(group.getMembers()[3].getLastName(), None)
        self.assertEqual(group.getMembers()[3].getPicture().getSmall(
        ), "https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-ruby47-50px.png")
        self.assertEqual(group.getMembers()[3].getPicture().getMedium(
        ), "https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-ruby47-100px.png")
        self.assertEqual(group.getMembers()[3].getPicture().getLarge(
        ), "https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-ruby47-200px.png")

    def test_getGroup_exception(self, mockMakeRequest):
        mockMakeRequest.side_effect = Exception(
            "Invalid response %s. Please check your consumer key and secret." % 404)
        with self.assertRaises(Exception):
            self.sObj.getGroup(123)
        mockMakeRequest.assert_called_with("https://secure.splitwise.com/api/v3.0/get_group/123")
