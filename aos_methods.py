from time import sleep
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import aos_locators as locators


def create_new_user(driver):
    print('---------- Create New User ----------')
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
                                f'//select[@name="{key}"]/option[@label="{locators.new_country}"]').click()
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(0.25)
    driver.find_element(By.ID, 'register_btnundefined').click()
    user = locators.User()
    print(
        f'New user with username: {user.username}, and password: {user.username} '
        f'was created!')

    return user


def log_in(driver, username, password):
    print('----------- Log in with new User ----------')
    sleep(1)
    driver.find_element(By.ID, "hrefUserIcon").click()
    sleep(1)
    driver.find_element(By.NAME, 'username').send_keys(username)
    sleep(1)
    driver.find_element(By.NAME, 'password').send_keys(password)
    sleep(1)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    print('Successfully log in!')
    go_to_homepage(driver)


def log_out(username, driver):
    print('---------- Log Out ----------')
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, username).click()
    sleep(1)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"Sign out")]').click()
    sleep(1)
    print('Successfully logged out!')
    sleep(1)
    go_to_homepage(driver)


def populate_contact_us_form(driver, email):
    print('---------- Check CONTACT US form ----------')
    dropdown_category = Select(driver.find_element(By.NAME, 'categoryListboxContactUs'))
    dropdown_category.select_by_visible_text('Laptops')
    sleep(1)
    dropdown_product = Select(driver.find_element(By.NAME, 'productListboxContactUs'))
    dropdown_product.select_by_index(1)
    driver.find_element(By.NAME, 'emailContactUs').send_keys(email)
    sleep(1)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys("Enter something..")
    sleep(1)


def go_to_my_account(username, driver):
    driver.find_element(By.LINK_TEXT, username).click()
    sleep(1)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"My account")]').click()
    sleep(1)


def add_product_to_shopping_cart(driver):
    print('---------- Click on product and add the product to shopping cart ----------')
    print(f'Find the first product from the popular items section on home page and add it to the shopping cart ')
    driver.find_element(By.XPATH,
                        '//article[@id="popular_items"]//div[@class="ng-scope"][1]/a/'
                        'label[contains(.,"View Details")]').click()
    sleep(1)
    selected_product_name = driver.find_element(By.XPATH, '//div[@id="Description"]/h1').text
    print(f'Your selected product is: "{selected_product_name}"!')
    driver.find_element(By.NAME, 'save_to_cart').click()
    sleep(1)
    driver.find_element(By.ID, 'shoppingCartLink').click()
    sleep(1)
    driver.find_element(By.ID, 'checkOutButton').click()
    sleep(1)

    return selected_product_name


def go_to_homepage(driver):
    driver.find_element(By.XPATH, '//a[@href="#/"]').click()
