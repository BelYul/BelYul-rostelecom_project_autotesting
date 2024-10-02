import pytest

from pages.auth_page import AuthPage
from config_data import Info
import time


@pytest.mark.parametrize("url_product",
                         [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_SmartHome_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_SmartHome_Web"])
def test_auth_log_and_pass_positive(web_browser, url_product):
    """16. Проверка авторизации пользователя с валидными данными в связке Логин/пароль"""

    page = AuthPage(web_browser, url_product)

    page.enter_with_password.click()

    page.tab_login.click()

    page.field_username.send_keys(Info.login_lc)
    page.field_password.send_keys(Info.valid_password1)

    page.button_enter_auth.click()

    if url_product == Info.URL_ELK_Web:
        page.personal_acc_elk.wait_to_be_clickable()
        assert page.personal_acc_elk.is_presented()

    elif url_product == Info.URL_START_Web:
        assert page.personal_acc_start.is_presented()

    elif url_product == Info.URL_SmartHome_Web:
        assert page.home_screen.is_presented()



@pytest.mark.parametrize("url_product",
                         [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_SmartHome_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_SmartHome_Web"])
def test_auth_mail_and_pass_positive(web_browser, url_product):
    """17. Проверка авторизации пользователя с валидными данными в связке почта/пароль"""

    page = AuthPage(web_browser, url_product)

    page.enter_with_password.click()

    page.tab_mail.click()

    page.field_username.send_keys(Info.mail_lc)
    page.field_password.send_keys(Info.valid_password1)

    page.button_enter_auth.click()

    if url_product == Info.URL_ELK_Web:
        page.personal_acc_elk.wait_to_be_clickable()
        assert page.personal_acc_elk.is_presented()


    if url_product == Info.URL_START_Web:
        assert page.personal_acc_start.is_presented()

    if url_product == Info.URL_SmartHome_Web:
        assert page.home_screen.is_presented()



@pytest.mark.parametrize("url_product",
                         [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_SmartHome_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_SmartHome_Web"])
def test_auth_phone_and_pass_positive(web_browser, url_product):
    """18.Проверка авторизации пользователя с валидными данными в связке телефон/пароль"""

    page = AuthPage(web_browser, url_product)

    page.enter_with_password.click()

    page.tab_phone.click()

    page.field_username.send_keys(Info.phone_lc)
    page.field_password.send_keys(Info.valid_password1)

    page.button_enter_auth.click()

    if url_product == Info.URL_ELK_Web:
        page.personal_acc_elk.wait_to_be_clickable()
        assert page.personal_acc_elk.is_presented()

    if url_product == Info.URL_START_Web:
        assert page.personal_acc_start.is_presented()

    if url_product == Info.URL_SmartHome_Web:
        assert page.home_screen.is_presented()



@pytest.mark.parametrize("url_product",
                         [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_SmartHome_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_SmartHome_Web"])
@pytest.mark.parametrize(("login", "password"),
                         [(Info.login_lc, Info.invalid_password2), (Info.invalid_login_lc, Info.valid_password1)],
                         ids=["верный логин - неверный пароль", "неверный логин - верный пароль"])
def test_auth_invalid_data_negative(web_browser, url_product, login, password):
    """19. Проверка авторизации пользователя с невалидными данными в связке логин/пароль"""

    page = AuthPage(web_browser)

    # для обхода капчи вход с валидными данными
    page.enter_with_password.click()
    page.tab_login.click()
    page.field_username.send_keys(Info.login_lc)
    page.field_password.send_keys(Info.valid_password1)
    page.button_enter_auth.click()
    page.enter_to_mini_lc_elk.wait_to_be_clickable()
    if page.enter_to_mini_lc_elk.is_clickable():
        page.enter_to_mini_lc_elk.click()
    page.button_exit_mini_elk.click()
    time.sleep(1)

    page = AuthPage(web_browser, url_product)

    # вход с невалидными данными
    page.enter_with_password.click()
    page.tab_login.click()

    page.field_username.send_keys(login)
    page.field_password.send_keys(password)
    page.button_enter_auth.click()

    assert page.error_message.is_presented()


@pytest.mark.parametrize("url_product",
                         [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_SmartHome_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_SmartHome_Web"])
@pytest.mark.parametrize(("email", "password"),
                         [(Info.mail_lc, Info.invalid_password2), (Info.invalid_mail_lc, Info.valid_password1)],
                         ids=["верная почта - неверный пароль", "неверная почта - верный пароль"])
def test_auth_invalid_data_negative(web_browser, url_product, email, password):
    """20. Проверка авторизации пользователя с невалидными данными в связке почта/пароль"""

    page = AuthPage(web_browser)

    # для обхода капчи вход с валидными данными
    page.enter_with_password.click()
    page.tab_login.click()
    page.field_username.send_keys(Info.login_lc)
    page.field_password.send_keys(Info.valid_password1)
    page.button_enter_auth.click()
    page.enter_to_mini_lc_elk.wait_to_be_clickable()
    if page.enter_to_mini_lc_elk.is_clickable():
        page.enter_to_mini_lc_elk.click()
    page.button_exit_mini_elk.click()
    time.sleep(1)

    page = AuthPage(web_browser, url_product)

    # вход с невалидными данными
    page.enter_with_password.click()
    page.tab_mail.click()

    page.field_username.send_keys(email)
    page.field_password.send_keys(password)
    page.button_enter_auth.click()

    assert page.error_message.is_presented()