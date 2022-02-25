import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators


class ShoppingCartSetUpTest(unittest.TestCase):

    # Scenario_01: test initial setup
    @staticmethod
    def test_setUp():
        # Open browser -> navigate to home page -> validate correct URL and title
        methods.setUp('Scenario_01')

        # Close the web browser
        methods.tearDown('Scenario_01')

