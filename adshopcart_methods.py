import datetime
from random import random
from time import sleep
import random

from prettytable import PrettyTable
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

import adshopcart_locators as locators

# ================================================= Variables

driver = webdriver.Chrome()
action = ActionChains(driver)

divider = '-----------------------------------------'

# =================================================


def setUp(scenario_num):
    # Test started
    print(divider)
    text = f'{scenario_num} started at {datetime.datetime.now()}'
    print(text)
    print(divider)

    # Navigating to the home page app website
    driver.get(locators.homepage_url)
    driver.implicitly_wait(30)

    # Make a full screen
    driver.maximize_window()

    # Validate correct URL address and correct title
    if driver.current_url == locators.homepage_url and driver.title.endswith('Advantage Shopping'):
        print(f'Home page --- loaded successfully')
        print(f'<{locators.homepage_url}> --- URL is correct')
        print(f'<Advantage Shopping> --- title is correct')
    else:
        print(f'=== Page URL <{locators.homepage_url}> --- not loaded successfully. Check your code ===')
        driver.close()
        driver.quit()


def tearDown(scenario_num):
    sleep(1)
    # check if driver is working
    if driver is not None:
        print(divider)
        text = f'{scenario_num} completed at {datetime.datetime.now()}'
        print(text)
        driver.close()
        driver.quit()


def register_new_user():
    print(divider)
    sleep(1)
    # Click USER icon on header
    sleep(1)
    user_link = driver.find_element(By.XPATH, '//*[@id = "menuUserLink"]')
    driver.execute_script('arguments[0].click();', user_link)
    #  Click CREATE NEW ACCOUNT
    sleep(1)
    create_new_account_link = driver.find_element(By.LINK_TEXT, "CREATE NEW ACCOUNT")
    driver.execute_script('arguments[0].click();', create_new_account_link)
    print("We landed successfully on Registration page ")

    # ====================  Starts fill form  =======================
    sleep(1)
    # Username
    driver.find_element(By.XPATH, '//input[@name = "usernameRegisterPage"]').send_keys(locators.username)
    sleep(1)
    # Email
    driver.find_element(By.XPATH, '//input[@name = "emailRegisterPage"]').send_keys(locators.email)
    sleep(1)
    # Password
    driver.find_element(By.XPATH, '//input[@name = "passwordRegisterPage"]').send_keys(locators.password)
    sleep(1)
    # Confirm Password
    driver.find_element(By.XPATH, '//input[@name = "confirm_passwordRegisterPage"]').send_keys(locators.password)
    sleep(1)
    # First Name
    driver.find_element(By.XPATH, '//input[@name = "first_nameRegisterPage"]').send_keys(locators.first_name)
    sleep(1)
    # Last Name
    driver.find_element(By.XPATH, '//input[@name = "last_nameRegisterPage"]').send_keys(locators.last_name)
    sleep(1)
    # Phone Number
    driver.find_element(By.XPATH, '//input[@name = "phone_numberRegisterPage"]').send_keys(locators.phone)
    sleep(1)
    # Country
    country_dropdown = driver.find_element(By.XPATH, '//select[@name = "countryListboxRegisterPage"]')
    Select(country_dropdown).select_by_visible_text(locators.country)
    sleep(1)
    # City
    driver.find_element(By.XPATH, '//input[@name = "cityRegisterPage"]').send_keys(locators.city)
    sleep(1)
    # State / Province / Region
    driver.find_element(By.XPATH, '//input[@name = "state_/_province_/_regionRegisterPage"]').send_keys(locators.state_province_region)
    sleep(1)
    # Address
    driver.find_element(By.XPATH, '//input[@name = "addressRegisterPage"]').send_keys(locators.address)
    sleep(1)
    #  Postal code
    driver.find_element(By.XPATH, '//input[@name = "postal_codeRegisterPage"]').send_keys(locators.postal_code)
    sleep(1)
    register_button = driver.find_element(By.XPATH, '//sec-sender[@a-value = "REGISTER"]')

    # Check that Register button is not clickable - because we didn't yet select "I agree" option
    try:
        if register_button.click():
            print('Register button is clickable - before we selected "I agree" option --- is not correct. Check code')
    except:
        print('')

    # Select "I agree" option
    driver.find_element(By.XPATH, '//input[@name = "i_agree"]').click()

    # Click Register button
    register_button.click()

    # =================  End to fill form =================

    # Summarize the form
    print(divider)
    print('Registration form filled successfully, with following details:')

    table = PrettyTable()
    table.field_names = ['Field', 'Value']
    table.add_rows([
        ['Username:', locators.username ],
        ['Email:', locators.email ],
        ['Password:', locators.password],
        ['First Name:', locators.first_name],
        ['Last Name:', locators.last_name],
        ['Phone Number:', locators.phone],
        ['Country:', locators.country],
        ['State / Province / Region:', locators.province],
        ['City:', locators.city],
        ['Address:', locators.address],
        ['Postal code:', locators.postal_code],
    ])

    table.align = 'l'
    # Print form to console
    print(table)


def check_user_account_details():
    sleep(1)
    print(divider)
    print('We check details of user:')
    # Validate username beside user icon
    username_object = driver.find_element(By.XPATH, '//*[@id= "menuUserLink"]/span')
    sleep(1)
    if driver.find_element(By.XPATH, f'//*[@id= "menuUserLink"]/span[contains(., "{locators.username}")]').is_displayed():
        print('Username beside user icon --- correct')
    else:
        print('CHECK CODE - Username beside user icon --- NOT correct.')

    # ====================   Validate details on My Account menu
    # Navigate to My Account menu
    sleep(1)
    username_object.click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[text() = "My account"]').click()
    # Validate correct Full name
    sleep(1)
    if driver.find_element(By.XPATH, f'//*[@id="myAccountContainer"]/div[1]/div/div[1]/label[contains(., "{locators.full_name}")]').is_displayed():
        print('Full name on My Account details --- correct')
    else:
        print('CHECK CODE - Full name on My Account details --- NOT correct.')

    # ====================   Validate details on My Orders menu
    # Navigate to My orders page
    sleep(1)
    username_object.click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[text() = "My orders"]').click()
    # Validate that no orders - because it's new registered user
    if driver.find_element(By.XPATH, '//div[@class="bigEmptyOrder center"]/label[text() = " - No orders - "]'):
        print('No orders --- correct')
    else:
        print('CHECK CODE - No orders not presents --- NOT correct.')


def sign_out():
    sleep(1)
    print(divider)
    driver.find_element(By.XPATH, '//*[@id= "menuUserLink"]/span').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[text() = "Sign out"]').click()
    print('Signed out successfully')


def sign_in():
    sleep(1)
    print(divider)
    # Click USER icon on header
    sleep(1)
    user_link = driver.find_element(By.XPATH, '//*[@id = "menuUserLink"]')
    driver.execute_script('arguments[0].click();', user_link)
    # Sign in
    # username
    sleep(1)
    driver.find_element(By.XPATH, '//input[@name = "username"]').send_keys(locators.username)
    # password
    sleep(1)
    driver.find_element(By.XPATH, '//input[@name = "password"]').send_keys(locators.password)
    # click Sign in
    driver.find_element(By.ID, 'sign_in_btnundefined').click()


def delete_account(): # while we are inside account
    sleep(1)
    print(divider)
    # Navigate to My Account menu
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id= "menuUserLink"]/span').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[text() = "My account"]').click()
    # Delete account
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'div.deleteBtnText').click()
    # Are sure you want to delete account? - yes
    sleep(1)
    driver.find_element(By.XPATH, '//div[@class = "deletePopupBtn deleteRed"]').click()
    print('Account deleted successfully')
    sleep(8) # long sleep because page is updated longer after deleting account


# Validate product categories:
# 1. category name is displayed/clickable/landed on correct page
# 2. for each category - Shop now is displayed/clickable/landed on correct page
def check_product_categories():
    sleep(1)
    print(divider)
    print('We check product categories: \n'
          '1. category name is displayed/clickable/landed on correct page\n'
          '2. for each category - "Shop now" is displayed/clickable/landed on correct page')

    def validate_categories(category, category_id, url, shop_now_id):
        print(f'\n ============  {category} ==============')
        if driver.find_element(By.ID, category_id).is_displayed():
            driver.find_element(By.ID, category_id).click()
            sleep(1)
            print(f'<{category}> category is displayed and clickable')
            if driver.current_url == url:
                print(f'Clicked on <{category}> ---  landed successfully on <{category}> page')

        sleep(1)
        driver.back()
        driver.refresh()
        sleep(2)

        action.move_to_element(driver.find_element(By.ID, category_id)).perform()
        driver.find_element(By.ID, shop_now_id).click()
        sleep(1)
        print(f'"Shop now" of <{category}> is displayed and clickable')
        if driver.current_url == url:
            print(f'Clicked on "Shop now" ---  landed successfully on <{category}> page')

        sleep(1)
        driver.back()
        driver.refresh()
        sleep(2)

    # SPEAKERS
    validate_categories('SPEAKERS', 'speakersTxt', 'https://advantageonlineshopping.com/#/category/Speakers/4', 'speakersLink')
    # TABLETS
    validate_categories('TABLETS', 'tabletsTxt', 'https://advantageonlineshopping.com/#/category/Tablets/3', 'tabletsLink')
    # HEADPHONES
    validate_categories('HEADPHONES', 'headphonesTxt', 'https://advantageonlineshopping.com/#/category/Headphones/2', 'headphonesLink')
    # LAPTOPS
    validate_categories('LAPTOPS', 'laptopsTxt', 'https://advantageonlineshopping.com/#/category/Laptops/1', 'laptopsLink')
    # MICE
    validate_categories('MICE', 'miceTxt', 'https://advantageonlineshopping.com/#/category/Mice/5', 'miceLink')


def check_top_navigation_menu():
    sleep(1)
    print(divider)
    print('Validation of navigation top menus: displayed and clickable')
    navigation_menu = ['SPECIAL OFFER', 'POPULAR ITEMS', 'CONTACT US', 'OUR PRODUCTS']
    for menu in navigation_menu:
        sleep(2)
        element = driver.find_element(By.LINK_TEXT, f'{menu}')
        if element.is_displayed():
            driver.execute_script("arguments[0].click();", element)
            print(f'<{menu}> is displayed and clickable')
        else:
            print(f'CHECK CODE --- <{menu}> is not clickable')


# Validate main logo is displayed
def main_logo():
    sleep(1)
    print(divider)
    print('We check that all three elements of main logo - are displayed:')
    # Element 1 - picture "A"
    if driver.find_element(By.XPATH, '//*[@id = "Layer_1"]').is_displayed():
        print('Element 1 - picture "A" --- is displayed')
    else:
        print(f'CHECK CODE --- Element 1 - picture "A" --- is NOT displayed')

    # Element 2 - text "dvantage"
    if driver.find_element(By.XPATH, '//span[text() = "dvantage"]').is_displayed():
        print('Element 2 - text "dvantage" --- is displayed')
    else:
        print(f'CHECK CODE --- Element 2 - text "dvantage" --- is NOT displayed')

    # Element 3 - text "DEMO"
    if driver.find_element(By.XPATH, '//span[text() = "DEMO"]').is_displayed():
        print('Element 3 - text "DEMO" --- is displayed')
    else:
        print(f'CHECK CODE --- Element 3 - text "DEMO" --- is NOT displayed')


def select_random_dropdown(xpath):
    sleep(1)
    dropdown = driver.find_element(By.XPATH, xpath)
    sleep(2)
    dropdown.click()
    sleep(1)
    dropdown_options = Select(dropdown).options
    dropdown_list = []
    for option in dropdown_options[1::]: # without first option
        dropdown_list.append(option.text)

    sleep(1)
    random_choice = random.choice(dropdown_list)
    sleep(1)
    Select(dropdown).select_by_visible_text(random_choice)
    return random_choice


def contact_us():
    sleep(1)
    print(divider)
    print('Validation of CONTACT US form:')
    # Navigate to CONTACT US form
    element = driver.find_element(By.LINK_TEXT, 'CONTACT US')
    if element.is_displayed():
        driver.execute_script("arguments[0].click();", element)
        print(f'We navigated successfully to CONTACT US form ')
    else:
        print(f'CHECK CODE --- We did not navigate to CONTACT US form')

    # =================  Start to fill form =================
    # Select Category
    sleep(1)
    selected_category = select_random_dropdown('//select[@name="categoryListboxContactUs"]')
    # Select Product
    sleep(1)
    selected_product = select_random_dropdown('//select[@name="productListboxContactUs"]')
    # Email
    sleep(1)
    driver.find_element(By.XPATH, '//input[@name = "emailContactUs"]').send_keys(locators.email)
    # Message
    sleep(1)
    driver.find_element(By.XPATH, '//textarea[@name="subjectTextareaContactUs"]').send_keys(locators.message)
    # Click SEND button
    sleep(1)
    driver.find_element(By.ID, 'send_btnundefined').click()

    # =================  End to fill form =================

    # Summarize the form
    print(divider)
    print('CONTACT US form filled successfully, with following details:')
    sleep(1)
    contact_us_form = PrettyTable()
    contact_us_form.field_names = ['Field:       Value']
    contact_us_form.add_rows([
        [f'Selected category: {selected_category}'],
        [f'Selected product: {selected_product}'],
        [f'Email: {locators.email}'],
        [f'Message: {locators.message}'],
    ])

    contact_us_form.align = 'l'
    # Print form to console
    print(contact_us_form)
    sleep(1)
    # Validate confirmation message that Contact US form submitted
    if driver.find_element(By.XPATH, '//p[contains(., "Thank you for contacting Advantage support.")]'):
        print('Confirmation message "Thank you for contacting Advantage support." --- is displayed \n'
              'CONTACT US form submitted')
    else:
        print('CHECK CODE --- no confirmation message displayed after submitting CONTACT US form')
    # Continue to Shopping
    sleep(1)
    driver.find_element(By.XPATH, '//a[contains(., "CONTINUE SHOPPING")]').click()
    print("Button <CONTINUE SHOPPING> - clicked")


































