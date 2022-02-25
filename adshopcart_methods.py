import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

import adshopcart_locators as locators

# ================================================= Variables

driver = webdriver.Chrome()

divider = '-----------------------------------------'

# =================================================


def setUp(scenario_num):
    # Test started
    print(divider)
    text = f'{scenario_num} started at {datetime.datetime.now()}'
    print(text)

    # Make a full screen
    driver.maximize_window()
    driver.implicitly_wait(30)

    # Navigating to the home page app website
    driver.get(locators.homepage_url)

    # Validate correct URL address and correct title
    if driver.current_url == locators.homepage_url and driver.title.endswith('Advantage Shopping'):
        print(f'Page URL <{locators.homepage_url}> --- loaded successfully')
        print(f'Page title <Advantage Shopping> is correct')
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

