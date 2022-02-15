from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_latter(self):
        # João has heard about a cool new online to-do app. He goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to0do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


        # He is invited to enter a to-do item straight away

        # He types "By my phone" into a text box (João likes to play
        # video game)

        # When he hits enter, the page updates, and now the page lists
        # "1: Buy my phone" as an item in a to-do list

        # There is still a text box inviting him to add another item. He
        # enters "Test the phone when it arrives"

        # The page updates again, and now shows both items on his list

        # João wonders whether the site will remember his list. Then he sees
        # that the site has generated a unique URL for him -- there is some
        # explanatory text to that effect.

        # He visits that URL - her to-do list is still there.

        # Satisfied, he goes back to sleep

if __name__=='__main__':
    unittest.main()
