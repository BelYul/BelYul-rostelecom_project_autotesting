# Информационный класс с тестовыми данными и URL
class Info():
    login_lc = "rtkid_1727460978242"
    invalid_login_lc = "rtkid_0000000000000" #незарегистрированный
    phone_lc = "+79041660090"
    mail_lc = "secita7890@aiworldx.com"
    invalid_mail_lc = "secita7890@aiworldx.ru" #незарегистрированная

    valid_password1 = "Test1234@"

    invalid_password2 = "TesT1234@" #незарегистрированный

    URL_ELK_Web = 'https://lk.rt.ru/'
    URL_Onlaim_Web = 'https://my.rt.ru/' #пока исключен из тестов,т.к. необходим лицевой счет в г. Москва (требуются др.тестовые данные)
    URL_START_Web = 'https://start.rt.ru/'
    URL_SmartHome_Web = 'https://lk.smarthome.rt.ru/'
    URL_Key_Web = 'https://key.rt.ru/' #не включен в тесты

    reg_text = "Зарегистрироваться"
    tab_phone_text = "Номер"
    tab_mail_text = "Почта"
    tab_login_text = "Логин"
    tab_personal_account_text = "Лицевой счёт"