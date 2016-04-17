"""End to end testing"""

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
from selenium import webdriver


class AppFunctionalityTestcase(StaticLiveServerTestCase):
    """Test main app fucntionality."""

    def setUp(self):
        """Set up base settings for end to end tests."""
        self.driver = webdriver.PhantomJS()

    def tearDown(self):
        """Clean up after successful test run."""
        self.driver.quit()

    def get_full_url(self, namespace):
        """Set up url to help access routs with name value."""
        return self.live_server_url + reverse(namespace)

    # def test_home_title(self):
    #     """Test that the index view can be accessed."""
    #     self.driver.get(self.get_full_url("index"))
    #     self.assertIn("Just-Do-It", self.driver.title)

    # def test_dashboard_access(self):
    #     """Test that a user can access the login and register views."""
    #     self.driver.get(self.get_full_url('login'))
    #     h5 = self.driver.find_element_by_tag_name("h5")
    #     self.assertIn("Life's too short not to.", h5)

    # def test_user_logout(self):
    #     """Test that a user can successfully logout."""
    #     self.browser.find_element_by_id('logout').click()
    #     body = self.browser.find_element_by_tag_name('body')
    #     self.assertIn('Just-Do-It', body.text)
