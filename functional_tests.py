from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\firefox.exe')

browser=webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title

# "C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
# from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#
# binary = FirefoxBinary('path/to/binary')
# driver = webdriver.Firefox(firefox_binary=binary)
# TODO find the reason this unit-test fails