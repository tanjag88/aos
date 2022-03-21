from time import sleep
from selenium.webdriver.common.by import By
import aos_methods as methods
import aos_locators as locators
from base_aos_test import BaseAOStest


class AosTestCases(BaseAOStest):
    user = locators.User()

    @classmethod
    def test_1_create_new_user_and_validate_if_is_created(cls):

        cls.user = methods.create_new_user(cls.driver)

        print('---------- Validate New User is created ----------')
        sleep(0.25)
        cls.driver.find_element(By.ID, 'menuUserLink')
        displayed_username = cls.driver.find_element(By.CSS_SELECTOR,
                                                     'span[data-ng-show="userCookie.response"]'
                                                     '[class="hi-user containMiniTitle ng-binding"]').get_attribute(
            'innerText')
        assert cls.user.username == displayed_username
        print('New user is created and new username is displayed in the top menu!')
        print(
            f'New user with username: {cls.user.username} was validate, new username: '
            f'{displayed_username} is displayed in the top menu: ')
        methods.log_out(username=cls.user.username, driver=cls.driver)

    @classmethod
    def test_2_validate_if_new_user_can_log_in(cls):
        methods.log_in(username=cls.user.username, password=cls.user.password, driver=cls.driver)
        print('---------- Validate New User can Sign in ----------')
        sleep(0.25)
        cls.driver.find_element(By.ID, 'menuUserLink')
        displayed_username = cls.driver.find_element(By.CSS_SELECTOR,
                                                     'span[data-ng-show="userCookie.response"]'
                                                     '[class="hi-user containMiniTitle ng-binding"]').get_attribute(
            'innerText')
        if cls.user.username == displayed_username:
            print('New user was successfully logged in!')
            print(f'New username: "{displayed_username}" is displayed in the top menu!')
        else:
            print('New user was not logged in!')
        methods.go_to_homepage(cls.driver)

    @classmethod
    def test_3_user_menu_validation(cls):
        print('---------- User Menu Validation ----------')
        cls.driver.find_element(By.LINK_TEXT, cls.user.username).click()
        sleep(1)
        print('Validate if there is no order in my orders!')
        cls.driver.find_element(By.XPATH, '//a/div/label[contains(.,"My orders")]').click()
        sleep(1)
        assert cls.driver.find_element(By.XPATH, '//label[contains(.," - No orders - ")]')
        print('Yes, "no orders" text is displayed in your orders')
        print('Go to my account and validate the full name!')
        sleep(1)
        cls.driver.find_element(By.LINK_TEXT, cls.user.username).click()
        cls.driver.find_element(By.XPATH, '//a/div/label[contains(.,"My account")]').click()
        sleep(1)
        fullname_displayed = cls.driver.find_element(By.XPATH,
                                                     '//div[@id="myAccountContainer"]//div[1]/'
                                                     'label[@class="ng-binding"]').text
        assert fullname_displayed == cls.user.full_name
        print('Yes, full name is correct: "Jessica Arellano" is displayed in Account details!')
        methods.go_to_homepage(cls.driver)

    @classmethod
    def test_4_checkout_shopping_cart(cls):
        selected_product = methods.add_product_to_shopping_cart(driver=cls.driver)
        cls.driver.find_element(By.ID, 'shoppingCartLink').click()
        sleep(1)
        cls.driver.find_element(By.ID, 'checkOutButton').click()
        sleep(1)
        print(
            f'Validate if full name: "{cls.user.full_name}" and product: "{selected_product}" '
            f'are correct in order payment')
        assert cls.driver.find_element(By.XPATH,
                                       f'//div[@id="userDetails"]/div/label[contains(.,"{cls.user.full_name}")]')
        sleep(1)
        displayed_product_text = cls.driver.find_element(By.XPATH,
                                                         '//div[@id="userCart"]//h3[@class="ng-binding"]').text
        sleep(1)
        assert displayed_product_text == selected_product
        print('Full name and product are correct, you can continue to payment method!')
        sleep(1)
        cls.driver.find_element(By.ID, 'next_btn').click()
        sleep(1)
        cls.driver.find_element(By.NAME, 'safepay_username').send_keys(cls.user.username)
        sleep(1)
        cls.driver.find_element(By.NAME, 'safepay_password').send_keys(cls.user.password)
        sleep(1)
        cls.driver.find_element(By.ID, 'pay_now_btn_SAFEPAY').click()
        sleep(1)
        print('Check the phone number!')
        sleep(1)
        order_phone_number = cls.driver.find_element(By.XPATH,
                                                     '//div[@id="orderPaymentSuccess"]//div[@class="innerSeccion"]'
                                                     '[3]/label[@class="ng-binding"]').text
        sleep(2)
        assert order_phone_number == cls.user.phone
        print(f'Phone number is correct! Order phone number: {order_phone_number}, your number:{cls.user.phone}')
        sleep(1)
        assert cls.driver.find_element(By.XPATH,
                                       '//span[contains(.,"Thank you for buying with Advantage")]').is_displayed()
        sleep(1)
        assert cls.driver.find_element(By.ID, 'trackingNumberLabel').is_displayed()
        t_number = cls.driver.find_element(By.ID, 'trackingNumberLabel').text
        sleep(1)
        assert cls.driver.find_element(By.ID, 'orderNumberLabel').is_displayed()
        sleep(1)
        o_number = cls.driver.find_element(By.ID, 'orderNumberLabel').text
        print('Message: "Thank you for buying with Advantage" is displayed!')
        print(f'Thank you, {cls.user.full_name}, your order is successful! Your order number is: {o_number} and '
              f'your tracking number is: {t_number}')
        methods.go_to_homepage(cls.driver)

    @classmethod
    def test_5_delete_account_and_check_if_is_deleted(cls):
        methods.go_to_my_account(username=cls.user.username, driver=cls.driver)
        print('Check if full name is correct in account details!')
        sleep(1)
        full_name_displayed = cls.driver.find_element(By.XPATH,
                                                      '//div[@id="myAccountContainer"]//div[@class="borderBox"][1]'
                                                      '//label[@class="ng-binding"]').text
        sleep(2)
        assert full_name_displayed == cls.user.full_name
        print(f'Yes, full name "{cls.user.full_name}" is correct. You can delete the account!')
        sleep(2)
        cls.driver.find_element(By.XPATH,
                                '//div[@id="myAccountContainer"]//button'
                                '[@class="deleteMainBtnContainer a-button ng-scope"]'
                                '/div[@class ="deleteBtnText"]').click()
        sleep(2)
        yes = cls.driver.find_element(By.CLASS_NAME, 'deleteBtnContainer')
        sleep(3)
        yes.find_element(By.CLASS_NAME, 'deletePopupBtn').click()
        sleep(1)
        print(
            f'Try to log in with deleted account username: "{cls.user.username}" and password: "{cls.user.password}"!')
        sleep(2)
        cls.driver.find_element(By.ID, "hrefUserIcon").click()
        sleep(2)
        cls.driver.find_element(By.NAME, 'username').send_keys(cls.user.username)
        sleep(1)
        cls.driver.find_element(By.NAME, 'password').send_keys(cls.user.password)
        sleep(3)
        cls.driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(1)
        signin_msg = cls.driver.find_element(By.XPATH,
                                             '//div[@class="login ng-scope"]/label[@id="signInResultMessage"]').text
        sleep(1)
        assert signin_msg == 'Incorrect user name or password.'
        sleep(2)
        cls.driver.find_element(By.XPATH,
                                '//div[@class="PopUp"]//div[@class="closeBtn loginPopUpCloseBtn"]').click()
        print('Message "Incorrect user name or password message" is displayed.')
        print('Account successfully deleted!')
        methods.go_to_homepage(cls.driver)

    @classmethod
    def test_6_check_top_heading_menu_links_on_homepage(cls):
        print('---------- Check top heading menu links ----------')
        assert cls.driver.find_element(By.XPATH, '//span[contains(text(),"dvantage")]').is_displayed()
        print('Main logo is displayed')
        for link_text in locators.links_text:
            assert cls.driver.find_element(By.LINK_TEXT, link_text).is_displayed()
            sleep(1)
            cls.driver.find_element(By.LINK_TEXT, link_text).click()
            sleep(1)
            print(f'Link "{link_text}", is displayed and clickable!')
            methods.go_to_homepage(cls.driver)

    @classmethod
    def test_7_check_all_texts_are_displayed_and_links_are_clickable_on_homepage(cls):
        print('---------- Check all texts are displayed and links are clickable on homepage ----------')
        for link in locators.links:
            assert cls.driver.find_element(By.XPATH, f'//span[contains(.,"{link}")]').is_displayed()
            print(f'{link} link is displayed!')
            sleep(2)
            cls.driver.find_element(By.XPATH, f'//span[contains(.,"{link}")]').click()
            print(f'{link} URL: {cls.driver.current_url}')
            sleep(2)
            methods.go_to_homepage(cls.driver)
        for text in locators.texts:
            assert cls.driver.find_element(By.XPATH, f'//*[contains(.,"{text}")]').is_displayed()
            sleep(1)
            print(f"Text: '{text}' is displayed on homepage!")
        assert cls.driver.find_element(By.ID, 'see_offer_btn').is_displayed()
        sleep(1)
        cls.driver.find_element(By.ID, 'see_offer_btn').click()
        print(f'Button "SEE OFFER" is clickable, URL is: {cls.driver.current_url}')
        sleep(1)
        methods.go_to_homepage(cls.driver)
        cls.driver.find_element(By.XPATH, '//button[@name="explore_now_btn"]').click()
        print(f'Button "EXPLORE NOW" is clickable, URL is: {cls.driver.current_url}')
        sleep(1)
        methods.go_to_homepage(cls.driver)
        for key, value in locators.social_media.items():
            assert cls.driver.find_element(By.XPATH, f'//img[@name="{value}"]').is_displayed()
            sleep(1)
            cls.driver.find_element(By.XPATH, f'//img[@name="{value}"]').click()
            sleep(1)
            tabs = cls.driver.window_handles
            cls.driver.switch_to.window(tabs[1])
            print(f'{key} page URL: {cls.driver.current_url}')
            cls.driver.close()
            cls.driver.switch_to.window(tabs[0])

    @classmethod
    def test_8_check_contact_us_form(cls):
        methods.populate_contact_us_form(driver=cls.driver, email=cls.user.email)
        print('Check if "send" button is active and click on if it is!')
        assert cls.driver.find_element(By.ID, 'send_btnundefined').is_enabled()
        cls.driver.find_element(By.ID, 'send_btnundefined').click()
        sleep(1)
        assert cls.driver.find_element(By.XPATH,
                                       '//p[contains(.,"Thank you for contacting Advantage support.")]').is_displayed()

        print(
            'CONTACT US form successfully populate. '
            '"Thank you for contacting Advantage support" message was displayed!')
        methods.go_to_homepage(cls.driver)
