import pytest
from datetime import datetime
from tests import config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.managers.webdriver_manager import WebdriverManager


def get_file_name():
    file_name = f'reports/images/{datetime.today().strftime("%m-%d_%H_%M_%s")}.png'
    return file_name


@pytest.fixture()
def browser():
    webdriver_manager = WebdriverManager()
    driver = webdriver_manager.get_webdriver()
    yield driver
    webdriver_manager.take_screenshot(file_location=get_file_name())
    webdriver_manager.close_driver()


# attach screenshot to html report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add image to report
        extra.append(pytest_html.extras.image(get_file_name()))
        report.extra = extra


def wait_for_element(browser, element):
    if element is not None:
        print(f"waiting for element {element} ... ")
        WebDriverWait(browser, get_implicit_wait()).until(
            EC.presence_of_element_located(element),
            f"Timeout: {element} is not shown for {get_implicit_wait()} seconds",
        )
        print(f"Element {element} appear!!!")


def get_implicit_wait():
    return float(config.IMPLICIT_WAIT)


def wait_for_disappear(browser, element):
    if element:
        WebDriverWait(browser, get_implicit_wait()).until(
            EC.invisibility_of_element(element),
            f"Timeout: waited for {get_implicit_wait()} seconds, {element} is still visible",
        )

def wait_for_clickability(browser, element):
    if element:
        WebDriverWait(browser, get_implicit_wait()).until(
            EC.element_to_be_clickable(element),
            f"Timeout: waited for {get_implicit_wait()} seconds, {element} is not clickable",
        )


