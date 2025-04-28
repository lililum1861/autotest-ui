import pytest
from playwright.sync_api import Playwright, Page

@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()

@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    # Открываем браузер и контекст
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Действия регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    page.locator('//div[@data-testid="registration-form-email-input"]//div//input').fill("user.name@gmail.com")
    page.locator('//div[@data-testid="registration-form-username-input"]//div//input').fill("username")
    page.locator('//div[@data-testid="registration-form-password-input"]//input').fill("password")
    page.locator('//button[@data-testid="registration-page-registration-button"]').click()

    # Сохраняем состояние в файл
    context.storage_state(path="browser-state.json")

    # Правильное закрытие ресурсов
    browser.close()

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    # Используем сохранённое состояние
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()
    yield page
    browser.close()

