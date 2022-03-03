import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators


driver = methods.driver
By = methods.By
sleep = methods.sleep


class RegisterNewUserCheckFirstSignIn(unittest.TestCase):

    # Scenario_01: Register new user and check first sign in with this new registered user
    @staticmethod
    def test_register_new_user_check_first_sign_in():
        # Open browser -> navigate to home page -> validate correct URL and title
        methods.setUp('Scenario_01')

        # Register new user
        methods.register_new_user()

        # Validate details of new registered user - direct after registration
        print(methods.divider)
        print('We validate details of new registered user - direct after registration')
        methods.check_user_account_details()

        # Sign out
        methods.sign_out()

        # Validate sign in of new registered user
        methods.sign_in()
        print('New user successfully signed in')

        # Validate details of new registered user - after sign in
        print(methods.divider)
        print('We validate details of new registered user - after sign in')
        methods.check_user_account_details()

        # Delete user - while we are already inside account
        print(methods.divider)
        print('After validating new user details - we delete the account')
        methods.delete_account()

        # Validate that we are not able to sign in with deleted user
        print(methods.divider)
        print('Validate that we are not able to sign in with deleted user')
        methods.sign_in()

        # Verification message - Incorrect user name or password.
        message_xpath = '//label[ @id = "signInResultMessage" and contains(., "Incorrect user name or password.") ]'
        if driver.find_element(By.XPATH, message_xpath).is_displayed:
            print('Verification message  "Incorrect user name or password." --- is displayed')
            print('Not exists user is not able to sign in --- correct')

        # Close the web browser
        methods.tearDown('Scenario_01')


class CheckHomePage(unittest.TestCase):

    # Scenario_02: We check content on home page - links/buttons/contact us form
    @staticmethod
    def test_check_home_page():
        # Open browser -> navigate to home page -> validate correct URL and title
        methods.setUp('Scenario_02')

        # Validate product categories:
        # 1. category name is displayed/clickable/landed on correct page
        # 2. for each category - Shop now is displayed/clickable/landed on correct page
        methods.check_product_categories()

        # Validation of navigation top menus: clickable and go to right section
        methods.check_top_navigation_menu()

        # Validate main logo is displayed
        methods.main_logo()

        # Validation of CONTACT US form
        methods.contact_us()

        # Close the web browser
        methods.tearDown('Scenario_02')







# class MyChecks(unittest.TestCase):
#
#     @staticmethod
#     def test_1():
#
#         methods.setUp('Scenario_01')
#
#         # methods.register_new_user()
#         # Username: | StephenBenson
#         # Password: | @@PTOWb1G4O
#         # Stephen Benson
#
#         # Sign in with my details
#         sleep(1)
#         user_link = driver.find_element(By.XPATH, '//*[@id = "menuUserLink"]')
#         driver.execute_script('arguments[0].click();', user_link)
#         sleep(1)
#         driver.find_element(By.XPATH, '//input[@name = "username"]').send_keys('StephenBenson')
#         sleep(1)
#         driver.find_element(By.XPATH, '//input[@name = "password"]').send_keys('@@PTOWb1G4O')
#         # click Sign in
#         driver.find_element(By.ID, 'sign_in_btnundefined').click()
#
#         # ====================   Validate details on My Account menu
#         # Navigate to My Account menu
#         sleep(1)
#         driver.find_element(By.XPATH, '//*[@id= "menuUserLink"]/span').click()
#         sleep(1)
#         driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[text() = "My account"]').click()
#         # Validate correct Full name
#         sleep(1)
#         # if driver.find_element(By.XPATH, f'//*[@id="myAccountContainer"]/div[1]/div/div[1]/label[contains(., "{locators.full_name}")]').is_displayed():
#         # if driver.find_element(By.XPATH, f'//*[@id="myAccountContainer"]/div[1]/div/div[1]/label[contains(., "Stephen Benson")]').is_displayed():
#         if driver.find_element(By.XPATH, f'//*[@id="myAccountContainer"]/*/label[contains(., "Stephen Benson")]').is_displayed():
#
#             print('Full name on My Account details --- correct')
#         else:
#             print('CHECK CODE - Full name on My Account details --- NOT correct.')
