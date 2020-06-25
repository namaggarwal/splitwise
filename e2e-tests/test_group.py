from splitwise import Splitwise
from splitwise.group import Group
import unittest


class GroupTestCase(unittest.TestCase):

    def setUp(self):
        self.sObj = Splitwise('consumerkey', 'consumersecret', {"oauth_token": "sdsd", "oauth_token_secret": "sdsdd"})

    def test_group_fail(self):
        group = Group()
        with self.assertRaises(Exception):
            self.sObj.createGroup(group)
