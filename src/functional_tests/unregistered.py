from .selenium import SeleniumTestCase

class UnregisteredTestCase(SeleniumTestCase):
    def test_app_is_on_root(self):
        self.browser.get(self.live_server_url)
        self.assertIn("shnip.it", self.browser.page_source)
