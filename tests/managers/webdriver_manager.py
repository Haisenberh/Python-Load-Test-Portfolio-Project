import tests.config as config
from selenium import webdriver


class WebdriverManager:
    selected_browser = None
    width = None
    height = None
    wait = None
    pagedriver = None

    def __init__(self):
        self.selected_browser = config.BROWSER
        self.width = config.BROWSER_WIDTH
        self.height = config.BROWSER_HEIGHT
        self.wait = float(config.IMPLICIT_WAIT)
        self.pagedriver = None

    def get_webdriver(self):
        if self.pagedriver is None:
            try:
                if self.selected_browser.lower() == "chrome":
                    print("Selected browser is Chrome")
                    self.pagedriver = webdriver.Chrome(service_log_path="chrome.log")
                elif self.selected_browser.lower() == "safari":
                    print("Selected browser is Safari")
                    self.pagedriver = webdriver.Safari(service_log_path="safari.log")
                elif self.selected_browser.lower() == "edge":
                    print("Selected browser is Edge")
                    self.pagedriver = webdriver.Edge(service_log_path="edge.log")
                elif self.selected_browser.lower() == "firefox":
                    print("Selected browser is Firefox")
                    self.pagedriver = webdriver.Firefox(service_log_path="firefox.log")
                self.pagedriver.set_window_size(width=self.width, height=self.height)
                self.pagedriver.implicitly_wait(self.wait)
                return self.pagedriver
            except (ValueError, NameError):
                print("Oops!  Can’t return webdriver ...")
        else:
            return self.pagedriver

    def close_driver(self):
        print("Closing driver")
        if self.pagedriver is not None:
            try:
                self.pagedriver.quit()
                self.pagedriver = None
            except (ValueError, NameError):
                self.pagedriver = None
                print("Oops!  Can’t close webdriver ...")
        else:
            print("Driver is already closed!")

    # make a screenshot with a name of the test, date and time
    def take_screenshot(self, file_location):
        print("Take screenshot")
        self.pagedriver.save_screenshot(file_location)
