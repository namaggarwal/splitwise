from splitwise import Splitwise
import unittest
from unittest.mock import patch

@patch('splitwise.Splitwise._Splitwise__makeRequest')
class GetCategoriesTestCase(unittest.TestCase):

    def setUp(self):
        self.sObj = Splitwise('consumerkey', 'consumersecret')

    def test_getCategories_success(self, mockMakeRequest):
        mockMakeRequest.return_value = '{"categories":[{"id":19,"name":"Entertainment","icon":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square/entertainment/other.png","icon_types":{"slim":{"small":"https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/other.png","large":"https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/other@2x.png"},"square":{"large":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/other@2x.png","xlarge":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/other@3x.png"}},"subcategories":[{"id":20,"name":"Games","icon":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square/entertainment/games.png","icon_types":{"slim":{"small":"https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/games.png","large":"https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/games@2x.png"},"square":{"large":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/games@2x.png","xlarge":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/games@3x.png"}}},{"id":21,"name":"Movies","icon":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square/entertainment/movies.png","icon_types":{"slim":{"small":"https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/movies.png","large":"https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/movies@2x.png"},"square":{"large":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/movies@2x.png","xlarge":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/movies@3x.png"}}},{"id":22,"name":"Music","icon":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square/entertainment/music.png","icon_types":{"slim":{"small":"https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/music.png","large":"https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/music@2x.png"},"square":{"large":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/music@2x.png","xlarge":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/music@3x.png"}}},{"id":23,"name":"Other","icon":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square/entertainment/other.png","icon_types":{"slim":{"small":"https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/other.png","large":"https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/other@2x.png"},"square":{"large":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/other@2x.png","xlarge":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/other@3x.png"}}},{"id":24,"name":"Sports","icon":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square/entertainment/sports.png","icon_types":{"slim":{"small":"https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/sports.png","large":"https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/sports@2x.png"},"square":{"large":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/sports@2x.png","xlarge":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/sports@3x.png"}}}]},{"id":25,"name":"Food and drink","icon":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square/food-and-drink/other.png","icon_types":{"slim":{"small":"https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/food-and-drink/other.png","large":"https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/food-and-drink/other@2x.png"},"square":{"large":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/food-and-drink/other@2x.png","xlarge":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/food-and-drink/other@3x.png"}},"subcategories":[{"id":13,"name":"Dining out","icon":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square/food-and-drink/dining-out.png","icon_types":{"slim":{"small":"https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/food-and-drink/dining-out.png","large":"https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/food-and-drink/dining-out@2x.png"},"square":{"large":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/food-and-drink/dining-out@2x.png","xlarge":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/food-and-drink/dining-out@3x.png"}}},{"id":12,"name":"Groceries","icon":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square/food-and-drink/groceries.png","icon_types":{"slim":{"small":"https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/food-and-drink/groceries.png","large":"https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/food-and-drink/groceries@2x.png"},"square":{"large":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/food-and-drink/groceries@2x.png","xlarge":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/food-and-drink/groceries@3x.png"}}},{"id":38,"name":"Liquor","icon":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square/food-and-drink/liquor.png","icon_types":{"slim":{"small":"https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/food-and-drink/liquor.png","large":"https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/food-and-drink/liquor@2x.png"},"square":{"large":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/food-and-drink/liquor@2x.png","xlarge":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/food-and-drink/liquor@3x.png"}}},{"id":26,"name":"Other","icon":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square/food-and-drink/other.png","icon_types":{"slim":{"small":"https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/food-and-drink/other.png","large":"https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/food-and-drink/other@2x.png"},"square":{"large":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/food-and-drink/other@2x.png","xlarge":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/food-and-drink/other@3x.png"}}}]}]}'  # noqa: E501
        categories = self.sObj.getCategories()
        mockMakeRequest.assert_called_with(
            "https://secure.splitwise.com/api/v3.0/get_categories")
        self.assertEqual(len(categories), 2)
        self.assertEqual(categories[0].getId(), 19)
        self.assertEqual(categories[0].getName(), "Entertainment")
        # self.assertEqual(categories[0].getIcon(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square/entertainment/other.png")
        # self.assertEqual(categories[0].getIconTypes().getSlim().getSmall(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/other.png")
        # self.assertEqual(categories[0].getIconTypes().getSlim().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/other@2x.png")
        # self.assertEqual(categories[0].getIconTypes().getSquare().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/other@2x.png")
        # self.assertEqual(categories[0].getIconTypes().getSquare().getXlarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/other@3x.png")
        self.assertEqual(len(categories[0].getSubcategories()), 5)
        self.assertEqual(categories[0].getSubcategories()[0].getId(), 20)
        self.assertEqual(categories[0].getSubcategories()[0].getName(), "Games")
        # self.assertEqual(categories[0].getSubcategories()[0].getIcon(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square/entertainment/games.png")
        # self.assertEqual(categories[0].getSubcategories()[0].getIconTypes().getSlim().getSmall(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/games.png")
        # self.assertEqual(categories[0].getSubcategories()[0].getIconTypes().getSlim().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/games@2x.png")
        # self.assertEqual(categories[0].getSubcategories()[0].getIconTypes().getSquare().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/games@2x.png")
        # self.assertEqual(categories[0].getSubcategories()[0].getIconTypes().getSquare().getXlarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/games@3x.png")
        self.assertEqual(categories[0].getSubcategories()[1].getId(), 21)
        self.assertEqual(categories[0].getSubcategories()[1].getName(), "Movies")
        # self.assertEqual(categories[0].getSubcategories()[1].getIcon(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square/entertainment/movies.png")
        # self.assertEqual(categories[0].getSubcategories()[1].getIconTypes().getSlim().getSmall(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/movies.png")
        # self.assertEqual(categories[0].getSubcategories()[1].getIconTypes().getSlim().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/movies@2x.png")
        # self.assertEqual(categories[0].getSubcategories()[1].getIconTypes().getSquare().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/movies@2x.png")
        # self.assertEqual(categories[0].getSubcategories()[1].getIconTypes().getSquare().getXlarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/movies@3x.png")
        self.assertEqual(categories[0].getSubcategories()[2].getId(), 22)
        self.assertEqual(categories[0].getSubcategories()[2].getName(), "Music")
        # self.assertEqual(categories[0].getSubcategories()[2].getIcon(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square/entertainment/music.png")
        # self.assertEqual(categories[0].getSubcategories()[2].getIconTypes().getSlim().getSmall(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/music.png")
        # self.assertEqual(categories[0].getSubcategories()[2].getIconTypes().getSlim().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/music@2x.png")
        # self.assertEqual(categories[0].getSubcategories()[2].getIconTypes().getSquare().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/music@2x.png")
        # self.assertEqual(categories[0].getSubcategories()[2].getIconTypes().getSquare().getXlarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/music@3x.png")
        self.assertEqual(categories[0].getSubcategories()[3].getId(), 23)
        self.assertEqual(categories[0].getSubcategories()[3].getName(), "Other")
        # self.assertEqual(categories[0].getSubcategories()[3].getIcon(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square/entertainment/other.png")
        # self.assertEqual(categories[0].getSubcategories()[3].getIconTypes().getSlim().getSmall(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/other.png")
        # self.assertEqual(categories[0].getSubcategories()[3].getIconTypes().getSlim().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/other@2x.png")
        # self.assertEqual(categories[0].getSubcategories()[3].getIconTypes().getSquare().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/other@2x.png")
        # self.assertEqual(categories[0].getSubcategories()[3].getIconTypes().getSquare().getXlarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/other@3x.png")
        self.assertEqual(categories[0].getSubcategories()[4].getId(), 24)
        self.assertEqual(categories[0].getSubcategories()[4].getName(), "Sports")
        # self.assertEqual(categories[0].getSubcategories()[4].getIcon(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square/entertainment/sports.png")
        # self.assertEqual(categories[0].getSubcategories()[4].getIconTypes().getSlim().getSmall(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/sports.png")
        # self.assertEqual(categories[0].getSubcategories()[4].getIconTypes().getSlim().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/entertainment/sports@2x.png")
        # self.assertEqual(categories[0].getSubcategories()[4].getIconTypes().getSquare().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/sports@2x.png")
        # self.assertEqual(categories[0].getSubcategories()[4].getIconTypes().getSquare().getXlarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/sports@3x.png")
        self.assertEqual(categories[1].getId(), 25)
        self.assertEqual(categories[1].getName(), "Food and drink")
        # self.assertEqual(categories[1].getIcon(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square/food-and-drink/other.png")
        # self.assertEqual(categories[1].getIconTypes().getSlim().getSmall(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/food-and-drink/other.png")
        # self.assertEqual(categories[1].getIconTypes().getSlim().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/food-and-drink/other@2x.png")
        # self.assertEqual(categories[1].getIconTypes().getSquare().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/food-and-drink/other@2x.png")
        # self.assertEqual(categories[1].getIconTypes().getSquare().getXlarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/food-and-drink/other@3x.png")
        self.assertEqual(len(categories[1].getSubcategories()), 4)
        self.assertEqual(categories[1].getSubcategories()[0].getId(), 13)
        self.assertEqual(categories[1].getSubcategories()[0].getName(), "Dining out")
        # self.assertEqual(categories[1].getSubcategories()[0].getIcon(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square/food-and-drink/dining-out.png")
        # self.assertEqual(categories[1].getSubcategories()[0].getIconTypes().getSlim().getSmall(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/food-and-drink/dining-out.png")
        # self.assertEqual(categories[1].getSubcategories()[0].getIconTypes().getSlim().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/food-and-drink/dining-out@2x.png")
        # self.assertEqual(categories[1].getSubcategories()[0].getIconTypes().getSquare().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/food-and-drink/dining-out@2x.png")
        # self.assertEqual(categories[1].getSubcategories()[0].getIconTypes().getSquare().getXlarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/food-and-drink/dining-out@3x.png")
        self.assertEqual(categories[1].getSubcategories()[1].getId(), 12)
        self.assertEqual(categories[1].getSubcategories()[1].getName(), "Groceries")
        # self.assertEqual(categories[1].getSubcategories()[1].getIcon(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square/food-and-drink/groceries.png")
        # self.assertEqual(categories[1].getSubcategories()[1].getIconTypes().getSlim().getSmall(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/food-and-drink/groceries.png")
        # self.assertEqual(categories[1].getSubcategories()[1].getIconTypes().getSlim().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/food-and-drink/groceries@2x.png")
        # self.assertEqual(categories[1].getSubcategories()[1].getIconTypes().getSquare().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/food-and-drink/groceries@2x.png")
        # self.assertEqual(categories[1].getSubcategories()[1].getIconTypes().getSquare().getXlarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/food-and-drink/groceries@3x.png")
        self.assertEqual(categories[1].getSubcategories()[2].getId(), 38)
        self.assertEqual(categories[1].getSubcategories()[2].getName(), "Liquor")
        # self.assertEqual(categories[1].getSubcategories()[2].getIcon(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square/food-and-drink/liquor.png")
        # self.assertEqual(categories[1].getSubcategories()[2].getIconTypes().getSlim().getSmall(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/food-and-drink/liquor.png")
        # self.assertEqual(categories[1].getSubcategories()[2].getIconTypes().getSlim().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/food-and-drink/liquor@2x.png")
        # self.assertEqual(categories[1].getSubcategories()[2].getIconTypes().getSquare().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/food-and-drink/liquor@2x.png")
        # self.assertEqual(categories[1].getSubcategories()[2].getIconTypes().getSquare().getXlarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/food-and-drink/liquor@3x.png")
        self.assertEqual(categories[1].getSubcategories()[3].getId(), 26)
        self.assertEqual(categories[1].getSubcategories()[3].getName(), "Other")
        # self.assertEqual(categories[1].getSubcategories()[3].getIcon(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square/food-and-drink/other.png")
        # self.assertEqual(categories[1].getSubcategories()[3].getIconTypes().getSlim().getSmall(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/food-and-drink/other.png")
        # self.assertEqual(categories[1].getSubcategories()[3].getIconTypes().getSlim().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/slim/food-and-drink/other@2x.png")
        # self.assertEqual(categories[1].getSubcategories()[3].getIconTypes().getSquare().getLarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/food-and-drink/other@2x.png")
        # self.assertEqual(categories[1].getSubcategories()[3].getIconTypes().getSquare().getXlarge(),
        # "https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/food-and-drink/other@3x.png")

    def test_getCategories_exception(self, mockMakeRequest):
        mockMakeRequest.side_effect = Exception(
            "Invalid response %s. Please check your consumer key and secret." % 404)
        with self.assertRaises(Exception):
            self.sObj.getCategories()
        mockMakeRequest.assert_called_with("https://secure.splitwise.com/api/v3.0/get_categories")
