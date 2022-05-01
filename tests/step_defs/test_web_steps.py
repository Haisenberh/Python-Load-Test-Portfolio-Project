from pytest_bdd import parsers, scenarios
from pytest_bdd.steps import given, when, then
from tests.managers.webdriver_manager import WebdriverManager
from tests.pages.home_page import HomePage
from tests.pages.search_result_page import SearchResultPage
from tests.pages.contact_us_page import ContactUsPage

webdriver_manager = WebdriverManager()

# Scenarios
scenarios("../features/web.feature")


@given("I opened home page")
def open_home_page(browser):
    print("I opened home page")
    home_page = HomePage(browser)
    home_page.load()


@given(parsers.parse('I search "{item}" on Home page'))
@when(parsers.parse('I search "{item}" on Home page'))
def i_search_element(browser, item):
    print(f'I search "{item}" on Home page')
    home_page = HomePage(browser)
    home_page.search_element(item)


@then(parsers.parse('I see that all elements contains text "{searched_text}"'))
def assert_result_items_contains_text(browser, searched_text):
    print(f"I see that all elements contains text '{searched_text}'")
    search_result_page = SearchResultPage(browser)
    results = search_result_page.get_search_items()
    for item in results:
        assert (searched_text in item.text), f"Assert Fail!!! Item with name: '{item.text}' not contain searched text: '{searched_text}'!"


@then(parsers.parse('I see that No results message is shown'))
def assert_empty_result(browser):
    print("I see that No results message is shown")
    search_result_page = SearchResultPage(browser)
    result = search_result_page.get_no_results_element()
    assert ("No results were found for your search" in result.text), "Assert Fail!!! Search result page is not empty!"


@when(parsers.parse(
    'I send contact us request with subject: "{subject}", email: "{email}", order_reference: "{order_reference}", message: "{message}", file: "{file}"'))
def send_contact_us_form(browser, subject, email, message, order_reference, file):
    print(f'I send contact us request with subject: "{subject}", email: "{email}", order_reference: "{order_reference}", message: "{message}", file: "{file}"')
    contact_us_page = ContactUsPage(browser)
    contact_us_page.send_contact_request(subject=subject, email=email, message=message, file=file, order_reference=order_reference)


@then(parsers.parse('I see that success contact us request was send'))
def see_success_alert(browser):
    print("I see success that success contact us request was send")
    contact_page = ContactUsPage(browser)
    result = contact_page.get_success_contact_us_message()
    expected_message = "Your message has been successfully sent to our team."
    assert (expected_message in result.text), f"Assert Fail!!! Expected success message {expected_message} is not as actual {result}"


@then(parsers.parse('I see that search result counter is "{condition}"'))
def check_result_counter(browser, condition):
    print(f"I see that search result counter is '{condition}'")
    search_result_page = SearchResultPage(browser)
    counter_text = search_result_page.get_result_counter().text
    if counter_text:
        if condition == "0":
            assert (int(counter_text[0]) == 0), f"Assert Fail!!! Counter is bigger than zero! Counter = {counter_text}"
        if condition == "more than 0":
            assert (int(counter_text[0]) > 0), f"Assert Fail!!! Counter is equal to zero! Counter = {counter_text}"
