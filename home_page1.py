from .base_page1 import BasePage
from .locators1 import HomePageLocators

class HomePage(BasePage):
    def elements_present_on_home_page(self):
        input_search=self.browser.find_element(*HomePageLocators.INPUT_SEARCH)
        button_search=self.browser.find_element(*HomePageLocators.BUTTON_SEARCH)
        button_registration=self.browser.find_element(*HomePageLocators.BUTTON_REGISTRATION)
        button_language=self.browser.find_element(*HomePageLocators.BUTTON_LANGUAGE)
        button_basket=self.browser.find_element(*HomePageLocators.BUTTON_BASKET)
        price_basket=self.browser.find_element(*HomePageLocators.PRICE_BASKET)
        recommend_books=self.browser.find_element(*HomePageLocators.RECOMMEND_BOOKS)
        description_page = self.browser.find_element(*HomePageLocators.DESCRIPTION_PAGE).text
        assert description_page != '','DESCRIPTION IS EMPTY'

    def should_show_page_on_russian_language(self):
        button=self.browser.find_element(*HomePageLocators.BUTTON_LANGUAGE).click()
        russian=self.browser.find_element(*HomePageLocators.RUSSIAN_LANGUAGE).click()
        apply=self.browser.find_element(*HomePageLocators.BUTTON_GO).click()
        language_page=self.browser.current_url
        assert 'com/ru/' in language_page, 'PAGE IS NOT TRANSLATED'

    def should_show_page_on_spain_language(self):
        button=self.browser.find_element(*HomePageLocators.BUTTON_LANGUAGE).click()
        spain=self.browser.find_element(*HomePageLocators.SPAIN_LANGUAGE).click()
        apply=self.browser.find_element(*HomePageLocators.BUTTON_GO).click()
        language_page=self.browser.current_url
        assert 'com/es/' in language_page, 'PAGE IS NOT TRANSLATED'

    def should_show_page_on_italian_language(self):
        button = self.browser.find_element(*HomePageLocators.BUTTON_LANGUAGE).click()
        italian=self.browser.find_element(*HomePageLocators.ITALIAN_LANGUAGE).click()
        apply=self.browser.find_element(*HomePageLocators.BUTTON_GO).click()
        language_page=self.browser.current_url
        assert 'com/it/' in language_page, 'PAGE IS NOT TRANSLATED'

    def we_can_go_to_login_page(self):
        login_page=self.browser.find_element(*HomePageLocators.BUTTON_REGISTRATION).click()
        current_link=self.browser.current_url
        assert '/login/' in current_link, 'THIS PAGE IS NOT LOGIN PAGE'

