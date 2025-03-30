from playwright.sync_api import sync_playwright, expect  # Импорт Playwright для синхронного режима и проверки

with sync_playwright() as playwright:  # Запуск Playwright в синхронном режиме
    browser = playwright.chromium.launch(headless=False)  # Открываем браузер Chromium
    page = browser.new_page()  # Создаем новую страницу
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration") #Переходицу

    email_input = page.locator('//div[@data-testid="registration-form-email-input"]//div//input')
    email_input.fill("user.name@gmail.com")  # Находим поле email и заполняем его

    username_input = page.locator('//div[@data-testid="registration-form-username-input"]//div//input')
    username_input.fill("username")  # Находим поле username и заполняем его

    password_input = page.locator('//div[@data-testid="registration-form-password-input"]//input')
    password_input.fill("password")  # Находим поле password и заполняем его

    registration_button = page.locator('//button[@data-testid="registration-page-registration-button"]')
    registration_button.click()  # Находим кнопку "Registration" и нажимаем на него

    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()  # Проверяем видимость элемента
    expect(dashboard_title).to_have_text('Dashboard')  # Проверяем текст
