from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest
import aos_methods as methods
import aos_locators as locators


class AosTestCases(unittest.TestCase):
    s = Service(executable_path='../chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    @classmethod
    def setUpClass(cls):
        methods.set_up(cls.driver)

    @classmethod
    def test_1_create_new_user_validate_log_in_log_out(cls):
        methods.create_new_user(cls.driver)
        methods.validate_if_new_user_is_created(new_username=locators.username, driver=cls.driver)
        methods.log_out(username=locators.username, driver=cls.driver)

    @classmethod
    def test_2_log_in_validate_log_out(cls):
        methods.log_in(new_username=locators.username, new_password=locators.password, driver=cls.driver)
        methods.validate_if_new_user_is_created(new_username=locators.username, driver=cls.driver)

    @classmethod
    def test_3_checkout_shopping_cart(cls):
        methods.checkout_shopping_cart(username=locators.username, password=locators.password,
                                       full_name=locators.full_name, product=locators.product_name,
                                       phone_number=locators.phone, driver=cls.driver)

    @classmethod
    def test_4_delete_account(cls):
        methods.delete_user(username=locators.username, driver=cls.driver)

    @classmethod
    def test_5_check_top_heading_menu_links_on_homepage_and_contact_us_form(cls):
        methods.check_top_heading_menu_links_on_homepage(driver=cls.driver)

    @classmethod
    def test_6_links_on_homepage_and_contact_us_form(cls):
        methods.check_all_texts_are_displayed_and_links_are_clickable_on_homepage(driver=cls.driver)

    @classmethod
    def test_7_check_contact_us_form(cls):
        methods.check_contact_us_form(driver=cls.driver, email=locators.email)

    @classmethod
    def tearDownClass(cls):
        methods.tear_down(cls.driver)
