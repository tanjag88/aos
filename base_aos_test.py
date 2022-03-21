from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest
import aos_locators as locators


class BaseAOStest(unittest.TestCase):
    s = Service(executable_path='../chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    @classmethod
    def setUpClass(cls):
        print(f'Launch {locators.website} Home Page')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get(locators.adv_url)
        sleep(2)
        if (cls.driver.current_url == locators.adv_url and
                cls.driver.title == locators.adv_title):
            print(f'{locators.website} Home Page Launched Successfully!')
            print(f'{locators.website} Home Page url:\nexpected result: {locators.adv_url} | '
                  f'actual result: {cls.driver.current_url}')
            print(f'{locators.website} Home Page title:\nexpected result: {locators.adv_title} | '
                  f'actual result: {cls.driver.title}')
            sleep(1)

        else:
            print(f'{locators.website} Home Page did not launch. Check your code and internet connection!')

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print(f'The test Completed at: {datetime.now()}')
            sleep(0.5)
            cls.driver.close()
            cls.driver.quit()
