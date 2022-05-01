from tests.config import HOME_URL
from tests.step_defs import conftest
from selenium.webdriver.common.by import By


class HomePage:
    SEARCH_INPUT = (By.ID, "search_query_top")
    SEARCH_BUTTON = (By.NAME, "submit_search")
    CONTACT_US_BUTTON = (By.XPATH, "//div[@id='contact-link']")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(str(HOME_URL))

    def search_element(self, text):
        conftest.wait_for_element(self.browser, self.SEARCH_INPUT)
        self.browser.find_element(*self.SEARCH_INPUT).send_keys(text)
        self.browser.find_element(*self.SEARCH_BUTTON).click()