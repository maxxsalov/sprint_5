from selenium.webdriver.common.by import By


class TestLocators:
    Input_name_locator = ".//input[@type='text']" # Ввод имени
    Input_password_locator = ".//input[@type='password']"  # Ввод пароля
    Input_email_locator = ".//input[@type='text']"  # Ввод email
    Log_in_locator = ".//*[@id='root']/div/main/div/form/button"  # Залогиниться/Зарегистрироваться
    Search_button_main_locator = ".//*[@id='root']/div/main/section[2]/div/button"  # Войти в аккаунт
    Search_personal_button_main_locator = "html/body/div/div/header/nav/a/p"  # Войти в личный кабинет
    Recover_password_locator = ".//*[@id='root']/div/main/div/div/p[2]/a"  # Восстановить пароль
    Recovery_button_locator = ".// *[@id ='root']/div/main/div/form/button"  # Кнопка "Восстановить"
    Login_button_locator = ".// *[@id ='root']/div/main/div/div/p/a"  # Кнопка "Войти"
    Constructor_button_locator = ".// *[@id ='root']/div/header/nav/ul/li[1]/a/p"  # Кнопка "Конструктор"
    Logo_button_locator = ".AppHeader_header__logo__2D0X2"  # Лого
    Logout_button_locator = ".//*[@id='root']/div/main/div/nav/ul/li[3]/button"  # Кнопка 'Выйти'
    Fillings_tab_locator = ".// *[@id = 'root']/div/main/section[1]/div[1]/div[3]/span"  # Переход к категории "Начинки"
    Example_fillings_locator = ".// *[@id = 'root']/div/main/section[1]/div[2]/ul[3]/a[1]/img"  # Мясо бессмертных моллюсков Protostomia
    Sauce_tab_locator = ".// *[@id = 'root']/div/main/ section[1]/div[1]/div[2]/span"  # Переход к категории "Соусы"
    Example_sauce_locator = ".// *[@id = 'root']/div/main/section[1]/div[2]/ul[2]/a[2]/img"  # Соус фирменный Space Sauce
    Buns_tab_locator = ".// *[@id = 'root']/div/main/ section[1]/div[1]/div[1]/span"  # Переход к категории "Булки"
    Example_buns_locator = ".// *[@id = 'root']/div/main/section[1]/div[2]/ul[1]/a[1]/img"  # Флюоресцентная булка
