from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser=webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
         # Josh has hearsd about a cool new online to-do app. She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to-do lists
        # assert 'Django' in browser.title
        # assert 'To-Do' in browser.title  # Original
        # assert 'To-Do' in browser.title, "Browser title was "+ browser.title # Enhanced printout
        self.assertIn('ToDo', self.browser.title)
        self.fail('finish the test')

        # He is invited to enter a to-do item straight away

        # He types "Buy peackcok feathers" into a text box (Josh's hobby is typing fly-fishing lures)

        # When he hits enter, the page updates, and now the page lists
        # 1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item.  She enters
        # "Use peacock feathers to make a fly:" (JOsh is very methodical)

        # The page updates again, and now shows both items on his list

        # Josh wonders whether the site will remember his list.  Then he sees that the site has generated a unique URL for him
        # -- there is some explanator text to that effect.

        # He visits that URL - his to-do list is still there

        #  Satisfied, he goes back to sleep

        browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
# TODO find the reason this unit-test fails


#  NOTES
# from selenium import webdriver
# browser=webdriver.Firefox()
# browser.get('http://localhost:8000')
# browser.get('http://www.google.ca')
# browser.quit()

