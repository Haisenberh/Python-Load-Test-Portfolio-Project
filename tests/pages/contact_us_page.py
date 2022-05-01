import os
from tests.step_defs import conftest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class ContactUsPage:
    CONTACT_US_BUTTON = (By.XPATH, "//div[@id='contact-link']")
    SEARCH_RESULTS_TITLES = (By.XPATH, "//a[@class='product-name' and @itemprop='url']")
    SEARCH_RESULT_COUNTER = (By.XPATH, "//span[@class='heading-counter']")
    NO_RESULTS_ALERT = (By.XPATH, "//p[@class='alert alert-warning']")
    SUBJECT_HEADING_DROPDOWN = (By.ID, "id_contact")
    EMAIL_INPUT = (By.ID, "email")
    MESSAGE_INPUT = (By.ID, "message")
    ORDER_REFERENCE_INPUT = (By.ID, "id_order")
    FILE_INPUT = (By.ID, "fileUpload")
    SEND_BUTTON = (By.ID, "submitMessage")
    SUCCESS_MESSAGE = (By.XPATH, "//p[@class='alert alert-success']")

    def __init__(self, browser):
        self.browser = browser

    def send_contact_request(self, subject, email, message, order_reference, file):
        conftest.wait_for_clickability(self.browser, self.CONTACT_US_BUTTON)
        self.browser.find_element(*self.CONTACT_US_BUTTON).click()
        subject_dropdown = Select(self.browser.find_element(*self.SUBJECT_HEADING_DROPDOWN))
        subject_dropdown.select_by_visible_text(subject)
        relative_path = f"tests/test_data/{file}.png"
        image_absolute_path = os.path.abspath(f"{relative_path}")
        self.browser.find_element(*self.FILE_INPUT).send_keys(image_absolute_path)
        self.browser.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*self.ORDER_REFERENCE_INPUT).send_keys(order_reference)
        self.browser.find_element(*self.MESSAGE_INPUT).send_keys(message)
        self.browser.find_element(*self.SEND_BUTTON).click()

    def get_success_contact_us_message(self):
        conftest.wait_for_element(self.browser, self.SUCCESS_MESSAGE)
        return self.browser.find_element(*self.SUCCESS_MESSAGE)