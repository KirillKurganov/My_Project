from selenium import webdriver
from.locators1 import HomePageLocators

class BasePage():
    def __init__(self,browser,link,timeout=3):
        self.browser=browser
        self.link=link
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.link)

    def translate_page(self):
        language=self.browser.find_element(*HomePageLocators.BUTTON_LANGUAGE).click()
        english=self.browser.find_element(*HomePageLocators.ENGLISH_LANGUAGE)
        english.click()

