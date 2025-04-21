from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.locator('//div[@data-testid="registration-form-email-input"]//div//input')
    email_input.fill("user.name@gmail.com")

    username_input = page.locator('//div[@data-testid="registration-form-username-input"]//div//input')
    username_input.fill("username")

    password_input = page.locator('//div[@data-testid="registration-form-password-input"]//input')
    password_input.fill("password")

    registration_button = page.locator('//button[@data-testid="registration-page-registration-button"]')
    registration_button.click()

    context.storage_state(path="browser-state.json")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    text_courses = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(text_courses).to_be_visible()
    expect(text_courses).to_have_text('Courses')

    svg = page.get_by_test_id('courses-list-empty-view-icon')
    expect(svg).to_be_visible()

    text_header = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(text_header).to_be_visible()
    expect(text_header).to_have_text('There is no results')

    text_subheader = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(text_subheader).to_be_visible()
    expect(text_subheader).to_have_text('Results from the load test pipeline will be displayed here')