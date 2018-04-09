from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\firefox.exe')

browser=webdriver.Firefox()
# Josh has hearsd about a cool new online to-do app. She goes to check out its homepage
browser.get('http://localhost:8000')

# He notices the page title and header mention to-do lists
# assert 'Django' in browser.title
# assert 'To-Do' in browser.title  # Original
assert 'To-Do' in browser.title, "Browser title was "+ browser.title # Enhanced printout

# He is invited to enter a to-do item straight away

# He types "Buy peackcok feathers" into a text box (Josh's hobby is typing fly-fishing lures)

# When he hits enter, the page updates, and now the page lists
# 1: Buy peackck feathers" as an item in a to-do list

# There is still a text box inviting her to add another item.  She enters
# "Use peacock feathers to make a fly:" (JOsh is very methodical)

# The page updates again, and now shows both items on his list

# Josh wonders wiether the site will hremmber his list.  Then he sees that the site has generated a uinique URL for him
# -- there is some explanator text to that effect.

# He visits that URL - his to-do list is still hthere

#  Satisfied, he goes back to sleep

browser.quit()

# TODO find the reason this unit-test fails