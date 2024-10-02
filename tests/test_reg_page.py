import pytest

from pages.reg_page import RegPage
from config_data import Info


@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_SmartHome_Web],
                         ids=["URL_ЕLK_Web", "URL_START_Web", "URL_SmartHome_Web"])
def test_reg_form(web_browser, url_product):
    """1. Проверяем наличие обязательных элементов"""

    page = RegPage(web_browser, url_product)

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    assert page.name_page_reg.is_presented(), "The element is missing on the page"
    assert page.first_name_field.is_presented(), "The element is missing on the page"
    assert page.surname_field.is_presented(), "The element is missing on the page"
    assert page.email_phone.is_presented(), "The element is missing on the page"
    assert page.pass_for_reg.is_presented(), "The element is missing on the page"
    assert page.pass_for_reg_confirm.is_presented(), "The element is missing on the page"
    assert page.agreement_reg.is_presented(), "The element is missing on the page"
    assert page.button_continue_on_reg_page.get_text() == Info.reg_text, "The element is missing on the page"
    #assert page.tagline_reg.is_presented(), "The element is missing on the page" не пройдет для URL_SmartHome_Web ввиду другого дизайна страницы



@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_SmartHome_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_SmartHome_Web"])
@pytest.mark.parametrize("name", ["з", "ХщЧЫОЧеММДЩЗЦящьРбАХцЙЫчаЮекнШц"], ids=["1 символ", "31 символ"])
def test_field_name_negative(web_browser, url_product, name):
    """2. Проверяем поле "Имя" на валидацию данных при некорректном количестве вводимых символов кириллицы (техника классы эквивалентности)"""

    page = RegPage(web_browser, url_product)

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.first_name_field.send_keys(name)

    page.surname_field.click()

    assert page.tooltip_first_name_field.is_presented(), "The tooltip was not found"


@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_SmartHome_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "Info.URL_SmartHome_Web"])
@pytest.mark.parametrize("name", ["ал",  "ЬКВЫОЧеММДЩЗЦящьРбАХцЙЫчаЮекнШ"],
                         ids=["2 сивмола",  "30 символов"])
def test_field_name_positive(web_browser, url_product, name):
    """3. Проверяем поле "Имя" на верную обработку граничных значений корректных символов"""

    page = RegPage(web_browser, url_product)

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.first_name_field.send_keys(name)

    page.surname_field.click()

    assert not page.tooltip_first_name_field.is_presented(), "A tooltip appeared"



@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_SmartHome_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_SmartHome_Web"])
@pytest.mark.parametrize("name", ["Ivan", "75646629", "^*)*&#&@!(^#@)*"],
                         ids=["латиница", "цифры", "спецсимволы"])
def test_field_name_latin_negative(web_browser, url_product, name):
    """4. Проверяем поле "Имя" на обработку невалидных данных"""

    page = RegPage(web_browser, url_product)

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.first_name_field.send_keys(name)

    page.surname_field.click()

    assert page.tooltip_first_name_field.is_presented(), "The tooltip was not found"



@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_SmartHome_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_SmartHome_Web"])
@pytest.mark.parametrize("surname", ["б", "ХщЧЫОЧеММДЗьПцщьРбАХцЙЫчаЮекнШц"], ids=["1 символ", "31 символ"])
def test_field_surname_negative(web_browser, url_product, surname):
    """5. Проверяем поле "Фамилия" на валидацию данных при некорректном количестве вводимых символов кириллицы (техника классы эквивалентности)"""

    page = RegPage(web_browser, url_product)

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.surname_field.send_keys(surname)

    page.first_name_field.click()

    assert page.tooltip_first_name_field.is_presented(), "The tooltip was not found"



@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_SmartHome_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_SmartHome_Web"])
@pytest.mark.parametrize("surname", ["ол",  "ЬКВЫОЧеММДЩЗЦящьРбАХцЙЫчаЮекнШ"],
                         ids=["2 символа", "30 символов"])
def test_field_surname_positive(web_browser, url_product, surname):
    """6. Проверяем поле "Фамилия" на верную обработку граничных значений корректных символов"""

    page = RegPage(web_browser, url_product)

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.surname_field.send_keys(surname)

    page.first_name_field.click()

    assert not page.tooltip_first_name_field.is_presented(), "A tooltip appeared"



@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_SmartHome_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_SmartHome_Web"])
@pytest.mark.parametrize("surname", ["Smirnov", "1675646629", "^*)*&#&@!(^#@)*"],
                         ids=["латиница", "цифры", "спецсимволы"])
def test_field_surname_latin_negative(web_browser, url_product, surname):
    """7. Проверяем поле "Фамилия" на обработку невалидных данных"""

    page = RegPage(web_browser, url_product)

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.surname_field.send_keys(surname)

    page.first_name_field.click()

    assert page.tooltip_first_name_field.is_presented(), "The tooltip was not found"



@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web],
                         ids=["URL_ELK_Web", "URL_START_Web"])
def test_reg_all_fields_empty_negative(web_browser, url_product):
    """8. Регистрация с пустыми полями - проверка корректной валидации данных системой"""

    page = RegPage(web_browser, url_product)

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.first_name_field.clear_field()
    page.surname_field.clear_field()
    page.email_phone.clear_field()
    page.pass_for_reg.clear_field()
    page.pass_for_reg_confirm.clear_field()
    page.button_continue_on_reg_page.click()

    assert page.tooltip_first_name_field.is_presented(), "The tooltip was not found"
    assert page.tooltip_surname_field.is_presented(), "The tooltip was not found"
    assert page.tooltip_email_phone.is_presented(), "The tooltip was not found"
    assert page.tooltip_pass_for_reg.is_presented(), "The tooltip was not found"
    assert page.tooltip_pass_for_reg_confirm.is_presented(), "The tooltip was not found"



@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web],
                         ids=["URL_ELK_Web", "URL_START_Web"])
@pytest.mark.parametrize("email_phone", ["drjghrt", "опкеоп", "123", "@", ""],
                         ids=["латиница", "кириллица", "цифры", "спецсимвол @", "пустое поле"])
def test_field_email_or_phone_negative(web_browser, url_product, email_phone):
    """9. Проверка поля "Email или мобильный телефон" на верную обработку невалидных данных"""

    page = RegPage(web_browser, url_product)

    page.enter_with_password.wait_to_be_clickable()
    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.email_phone.send_keys(email_phone)

    page.button_continue_on_reg_page.click()

    assert page.tooltip_email_phone.is_presented(), "The tooltip was not found"




@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web],
                         ids=["URL_ELK_Web", "URL_START_Web"])
@pytest.mark.parametrize("email_phone", ["8985683t123", "test@test"],
                         ids=["телефон с символом", "невалидная почта"])
def test_field_email_or_phone_negative2(web_browser, url_product, email_phone):
    """10. Проверка поля "Email или мобильный телефон" на верную обработку невалидных данных"""

    page = RegPage(web_browser, url_product)

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.email_phone.send_keys(email_phone)

    page.button_continue_on_reg_page.click()

    assert page.tooltip_email_phone.is_presented(), "The tooltip was not found"


@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_SmartHome_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_SmartHome_Web"])
@pytest.mark.parametrize("password",
                         ["iumemaf", "iumemafp", "iumemafQ", "iumemafpiumemafpemafp"],
                         ids=["7 строчных латинских символов", "8 строчных латинских символов", "7 строчных латинских символов и 1 заглавная", "21 строчный латинский символ"])
def test_field_password_negative(web_browser, url_product, password):
    """11. Проверка поля "Пароль" на невалидные данные + проверка на классы эквивалентности"""

    page = RegPage(web_browser, url_product)

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.pass_for_reg.send_keys(password)

    page.pass_for_reg_confirm.click()

    assert page.tooltip_pass_for_reg.is_presented(), "The tooltip was not found"


@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_SmartHome_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_SmartHome_Web"])
@pytest.mark.parametrize("password",
                         ["iumemaF$", "iumemafpiumemafpmaF$"],
                         ids=["8 корректных символов", "20 корректных символов"])
def test_field_password_negative(web_browser, url_product, password):
    """12. Проверка поля "Пароль" на граничные значения, валидными данными"""

    page = RegPage(web_browser, url_product)

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.pass_for_reg.send_keys(password)

    page.pass_for_reg_confirm.click()

    assert not page.tooltip_pass_for_reg.is_presented(), "The tooltip was not found"


@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_SmartHome_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_SmartHome_Web"])
@pytest.mark.parametrize("password", ["аопру256пкуП", "589龍門大酒家龍門大酒家", "Óèêèïåäèÿåìíîãî678åçè"],
                         ids=["кириллица", "китайские символы", "символы юникода"])
def test_field_password_negative2(web_browser, url_product, password):
    """13. Проверка поля "Пароль" на невалидные данные - отсутствие латинских символов """

    page = RegPage(web_browser, url_product)

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.pass_for_reg.send_keys(password)

    page.pass_for_reg_confirm.click()

    assert page.tooltip_pass_for_reg.is_presented(), "The tooltip was not found"



@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_SmartHome_Web],
                         ids = ["URL_ELK_Web", "URL_START_Web", "URL_SmartHome_Web"])
@pytest.mark.parametrize("password", ["12345678910", "~`!@#$%^&*()_+", "Test 1234%"],
                         ids = ["цифры", "спецсимволы", "с пробелом"])
def test_field_password_negative3(web_browser, url_product, password):
    """14. Проверка поля "Пароль" на невалидные данные."""

    page = RegPage(web_browser, url_product)

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.pass_for_reg.send_keys(password)

    page.pass_for_reg_confirm.click()

    assert page.tooltip_pass_for_reg.is_presented(), "The tooltip was not found"



@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_SmartHome_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_SmartHome_Web"])
def test_fields_passwords_with_mismatched_data(web_browser, url_product):
    """15. Подтверждение пароля - не совпадает. Проверка корректной валидации данных системой."""

    page = RegPage(web_browser, url_product)

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.pass_for_reg.send_keys(Info.valid_password1)
    page.pass_for_reg_confirm.send_keys(Info.invalid_password2)

    page.button_continue_on_reg_page.click()

    assert page.tooltip_pass_for_reg_confirm.is_presented(), "The tooltip was not found"