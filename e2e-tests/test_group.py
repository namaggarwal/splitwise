import unittest
import os
from splitwise import Splitwise
from splitwise.group import Group
from splitwise.exception import SplitwiseUnauthorizedException


class GroupTestCase(unittest.TestCase):

    def setUp(self):
        consumer_key = os.environ['CONSUMER_KEY']
        consumer_secret = os.environ['CONSUMER_SECRET']
        oauth_token = os.environ['OAUTH_TOKEN']
        oauth_token_secret = os.environ['OAUTH_TOKEN_SECRET']

        self.sObj = Splitwise(consumer_key, consumer_secret)
        self.sObj.setAccessToken({'oauth_token': oauth_token, 'oauth_token_secret': oauth_token_secret})

    def test_group_flow(self):
        group = Group()
        group.setName("Splitwise_test_case")
        group, error = self.sObj.createGroup(group)
        self.assertIsNotNone(group.getId())

    def test_group_invalidkeys_fail(self):
        sObj = Splitwise('consumerkey', 'consumersecret', {"oauth_token": "sdsd", "oauth_token_secret": "sdsdd"})
        group = Group()
        with self.assertRaises(SplitwiseUnauthorizedException):
            sObj.createGroup(group)
