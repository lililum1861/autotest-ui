import pytest
from playwright.sync_api import expect, Page, Playwright

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state  # ПРАВИЛЬНО получаем страницу из фикстуры

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
