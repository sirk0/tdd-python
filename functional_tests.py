from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		#Edith has heard about a cool new online to-do app
		#She goes to check out its homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title and heade mention to-d- list
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# She is invited to enter a to-do item straight away

		# She types "Buy peacocks feathers" into a text box 
		# (Edith's hobby is tying fly-fishing lures)

		# When she hits enter, the page updates, and now the page lists
		# "1: Buy peacocks feathers" sa an item in to-do list

		# There is still a text box inviting her to add another item. 
		# She enters "Use pacocks feathers to make a fly" (Edith is very methodical)

		# The page updates again, and now shows both items on her list

		# Edith wonders whether site will remember her list. Then she sees
		# that the site has generated a uniques URL for her -- there is some
		# explanatory text to that effect

		# She vsists site URL - her to-do list is still here.

		#Satisfied, she goes to sleep

if __name__ == '__main__':
	unittest.main(warnings='ignore')
