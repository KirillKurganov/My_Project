import pytest
from .product_page1 import ProductPage
import time
from .home_page1 import HomePage
from .login_page1 import LoginPage

@pytest.mark.product_page
class TestForProductPage():
    def test_should_be_name_price_description(self,browser):
        link='http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
        page=ProductPage(browser,link)
        page.open()
        page.should_be_name_price_description_of_book()

    def test_add_to_basket_and_verify_message_and_price(self,browser):
        link='http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
        page=ProductPage(browser,link)
        page.open()
        page.add_to_basket()
        page.should_be_message_of_adding()
        page.price_is_correct()
        time.sleep(1)

    def test_should_be_form_for_review(self,browser):
        link='http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
        page=ProductPage(browser,link)
        page.open()
        page.go_to_review_page()
        page.should_be_form_for_review()
        time.sleep(1)

@pytest.mark.home_page
class TestForHomePage():
    def test_elements_present_on_page(self,browser):
        link='http://selenium1py.pythonanywhere.com/en-gb/'
        page=HomePage(browser,link)
        page.open()
        page.elements_present_on_home_page()

    def test_page_should_be_on_three_diffirent_language(self,browser):
        link='http://selenium1py.pythonanywhere.com/en-gb/'
        page=HomePage(browser,link)
        page.open()
        page.should_show_page_on_russian_language()
        page.should_show_page_on_spain_language()
        page.should_show_page_on_italian_language()

    def test_can_go_to_login_page_from_home_page(self,browser):
        link='http://selenium1py.pythonanywhere.com/en-gb/'
        page=HomePage(browser,link)
        page.open()
        page.we_can_go_to_login_page()
@pytest.mark.login_page
class TestLoginPage():
    def test_can_registration_on_site(self,browser):
        link='http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page=LoginPage(browser,link)
        page.open()
        page.can_registration()


    def test_can_come_in_account(self,browser):
        link='http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page=LoginPage(browser,link)
        page.open()
        page.can_login()


    def test_show_error_for_bad_password(self,browser):
        link='http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page=LoginPage(browser,link)
        page.open()
        page.show_wrong_for_not_correct_password()

    def test_show_error_for_bad_password_for_registration(self,browser):
        link='http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page=LoginPage(browser,link)
        page.open()
        page.show_wrong_for_bad_second_password_for_registration()

    def test_should_open_form_for_restore_password(self,browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        page.should_be_form_restore_password()