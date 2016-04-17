"""End to end testing"""

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
from selenium import webdriver


class AppFunctionalityTestcase(StaticLiveServerTestCase):
    """Test main app fucntionality."""

    def setUp(self):
        """Set up base settings for end to end tests."""
        self.browser = webdriver.PhantomJS()
        self.browser.set_window_size(1400, 1000)
        self.browser.implicitly_wait(10)

    # def tearDown(self):
    #     """Clean up after successful test run."""
    #     self.browser.quit()

    # def get_full_url(self, namespace):
    #     """Set up url to help access routes with name value."""
    #     return self.live_server_url + reverse(namespace)

    # # def test_home_title(self):
    # #     """Test that the index view can be accessed."""
    # #     self.browser.get(self.get_full_url("index"))
    # #     body = self.browser.find_element_by_class('well')
    # #     # self.assertIn("Just-Do-It", self.driver.title)
    #     # self.assertIn('Just-Do-It', body)

    # def test_url(self):
    #     self.browser.get("http://localhost:8000/")
    #     self.browser.find_element_by_id("login").click()

    # def test_dashboard_access(self):s
    #     """Test that a user can access the login and register views."""
    #     self.driver.get(self.get_full_url('login'))
    #     h5 = self.driver.find_element_by_tag_name("h5")
    #     self.assertIn("Life's too short not to.", h5)

    # def test_user_logout(self):
    #     """Test that a user can successfully logout."""
    #     self.browser.find_element_by_id('logout').click()
    #     body = self.browser.find_element_by_tag_name('body')
    #     self.assertIn('Just-Do-It', body.text)
