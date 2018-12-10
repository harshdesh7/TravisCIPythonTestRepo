import requests
import unittest

class TestAPICalls(unittest.TestCase):

	def test_recipe(self):
		resp = requests.get('https://djibouti-recipe.herokuapp.com/api/recipes/410')
		for res in resp.json():
			print(res['name'])
			self.assertEqual(res['name'], "F in the Chat");

	def test_ingredient(self):
		resp = requests.get('https://djibouti-recipe.herokuapp.com/api/ingredients/20')
		for res in resp.json():
			print(res['name'])
			self.assertEqual(res['name'], "waffles");

	def test_user(self):
		resp = requests.get('https://djibouti-recipe.herokuapp.com/api/users/17')
		for res in resp.json():
			print(res['username'])
			self.assertEqual(res['username'], "admin");

if __name__ == '__main__':
    unittest.main()