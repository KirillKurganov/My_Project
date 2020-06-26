from selenium.webdriver.common.by import By

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET=(By.CSS_SELECTOR,'.btn-add-to-basket')
    MESSAGE_OF_ADDING=(By.CSS_SELECTOR,'div.alertinner')
    PRICE_BOOK=(By.CSS_SELECTOR,'div p.price_color')
    PRICE_BASKET=(By.CSS_SELECTOR,'div.alertinner p strong')
    NAME_BOOK=(By.CSS_SELECTOR,'div h1')
    DESCRIPTION=(By.CSS_SELECTOR,'#product_description')
    LINK_REVIEW=(By.CSS_SELECTOR,'section p a')

class ReviewPageLocators():
    INPUT_TITTLE=(By.CSS_SELECTOR,'#id_title')
    INPUT_BODY=(By.CSS_SELECTOR,'#id_body')
    INPUT_NAME=(By.CSS_SELECTOR,'#id_name')
    INPUT_EMAIL=(By.CSS_SELECTOR,'#id_email')

class HomePageLocators():
    INPUT_SEARCH=(By.CSS_SELECTOR,'#id_q')
    BUTTON_SEARCH=(By.CSS_SELECTOR,'input.btn-default')
    BUTTON_REGISTRATION=(By.CSS_SELECTOR,'#login_link')
    BUTTON_LANGUAGE=(By.CSS_SELECTOR,'select.form-control')
    BUTTON_BASKET=(By.CSS_SELECTOR,'.btn-group a')
    PRICE_BASKET=(By.CSS_SELECTOR,'div strong')
    DESCRIPTION_PAGE=(By.CSS_SELECTOR,'div h2')
    RECOMMEND_BOOKS=(By.CSS_SELECTOR,'.sub-header h3')
    RUSSIAN_LANGUAGE=(By.CSS_SELECTOR,"[value='ru']")
    SPAIN_LANGUAGE=(By.CSS_SELECTOR,"[value='es']")
    ITALIAN_LANGUAGE=(By.CSS_SELECTOR,"[value='it']")
    BUTTON_GO=(By.CSS_SELECTOR,'#language_selector button.btn-default')
    ENGLISH_LANGUAGE=(By.CSS_SELECTOR,"[value='en-gb']")


class LoginPageLocators():
    REGISTRATION_EMAIL=(By.CSS_SELECTOR,'#id_registration-email')
    REGISTRATION_PASSWORD1=(By.CSS_SELECTOR,'#id_registration-password1')
    REGISTRATION_PASSWORD2=(By.CSS_SELECTOR,'#id_registration-password2')
    BUTTON_REGISTRATION=(By.CSS_SELECTOR,"[name='registration_submit']")
    MESSAGE_ABOUT_REGISTRATION=(By.CSS_SELECTOR,'.alertinner')
    LOGIN_EMAIL=(By.CSS_SELECTOR,'#id_login-username')
    LOGIN_PASSWORD=(By.CSS_SELECTOR,'#id_login-password')
    BUTTON_FOR_LOGIN=(By.CSS_SELECTOR,'button.btn-lg')
    VERIFY_LOGIN=(By.CSS_SELECTOR,'a i.icon-signout')
    ACCOUNT=(By.CSS_SELECTOR,'a i.icon-user')
    ERRORS=(By.CSS_SELECTOR,'.alert-danger strong')
    ERRORS_FOR_REGISTRATION=(By.CSS_SELECTOR,'.alert-danger')
    BUTTON_RESTORE_PASSWORD=(By.CSS_SELECTOR,"[href='/en-gb/password-reset/']")
    INPUT_EMAIL_FOR_RESTORE=(By.CSS_SELECTOR,'#id_email')




