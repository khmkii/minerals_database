import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_home_page_shown(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn("Macky's Minerals", self.browser.title)

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()