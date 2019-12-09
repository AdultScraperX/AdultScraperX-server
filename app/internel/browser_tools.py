from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import config as CONFIG


class BrowserTools:
    browser = None
    display = None

    def getBrowser(self):
        firefox_opt = Options()
        firefox_opt.headless = True

        if CONFIG.BROWSER_DRIVE is 'firefox':
            self.browser = webdriver.Firefox(options=firefox_opt)
        if CONFIG.BROWSER_DRIVE is 'chrome':
            self.browser = webdriver.Chrome(options=firefox_opt)

        return self.browser

    def closeBrowser(self):
        self.browser.close()
