from time import sleep
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import aos_locators as locators
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# s = Service(executable_path='../chromedriver.exe')
# driver = webdriver.Chrome(service=s)


def set_up(driver):
    print(f'Launch {locators.website} Home Page')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.adv_url)
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


def check_top_heading_menu_links_on_homepage(driver):
    assert driver.find_element(By.XPATH, '//span[contains(text(),"dvantage")]').is_displayed()
    print('Main logo is displayed')
    for link_text in locators.links_text:
        assert driver.find_element(By.LINK_TEXT, link_text).is_displayed()
        sleep(1)
        driver.find_element(By.LINK_TEXT, link_text).click()
        sleep(1)
        print(f'Link "{link_text}", is displayed and clickable!')
        driver.find_element(By.XPATH, '//a[@href="#/"]').click()


def check_all_texts_are_displayed_and_links_are_clickable_on_homepage(driver):
    print('---- Check all texts are displayed and links are clickable on homepage ----')

    for link in locators.links:
        assert driver.find_element(By.XPATH, f'//span[contains(.,"{link}")]').is_displayed()
        print(f'{link} link is displayed!')
        sleep(2)
        driver.find_element(By.XPATH, f'//span[contains(.,"{link}")]').click()
        print(f'{link} URL: {driver.current_url}')
        sleep(2)
        driver.back()
        # driver.find_element(By.XPATH, '//a[@href="#/"]').click()
    for text in locators.texts:
        assert driver.find_element(By.XPATH, f'//*[contains(.,"{text}")]').is_displayed()
        sleep(1)
        print(f"Text: '{text}' is displayed on homepage!")
    assert driver.find_element(By.ID, 'see_offer_btn').is_displayed()
    sleep(1)
    driver.find_element(By.ID, 'see_offer_btn').click()
    print(f'Button "SEE OFFER" is clickable, URL is: {driver.current_url}')
    sleep(1)
    # Go to homepage
    driver.back()
    driver.find_element(By.XPATH, '//button[@name="explore_now_btn"]').click()
    print(f'Button "EXPLORE NOW" is clickable, URL is: {driver.current_url}')
    sleep(1)
    driver.back()
    for key, value in locators.social_media.items():
        assert driver.find_element(By.XPATH, f'//img[@name="{value}"]').is_displayed()
        sleep(1)
        driver.find_element(By.XPATH, f'//img[@name="{value}"]').click()
        print(f'{key} page URL: {driver.current_url}')
        # close tab
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        driver.close()
        driver.switch_to.window(tabs[0])


def check_contact_us_form(driver, email):
    dropdown_category = Select(driver.find_element(By.NAME, 'categoryListboxContactUs'))
    dropdown_category.select_by_visible_text('Laptops')
    sleep(1)
    dropdown_product = Select(driver.find_element(By.NAME, 'productListboxContactUs'))
    dropdown_product.select_by_index(1)
    driver.find_element(By.NAME, 'emailContactUs').send_keys(email)
    sleep(1)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys("Enter something..")
    sleep(1)
    driver.find_element(By.ID, 'send_btnundefined').click()
    sleep(1)
    assert driver.find_element(By.XPATH,
                               '//p[contains(.,"Thank you for contacting Advantage support.")]').is_displayed()
    print(
        'CONTACT US form successfully populate. "Thank you for contacting Advantage support" message was displayed!')


def delete_user(username, driver):
    print('----------Delete Account--------------')
    driver.find_element(By.LINK_TEXT, username).click()
    sleep(1)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"My account")]').click()
    sleep(1)
    delete_btn = driver.find_element(By.CLASS_NAME, 'deleteBtnText')
    driver.execute_script("arguments[0].click();", delete_btn)
    sleep(1)
    yes = driver.find_element(By.CLASS_NAME, 'deleteBtnContainer')
    yes.find_element(By.CLASS_NAME, 'deletePopupBtn').click()
    sleep(1)
    print('Account successfully deleted!')
