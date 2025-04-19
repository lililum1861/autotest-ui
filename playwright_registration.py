from playwright.sync_api import sync_playwright, expect  # Импорт Playwright для синхронного режима и проверки

with sync_playwright() as playwright:  # Запуск Playwright в синхронном режиме
    browser = playwright.chromium.launch(headless=False)  # Открываем браузер Chromium
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration") #Переходицу

    email_input = page.locator('//div[@data-testid="registration-form-email-input"]//div//input')
    email_input.fill("user.name@gmail.com")  # Находим поле email и заполняем его

    username_input = page.locator('//div[@data-testid="registration-form-username-input"]//div//input')
    username_input.fill("username")  # Находим поле username и заполняем его

    password_input = page.locator('//div[@data-testid="registration-form-password-input"]//input')
    password_input.fill("password")  # Находим поле password и заполняем его

    registration_button = page.locator('//button[@data-testid="registration-page-registration-button"]')
    registration_button.click()  # Находим кнопку "Registration" и нажимаем на него

    context.storage_state(path="browser-state.json")

from playwright.sync_api import sync_playwright

# Остальной код регистрации нового польозвателя без изменений

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json") # Указываем файл с сохраненным состоянием
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    page.wait_for_timeout(5000)