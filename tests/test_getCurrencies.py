from splitwise import Splitwise
import unittest
try:
    from unittest.mock import patch
except ImportError:  # Python 2
    from mock import patch


@patch('splitwise.Splitwise._Splitwise__makeRequest')
class GetCurrenciesTestCase(unittest.TestCase):

    def setUp(self):
        self.sObj = Splitwise('consumerkey', 'consumersecret')

    def test_getCurrencies_success(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"currencies":[{"currency_code":"AED","unit":"DH"},{"currency_code":"AFN","unit":"Afs"},{"currency_code":"ALL","unit":"L"}]}'  # noqa: E501
        currencies = self.sObj.getCurrencies()
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/get_currencies")
        self.assertEqual(len(currencies), 3)
        self.assertEqual(currencies[0].getCode(), "AED")
        self.assertEqual(currencies[0].getUnit(), "DH")
        self.assertEqual(currencies[1].getCode(), "AFN")
        self.assertEqual(currencies[1].getUnit(), "Afs")
        self.assertEqual(currencies[2].getCode(), "ALL")
        self.assertEqual(currencies[2].getUnit(), "L")

    def test_getCurrencies_exception(self, mockMakeRequest):
        mockMakeRequest.side_effect = Exception(
            "Invalid response %s. Please check your consumer key and secret." % 404)
        with self.assertRaises(Exception):
            self.sObj.getCurrencies()
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/get_currencies")
