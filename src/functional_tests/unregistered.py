from .selenium import SeleniumTestCase

class UnregisteredTestCase(SeleniumTestCase):
    def test_app_is_on_root(self):
        self.browser.get(self.live_server_url)
        self.assertIn("shnip.it", self.browser.page_source)

    def test_registration_form_exists(self):
        self.browser.get(self.live_server_url + "/account/signup/")
        self.assertIn("Sign up", self.browser.page_source)

    def test_login_form_exists(self):
        self.browser.get(self.live_server_url + "/account/login/")
        self.assertIn("Log in", self.browser.page_source)
        
