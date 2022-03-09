from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest
import aos_methods as methods
import aos_locators as locators


class AosTestCases(unittest.TestCase):
    s = Service(executable_path='../chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    def setUp(self):
        methods.set_up(self.driver)

    @classmethod
    def test_create_new_user_validate_log_in_log_out(cls):
        methods.create_new_user(cls.driver)
        methods.validate_if_new_user_is_created(new_username=locators.username, driver=cls.driver)
        methods.log_out(username=locators.username, driver=cls.driver)
        methods.log_in(new_username=locators.username, new_password=locators.password, driver=cls.driver)
        methods.validate_if_new_user_is_created(new_username=locators.username, driver=cls.driver)

    def tearDown(self):
        methods.tier_down(self.driver)
