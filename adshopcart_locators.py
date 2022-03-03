import random

from faker import Faker
import faker.providers.address

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# ===============================================  Variables

# URLs and Titles
homepage_url = 'https://advantageonlineshopping.com/#/'

# Variables for form
fake = Faker('en_CA')

# First name / Last name - length 2-30 characters
# tried to limit with min_chars / max_chars options - it didn't work
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'

# Username - length 5-15 characters
# first I used random.randint(4, 14) as it should be
# but one time was shown message that username is exists. so I limited it to 14-15 characters
username = f'{first_name}{last_name}'[0:random.randint(13, 14)]


# Email
domain_list = ['gmail.com', 'yahoo.com']
email = f'{first_name}.{last_name}@{random.choice(domain_list)}'

# Password - length 4-12 characters
password = fake.password(length=random.randint(4, 12))

# Phone - length max 20 characters
# Some random phones include extensions, so could be more than 20 characters.
# If it's more than 20 characters, we will create another one
phone = fake.phone_number()
if len(phone) > 20:
    while len(phone) <= 20:
        phone = fake.phone_number()

# Message text box
message = fake.sentence(nb_words=random.randint(1, 30))

# Country - random select from dropdown
# country_dropdown = driver.find_element(By.XPATH, '//select[@name = "countryListboxRegisterPage"]')
# country_dropdown.click()
# country_dropdown_options = Select(country_dropdown).options
# country_dropdown_list = []
# for option in country_dropdown_options:
#     country_dropdown_list.append(option.text)
# country = random.choice(dropdown_list)


country = 'Canada'


# Country = Canada >> City - Address - Province - Postal Code
if country == 'Canada':
    province = fake.province_abbr()
    state_province_region = province
    postal_code = fake.postalcode()


city = fake.city()
address = fake.street_address()



# =================================