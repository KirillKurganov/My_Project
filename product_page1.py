from .base_page1 import BasePage
from .locators1 import ProductPageLocators
from .locators1 import ReviewPageLocators

class ProductPage(BasePage):
    def should_be_name_price_description_of_book(self):
        name=self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        price=self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        description=self.browser.find_element(*ProductPageLocators.DESCRIPTION).text
        assert name != '', 'NAME IS NOT CORRECT'
        assert price != '', 'PRICE IS NOT CORRECT'
        assert description != '', 'DESCRIPTION IS NOT CORRECT'


    def add_to_basket(self):
        button_add_to_basket=self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_message_of_adding(self):
        message=self.browser.find_element(*ProductPageLocators.MESSAGE_OF_ADDING).text
        assert 'has been added to your basket' in message, 'MESSAGE IS NOT CORRECT'

    def price_is_correct(self):
        price_book=self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        price_basket=self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        assert price_basket == price_book, 'PRICE IS NOT CORRECT'

    def go_to_review_page(self):
        link=self.browser.find_element(*ProductPageLocators.LINK_REVIEW).click()
        current_link=self.browser.current_url
        assert 'addreview' in current_link, 'THIS PAGE IS NOT REVIEW PAGE'

    def should_be_form_for_review(self):
        input_tittle=self.browser.find_element(*ReviewPageLocators.INPUT_TITTLE)
        input_body=self.browser.find_element(*ReviewPageLocators.INPUT_BODY)
        input_name=self.browser.find_element(*ReviewPageLocators.INPUT_NAME)
        input_email=self.browser.find_element(*ReviewPageLocators.INPUT_EMAIL)










