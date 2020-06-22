from splitwise import Splitwise
import unittest
try:
    from unittest.mock import patch
except ImportError:  # Python 2
    from mock import patch


@patch('splitwise.Splitwise._Splitwise__makeRequest')
class GetGroupsTestCase(unittest.TestCase):

    def setUp(self):
        self.sObj = Splitwise('consumerkey', 'consumersecret')

    def test_getGroups_success(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"groups":[{"id":0,"name":"Non-group expenses","created_at":"2012-08-21T16:11:14Z","updated_at":"2020-06-22T16:27:14Z","members":[{"id":79774,"first_name":"Naman","last_name":"Aggarwal","picture":{"small":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/small_mypic.jpg","medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg","large":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/large_mypic.jpg"},"custom_picture":true,"email":"naman@yahoo.com","registration_status":"confirmed","balance":[{"amount":"115000.0","currency_code":"INR"},{"amount":"2162.82","currency_code":"SGD"}]}],"simplify_by_default":false,"original_debts":[{"to":79774,"from":18145926,"amount":"115000.0","currency_code":"INR"},{"to":79774,"from":784241,"amount":"2162.82","currency_code":"SGD"}],"simplified_debts":[{"to":79774,"from":18145926,"amount":"115000.0","currency_code":"INR"},{"to":79774,"from":784241,"amount":"2162.82","currency_code":"SGD"}],"avatar":{"original":null,"xxlarge":"https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-nongroup-1000px.png","xlarge":"https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-nongroup-500px.png","large":"https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-nongroup-200px.png","medium":"https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-nongroup-100px.png","small":"https://s3.amazonaws.com/splitwise/uploads/group/default_avatars/avatar-nongroup-50px.png"},"custom_avatar":false,"cover_photo":{"xxlarge":"https://s3.amazonaws.com/splitwise/uploads/group/default_cover_photos/coverphoto-nongroup-1000px.png","xlarge":"https://s3.amazonaws.com/splitwise/uploads/group/default_cover_photos/coverphoto-nongroup-500px.png"}},{"id":10843533,"name":"Flatmates Again","created_at":"2019-01-01T06:01:57Z","updated_at":"2020-06-22T07:17:54Z","members":[{"id":79774,"first_name":"Naman","last_name":"Aggarwal","picture":{"small":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/small_mypic.jpg","medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg","large":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/large_mypic.jpg"},"custom_picture":true,"email":"naman@yahoo.com","registration_status":"confirmed","balance":[{"currency_code":"SGD","amount":"-20.13"}]},{"id":281236,"first_name":"Siddharth","last_name":"Goel","picture":{"small":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/small_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg","medium":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/medium_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg","large":"https://splitwise.s3.amazonaws.com/uploads/user/avatar/281236/large_f5fccc37-0a88-4519-9398-59c8c19b92aa.jpeg"},"custom_picture":true,"email":"siddharth98391@gmail.com","registration_status":"confirmed","balance":[{"currency_code":"SGD","amount":"978.02"}]},{"id":643871,"first_name":"Shantanu","last_name":"Alshi","picture":{"small":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-blue19-50px.png","medium":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-blue19-100px.png","large":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-blue19-200px.png"},"custom_picture":false,"email":"shantanuals@gmail.com","registration_status":"confirmed","balance":[{"currency_code":"SGD","amount":"-957.89"}]},{"id":784241,"first_name":"ruks","last_name":null,"picture":{"small":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-ruby47-50px.png","medium":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-ruby47-100px.png","large":"https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-ruby47-200px.png"},"custom_picture":false,"email":"rukmanivaithy@gmail.com","registration_status":"confirmed","balance":[{"currency_code":"SGD","amount":"0.0"}]}],"simplify_by_default":true,"original_debts":[{"from":281236,"to":79774,"amount":"2304.26","currency_code":"SGD"},{"currency_code":"SGD","from":79774,"to":643871,"amount":"2314.73"},{"currency_code":"SGD","from":79774,"to":784241,"amount":"9.66"},{"from":643871,"to":281236,"amount":"2520.67","currency_code":"SGD"},{"from":784241,"to":281236,"amount":"761.61","currency_code":"SGD"},{"currency_code":"SGD","from":643871,"to":784241,"amount":"751.95"}],"simplified_debts":[{"from":79774,"to":281236,"amount":"20.13","currency_code":"SGD"},{"from":643871,"to":281236,"amount":"957.89","currency_code":"SGD"}],"whiteboard":null,"group_type":"apartment","invite_link":"https://www.splitwise.com/join/d7bsHriQF5A+1pjy","avatar":{"original":"https://splitwise.s3.amazonaws.com/uploads/group/avatar/10843533/a3734b4d-817e-42f4-9763-8001b12e33b8.jpeg","xxlarge":"https://splitwise.s3.amazonaws.com/uploads/group/avatar/10843533/xxlarge_a3734b4d-817e-42f4-9763-8001b12e33b8.jpeg","xlarge":"https://splitwise.s3.amazonaws.com/uploads/group/avatar/10843533/xlarge_a3734b4d-817e-42f4-9763-8001b12e33b8.jpeg","large":"https://splitwise.s3.amazonaws.com/uploads/group/avatar/10843533/large_a3734b4d-817e-42f4-9763-8001b12e33b8.jpeg","medium":"https://splitwise.s3.amazonaws.com/uploads/group/avatar/10843533/medium_a3734b4d-817e-42f4-9763-8001b12e33b8.jpeg","small":"https://splitwise.s3.amazonaws.com/uploads/group/avatar/10843533/small_a3734b4d-817e-42f4-9763-8001b12e33b8.jpeg"},"custom_avatar":true,"cover_photo":{"xxlarge":"https://splitwise.s3.amazonaws.com/uploads/group/avatar/10843533/xxlarge_a3734b4d-817e-42f4-9763-8001b12e33b8.jpeg","xlarge":"https://splitwise.s3.amazonaws.com/uploads/group/avatar/10843533/xlarge_a3734b4d-817e-42f4-9763-8001b12e33b8.jpeg"}}]}'.encode('utf-8')  # noqa: E501
        groups = self.sObj.getGroups()
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/get_groups")
        self.assertEqual(len(groups), 2)
        self.assertEqual(groups[0].getId(), 0)
        self.assertEqual(groups[0].getName(), 'Non-group expenses')
        self.assertEqual(groups[0].getType(), None)
        self.assertEqual(len(groups[0].getMembers()), 1)
        self.assertEqual(groups[0].getMembers()[0].getId(), 79774)
        self.assertEqual(groups[0].getMembers()[0].getFirstName(), 'Naman')
        self.assertEqual(groups[0].getMembers()[0].getLastName(), 'Aggarwal')
        self.assertEqual(groups[0].getMembers()[0].getEmail(), 'naman@yahoo.com')
        self.assertEqual(
          groups[0].getMembers()[0].getPicture().getSmall(),
          'https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/small_mypic.jpg'
        )
        self.assertEqual(
          groups[0].getMembers()[0].getPicture().getMedium(),
          'https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/medium_mypic.jpg'
        )
        self.assertEqual(
          groups[0].getMembers()[0].getPicture().getLarge(),
          'https://splitwise.s3.amazonaws.com/uploads/user/avatar/79774/large_mypic.jpg'
        )
        self.assertEqual(groups[0].getMembers()[0].getRegistrationStatus(), 'confirmed')
        self.assertEqual(len(groups[0].getMembers()[0].getBalances()), 2)
        self.assertEqual(groups[0].getMembers()[0].getBalances()[0].getAmount(), '115000.0')
        self.assertEqual(groups[0].getMembers()[0].getBalances()[0].getCurrencyCode(), 'INR')
        self.assertEqual(groups[0].isSimplifiedByDefault(), False)
        self.assertEqual(len(groups[0].getOriginalDebts()), 2)
        self.assertEqual(groups[0].getOriginalDebts()[0].getToUser(), 79774)
        self.assertEqual(groups[0].getOriginalDebts()[0].getFromUser(), 18145926)
        self.assertEqual(groups[0].getOriginalDebts()[0].getAmount(), '115000.0')
        self.assertEqual(groups[0].getOriginalDebts()[0].getCurrencyCode(), 'INR')
        self.assertEqual(len(groups[0].getSimplifiedDebts()), 2)
        self.assertEqual(groups[0].getSimplifiedDebts()[0].getFromUser(), 18145926)
        self.assertEqual(groups[0].getSimplifiedDebts()[0].getToUser(), 79774)
        self.assertEqual(groups[0].getSimplifiedDebts()[0].getAmount(), '115000.0')
        self.assertEqual(groups[0].getSimplifiedDebts()[0].getCurrencyCode(), 'INR')
        self.assertEqual(groups[0].getWhiteBoard(), None)
        self.assertEqual(groups[0].getInviteLink(), None)

    def test_getGroups_exception(self, mockMakeRequest):
        mockMakeRequest.side_effect = Exception(
            "Invalid response %s. Please check your consumer key and secret." % 404)
        with self.assertRaises(Exception):
            self.sObj.getGroups()
            mockMakeRequest.assert_called_with(
                "https://secure.splitwise.com/api/v3.0/get_groups")
