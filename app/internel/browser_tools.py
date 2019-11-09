from selenium.webdriver.firefox.options import Options
from selenium import webdriver


class BrowserTools:
    browser = None
    display = None

    def getBrowser(self):
        firefox_opt = Options()
        firefox_opt.headless = True
        self.browser = webdriver.Firefox(options=firefox_opt)
        return self.browser

    def closeBrowser(self):
        self.browser.close()
