
class TestLocators:
    Input_name_locator = ".//input[@name='name']" # Ввод имени
    Input_password_locator = ".//input[@type='password']"  # Ввод пароля
    Input_email_locator = ".//input[@type='text']"  # Ввод email
    Log_in_locator = ".//button[text()='Зарегистрироваться' or text()='Войти']"  # Залогиниться/Зарегистрироваться
    Search_button_main_locator = ".//button[text()='Войти в аккаунт']"  # Войти в аккаунт
    Search_personal_button_main_locator = './/a[@href="/account"]'  # Войти в личный кабинет
    Recover_password_locator = './/a[@href="/forgot-password"]'  # Восстановить пароль
    Recovery_button_locator = ".//button[text()='Восстановить']"  # Кнопка "Восстановить"
    Login_button_locator = './/a[@href="/login"]'  # Кнопка "Войти"
    Constructor_button_locator = './/p[text()="Конструктор"]'  # Кнопка "Конструктор"
    Logo_button_locator = './/div[@class="AppHeader_header__logo__2D0X2"]'  # Лого
    Logout_button_locator = ".//button[text()='Выход']"  # Кнопка 'Выйти'
    Fillings_tab_locator = './/span[text()="Начинки"]'  # Переход к категории "Начинки"
    Example_fillings_locator = './/img[@alt="Мясо бессмертных моллюсков Protostomia"]'  # Мясо бессмертных моллюсков Protostomia
    Sauce_tab_locator = './/span[text()="Соусы"]'  # Переход к категории "Соусы"
    Example_sauce_locator = './/img[@alt="Соус фирменный Space Sauce"]' # Соус фирменный Space Sauce
    Buns_tab_locator = './/span[text()="Булки"]'  # Переход к категории "Булки"
    Example_buns_locator = './/img[@alt="Флюоресцентная булка R2-D3"]'  # Флюоресцентная булка
    Order_button_locator = './/button[text()="Оформить заказ"]' # кнопка Оформить заказ
