from .base_page1 import BasePage
from .locators1 import LoginPageLocators
import time

reg_email = str(time.time()) + "@mail.ru"
reg_password = '12345qazwsXvvvvvvew'
reg_email1='tyqwudi7wqdH@mail.ru'
bad_password='12345qazwsXvvvvvv'

class LoginPage(BasePage):
    def can_registration(self):
        global reg_email
        global reg_password
        #reg_email=str(time.time())+"@mail.ru"
        #reg_password='12345qazwsXvvvvvvew'
        email=self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email.send_keys(reg_email)
        password1=self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password1.send_keys(reg_password)
        password2=self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password2.send_keys(reg_password)
        button=self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION).click()
        time.sleep(2)
        message=self.browser.find_element(*LoginPageLocators.MESSAGE_ABOUT_REGISTRATION).text
        assert 'Thanks for registering!' in message, 'REGISTRATION IS NOT SUCCESSFUL'

    def can_login(self):
        global reg_email1
        global reg_password
        email=self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        email.send_keys(reg_email1)
        password=self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        password.send_keys(reg_password)
        button=self.browser.find_element(*LoginPageLocators.BUTTON_FOR_LOGIN)
        button.click()
        time.sleep(1)
        verify=self.browser.find_element(*LoginPageLocators.ACCOUNT)
        assert verify, 'LOGIN IS NOT SUCCESSFUL'

    def show_wrong_for_not_correct_password(self):
        global bad_password
        global reg_email1
        email=self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        email.send_keys(reg_email1)
        password=self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        password.send_keys(bad_password)
        button=self.browser.find_element(*LoginPageLocators.BUTTON_FOR_LOGIN)
        button.click()
        time.sleep(1)
        error=self.browser.find_element(*LoginPageLocators.ERRORS).text
        assert 'errors' in error, 'ERROR BE AWAY'

    def show_wrong_for_bad_second_password_for_registration(self):
        global reg_email
        global bad_password
        global reg_password
        email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email.send_keys(reg_email)
        password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password1.send_keys(reg_password)
        password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password2.send_keys(bad_password)
        button=self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION).click()
        time.sleep(2)
        error=self.browser.find_element(*LoginPageLocators.ERRORS_FOR_REGISTRATION).text
        assert 'errors' in error, 'ERROR BE AWAY'

    def should_be_form_restore_password(self):
        button=self.browser.find_element(*LoginPageLocators.BUTTON_RESTORE_PASSWORD).click()
        input_for_email=self.browser.find_element(*LoginPageLocators.INPUT_EMAIL_FOR_RESTORE)
        current_link=self.browser.current_url
        assert '/password-reset/' in current_link, 'THIS PAGE NOT FOR RESTORE PASSWORD'



