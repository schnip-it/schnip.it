from django.test import LiveServerTestCase
from selenium import webdriver

class SeleniumTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.PhantomJS()

    def tearDown(self):
        self.browser.quit()

