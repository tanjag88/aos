from time import sleep
import datetime
from selenium.webdriver.common.by import By
import aos_locators as locators


def set_up(driver):
    print(f'Launch {locators.website} Home Page')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('https://advantageonlineshopping.com/#/')
    sleep(2)
    if (driver.current_url == locators.adv_url and
            driver.title == locators.adv_title):
        print(f'{locators.website} Home Page Launched Successfully!')
        print(f'{locators.website} Home Page url:\nexpected result: {locators.adv_url} | '
              f'actual result: {driver.current_url}')
        print(f'{locators.website} Home Page title:\nexpected result: {locators.adv_title} | '
              f'actual result: {driver.title}')
        sleep(1)
    else:
        print(f'{locators.website} Home Page did not launch. Check your code and internet connection!')


def tier_down(driver):
    if driver is not None:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'The test Completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()


def create_new_user(driver):
    print('--------------Create New User--------------')
    sleep(2)
    driver.find_element(By.ID, "hrefUserIcon").click()
    sleep(2)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(2)
    for key, value in locators.account_dict.items():
        if key != 'countryListboxRegisterPage':
            driver.find_element(By.XPATH, f'//input[@name="{key}"]').send_keys(value)
            sleep(0.25)
        else:
            driver.find_element(By.XPATH,
                                f'//select[@name="{key}"]/option[@label="{locators.country}"]').click()
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(0.25)
    driver.find_element(By.ID, 'register_btnundefined').click()
    print(f'New user with username: {locators.username}, and password: {locators.password} was created!')


def validate_if_new_user_is_created(new_username, driver):
    print('----------Validate New User is created--------')
    sleep(0.25)
    driver.find_element(By.ID, 'menuUserLink')
    displayed_username = driver.find_element(By.CSS_SELECTOR,
                                             'span[data-ng-show="userCookie.response"]'
                                             '[class="hi-user containMiniTitle ng-binding"]').get_attribute('innerText')
    if new_username == displayed_username:
        print('New user is created and new username is displayed in the top menu!')
        print(f'New user username: {new_username}, new username displayed in the top menu: {displayed_username}')
    else:
        print('New user was not created!')


def log_in(new_username, new_password, driver):
    print('-------Log in with new User----------')
    driver.find_element(By.ID, "hrefUserIcon").click()
    sleep(1)
    driver.find_element(By.NAME, 'username').send_keys(new_username)
    sleep(1)
    driver.find_element(By.NAME, 'password').send_keys(new_password)
    sleep(1)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    print('Successfully log in!')


def validate_if_new_user_can_log_in(new_username, driver):
    print('----------Validate New User can Sign in--------')
    sleep(0.25)
    driver.find_element(By.ID, 'menuUserLink')
    displayed_username = driver.find_element(By.CSS_SELECTOR,
                                             'span[data-ng-show="userCookie.response"]'
                                             '[class="hi-user containMiniTitle ng-binding"]').get_attribute('innerText')
    if new_username == displayed_username:
        print('New user was successfully logged in!')
        print(f'New user username: {new_username}, new username displayed in the top menu: {displayed_username}')
    else:
        print('New user was not logged in!')


def log_out(username, driver):
    print('----------Log Out--------------')
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, username).click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"Sign out")]').click()
    sleep(0.25)
    print('Successfully logged out!')
